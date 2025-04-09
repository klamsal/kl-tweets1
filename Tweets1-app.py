import streamlit as st
import pandas as pd
import plotly.express as px
import seaborn as sns
import matplotlib.pyplot as plt

# Load tweets data
tweets = pd.read_csv('https://raw.githubusercontent.com/klamsal/kl-tweets1/refs/heads/main/Tweets.csv')

# Display the dataframe in Streamlit
st.title("Tweets Analysis")
st.subheader("First 5 Rows of the Dataset")
st.write(tweets.head())

# Sentiment distribution plot
st.subheader("Count of Tweets by Sentiment")
sentiment_counts = tweets['airline_sentiment'].value_counts().reset_index()
sentiment_counts.columns = ['sentiment', 'count']

fig1 = px.pie(sentiment_counts,
              values='count',
              names='sentiment',
              title="Count of tweets by Sentiment")
st.plotly_chart(fig1)

# Airline tweet counts plot
st.subheader("Tweet Counts by Airlines")
airline_counts = tweets['airline'].value_counts().reset_index()
airline_counts.columns = ['airline', 'count']

# Create a bar plot using Seaborn
plt.figure(figsize=(10, 6))
sns.barplot(x='airline', y='count', hue='airline', palette='pastel', legend=False, data=airline_counts)
plt.title('Tweet counts by Airlines')
plt.xlabel('Airline')
plt.ylabel('Count')

# Display the plot in Streamlit
plt.tight_layout()
st.pyplot(plt)

