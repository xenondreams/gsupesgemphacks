# -*- coding: utf-8 -*-
"""
Created on Fri Dec  1 17:07:00 2023

Generates a comma seperate list of card names and underlying vcards using 
an .xml decklist exported from gemp

@author: gsupestar

Sponsored by the CT CNTGNT in celebration of the First Annual BeezerBowl


"""

import xml.etree.ElementTree as ET
import os 
import csv

#change to working directory if you need to 
os.chdir('C:\\Users\\miket\\Downloads')

#set file name for deck list (from gemp) and master card list (csv format)
deckname = "open tatooine objective etc.txt"
masterlist = "Star_Wars_CCG_Master_Cardlist_11_14_2023.xlsx - FullCardList.csv"


#searches master card list for card name and underlying card
def find_voucher(cardname,filename):
    with open(filename, "r") as infile:
        reader = csv.reader(infile)
        next(reader)
        for line in reader:
           if cardname == line[4]:
                return line[5]     

#iterates though deck and prints it all out
print("CARD, UNDERLYING CARD")
balls = open(deckname)
mytree = ET.parse(balls)
root = mytree.getroot()
for child in root.findall('card'):
    string = child.attrib
    title = string['title']
    print(title,",",find_voucher(title,masterlist))
   

##shields LOL
print("SHIELDS IF YOU WANT EM")
for child in root.findall('cardOutsideDeck'):
    string = child.attrib
    title = string['title']
    print(title,",",find_voucher(title,masterlist))





