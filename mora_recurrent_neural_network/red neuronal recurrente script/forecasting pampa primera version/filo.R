data1 <- read.csv("C:\\Users\\LAC40641\\Desktop\\forecasting mora\\trend.csv")


#http://r-statistics.co/Time-Series-Analysis-With-R.html

tsData <- EuStockMarkets[, 1]
decomposedRes <- decompose(tsData, type="mult") # use type = "additive" for additive components
plot (decomposedRes) # see plot below
stlRes <- stl(tsData, s.window = "periodic")


#---------------------------------------------------------------
  

data2 <- read.csv("C:\\Users\\LAC40641\\Desktop\\forecasting mora\\trend2.csv")

tsData2 <- ts(
  data=data2[2], 
  start = c(2012,12), 
  end = c(2017,12), 
  frequency = 12)


decomposedRes<-decompose(tsData2, type="mult")
plot (decomposedRes)


--
  
data3 <- read.csv("C:\\Users\\LAC40641\\Desktop\\forecasting mora\\trend3.csv")

plot(data3[1])

tsData2 <- ts(
  data=data3[1], 
  start = c(2017,03,15), 
  end = c(2018,01,15), 
  frequency = 30)


decomposedRes<-decompose(tsData2, type="mult")
decomposedRes<-decompose(tsData2, type="additive")
plot (decomposedRes)


