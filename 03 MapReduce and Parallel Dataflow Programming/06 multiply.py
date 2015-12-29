import MapReduce

import sys



"""
Map Reduce Algorithm to compute Matrix multiplication A x B.
"""


"""Map Input:The input to the map function will be a row of a matrix represented as a list. Each list will be of the form [matrix, i, j, value] where matrix is a string and i, j, and value are integers.The first item, matrix, is a string that identifies which matrix the record originates from. 
"""

"""Reduce output: The output from the reduce function is a row of the result matrix represented as a tuple. Each tuple will be of the form (i, j, value) where each element is an integer.
"""

mr = MapReduce.MapReduce()





def mapper(record):
    
    # record: [matrix,i,j,value]
    value = []
    key=""
    mat_name = record[0]

    n = 0
    if mat_name == "a":
       i =   record[1]
       j =   record[2]
       Aij = record[3]
       for n in range(0,5):
           key  = (i,n)
           value= [mat_name,j,Aij]
           mr.emit_intermediate(key,value)     #----For each (i,j) of A emit ((i,n),Aij) for n in 0...5
    else:
       j =   record[1]
       k =   record[2]
       Bjk = record[3]
       for n in range(0,5):
           key  = (n,k)
           value= [mat_name,j,Bjk]
           mr.emit_intermediate(key,value)     #----For each (j,k) of B emit ((n,j),Bjk) for n in 0...5 
    
def reducer(key,values):
    
    list_a = {}
    list_b = {}
    final_key = []
    for value in values:                       #----prepare list a & list b based in the matrix name ("a" or "b")
        if value[0] == "a":
            list_a[value[1]] = value[2]
        else:
            list_b[value[1]] = value[2]
    result = 0
    for j in range(0,5):
        if j not in list_a.keys(): continue
        if j not in list_b.keys(): continue
        result += (list_a[j] * list_b[j])
    final_key = key[0],key[1],result
    mr.emit((final_key))                    #-----emit (key= (i,j) ,value = Sum [(Aij * B jk) ]) 


if __name__ == '__main__':
  
   inputdata = open(sys.argv[1])
  
   mr.execute(inputdata, mapper, reducer)
