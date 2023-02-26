import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import plotly.figure_factory as ff
import plotly.graph_objects as go


from sklearn.preprocessing import LabelEncoder
import warnings

# Ne pas afficher les messages de warning
warnings.filterwarnings('ignore')




st.set_page_config(page_title="My Streamlit App")
st.markdown("""
<style>
body {
    background-color: #1E1E1E;
    color: #FFFFFF
}
</style>
""", unsafe_allow_html=True)
st.set_option('deprecation.showPyplotGlobalUse', False)




# Load data
@st.cache
def load_data():
    df = pd.read_csv("Data_Hackathon.csv")
    le = LabelEncoder()
    df['AGE_INT'] = le.fit_transform(df['AGE'])
    df.drop("Unnamed: 0", axis=1,inplace=True)

    return df

df = load_data()

le = LabelEncoder()
df['AGE_INT'] = le.fit_transform(df['AGE'])



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
    fig.update_layout(
    title={
        'text': 'Histogramme de la question '+str(x_col),
        'y':0.95,
        'x':0.5,
        'xanchor': 'center',
        'yanchor': 'middle',
        'font': dict(
            size=50,
            color="black")})

    # Afficher le graphique avec Streamlit
    st.plotly_chart(fig, use_container_width=True)


    
    
    
# Circle plot
elif chart_type == "Circle plot":
    
    options = list(df.keys())
    selection = st.multiselect("Sélectionner les catégories à afficher:", options)

    # Créer les pie plots pour chaque catégorie sélectionnée
    for cat in selection:
        fig = go.Figure(df=[go.Pie(labels=list(df[cat].keys()), values=list(df[cat].values()))])
        fig.update_traces(hoverinfo='label+value', textinfo='percent+label')
        fig.update_layout(title=cat, width=400, height=400)
        st.plotly_chart(fig)

        
        
        
        
# Box plot
elif chart_type == "Box plot":
    st.header("Box plot")
    x_col = st.selectbox("Select a column for the x-axis", df.columns)
    y_col = st.selectbox("Select a column for the y-axis", df.columns)

    # Création de la figure
    fig = px.box(df, x=x_col, y=y_col)

    # Affichage de la figure
    st.plotly_chart(fig)

    
    
    
    
    
    
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
            z=data[options].corr().values,
            x=options,
            y=options,
            colorscale='purples',
            showscale=False,
            reversescale=False
        )

        # Mise en forme de la matrice de corrélation
        fig.update_layout(
            title="Matrice de corrélation",
            xaxis={'title': 'Variable'},
            yaxis={'title': 'Variable'},
            width=800, height=800
            
        )

        # Affichage de la matrice de corrélation sur Streamlit
        st.plotly_chart(fig)
        
    # Appel de la fonction pour créer la matrice de corrélation
    if selected_columns:
        correlation_matrix(df, selected_columns)
    else:
        st.warning("Veuillez sélectionner au moins une colonne.")