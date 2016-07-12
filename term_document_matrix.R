
library(tm)
a <- c("Hello hello hello! You have won the Jackpot jA@ckpot for USD $80 million. To encash your prize, mail your credit card number to sab030193@gmail.com", "hello!!! YOU HAVE won $1 million for playing at the casino this Friday. To avail the offer please send your debit card number and its :'sf@'ATM pin to 8983331089","Hey brother! How are you? Hope you are doing fin@----#<>e. What are your plans for this Sunday", "We have not m%^IT(et yet. But I as!!!sure you if you SEND ME YOUR account details, I will send you 10 million dollars")

myCorpus <- Corpus(VectorSource(a))
myCorpus
getTransformations()

toSpace <- content_transformer(function(x, pattern) {return (gsub(pattern, " ", x))})
myCorpus <- tm_map(myCorpus, toSpace, "-")
myCorpus <- tm_map(myCorpus, toSpace, ":")
myCorpus <- tm_map(myCorpus, removePunctuation)

writeLines(as.character(myCorpus[[3]]))

myCorpus <- tm_map(myCorpus, toSpace, "'")
myCorpus <- tm_map(myCorpus,content_transformer(tolower))
  
myCorpus <- tm_map(myCorpus, removeWords, c(stopwords('english'),"hope","sunday"))
writeLines(as.character(myCorpus[[3]]))



tdm <- TermDocumentMatrix(myCorpus)
tdm
b <- inspect(tdm)
b <- as.matrix(b)
b <- t(b)
b




#tdm <- TermDocumentMatrix(myCorpus, control = list(removePunctuation = TRUE, stopwords=TRUE))
#tdm
#b <- inspect(tdm)
#b <- as.matrix(b)
#b <- t(b)
#b


?tm_map


