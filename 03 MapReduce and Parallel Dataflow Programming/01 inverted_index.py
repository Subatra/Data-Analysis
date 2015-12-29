import MapReduce

import sys



"""
Python MapReduce Framework - Create Inverted Index - A dictionary where each word is associated with a list of document identifiers in which that word appears
"""



mr = MapReduce.MapReduce()



"""Mapper Input: 2-element list: [document_id, text], where document_id is a string representing a document identifier and text is a string representing the text of the document. 
"""

"""Reducer Output: (word, document ID list) tuple where word is a String and document ID list is a list of Strings.
"""


def mapper(record):
    
    # key: document identifier
    
    # value: document contents
    
    key = record[0]
    
    value = record[1]
    
    words = value.split()
    
    for w in words:
      
        mr.emit_intermediate(w, key)


def reducer(key, list_of_values):
   
    # key: word
    
    # value: list of docids
    docid_list = []
    for docid in list_of_values:
        if docid in docid_list: continue
        docid_list.append(docid)   
    mr.emit((key,docid_list))

# Do not modify below this line

# =============================


if __name__ == '__main__':
  
   inputdata = open(sys.argv[1])
  
   mr.execute(inputdata, mapper, reducer)
