import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import plotly.figure_factory as ff
import plotly.graph_objects as go
import plotly.io as pio
import numpy as np

from sklearn.preprocessing import LabelEncoder
import warnings

# Ne pas afficher les messages de warning
warnings.filterwarnings('ignore')

st.set_page_config(page_title="My Streamlit App",layout="wide" )

# Load data

# Récupérer les fichiers Excel téléchargés par l'utilisateur
files = st.file_uploader("Choose Excel files", type=["xlsx"], accept_multiple_files=True)

# Concaténer tous les fichiers en un seul dataframe

if files:
    dfs = []
    for file in files:
        df2 = pd.read_excel(file, header=1)  # spécifier la ligne de l'en-tête
        dfs.append(df2)
    df = pd.concat(dfs, ignore_index=True)
    


    df = df.rename(columns={'Je suis':'Genre'})

    for i in range(len(df["Genre"])): 
        if df["Genre"][i]== 'un homme':
            df["Genre"][i] = 'homme' ,
        elif df["Genre"][i] =='une femme':
            df["Genre"][i] = 'femme'
        else: continue    

    df["Age"]=df["55 ans et plus"]
    for i in range(len(df["15-20 ans"])): 
        if df["15-20 ans"][i]== '15-20 ans':
            df["Age"][i] = "15-20 ans"
        elif df["21-25 ans"][i] =='21-25 ans':
            df["Age"][i] = "21-25 ans" 
        elif df["26-30 ans"][i] =='26-30 ans':
            df["Age"][i] = "26-30 ans" 
        elif df["31-35 ans"][i] =='31-35 ans':
            df["Age"][i] = "31-35 ans" 
        elif df["36-40 ans"][i] =='36-40 ans':
            df["Age"][i] = "36-40 ans" 
        elif df["41-45 ans"][i] =='41-45 ans':
            df["Age"][i] = "41-45 ans" 
        elif df["46-50 ans"][i] =='46-50 ans':
            df["Age"][i] = "46-50 ans" 
        elif df["51-55 ans"][i] =='51-55 ans':
            df["Age"][i] = "51-55 ans" 
        elif df["55 ans et plus"][i] =='55 ans et plus':
            df["Age"][i] = "55 ans et plus"
        else : df["Age"][i] = 0
        
    df=df.drop(["51-55 ans","46-50 ans","36-40 ans","41-45 ans","15-20 ans","31-35 ans","21-25 ans","26-30 ans","55 ans et plus"],axis="columns")
    df=df.drop(["#", "Network ID", "Start Date (UTC)", "Submit Date (UTC)"], axis = 1)
else:
    st.warning("Veuillez insérer votre/vos excel")

# le = LabelEncoder()
# df['AGE_INT'] = le.fit_transform(df['Age'])


# Set up sidebar
st.sidebar.title("Data Visualisation des données du Hackathon")

chart_type = st.sidebar.selectbox(
    "Choose a chart type",
    ["Histogram", "Circle plot", "Box plot", "Heatmap"]
)



# Histogram

if chart_type == "Histogram":
    st.header("Histogram")
    st.write("")
    x_col = st.selectbox("Select a column for the x-axis", df.columns)
    # Créer l'histogramme avec Plotly
    fig = px.histogram(df[x_col], nbins=30, width=600, height=600)
    fig.update_traces(showlegend=False)
    fig.update_layout(
    title={
        'text': 'Répartition de la variable',
        'y':0.95,
        'x':0.5,
        'xanchor': 'center',
        'yanchor': 'middle',
        'font': dict(
            size=30,
            color= '#84E4F8')})
    

    # Afficher le graphique avec Streamlit
    st.plotly_chart(fig, use_container_width=True)


    
    
    
