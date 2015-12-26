import sys
import json
import operator
    
def main():
    Json_file = sys.argv[1]
    hash_dict = {}
    ttfile = open(Json_file) # twitterstream output json file
    for tweet_line in ttfile:                        
        tweet = json.loads(tweet_line)             
        if "entities" in tweet.keys():                     
           hashtags = tweet["entities"]["hashtags"]
           for ent in hashtags:         
              if ent != None:                                 
                 if ent["text"].encode("utf-8") in hash_dict.keys():  
                    hash_dict[ent["text"].encode("utf-8")] += 1        
                 else:
                    hash_dict[ent["text"].encode("utf-8")] = 1

    sum_all_hash = float(sum(hash_dict.values()))
    #print "sum all",sum_all_hash
    #freq = 1.0000
    #freq_hash = {}   
    #for key in hash_dict:    
    #    freq = hash_dict[key]/sum_all_hash
    #    freq = round(freq,4)
    #    freq_hash[key] = round(float(freq),4)
    #print "dict",hash_dict
    top_10_hash = dict(sorted(hash_dict.items(), key=operator.itemgetter(1), reverse=True)[:10])
    for key,value in sorted(top_10_hash.items(), key=lambda kv: (kv[1],kv[0]),reverse=True):      
        print("#%s %d" % (key.decode("utf-8"), value))   

    #out_file = open('o_dict.txt','w')
    #json.dump(freq_dict,out_file)
    #out_file.close() 
             
  
if __name__ == '__main__':
    main()	
