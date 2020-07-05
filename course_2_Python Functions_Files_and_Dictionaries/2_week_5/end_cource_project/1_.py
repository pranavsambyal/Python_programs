'''We have provided some synthetic (fake, semi-randomly generated) twitter data in a csv file named
project_twitter_data.csv which has the text of a tweet, the number of retweets of that tweet, and the number of replies
to that tweet. We have also words that express positive sentiment and negative sentiment, in the files
positive_words.txt and negative_words.txt.

Your task is to build a sentiment classifier, which will detect how positive or negative each tweet is. You will create
a csv file, which contains columns for the Number of Retweets, Number of Replies, Positive Score (which is how many
happy words are in the tweet), Negative Score (which is how many angry words are in the tweet), and the Net Score for
each tweet. At the end, you upload the csv file to Excel or Google Sheets, and produce a graph of the Net Score vs
Number of Retweets.

To start, define a function called strip_punctuation which takes one parameter, a string which represents a word, and
removes characters considered punctuation from everywhere in the word. (Hint: remember the .replace() method for
strings.)

Next, copy in your strip_punctuation function and define a function called get_pos which takes one parameter, a string
which represents one or more sentences, and calculates how many words in the string are considered positive words. Use
the list, positive_words to determine what words will count as positive. The function should return a positive integer
- how many occurrences there are of positive words in the text. Note that all of the words in positive_words are lower
cased, so you’ll need to convert all the words in the input string to lower case as well.
'''



#header of  given csv = tweet_text,retweet_count,reply_count

def strip_punctuation(st):
    punctuation_chars = ["'", '"', ",", ".", "!", ":", ";", '#', '@']
    new_l=[]
    for x in punctuation_chars:
        print(x)
        st=(st.replace(x,''))
    return st


def words_loader(name,offset=36):
    raw_words=open(name,'r')
    words=raw_words.readlines()[offset:]
    print(words)
    ret_word=[]
    for x in words:
        ret_word.append(x[:-1])
    print(ret_word)
    return ret_word

def pos_score(st):
    pos_words=words_loader('positive_words.txt')
    comments=st



def neg_score(st):
    neg_words=words_loader('negative_words.txt')
    comments=st





def dataingestor(filelist):  #variable of file as list
    out_file=[]
    for x in filelist:
        #out_file.append(x[1],x[2],pos_score(x[0]),neg_score(x[0]),tot_score(x[0]))
    return out_file


classified_csv=open('classifieed.csv','w')
classified_csv.write('Number of Retweets,Number of Replies,Positive Score,Negative Score,Net Score\n')

given_data=open('project_twitter_data.csv','r')
variable_of_data=given_data.readlines()[1:]
dataingestor(variable_of_data)