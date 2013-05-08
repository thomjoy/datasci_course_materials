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
            tweet_text = tweet[u'text'].encode('utf-8')
            words = tweet_text.split()
            words = [w.lower() for w in words]

            scores_per_word = {}
            total_pos = 0
            total_neg = 0

            for word in words:
                if word in sentiments:
                    sentiment_value = float(sentiments[word])
                    scores_per_word[word] = sentiment_value

                    if sentiment_value < 0:
                        total_neg += 1
                    else:
                        total_pos += 1

                    avg = total_neg / total_pos

                else:
                    scores_per_word[word] = 0.0

            count = (scores_per_word.vals())
            tweet_scores.append(scores_per_word)

    for t in tweet_scores:
        print "<sentiment:" + str(t) + ">"


if __name__ == '__main__':
    main()
