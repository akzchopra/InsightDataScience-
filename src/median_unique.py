import numpy as np

def create_dictionary(word_list):
    word_count = {}
    for word in word_list:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
    return len(word_count)
    
tweets = open('tweet_input/tweets.txt')
text_file = open('tweet_output/ft2.txt','w')
length_tweet = []

for line in iter(tweets):
     words =  line.split(' ',len(line)-1)
     length_tweet.append(create_dictionary(words))

for l in range(len(length_tweet)):
    text_file.write('%.3f\n'%np.median(length_tweet[0:l+1]))

tweets.close()
text_file.close()


    
