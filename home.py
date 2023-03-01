import streamlit as st
import requests
from PIL import Image
from streamlit_lottie import st_lottie

st.set_page_config(page_title="My Streamlit App")
def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code !=200:
        return None
    return r.json()
lottie_h = load_lottieurl("https://assets8.lottiefiles.com/packages/lf20_49rdyysj.json")

def main() : 
     
    # st.image('https://langagevisuel.unistra.fr/fileadmin/Contenu/2.1_signature_universite/gif-image-detouree-retina.gif',width=800)
    # st.title("Hackathon Dashboard")
    # st.write('##')
     #c'est vraiment trop moche mec, je suis dsl


    st.subheader("What is this website ?")
    st.write(
        """
        This project is a response of a need of sociology reserachers of the university of Strasbourg. They wanted a visualisation tools to easily see what the data is all about.
        The data that will be uploaded directly uploaded from the user's computer to the website. The data that will be uploaded by sociologists come from surveys done during different hackatons. We then created a "dynamic" tool so the reserachers can upload their excel data in it as long as it respect the initial form.
        
        """
        )
    st.write(
        """
        [here find the full code](https://github.com/LANEVE/Dashboard_Hackathon)
        """
        )
    st.write("---")
    st.subheader("How it works")   
    st.write(
        """
        1. Upload your excel files in the section make for. The file must be a .XLSX either it wont work? If you see a weird red error message it is because you didn't upload anything yet'
        
        2. Select the different vizualisation you want between histogram, circle plot, boxplot and a heatmap.
        
             a. the histogram is usefull to see the repartition of a varaible among your dataset
             
             b. circle plot gives information about gender, place of living, ages and jobs repartition among the participants. We added a filter by question. For example if you want to see what kind of profile like best a question.
        
             c. boxplot to observe repartition of a certain variable depending of an other
             
             d. heatmap to glance any correlation between variables
        """
        )

    st.write("##")
    with st.container() :
        st.write("---")
        left_column, right_column = st.columns(2)
        with left_column :
            st.write("##")
            st.write(
                """
                
                
                We hope you will find something interesting using our tools !
        
                """)
        with right_column :
            st_lottie(lottie_h, height=200, key="morty")
    
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