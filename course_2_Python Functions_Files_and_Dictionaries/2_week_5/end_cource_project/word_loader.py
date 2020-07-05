def words_loader(name,offset=36):
    raw_words=open(name,'r')
    words=raw_words.readlines()[offset:]
    ret_word=[]
    for x in words:
        ret_word.append(x[:-1])
    return ret_word
