import sys
import json
import urllib 
from urllib2 import urlopen
import operator

    
def main():
    AFINN_file = sys.argv[1] 
    tweet_file = sys.argv[2]
    afinnfile = open(AFINN_file) # open sentiment scores input file
    scores = {} # initialize an empty dictionary
    for line in afinnfile:
        term, score  = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
        scores[term] = int(score)  # Convert the score to an integer
    #------------------------------------------------------------#
    #---- Read the tweets and get the location, Tweet text-------#
    #---- Initialize counters-------#

    serviceurl = 'http://maps.googleapis.com/maps/api/geocode/json?'
    data = [] 
    place_list = []
    place_dict = {}
    ttl_st = 0
    happy_st = {}
    ttfile = open(tweet_file) # twitterstream output json file
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
                if single_dict["geo"]  != None: # Filtering the tweets that has geological data
                   if single_dict["text"] == prev_tweet: continue
                   prev_tweet = single_dict["text"]  
                   lats = single_dict["geo"]["coordinates"][0]# Latitude, Logitude data
                   lons = single_dict["geo"]["coordinates"][1]
                   state,country = getstate(lats, lons) # fn to get the country,state based on lat,long 
                   if country != 'United States': continue # Filtering the data for United States
                   twt_id  = single_dict["id"]# parse tweet id
                   twt_line = single_dict["text"] # parse tweet text
                   twt_line = twt_line.rstrip()
                   tweet_text = twt_line.split()
                   tweet_text2 = twt_line.split()
                   cnt = 0
# parse every single word from tweet text and search in sentiment #scores dictionary and print the scores - Assignment 1 - Problem 2
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
# Store the final scores the states in United states
                   if state in happy_st:  
                      happy_st[state] += score        
                   else:
                      happy_st[state] = score
                      ttl_st += 1
            except:
               pass
        ind = ind + 1

    #print top 20 happiest states in United States based on the tweet score
    top_20_happyst = dict(sorted(happy_st.items(), key=operator.itemgetter(0), reverse=True)[:1])

    for key,value in sorted(top_20_happyst.items(), key=lambda kv: (kv[1],kv[0]),reverse=True):      
        print("%s" % (key.decode("utf-8")))   

  
def getstate(lat, lon):

    google_mapsurl = "http://maps.googleapis.com/maps/api/geocode/json?"
    google_mapsurl += "latlng=%s,%s&sensor=false" % (lat, lon)
    data = urlopen(google_mapsurl).read()
    data_json = json.loads(data)
    components = data_json['results'][0]['address_components']
    country = state = None
    for c in components:
        if "country" in c['types']:
            country = c['long_name']
        if "administrative_area_level_1" in c['types']:
            state = c['long_name']
    return state, country



if __name__ == '__main__':
    main()	
