import streamlit as st
import pickle
import string
import nltk
nltk.download('punkt_tab')
nltk.download('stopwords')
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer

ps=PorterStemmer()

def transform_text(text):
  text=text.lower()
  text=nltk.word_tokenize(text)

  y=[]
  for i in text:
    if i.isalnum:
      y.append(i)
  text=y[:]
  y.clear()

  for i in text:
    if i not in stopwords.words('english') and i not in string.punctuation:
      y.append(i)

  text=y[:]
  y.clear()

  for i in text:
    y.append(ps.stem(i))

  return " ".join(y)

tfidf=pickle.load(open('Vectorizer.pkl','rb'))
model=pickle.load(open('model (2).pkl','rb'))

st.title("Email/Sms Spam Classifier")
input_sms=st.text_area("Enter the Message")

if st.button("Predict"):
  transformed_text=transform_text(input_sms)
  vector_input=tfidf.transform([transformed_text])
  result=model.predict(vector_input)[0]
  if result==1:
      st.header("Spam")
  else:
      st.header("Not Spam")