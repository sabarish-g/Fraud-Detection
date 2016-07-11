# -*- coding: utf-8 -*-
"""
Created on Mon Jun 20 18:19:08 2016
Reading a smaller file for mails
@author: prato_s
"""
import re
import glob ## to get all files from a directory
#import lepl.apps.rfc3696
import pandas as pd
#import prettytable
import csv

''' Get the directory and list of files using glob '''
listoffiles = glob.glob('F:/Final Project - E-mail Fraud Detection/FRAUD E-Mail \
Database/From Patil Sir/Uncompressed/2002/temp/*.*')
print listoffiles

'''
Getting the entire content from the mails in a single list
We'll be separating out the list using the regular expressions to get different lists
which will be the features for the supervised learning

e.g. From, To, Timestamp, etc
'''

contentDict = {}
cnt = 1

'''TRY USING enumerate() instead of cnt+=1
Looks stupid
'''

for filename in listoffiles:
    with open(filename, 'r') as files:
        content = []
        for filecontent in files:
            content.append(filecontent)
                            
        contentDict[cnt] = content
        cnt += 1
        
print contentDict

'''
SNIPPET of code to check the logic
'''
'''##################         Starts here          ############################'''
contentDict1 = dict()
contentDict1['mail1'] = ['1,2,3,','getting the install \n']
contentDict1['mail2'] = ['1,2,3,','getting the install2222 \n']
print contentDict1

content = []

for k,v in contentDict1.items():
    for val in contentDict1[k]:
        print k
        temp = val.rstrip('\n')
        content.append(temp)
        
    contentDict1[k] = content
    
print contentDict1  

'''To join the lists in the dictionaries'''
cont = ' '.join(contentDict1['mail1'])
print cont

for k,v in contentDict1.items():
        cont = ' '.join(contentDict1[k])
        contentDict1[k] = cont

print contentDict1
        
'''To delete a item inside a list in dict element'''
del contentDict1['mail2'][contentDict1['mail2'].index('1,2,3,')]


'''##################         Ends here          ############################'''

'''
###### Separating out the contents of each mail into a feature list
'''
## Cleaner list
cleanDictOg = dict()

## To remove all the tabs and special characters
for k,v in contentDict.items():
    clean = []
    for val in contentDict[k]:
        temp = val.rstrip('\t\r\n')
        temp1 = re.sub(r'[\t]',r'', temp)
        if temp1 != '':
            clean.append(temp1)
    
    cleanDictOg[k] = clean

#print clean
print cleanDictOg[3]

cleanDict = cleanDictOg
print cleanDict
'''
To get all the special features from the mailers - Timestamp, To, From, Subject in 
separate lists
To separate out the content, need to pop out the other tags from the clean list

For that need to get the list[index], index from the operated value
Once we get the index, it is possible
'''

'''
Timestamp raw will provide 'From whom it was' and 'Who sent it'
'''
timestampRaw = {}
print timestampRaw

regex = r"(From |from:|From:)"

for k,v in cleanDict.items():
    for val in cleanDict[k]:
        if re.search(regex,val):
            temp = re.sub(regex, r'',val)
            print "The content of ",k," is :::::::::::::", temp
            timestampRaw[k] = temp.strip()
            del cleanDict[k][cleanDict[k].index(val)]
            break
        else:
            timestampRaw[k] = ''
        
        

print cleanDict[2]
print "The timestamp is ", timestampRaw

'''
Return-path seems to be the sender
NOTE: rstrip will do right strip, strip will remove from both ends
Search and replace with regular expressions work better always
Instead of creating a list, dictionary would be a good option -- NEXT Step

The Return-path is the higher level sender, not the actual sender
'''
returnPath = {}
#senderDict= dict()
regex = r"(Return-Path:|Return-path|return-path)"
reg = '[<>]'
for k,v in cleanDict.items():
    for val in cleanDict[k]:
        if re.search(regex,val):
            temp = re.sub(regex, r'',val)
            #print "The content of ",k," is :::::::::::::", temp
            returnPath[k] = re.sub(reg, r'',val)
            del cleanDict[k][cleanDict[k].index(val)]
            break
        else:
            returnPath[k] = ''

print "The list of Return Path is ", returnPath


'''
The recievers of the mails
'''
receiver = {}