# Circle plot
elif chart_type == "Circle plot":
    
    var_analy=st.selectbox('Choisissez la variable d''analyse',df.columns.tolist())
    cat_analy=st.multiselect('Choisissez la catégorie d''analyse',df[var_analy].unique(), default=df[var_analy].unique())
    df_circleplot=df[df[var_analy].isin(cat_analy)]
    
    truc1 = pd.Series(df_circleplot.index, index=df_circleplot['Genre']).groupby(level=0).size().tolist()
    label_truc1 = df_circleplot['Genre'].unique().tolist()
    fig1 = go.Figure(data=[go.Pie(labels=label_truc1, 
                                      values = truc1,
                                      hole=.4)])
    fig1.update_layout(
            title_text="Répartition des genres", title_x =0.32)

    
    truc2 = pd.Series(df_circleplot.index, index=df_circleplot['Age']).groupby(level=0).size().tolist()
    label_truc2 = df_circleplot['Age'].unique().tolist()
    fig2 = go.Figure(data=[go.Pie(labels=label_truc2, 
                                      values = truc2,
                                      hole=.4)])
    fig2.update_layout(
            title_text="Répartition des ages", title_x =0.32)

    
    truc3 = pd.Series(df_circleplot.index, index=df_circleplot['Je vis']).groupby(level=0).size().tolist()
    label_truc3 = df_circleplot['Je vis'].unique().tolist()
    fig3 = go.Figure(data=[go.Pie(labels=label_truc3, 
                                      values = truc3,
                                      hole=.4)])
    fig3.update_layout(
            title_text="Répartition des lieux de résidence", title_x =0.21)
    
    truc4 = pd.Series(df_circleplot.index, index=df_circleplot['Je suis.1']).groupby(level=0).size().tolist()
    label_truc4 = df_circleplot['Je suis.1'].unique().tolist()
    fig4 = go.Figure(data=[go.Pie(labels=label_truc4, 
                                      values = truc4,
                                      hole=.4)])
    fig4.update_layout(
            title_text="Répartition des rôles", title_x =0.26)

    # Diviser la page en deux colonnes et deux rangées
    col1, col2 = st.columns(2)

    with col1:
            st.plotly_chart(fig1)
            st.plotly_chart(fig2)

    with col2:
            st.plotly_chart(fig3)
            st.plotly_chart(fig4)
        
        
        
        
# Box plot
elif chart_type == "Box plot":
    st.header("Box plot")
    x_col = st.selectbox("Select a column for the x-axis", df.columns)
    y_col = st.selectbox("Select a column for the y-axis", df.columns)

    # Création de la figure
    fig = px.box(df, x=x_col, y=y_col)
    fig.update_layout(
    width=1500,
    height=700,
    title={
        'text': 'Box plot de x en fonction de y',
        'y':0.95,
        'x':0.5,
        'xanchor': 'center',
        'yanchor': 'middle',
        'font': dict(
            size=30,
            color='#84E4F8')
    },
    xaxis_title= "variable selectionnée en x",
    yaxis_title= "variable selectionnée en ",
    font=dict(size=18),
    hoverlabel=dict(
        font=dict(size=18)
    )
)


    # Affichage de la figure
    st.plotly_chart(fig, width=1000, height=1000)

    
    
    
    
    
# Heatmap
else:
    
    st.header("Heatmap des corrélations entre les questions")
    st.write("")
    
    # Liste des colonnes disponibles pour la sélection
    all_columns = df.columns.tolist()

    # Sélection des colonnes
    selected_columns = st.multiselect("Sélectionner les colonnes", all_columns)
    
    # Fonction pour calculer la matrice de corrélation et créer la visualisation
    def correlation_matrix(data, columns):
        
        # Créer la heatmap avec Plotly
        # Sélection des colonnes à utiliser dans la matrice de corrélation
        options = columns
        
        # Création de la matrice de corrélation
        fig = ff.create_annotated_heatmap(
            z=np.round(data[options].corr().values, decimals=2),
            x=options,
            y=options,
            colorscale='purples',
            showscale=False,
            reversescale=False,
        )

        # Mise en forme de la matrice de corrélation
        fig.update_layout(
        title="Matrice de corrélation",
        xaxis={'title': 'Variable',
               'tickmode': 'array',
               'tickvals': [i for i in range(len(options))],
               'ticktext': [col[:10] + "..." if len(col) > 13 else col for col in options]},
        yaxis={'title': 'Variable',
               'tickmode': 'array',
               'tickvals': [i for i in range(len(options))],
               'ticktext': [col[:10] + "..." if len(col) > 13 else col for col in options]},
        width=800, height=800
    )

        # Affichage de la matrice de corrélation sur Streamlit
        st.plotly_chart(fig)
        
    # Appel de la fonction pour créer la matrice de corrélation
    if selected_columns:
        correlation_matrix(df, selected_columns)
    else:
        st.warning("Veuillez sélectionner au moins une colonne.")

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
