#!/usr/local/bin/python
# -*- coding: UTF-8 -*-
# Rastreador de presidente / governador?
# @mtrpires

import cgitb
cgitb.enable()

from functions import Candidate

dilma = Candidate('Dilma Rousseff', 'dilmabr', '112476482098688',
                  'http://www.dilma.com.br/',
                  'http://pt.wikipedia.org/wiki/Dilma_Rousseff')
                  
aecio = Candidate('Aecio Neves', 'aecioneves', '411754008869486',
                  'http://www.aecioneves.com.br/',
                  'http://pt.wikipedia.org/wiki/Aecio_Neves')
                  
eduardo = Candidate('Eduardo Campos', 'eduardocampos40',
                    '100001008251772',
                    'http://www.eduardocampos40.com.br/',
                    'http://pt.wikipedia.org/wiki/Eduardo_campos')
                    
marina = Candidate('Marina Silva', 'silva_marina', '126351747376464',
                   'http://www.minhamarina.org.br/',
                   'http://pt.wikipedia.org/wiki/Marina_Silva')

candidatos = [dilma, aecio, eduardo, marina]

print "Content-type: text/html"
print 
print "<html>"
print "<body><p>"

for i in range(len(candidatos)):
    
    print "<h1>", candidatos[i].getName(), "</h1><h2>", candidatos[i].getNumFollowers(), "</h2> seguidores no twitter. </p><p>"
    print "Website:", candidatos[i].getWebsite(), "</p><p>"
    print "Wikipedia:", candidatos[i].getWiki(), "</p>"
    print "<h2>", candidatos[i].getNumTweets(), "</h2> tweets. </p><p>"
    print "<h2>", candidatos[i].getNumLikes(), "</h2> seguidores no Facebook. </p><p>"
    print
    print
    print "Últimos tweets: </p><p>"

    if candidatos[i].getNumTweets() == 0:
        print "Nenhum Tweet!</p><p>"
    else: 
        tweets = candidatos[i].getLatestTweets()
        for j in range(3):
            print "<h3>", tweets[j][u'text'].encode('utf_8'),"</h3></p><p>"
            
    print
    print "Últimas reportagens sobre", candidatos[i], "</p>"
    print
    news = candidatos[i].getStories()
    for k in range(3):
        print news[k].encode('utf_8')

print "</p></body>"
print "</html>"
