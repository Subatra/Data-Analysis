import MapReduce

import sys



"""Map Reduce Framework to produce unique trimmed nucleotide strings from a DNA file
"""



"""Map Input:Each input record is a 2 element list [sequence id, nucleotides] where sequence id is a string representing a unique identifier for the sequence and nucleotides is a string representing a sequence of nucleotides
"""

"""Reduce Output:The output from the reduce function should be the unique trimmed nucleotide strings.
"""
mr = MapReduce.MapReduce()





def mapper(record):
    
    # key: Sequence Id    
    # value: nucleotines    
    seq_id = record[0]

    nucleotide = record[1]
    
    nucleotide = nucleotide[:-10]
    values = mr.intermediate.values()
    # ---- remove the duplicates--------#
    if nucleotide not in [x for v in values for x in v if type(v) == list]:
       mr.emit_intermediate(seq_id,nucleotide)
  
def reducer(seq_id,nucleotide):
    
    # key: sequence id    
    # value: unique trimmed nucleotide
    for nuc in nucleotide:
        mr.emit(nuc)                    

if __name__ == '__main__':
  
   inputdata = open(sys.argv[1])
  
   mr.execute(inputdata, mapper, reducer)
