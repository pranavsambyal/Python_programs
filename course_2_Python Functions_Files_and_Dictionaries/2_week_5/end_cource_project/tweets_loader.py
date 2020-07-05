def tweets_loader(x):
    file = open(x, 'r')
    all_lines = file.readlines()[1:]
    tweets = []
    for x in all_lines:
        y = x.split(',')
        tweets.append(y[0])
    return tweets
