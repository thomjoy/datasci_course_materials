from __future__ import division
import sys
import json

def main():
    # get the tweet data
    tweet_data = []
    with open(sys.argv[1]) as tweet_file:
        for tweet in tweet_file:
            tweet_data.append(json.loads(tweet))

    # word count
    word_count = {}
    total = 0
    for tweet in tweet_data:
        if u'text' in tweet:
            tweet_text = tweet[u'text'].encode('utf-8')
            words = tweet_text.split()

            for word in words:
                if word in word_count:
                    word_count[word] = word_count[word] + 1
                else:
                    word_count[word] = 1

                total = total + 1

    freqs = {}
    for word in word_count:
        freq = round(float(word_count[word] / total), 5)
        freqs[word] = freq
        print word  + " " + str(freq)

if __name__ == '__main__':
    main()
