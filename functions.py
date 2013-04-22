#!/usr/local/bin/python
# -*- coding: UTF-8 -*-
# Rastreador de presidente / governador?
# @mtrpires

import urllib
import json
from bs4 import BeautifulSoup

class Candidate(object):
    """
    Initiates a Candidate instance, saves all parameters
    as atributes of the instance.
    name: a string containing the candidate's real name
    twitterURL: a string containing the candidate's twitter URL
    facebookID: a string containing the candidate's fbID
    website: a string containing the candidate's official website
    wiki: a string containing the Wikipedia (pt) entry for the candidate
    """

    def __init__(self, name, twitterName, facebookID, website, wiki):
        self.name = name
        self.twitterName = twitterName
        self.facebookID = facebookID
        self.website = website
        self.wiki = wiki

    def getName(self):
        """
        Returns the candidate's name
        """
        return self.name

    def setTwitter(self, twitterName):
        """
        Sets twitterName for candidate
        """
        self.twitterName = twitterName
        print self.name, " - twitterName set to:", self.twitterName

    def getTwitter(self):
        """
        Returns the candidate's twitter profile name
        """
        return self.twitterName

    def setFacebook(self, facebookID):
        """
        Sets Facebook ID for candidate
        """
        self.facebookID = facebookID
        print self.name, " - facebookID set to:", self.facebookID

    def getFacebook(self):
        """
        Returns the candidate's Facebook ID
        """
        return self.facebookID

    def setWebsite(self, website):
        """
        Sets website for candidate
        """
        self.website = website
        print self.name, " - website set to:", self.website
        
    def getWebsite(self):
        """
        Returns the candidate's website
        """
        return self.website

    def setFacebook(self, wiki):
        """
        Sets Wikipedia page (PT-BR) for candidate
        """
        self.wiki = wiki
        print self.name, " - Wikipedia page set to:", self.wiki
        
    def getWiki(self):
        """
        Returns the Wikipedia entry on the candidate (PT-BR)
        """
        return self.wiki

    def getNumFollowers(self):
        """
        Uses the helper function getTwitterDump to extract
        the number of followers from the JSON dictionary.

        returns: the number of followers of a given user.
        """

        return getTwitterDump(self, 'u')[u'followers_count']

    def getNumTweets(self):
        """
        Uses the helper function getTwitterDump to extract
        the number of tweets from the JSON dictionary.

        returns: the number (int) of tweets of a given user.
        """

        return getTwitterDump(self, 'u')[u'statuses_count']

    def getLatestTweets(self):
        """
        Uses the helper function getTwitterDump to extract the
        latest tweets from a given user.

        returns: list of tweets, UTF-8 encoded. 
        Each index of the list is a tweet.
        """
        tweets = []
        tweetsList = getTwitterDump(self, 's')
        for i in tweetsList:
            tweets.append(i[u'text'].encode('utf_8'))
            
        return tweets

    def getNumLikes(self):
        """
        Uses the helper function getFacebookDump to extract
        the number of likes from the JSON dictionary.
        
        If the candidate doesn't have a public profile,
        he/she won't have a "likes" number, producing a "key error". 
        Instead, an FQL query is made to get the number of friends.

        returns: the number (int) of likes of a given Facebook page.
        """
        try:
            friendCount = getFacebookDump(self)[u'likes']
            
        except KeyError:
            dump = json.loads(urllib.urlopen(\
            "https://graph.facebook.com/fql?q=SELECT%20friend_count%20FROM%20user%20WHERE%20uid="\
            +self.getFacebook()).readline())
            friendCount = dump[u'data'][0][u'friend_count']
            
        return friendCount
            
    def getStories(self):
        """
        Goes to Folha.com and searches for 'candidate'.
        Returns the last three stories where his/her name shows up.

        returns: list with HTML for stories.
        """
        news = []
        results = \
        "http://search.folha.com.br/search?q=%s&site=online" % self.name
        soupResults = BeautifulSoup(urllib.urlopen(results).read())
        resultsList = soupResults.findAll('p')
        
        # Encode to UTF-8 each piece of news
        for noticias in resultsList[2:5]:
            noticias.encode('utf_8')
            news.append(noticias)

        return news

    def __repr__(self):
        """
        Shows useful information about the Object when called from prompt
        """
        return self.getName()


def getTwitterDump(candidate, kind):
    """
    Gets the JSON string for 'candidate.getTwitter()' and defined
    type (status or general information) and converts
    it into a dictionary (general) or list (status)
    using json.loads. Default value for latest tweets is 3.

    candidate: an instance of the object Candidate.

    returns: dictionary with JSON items as keys and its
    respective values.
    """

    if kind == 's':
        twitterJSON = \
        "https://api.twitter.com/1/statuses/user_timeline.json?\
        include_rts=true&screen_name=%s"\
        % candidate.getTwitter()
    elif kind == 'u':
        twitterJSON = \
        "https://api.twitter.com/1/users/show.json?screen_name=%s"\
        % candidate.getTwitter()

    dump = json.loads(urllib.urlopen(twitterJSON).read())
    return dump


def getFacebookDump(candidate):
    """
    Gets the JSON string for 'facebookID' and converts
    it into a dictionary using json.loads.

    returns: dictionary with JSON items as keys and its
    respective values.
    """
    
    facebookJSON = \
    "http://graph.facebook.com/%s/" % candidate.getFacebook()
    
    dumpDict = json.loads(urllib.urlopen(facebookJSON).readline())
    
    return dumpDict

#Intencoo de voto
#Ultima pesquisa datafolha? Medias das ultimas pesquisas?

#Dinheiro arrecadado
#Declarado no governo federal. Site? DB?

#Principais doadores
#Exibidos no site do governo federal. Site? DB?
