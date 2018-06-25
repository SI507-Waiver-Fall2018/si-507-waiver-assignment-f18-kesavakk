import tweepy
import nltk
import csv
import sys
consumer_key = "Rwcyy6WOuyiVG8YVCBOo4m8CT"
consumer_secret = "45D2Bu1bP6i9AjQHLGBZiSqusCmu72LzLrekL336CIThENiMKt"
access_token = "153471706-mEjdoW7lDmVWeAlAheEQcyR0C9FCkIDgsuQnTmP9"
access_token_secret = "WYa9GhgcHGCW7JDgveAvSNVnv5hQJgKnWyYrUXbzZKSNC"
stopWords = ['http','https','RT']
suitableTokens = []
f = open('noun_data.csv','w')
f.write('Noun,Number\n')

def printwords(figofspeech, writecommafile):
    fig_dict = {}
    count = 0
    for v in figofspeech:
        if v in fig_dict.keys():
            fig_dict[v]+=1
        else:
            fig_dict[v]=1
    finalString= ""
    for (word, tag) in sorted(fig_dict.items(), key=lambda x: (-x[1], x[0])):
        if count < 5:
            writeString = ""
            if writecommafile:
                writeString = str(word)+","+str(tag) + "\n"
                f.write(writeString)
            finalString += (word + "(" + str(tag) + ") ")
            count +=1
        else:
            break
    return finalString


def main():
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)
    retweetcount = 0
    user = sys.argv[1]
    numOfTweets = sys.argv[2]
    favorites = 0
    tweets = api.user_timeline(screen_name = user,count = numOfTweets,include_rts=False)
    originalTweets = len(tweets)
    for tweet in tweets:
        retweetcount += tweet.retweet_count
        favorites += tweet.favorite_count
        tweet_tokens = nltk.word_tokenize(tweet.text)
        for w in tweet_tokens:
            if (w[0].isalpha()) and (w not in stopWords) and (len(w)>1):
                suitableTokens.append(w)
    adjectives = []
    verbs = []
    nouns = []
    for word,tag in nltk.pos_tag(suitableTokens):
        if tag[0] == "V" and tag[1] == "B":
            verbs.append(word)
        elif tag[0] == "N" and tag[1] == "N":
            nouns.append(word)
        elif tag[0] == "J" and tag[1] == "J":
            adjectives.append(word)
    print("USER:", user)
    print("TWEETS ANALYZED:", numOfTweets)
    print("VERBS: ", printwords(verbs, False))
    print("NOUNS: ", printwords(nouns, True))
    f.close()
    print("ADJECTIVES: ", printwords(adjectives,False))
    print("ORIGINAL TWEETS: ", originalTweets)
    print("TIMES FAVORITED (ORIGINAL TWEETS ONLY): ", favorites)
    print("TIMES RETWEETED (ORIGINAL TWEETS ONLY): ", retweetcount)
main()
