import sys
import json
    
def main():
    Json_file = sys.argv[1]
    data = [] # initializes an empty list
    term_occurrence = {}
    tweet_str = " "
    ttfile = open(Json_file) # twitterstream output json file
    for line in ttfile: # loads the twitterstream json into list  
        data.append(json.loads(line))
    ind = 0
    prev_twt = " " 
    for item in data:
        single_twt = data[ind]
        single_dict = {}
        for id,text in data[ind].iteritems(): # Json to dictionary   
            single_dict[id]=text
            score = 0 
            try:
                twt_id  = single_dict["id"]# parse tweet id
                twt_line = single_dict["text"] # parse tweet text
                twt_line = twt_line.rstrip()
                if twt_line == prev_twt: continue
                prev_twt= twt_line
                tweet_text = twt_line.split()   
                cnt = 0
# parse every single word from tweet text and search in sentiment #scores dictionary and print the scores - Assignment 1 - Problem 2
                for word in tweet_text:
                    tweet_str = tweet_text[cnt]
                    tweet_str = tweet_str.lower()
                    tweet_str = tweet_str.rstrip()
                    if tweet_str not in term_occurrence:
                       term_occurrence[tweet_str] = 1
                       cnt = cnt + 1
                    else:
                       term_occurrence[tweet_str] += 1
                       cnt = cnt + 1  
            except:
               pass
        ind = ind + 1

    sum_all = float(sum(term_occurrence.values()))
    freq = 1.0000
    freq_dict = {}   
    for key in term_occurrence:    
        freq = term_occurrence[key]/sum_all
        freq = round(freq,4)
        freq_dict[key] = round(float(freq),4)

    for key1 in freq_dict:    
        print key1,freq_dict[key1]

    out_file = open('o_dict.txt','w')
    json.dump(freq_dict,out_file)
    out_file.close() 
             
  
if __name__ == '__main__':
    main()	
