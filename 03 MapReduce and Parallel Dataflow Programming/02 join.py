import MapReduce

import sys



"""Implement a relational join as a MapReduce query
   SELECT * 
   FROM Orders, LineItem 
   WHERE Order.order_id = LineItem.order_id 
"""


"""Map Input: each input record is a list of strings representing a tuple in the database. First item(index 0) is string that identifies the table("line_item", "order")
   Reduce output: Joined record. A single record that contains all attributes from "order" followed by fields from Line_item record. 
"""



mr = MapReduce.MapReduce()



def mapper(record):
    
    # key: Identifier String
    # value: Attributes of tuple

    idstring = record[0]    
    key = record[1]
    
    value = record[2:]

    value.insert(0,idstring)
    mr.emit_intermediate(key,value)


def reducer(key, list_of_values):
   
    # key: Order_id    
    # value: list of tuples
    len_list = len(list_of_values)
    i=0
    Order_tuple = ""
    values = []
    for i in range(0,len_list):
        if list_of_values[i][0] == "order":
           list_of_values[i].insert(1,key)
           order_tuple = list_of_values[i]
        if list_of_values[i][0] == "line_item":
           list_of_values[i].insert(1,key)
           values = order_tuple + list_of_values[i]
           print(len(values))
           mr.emit((values))


if __name__ == '__main__':
  
   inputdata = open(sys.argv[1])
  
   mr.execute(inputdata, mapper, reducer)
