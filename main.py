import streamlit as st
import pandas as pd
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import plotly.express as px
st.set_page_config(page_title="Sentiment Analysis System",page_icon="https://tse3.mm.bing.net/th?id=OIP.c3f3YCJHoLPDY84lxaZZsQHaHa&pid=Api&P=0&h=220")
st.title("SENTIMENT ANALYSIS SYSTEM")
choice=st.sidebar.selectbox("Main Menu",("HOME","ANALYSIS","VISUALIZATION"))
st.sidebar.image("https://tse3.mm.bing.net/th?id=OIP.p7CgQ0ovg8LeDYQlQa_ZIwHaDq&pid=Api&P=0&h=220")

if(choice=="HOME"):
    st.image("https://miro.medium.com/proxy/1*_JW1JaMpK_fVGld8pd1_JQ.gif")
    st.write("This is a Sentiment Analysis System that classify the customer reviews into 'Positive' ,'Negative' and 'Neutral' sentiments ,helping the organisation to take required actions to improve their product or services . ")   
elif(choice=="ANALYSIS"):
    url=st.text_input("Enter Google sheet URL(Please replace edit# with export?format=csv&)")
    btn=st.button("Analyze")
    if btn:
        df=pd.read_csv(url)
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
        df.to_csv("results.csv",index=False)
        st.subheader("Analysis Successful and saved as results.csv")
elif(choice=="VISUALIZATION"):
    df=pd.read_csv("results.csv")
    c=st.selectbox("Choose Category",("Positive","Negative","Neutral"))
    df2=df[df['Sentiment']==c]
    st.dataframe(df2)
    choice2=st.selectbox("Choose Visualization",("NONE","PIE","HISTOGRAM"))
    if choice2 == "PIE":
        pos_count = len(df[df['Sentiment'] == "Positive"])
        neg_count = len(df[df['Sentiment'] == "Negative"])
        neu_count = len(df[df['Sentiment'] == "Neutral"])
        total_count = len(df)
        pos_per = (pos_count / total_count) * 100
        neg_per = (neg_count / total_count) * 100
        neu_per = (neu_count / total_count) * 100
        fig = px.pie(values=[pos_per, neg_per, neu_per], names=["Positive", "Negative", "Neutral"])
        st.plotly_chart(fig)
    elif(choice2 == "HISTOGRAM"):
        k=st.text_input("Enter Category")
        if k:
            fig=px.histogram(x=df[k],color=df['Sentiment'])
            st.plotly_chart(fig)
        

    
    
