import streamlit as st
from streamlit_option_menu import option_menu
import plotly.express as px
import pandas as pd
import json
import glob
import re



def extraire_contenu_apres_backslash(ma_ligne):
    # Regex pour supprimer tout le contenu avant le dernier caractère '\'
    nouveau_contenu = re.sub(r'^.*\\', '', ma_ligne)
    return nouveau_contenu


def getCheminForImage(nomfichier):
    regexSelect = extraire_contenu_apres_backslash(nomfichier)
    # Utiliser split pour séparer la chaîne en fonction de ":"
    parts = regexSelect.split(":")

    # Concaténer les parties avec le format souhaité
    result = f"assets/plots/{parts[1]}_plot.svg"
    return result


# 2023 Analyse page Content
def content_2022(data_plotly_sunburst,data_plotly_treemap, target_classes):
    st.title("""Schema.org annotations observatory in 2022""")
    st.write("### Deep dive into WebDataCommons JSON-LD markup")
    st.markdown("---")

    st.markdown(
        """
        In the following sunburst plot, the count of typed entities is displayed through the 'value' attribute.
        """
    )


    print("Names in Treemap:")
   
    style = {
        "padding": 10,
        "width": "100%",
        "display": "inline-block",
        "vertical-align": "right",
    },

    # Display the Sunburst figure using st.plotly_chart
    # st.write("## Sunburst")
    # st.plotly_chart(figureSunburst, use_container_width=True, style=style)
    # st.markdown("---")
    # Display the Treemap figure using st.plotly_chart
    

    st.markdown("---")
    st.write("## Upset Plot")
    st.markdown(
        """
        Per-class top-10 property combinations.
        In the following upset plots, you can select a Schema.org class and display the most used property combinations (top-10).
        All these 776 plots have been rendered based on the Schema.org characteristic sets we pre-computed and made available at [https://zenodo.org/records/8167689](https://zenodo.org/records/8167689)

        """
    )
    # nomFichierAOuvrir = "assets/plots/3DModel_plot.svg"
    # st.image(nomFichierAOuvrir)
    # st.write('chemin complet nomFichierAOuvir:',nomFichierAOuvrir)
    # regexTargetClasse = extraire_contenu_apres_backslash(target_classes)
    # regexTargetClasse
    select = st.selectbox("", target_classes)
    result = getCheminForImage(select)
    col1, col2 = st.columns(2)
    
    with col1:
      
      st.image(result)
    
    with col2 :
     dd_data_plotly_sunburst = {"ids": [], "names": [], "parents": [], "values": []}
     parents_d = 0
      
     df_data_plotly_treemap = pd.DataFrame(data_plotly_treemap)
     
     filtred_data = df_data_plotly_treemap[df_data_plotly_treemap["names"]== select]
     
     # Parcourir le DataFrame et collecter les parents
     for index, row in df_data_plotly_treemap.iterrows():
      parent_name = row['parents']
      name = row['names']
      val= row['values']
      ids = row['ids']
     
      if  (parent_name == select):
        print("entree")
        parents_d=1
        dd_data_plotly_sunburst["parents"].append(parent_name)
        dd_data_plotly_sunburst["names"].append(name)
        dd_data_plotly_sunburst["values"].append(val)
        dd_data_plotly_sunburst["ids"].append(ids)


     if parents_d == 0 : 
       fig_all_data = px.treemap(
         filtred_data,
         ids= "ids",
         names= "names",
         parents= "parents",
         values="values",
         color= "values"
     )
     else:

      print(dd_data_plotly_sunburst)
      fig_all_data = px.treemap(
         dd_data_plotly_sunburst,
         ids= "ids",
         names= "names",
         parents= "parents",
         values="values",
         color= "values"
     )
     st.write("## Treemap")
     st.plotly_chart(fig_all_data, use_container_width=True, style=style, color= "streamlit")


