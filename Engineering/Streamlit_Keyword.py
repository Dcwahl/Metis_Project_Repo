import streamlit as st
from streamlit_tags import st_tags
from pymongo import MongoClient
import numpy as np
from operator import itemgetter

def findTopN(word,db,collectionName,n=3):
    cursor = db[collectionName].find({'word':word})
    listCursor = list(cursor)
    if len(listCursor)!=1:
        return None #may as well give up
    counts = listCursor[0]['counts']
    returnDict = dict(sorted(counts.items(), key = itemgetter(1), reverse = True)[:n])
    return list(returnDict.keys())

def findSuggestions(db,collectionName):
	cursor = db[collectionName].find({},{'_id':0,'word':1})
	listCursor = list(cursor)
	return [i['word'] for i in listCursor]

client = MongoClient()
db= client.testing
collName = 'processTest'
suggestions = findSuggestions(db,collName)
st.title('Search for keywords from our tweets!')


keywords = st_tags(
    label='Enter Search Word:',
    text='Enter Search Word',
    value=['boris'],
    suggestions=suggestions,
    maxtags = 1,
    key='1')

st.write('Results:')
result = findTopN(keywords[0],db,collName)
try:
	for i in result:
		st.write(i)
except (TypeError, IndexError):
	"Waiting on search word"

#st.write(findTopN(keywords[0],db,collName))
