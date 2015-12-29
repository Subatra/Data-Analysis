import MapReduce

import sys



"""Implement a MapReduce algorithm to generate a list of all non-symmetric friend relationships.
"""


"""Map Input:Each input record is a 2 element list [personA, personB] where personA is a string representing the name of a person and personB is a string representing the name of one of personA's friends.
"""

"""Reduce output:The output is list of all pairs (friend, person) such that (person, friend) appears in the dataset but (friend, person) does not.
"""

mr = MapReduce.MapReduce()





def mapper(record):
    
    # key: personA    
    # value: Friend    
    personA = record[0]

    friend = record[1]
    
    mr.emit_intermediate(personA,friend )

def reducer(personA, friends):
    
    # key: word
    
    # value: list of friends
    for friend in friends:
        if friend in mr.intermediate.keys():
           if personA not in mr.intermediate[friend]:
              mr.emit((friend, personA))

              mr.emit((personA, friend))

        else:           
           mr.emit((friend,personA))

           mr.emit((personA, friend))

   
if __name__ == '__main__':
  
   inputdata = open(sys.argv[1])
  
   mr.execute(inputdata, mapper, reducer)
