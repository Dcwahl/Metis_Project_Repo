# IMDB: Gaming the Rating System
Diego Wahl

# Abstract
IMDB is easily the most popular film and television related website currently on the internet. As a result, there is actually quite a bit to gain by having your film well rated and thus highly visible in the form of Top X lists by rating. This project looks to explore a number of features of the movies in the IMDB Top 1000 list by rating to see if a Linear Regressive Model can be trained to accurately predict whether a movie, based on these attributes, will be succesful in the IMDB rating system. The IMDB rating system is a community driven system in which users rate movies indivudually, and those scores are compiled to create the ranking on the IMDB website. As a result of this community driven approach, no perfect model can be created to predict the eventual rating of movies, but we look to explore just how close we can get with the features chosen. 

# Design
This project sought to create a working regression model in order to predict the IMDB ratings for movies using features solely available from the IMDB and Box Office Mojo websites. It should be noted that while IMDB rating are in fact discrete values, it should still suffice as a target variable. For reference, the allowed values for rating are on the range of [0,10] in .1 increments. Features were chosen on the basis of the idea that this model would be used ahead of a movie's release in order to predict an eventual IMDB score. Features include, but were not limited to: Runtime, Genre, Budget, MPAA Rating, and Month of Release.

# Data
The data used in this project were scraped entirely from IMDB and Box Office Mojo websites. In all, the top 1000 movies by rating from the IMDB were selected. It should be noted that while IMDB has an accessible API from which to pull (after all, IMDB is an acronym for Internet Movie Database), this project sought to employ and practice web scraping through Python. A more thorough model would likely include a more randomly selected volume of movies, rather than biasing towards just the top rated ones. Unfortunately, simply due to time constraints as well as the structure of the IMDB website, the top 1000 were selected due to ease of scraping. A fair amount of feature engineering was required due to variances in presented data. An example would include movie budgets, which were available in a number of different currencies and thus had to be adjusted accordingly.

# Algorithms
After training and scoring the dataset through a number of different regression models (namely: Linear, Polynomial, Ridge and LASSO regression), a Ridge Regression was chosen as the final model due to it's propencity towards a low mean absolute error in comparison to the other models. The Ridge's MAE of .221 shows that the model was able to routinely predict quite close to the actual rating values for those movies on which the model was tested. However, it should be noted that, regardless of choice of model, the R-squared values were generally small in magnitude, often on the order of 0.05 or lower. 

# Relevant Tools
* Selenium was used to scrape from IMDB as well as from Box Office Mojo for additional features (which happens to be a subsidiary of IMDB)

# Communication
Findings were shared with Metis Data Science cohort in addition to being posted on github. Matplotlib and Seaborn were used for visualization.
