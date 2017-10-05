#!/usr/bin/python
# -*- coding: utf-8 -*-

import csv
import codecs

def writeToXML():
    xmlFileName = 'myData.lsl' #creating destination file
    xmlFile = codecs.open(xmlFileName, 'w', 'utf-8')

    #creating the header of the file
    hardcodedHeader = writeHeader(xmlFile) 
    xmlFile.write(hardcodedHeader)

    reader = csv.DictReader(open('list.csv', encoding = 'utf - 8')) # opening csv as a dict
    codeIndex = 1

    for row in reader:
        for lang in row.keys():
            writeRow(xmlFile, language=makeLangAbb(lang), index=codeIndex, title=row[lang].strip())
        codeIndex += 1

    xmlFile.write(writeFooter(xmlFile)) 
    xmlFile.close()        

def writeHeader(xmlData):
    hardcodedHeader = """<?xml version="1.0" encoding="UTF-8"?>
<document>
 <LimeSurveyDocType>Label set</LimeSurveyDocType>
 <DBVersion>263</DBVersion>
 <labelsets>
  <fields>
   <fieldname>lid</fieldname>
   <fieldname>label_name</fieldname>
   <fieldname>languages</fieldname>
 </fields>
 <rows>
 <row>
  <lid><![CDATA[6]]></lid>
  <label_name><![CDATA[Country list]]></label_name>
  <languages><![CDATA[ar zh-Hans da nl en fi fr de hi it ja ko fa pl pt ru es sv th tr uk ur vi pt-BR]]></languages>
 </row>
 </rows>
</labelsets>
<labels>
 <fields>
  <fieldname>lid</fieldname>
  <fieldname>code</fieldname>
  <fieldname>title</fieldname>
  <fieldname>sortorder</fieldname>
  <fieldname>language</fieldname>
  <fieldname>assessment_value</fieldname>
 </fields>
<rows>""" + '\n'
    return hardcodedHeader

def writeRow(xmlFile, index, language, title):
        xmlFile.write('<row>' + '\n')
        xmlFile.write(' ' + '<lid>6</lid>' + '\n')
        xmlFile.write(' ' + '<code>A' + str(index)  + '</code>' + '\n')
        xmlFile.write(' '  + '<title><![CDATA[' + title + ']]>' +'</title>' + '\n')
        xmlFile.write(' ' + '<sortorder>'  + str(index-1)  + '</sortorder>' + '\n')
        xmlFile.write(' '  + '<language>' + language + '</language>' + '\n')
        xmlFile.write(' ' + '<assessment_value>0</assessment_value>' + '\n')        
        xmlFile.write('</row>' + '\n') 

def makeLangAbb(language):
    langAbbrev = {'English': 'en', 'Arabic': 'ar', 'French': 'fr', 'Spanish': 'es', 'Swedish': 'sv', 'Dutch': 'nl', 'Danish': 'da', 'Finnish': 'fi', 'Italian': 'it',
                  'Vietnamese': 'vi', 'Korean': 'ko', 'Russian': 'ru', 'German': 'de', 'Thai': 'th', 'Mandarin-Chinese': 'zh-Hans', 'Japanese': 'ja', 'Turkish': 'tr',
                  'Hindi': 'hi', 'Ukrainian': 'uk', 'Persian': 'fa', 'Portuguese': 'pt', 'Polish': 'pl', 'Urdu': 'ur', 'Brasilian Portugese': 'pt-BR'}

    for fullLang, abbLang in langAbbrev.items():
        if fullLang == language:
            language = abbLang

    return language

def writeFooter(xmlData):
    footer = """
  </rows>
 </labels>
</document>"""
    return footer 
    

writeToXML()

print ("done")  



