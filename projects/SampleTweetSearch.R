---
title: "Twitter Search Example R Notebook"
author: Sophie Peet
output: html_notebook
---
#Install all of these packages using install.packages() to sucessfully run this code.
install.packages("rtweet")
install.packages("maps")
install.packages("dplyr")
install.packages("data.table")

#Make sure all packages are loaded with the library() function.
library(rtweet)
library(dplyr)
library(maps)
library(data.table)


ex <- search_tweets(
  
  "lang:en keyword", #use any keyword, set language to english
  
  include_rts = FALSE, #do not include retweets in search
  
  geocode = lookup_coords("usa"), #Only use tweets with location in the United States.
  
  n = 500000, #How many tweets should be searched.
  
  retryonratelimit = TRUE #Use this to let this functiion run on a loop until your 'n' is hit, twitter only allows 18000 tweets/15 minutes, this will let you run your chunk and then run every 15 minutes for as long as needed.
)

#Add latitude and longitude to each tweet.

ex <- lat_lng(ex)



# This filters to only geotagged tweets with a latitude, which will also have longitude.

ex <- subset(ex, !is.na(lat))

#Add these tweets to a file on your computer, to the same path where your R.md is saved.

fwrite(ex, file="ExampleTweetSearchKeyword.csv")