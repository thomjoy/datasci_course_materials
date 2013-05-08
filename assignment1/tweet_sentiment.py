import sys
import json

def main():
    # create the sentiments dict
    sentiments = {}
    with open(sys.argv[1]) as sent_file:
        for line in sent_file:
            l = line.replace("'", "\\'").split("\t")
            sentiments[l[0]] = float(l[1])

    # get the tweet data
    tweet_data = []
    with open(sys.argv[2]) as tweet_file:
        for tweet in tweet_file:
            tweet_data.append(json.loads(tweet))

    # scoring
    tweet_scores = []
    for tweet in tweet_data:
        if u'text' in tweet:
            score = 0
            tweet_text = tweet[u'text'].encode('utf-8')
            for sent in sentiments:
                if sent in tweet_text:
                    score = score + float(sentiments[sent])
            tweet_scores.append(score)

    for t in tweet_scores:
        print "<sentiment:" + str(t) + ">"


if __name__ == '__main__':
    main()
