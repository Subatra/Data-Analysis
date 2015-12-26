import sys
import json

def main():
    AFINN_file = sys.argv[1] 
    Json_file = sys.argv[2]
    afinnfile = open(AFINN_file) # open sentiment scores input file
    scores = {} # initialize an empty dictionary
    term_sent = {}
    for line in afinnfile:
        term, score  = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
        scores[term] = int(score)  # Convert the score to an integer
    #--------------------------------------------------
    #---- Read the tweets and determine Sentimen-------
    data = [] # initializes an empty list
    term_sent = {}
    ttfile = open(Json_file) # twitterstream output json file
    for line in ttfile: # loads the twitterstream json into list  
        data.append(json.loads(line))
    ind = 0
    prev_tweet = " "
    for item in data:
        single_twt = data[ind]
        single_dict = {}
        for id,text in data[ind].iteritems(): # Json to dictionary   
            single_dict[id]=text
            score = 0 
            try:
               if single_dict["lang"]  == 'en': # Filtering the "English" tweets
                  twt_id  = single_dict["id"]# parse tweet id
                  twt_line = single_dict["text"] # parse tweet text
                  twt_line = twt_line.rstrip()
                  if twt_line == prev_tweet: continue
                  prev_tweet = twt_line
                  tweet_text = twt_line.split()
                  tweet_text2 = twt_line.split()
                  cnt = 0
                  pos_cnt = 0.0
                  neg_cnt = 0.0
# parse every single word from tweet text and search in sentiment #scores dictionary and print the scores 
# If there is no score for a word in AFINN-111.txt then it will 
# assign score for the words based on the score of other words in #tweet   
                  for word in tweet_text:
                      curr_score = 0
                      tweet_str = tweet_text[cnt]
                      if tweet_str not in scores:
                         curr_score = 0
                         score = score + curr_score
                         cnt = cnt + 1
                      else: 
                         curr_score = scores[tweet_str]
                         score = score + curr_score
                         cnt = cnt + 1
                         if curr_score > 0:
                            pos_cnt = pos_cnt + 1
                         elif curr_score < 0:
                            neg_cnt = neg_cnt + 1
# Scores are derived based on the ratio of positive or negative words in a tweet. 
                  cnt2 = 0
                  neg_ratio = 0.0
                  pos_ratio = 0.0
                  if neg_cnt > pos_cnt:                     
                     neg_ratio = neg_cnt / cnt
                     curr_score0 = round(-neg_ratio,4)
                  elif pos_cnt > neg_cnt:
                     pos_ratio = pos_cnt / cnt
                     curr_score0 = round(pos_ratio,4)
                   
                  score2 = 0
                  for word1 in tweet_text2:
                      tweet_str2 = tweet_text[cnt2]
                      cnt2 = cnt2 + 1
                      if tweet_str2 not in scores:
                         cnt2 = cnt2 + 1
# Print the sentiment score for the terms not in AFINN-111.txt
                         print tweet_str2," ",curr_score0                   
            except:
               pass
        ind = ind + 1

  


if __name__ == '__main__':
    main()	
