import pandas as pd
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
df=pd.read_csv("https://docs.google.com/spreadsheets/d/1pR7erKRNMoAv-bsGSLK0bDyIiA1mBCJ7L4NC_ZomXjE/export?format=csv&usp=sharing")
mymodel=SentimentIntensityAnalyzer()
x=df['Feedback']
l=[]
for k in x:
    pred=mymodel.polarity_scores(k)
    if(pred['compound']>0.5):
        l.append("Positive")
    elif(pred['compound']<-0.5):
        l.append("Negative")
    else:
        l.append("Neutral")
df['Sentiment']=l        
print(df)
df.to_csv("results.csv",index=False)
