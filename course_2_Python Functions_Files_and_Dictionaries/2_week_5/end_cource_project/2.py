punctuation_chars = ["'", '"', ",", ".", "!", ":", ";", '#', '@']
# lists of words to use
positive_words = []
with open("positive_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            positive_words.append(lin.strip())

negative_words = []
with open("negative_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            negative_words.append(lin.strip())


def strip_punctuation(st):
    new_l = []
    for x in punctuation_chars:
        st = (st.replace(x, ''))
    return st


def get_pos(tweet):
    pos_score = 0
    words_s = tweet.split(" ")
    words_striped_punc = []
    for x in words_s:
        words_striped_punc.append(strip_punctuation(x))
    for y in words_striped_punc:
        if y.lower() in positive_words:
            pos_score += 1

    return pos_score


def get_neg(tweet):
    neg_score = 0
    words_s = tweet.split(" ")
    words_striped_punc = []
    for x in words_s:
        words_striped_punc.append(strip_punctuation(x))
    for y in words_striped_punc:
        if y.lower() in negative_words:
            neg_score += 1

    return neg_score


def tot_score(st):
    return get_pos(st) - get_neg(st)


def dataingestor(filelist):  # variable of file as list
    out_file = []
    x = filelist
    out_file.append((int(x[1]), (x[2]), get_pos(x[0]), get_neg(x[0]), tot_score(x[0])))
    return out_file


given_data = open('project_twitter_data.csv', 'r')
variable_of_data = given_data.readlines()[1:]
outfile=[]
for x in variable_of_data:
    y=x[:-1]
    readcsv=y.split(',')
    outfile.append(dataingestor(readcsv))

file2=open('resulting_data.csv','w')
file2.write("Number of Retweets, Number of Replies, Positive Score, Negative Score, Net Score\n")

for x in range(len(outfile)):
    z=outfile[x]
    y=z[0]
    file2.write("{},{},{},{},{}\n".format(y[0],y[1],y[2],y[3],y[4]))