import streamlit as st
import requests
from PIL import Image


st.set_page_config(page_title="My Streamlit App")

def main() : 
     
    st.image('https://langagevisuel.unistra.fr/fileadmin/Contenu/2.1_signature_universite/gif-image-detouree-retina.gif',width=800)
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
    
    st.sidebar.write("##")
    st.sidebar.write("##")
    st.sidebar.write("##")
    st.sidebar.write("##")
    st.sidebar.write("##")
    st.sidebar.write("##")
    st.sidebar.write("##")
    st.sidebar.write("##")
    st.sidebar.write("##")
    st.sidebar.write("##")
    st.sidebar.write("##")
    st.sidebar.write("##")
    st.sidebar.write("##")
    st.sidebar.write("##")
    st.sidebar.write("##")
    st.sidebar.write("##")
    st.sidebar.write("##")
    st.sidebar.write("##")
    st.sidebar.image('https://cdn.discordapp.com/attachments/1017376281769300013/1079828396466516100/signature_unistra_fond_transparent.png',width=300)
    
if __name__ == '__main__' :
    main()