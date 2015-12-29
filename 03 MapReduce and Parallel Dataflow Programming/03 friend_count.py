import MapReduce

import sys



"""
A Python Mapreduce framework to count the number of friends for each person
"""


"""
Map Input: Each input record is a 2 element list [personA, personB] where personA is a string representing the name of a person and personB is a string representing the name of one of personA's friends.
"""


"""Reduce Output: The output is a pair (person, friend_count) where person is a string and friend_count is an integer indicating the number of friends associated with person.
"""



mr = MapReduce.MapReduce()



def mapper(record):
    
    # key: document identifier
    
    # value: document contents
    
    key = record[0]
    
    if record[1] != None:
       friend = record[1]
    
       mr.emit_intermediate(key, 1)


def reducer(key, list_of_values):
    
    # key: word
    
    # value: list of occurrence counts
    
    total = 0
    
    for v in list_of_values:
      
        total += v
    
    mr.emit((key, total))




if __name__ == '__main__':
  
   inputdata = open(sys.argv[1])
  
   mr.execute(inputdata, mapper, reducer)
