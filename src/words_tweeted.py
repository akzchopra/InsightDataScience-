import operator

def create_dictionary(word_list):
    word_count = {}
    text_file = open('tweet_output/ft1.txt','w')
    for word in word_list:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
    for key,value in sorted(word_count.items(),key = operator.itemgetter(0)):       
        text_file.write(key)
        text_file.write('  %d\n'%value)
    text_file.close()

tweets = open('tweet_input/tweets.txt')
lines = tweets.read().replace('\r\n',' ')
word_list = lines.split(' ',len(lines))
create_dictionary(word_list)
tweets.close()