regex = r"^(To:|to:)"
for k,v in cleanDict.items():
    for val in cleanDict[k]:
        if re.search(regex,val):
            temp = re.sub(regex, r'',val)
            #print "The value ",k, "is ",temp
            receiver[k] = temp.strip('<>')
            #print "The value of receiver ",k, "is", receiver[k]
            del cleanDict[k][cleanDict[k].index(val)]
            break
        else:
            receiver[k] = ''

print "The list of recievers is ", receiver

'''
The subject of the mails
'''
subject = {}
regex = r"^(Subject:|subject:)"
for k,v in cleanDict.items():
    for val in cleanDict[k]:
        if re.search(regex,val):
            temp = re.sub(regex, r'',val)
            subject[k] = temp.strip()
            del cleanDict[k][cleanDict[k].index(val)]
            break
        else:
            subject[k] = ''

print subject

'''
Timestamp of the mail
'''
timestamp = {}
regex = r"^(Date:|date)"
for k,v in cleanDict.items():
    for val in cleanDict[k]:
        if re.search(regex, val):
            temp1 = re.sub(regex,r'', val)
            timestamp[k] = temp1
            
            del cleanDict[k][cleanDict[k].index(val)]
            break
        else:
            timestamp[k] = ''

print timestamp

'''
Get the Message-ID
'''
messageID = {}
regex = r"^(Message-ID:|Message-Id:|Message-id|message-id)"
for k,v in cleanDict.items():
    for val in cleanDict[k]:
        if re.search(regex, val):
            temp = re.sub(regex, r'', val)
            messageID[k] = temp.strip('<>')
            
            del cleanDict[k][cleanDict[k].index(val)]
            break
        else:
            messageID[k] = ''

print messageID

'''
Getting the content type and Content-transfer-encoding
'''
contentType = {}
regex = r"^(Content-Type:|content-type|Content-type)"
for k,v in cleanDict.items():
    for val in cleanDict[k]:
        if re.search(regex, val):
            temp = re.sub(regex, r'', val)
            contentType[k] = temp.strip()
            
            del cleanDict[k][cleanDict[k].index(val)]
            break
        else:
            contentType[k] = ''

print contentType

contentEncoding = {}
regex = r"^(Content-Transfer-Encoding: )"
for k,v in cleanDict.items():
    for val in cleanDict[k]:
        if re.search(regex, val):
            temp = re.sub(regex, r'', val)
            contentEncoding[k] = temp.strip()
            
            del cleanDict[k][cleanDict[k].index(val)]
            break
        else:
            contentEncoding[k] = ''
        
print contentEncoding

print cleanDict

'''
GET THE CONTENT HERE
To delete all the remaining tags, so that we can get only the content in the final file.
Using Regex to remove the majority of the unnecessary tags, might be possible that all
the words might not be removed, for that another round of pre-processing might be 
required while creating the term document matrix
'''
contentForTermDoc = {}

regex = r"""(Delivered|Received|Received:|POP|EMAP|ESMTP id|Sender:|Mime-Version|
Mime-version|X-Priority|X-priority|IMAP|SMTPSVC|X-Authentication-Warning:|
localhost|From:|MIME-Version:|X-Mailer:|X-Mimeole:|Thread-Index:|Content-Class:|
X-Originalarrivaltime:)"""

for k,v in cleanDict.items():
    for val in cleanDict[k]:
        if re.search(regex, val):
            print "The content from ", k, ":::::",val
            del cleanDict[k][cleanDict[k].index(val)]
            
        
print contentEncoding

print cleanDict

'''Joining all the content in the list as one column
The csv file is going to bulge
'''
for k,v in cleanDict.items():
        cont = ' '.join(cleanDict[k])
        cleanDict[k] = cont

print cleanDict[1]

'''
Convert the lists into dataframes
'''
table = [timestamp, returnPath, receiver, subject, messageID,contentType, 
         contentEncoding, cleanDict]
print table

dataframe = pd.DataFrame(table)
print dataframe
## Transpose the data 
dataframe = dataframe.transpose()
col = ['Timestamp', 'Sender', 'Reciever', 'Mail subject', 'MessageID', 
       'Content Type', 'Content Encoding', 'Content']

dataframe.columns = col
dataframe['Spam'] = 'Yes'

print dataframe

dataframe.to_csv('final_dataset.csv')