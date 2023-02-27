import streamlit as st
import requests
from PIL import Image


st.set_page_config(page_title="My Streamlit App", layout="wide")
st.markdown("""
<style>
body {
    background-color: #1E1E1E;
    color: #FFFFFF
}
</style>
""", unsafe_allow_html=True)


def main() : 
    st.title("Hackathon Dashboard")
    st.write('##')

    st.subheader("Why this project")
    st.write(
        """
        The goal of this prject was to create a tool which analyze sentences and detect
        if the sentences is sarcastic or not using NLP (Natural Language Processing).  
        
        First of all, before any model creation we need data. The database come from Kaggle.
        This dataset is filled with articles headlines of two different websites. huffingpost and theonion
        This dataset contains two different labels, 1 for sarcastic and 0 if not sarcastic.
        TheOnion is known to publish very sarcastic news helping us with high quality sarcastic healines.
        """
        )
    st.write(
        """
        [here find the dataset](https://www.kaggle.com/datasets/saurabhbagchi/sarcasm-detection-through-nlp)
        """
        )
    st.write("##")
    st.subheader("How it works")   
    st.write(
        """
        We had more or less 50/50 with sarcastic sentences and not sarcastics headlines for a total of 26.000 headlines.
        We then cleaned the database, removed stop_words, etc... and convert all words to tokens. After getting our bag of words 
        we vectorized it and use a logistic regression to train a model. 
        
        We end up having a 90% precision with this model.
        """
        )

    st.write("##") 
    st.image('https://mir-s3-cdn-cf.behance.net/project_modules/fs/bc90cc81411939.5d2f90e336b69.gif',width=1000)
    
if __name__ == '__main__' :
    main()