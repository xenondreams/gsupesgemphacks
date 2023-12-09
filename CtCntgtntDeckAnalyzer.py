# -*- coding: utf-8 -*-
"""
Created on Sat 12/9/23

Accepts as its input an exported xml decklist from GEMP, and provides
feedback on the quality of your deck!!!
@author: gsupestar

Sponsored by the CT CNTGNT in celebration of the First Annual BeezerBowl!!!
IYGTB


"""

import xml.etree.ElementTree as ET
import os 
import csv


#change to working directory if you need to 
os.chdir('C:\\Users\\miket\\Downloads')

#set file name for deck list (from gemp) and master card list (csv format)
DeckUnderTest = "open tatooine objective etc.txt"



#searches master card list for card name and underlying card

def CountNumberOfCardsInDeck(cardname,deckname):
    CardCount = 0
    balls = open(deckname)
    mytree = ET.parse(balls)    
    root = mytree.getroot()
    for child in root.findall('card'):
        string = child.attrib
        title = string['title']
        if title == cardname:
            CardCount += 1
    return CardCount
 

BeezerCount = CountNumberOfCardsInDeck("Corporal Beezers", DeckUnderTest)

print("You have this many Beezers:",BeezerCount)

if BeezerCount == 0:
    print("This is the worst deck of all time. Shame on you!!")
elif BeezerCount <= 1:
    print("This isn't the worst deck I've ever seen, but it ain't great")
elif BeezerCount <= 3:
    print("This is a half-decent deck, but needs some improvement")
elif BeezerCount <= 10:
    print("There is real potential here--this deck could be tournament ready!")
elif BeezerCount <= 30:
    print("This could be a great deck.  Lotsa potential.  You're close")
elif BeezerCount <= 60:
    print("This is the greatest deck of all time!!!")    
else:
    print("You have transcended space and time! OMFG!!!")









