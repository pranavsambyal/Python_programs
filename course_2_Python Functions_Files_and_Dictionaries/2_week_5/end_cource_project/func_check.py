def words_loader(name,offset=36):
    raw_words=open(name,'r')
    words=raw_words.readlines()[offset:]
    ret_word=[]
    for x in words:
        ret_word.append(x[:-1])
    return ret_word


def strip_punctuation(st):
    punctuation_chars = ["'", '"', ",", ".", "!", ":", ";", '#', '@']
    new_l=[]
    for x in punctuation_chars:
        st=(st.replace(x,''))
    return st

def get_pos(tweet):
    pos_score=0
    words=words_loader('positive_words.txt')
    words_s=tweet.split(" ")
    words_striped_punc=[]
    for x in words_s :
        words_striped_punc.append(strip_punctuation(x))
    for y in words_striped_punc:
        if y.lower() in words:
            print("tri")
            pos_score+=1

    return print(pos_score)


get_pos('@twitteruser: On  backbone now - @Fusion scores first points #FirstFinals @overwatchleague @umich @umsi Michigan Athletics made out of emojis. #GoBlue')