# Twitter Political Censorship
Diego Wahl

# Abstract
Using Tweets as the basis for our dataset, we sought to explore the variety of political discussions on Twitter, and see if it could lend us any information as to whether one could reasonably say that certain political ideologies, namely those of the American right-wing, are 'censored' in any capacity on Twitter. In order to do so, we decided to look into the topics of conversation as relates to two key political figures in contemporary American politics, Biden and Trump, separately. By performing sentiment analysis, topic modeling, and creating a Scattertext to compare and contrast the lexicon of the formed conversations we believe that one can gather insights as to whether certain topics and conversations are indeed suppressed on Twitter. 

# Design
This project aimed to investigate and display the topics formed by Twitter discourse in relation to the two aforementioned political figures. By performing topic modeling and sentiment analysis, we hope to display that at least some specific claims regarding ideological censorship on Twitter, namely claims that topics potentially damaging to the American political left-wing are being censored, are not indeed suppressed in a major capacity on the platform. 

# Data
Data for this project were pulled directly from Twitter via the Twitter API in conjunction with Tweepy in order to 'stream' tweets as they were posted live. Specifically, the timeframe for the scraping of these tweets was limited to the week of June 14th, 2021. Additionally, scraped tweets were categorized as belonging to one of two groups, either the Biden dataset or the Trump dataset, on the basis of the search terms used to scrape those specific tweets (that is, on 'Biden' and Biden related search terms, and vice-versa for Trump). In total, some 70,000 tweets were scraped for each dataset, totaling over 140,000 tweets to form our corpuses. 

# Algorithms
A variety of unsupervised learning tools in Python were employed throughout the scope of this project:
* CorEx topic modeling was used to create both baseline topics, i.e., without the use of anchor words, as well as to further refine the topics created via the use of anchor words. The topics formed can then naturally give us insights as to what topics of conversation are prevelant and being discussed on the platform. 
* A Scattertext was created from the two datasets in order to compare common words and topics and how they differ between the two sets.
* VADER Sentiment analysis was performed to get a rough gauge of how positively or negatively each topic was discussed.
* Lastly, Word Clouds were created for each set to display common words associated with each topic.

# Tools
* Twitter API and Tweepy for data-gathering
* SKLearn's implementation of CountVectorizer and TF-IDF
* Corextopic Python package for (CorEx) topic modeling
* Scattertext Python package for Scattertext creation
* VaderSentiment Python package for sentiment analysis
* Wordcloud Python package for Word Cloud creation

# Communication
Findings were communicated to Metis cohort.
