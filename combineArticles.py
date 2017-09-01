__author__ = "Huangxuanyu Gong"

#Open & read all needed xml files in folder record_archive
import os
from lxml import objectify
import sys

#needfiles = ['ABCNews.txt', 'CNN.txt', 'FOXNews.txt', 'BBCWorld.txt', 'NBCNews.txt', 'USAToday.txt']
needfiles =  ['CNN.txt', 'FOXNews.txt', 'NBCNews.txt']

#Create a dictionary
article_dict = {}
for key in needfiles:
    article_dict[key] = ""

for folder in os.listdir("./record_archive"):
    for file in needfiles:
        print(folder + "/" + file) 
        openfile = open("./record_archive/" + folder + "/" + file, 'r')
        readfile = openfile.read()
        openfile.close()
        #add root
        filestring = "<articles>\n"
        filestring += readfile
        filestring += "</articles>"
        #replace & with &amp;
        filestring = filestring.replace('&', '&amp;')
        #keep the title and description
        root = objectify.fromstring(filestring)
        for i in range(0, len(root.getchildren())):
            obj = root.getchildren()[i].getchildren()
            title = obj[1].text
            descrip = obj[3].text
            if title is None:
                title = ""
            elif title[len(title)-1] != '.' and title[len(title)-1] != '?':
                title += '.'

            if descrip is None:
                descrip = ""
            elif descrip[len(descrip)-1] != '.' and descrip[len(descrip)-1] != '?':
                descrip += '.'

            content = str(title) + "\n" + str(descrip) + "\n"
            article_dict[file] += content

#Put in new txt file in data directory
for key in article_dict.keys():
    new_file = open('./data/' + key, 'w')
    new_file.write(article_dict[key])
    new_file.close()
