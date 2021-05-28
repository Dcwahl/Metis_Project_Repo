# Tweet Keyword Search Engine 
Diego Wahl

# Abstract
Using Tweets as the basis for our dataset, we sought to design a system to:
1. Intake and store Tweets (as a foundation for future projects)
2. Pull, process, and convert the Tweets into matrices of token counts (that is, counts of occurrences between two words in a Tweet)
3. Store those matrices in an equivalent database schema
4. Design an interface that can receive an input of a search term and output the most 'related' (that is, the most co-occurring) words to the search term.
Importantly, the system was intended to handle large quantities of data (100,000+ individual Tweets, in this context) in an appropriate and timely fashion. 

# Design
This project sought to create a keyword search mechanism that could be pulled from in a reasonable capacity and time. In order to accomplish the goal of pulling keywords in a reasonable time, a well-structured database was required to avoid any major calculations at time of query.  
Although at face-value one may assume that a matrix would lend itself to a relational database, due to A) the scarcity of data points, B) that matrices in Python/Numpy (which are default outputs of SKLearn's CountVectorizer) do not inherently have a concept row and column identifiers, it was decided that the appropriate approach to storage would be by way of a non-relational (Mongo DB) database. Each document in the collection consists of word field to identify the search term, followed by a dictionary of words and their values corresponding to their co-occurrence with the search term. This reduces the querying to a simple find of the appropriate word/search term, followed by a quick calculation to find the word with the highest value, and thus highest correspondence with the search term.

# Data
Data for this project were pulled directly from Twitter via their API using Python with the Tweepy Python library. We found that taking advantage of the Streaming framework (i.e., receiving the Tweets as they are posted live) was the most appropriate approach given the scale of the intended dataset. In addition to storing the Tweets themselves, we also gathered the Quoted-Tweets when appropriate, as well as the text of the Re-Tweet for any Re-Tweet.
In total, we gathered over 100,000 individual Tweets, though this choice in quantity was relatively arbitrary. Due to the volume of tweets that occur, this dataset can be scaled up quite quickly as needed.

# Algorithms
Data in the form of tweets were cleaned via standard text pre-processing approaches, including; stemming, removal of punctuation and ASCII characters, and removal of twitter-specific strings such as handles. 
A key piece in the deployment of this model is the process in which the tweets, after cleaning, are fed into SKLearn's CountVectorizer() function to create our co-occurrence matrices. Due to the sparsity of the resultant matrix, and the nature of this particular method, we found it was best to feed tweets into the vectorization process in smaller chunks (on the order of 500 at a time) to avoid unecessary run-time in the subsequent transformations to a well-structured JSON format for insertion into MongoDB.

# Relevant Tools
* Twitter API and Tweepy for data-gathering
* MongoDB for storage
* SKLearn and Spark for Vectorizing
* Streamlit for front-end/web app

# Communication
A front-end app/interface was created in order to query from the keyword database via Streamlit, and the findings of this project were presented to Metis cohort. 
