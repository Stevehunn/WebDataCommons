import streamlit as st
from streamlit_option_menu import option_menu
import plotly.express as px
import pandas as pd
import json
import glob
import re
from matplotlib import pyplot as plt
from upsetplot import plot, from_memberships, UpSet

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


def content_testplot(target_classes):
    st.write("genere plot")
    target_select = st.selectbox("", target_classes)
    result = target_select.split(":")[1]
    cheminTarget = './newData/after/'+result+'.json'
    #st.write(cheminTarget)
    row = ["10", "15", "20", "30", "40", "50", "all"]
    select = st.selectbox("Select the number of row", row, index=0)
    with open(cheminTarget, 'r') as f:
    #with open('./newData/after/Action.json', 'r') as f:
        data_dict = json.load(f)
        # st.write(data_dict)
    #data_frame = pd.DataFrame(data_dict)
    #st.write(data_frame)
    # récuperer tous les labels
    labels = set()
    for item in data_dict:
        labels.update(item["pset"])
    # creer bitmap a partir des labels et des counts
    list_labels = list(labels)
    #st.write(list_labels)
    #st.write([[e in item["pset"] for item in data_dict] for e in list_labels])
    #df = pd.DataFrame([[e in item["pset"] for e in list_labels] for item in data_dict], columns=list_labels)
    df = pd.DataFrame([[e in item["pset"] for e in list_labels] + [item["count"]] for item in data_dict], columns=list_labels+["count"])
    count_column = df.pop("count")
    #st.write(df)
    if select !="all":
        select = int(select)
        df_reduce = df.head(select)
        column_to_remove = list()
        for column in df_reduce.columns:
            canary = False
            for item in df_reduce[column]:
                canary |= item
            if not canary:
                column_to_remove.append(column)
        #print(column_to_remove)
        for column in column_to_remove:
            df_reduce.pop(column)
            list_labels.remove(column)
        #st.write(df_reduce)

        #----------Save and Show n row of the dataframe------------------
        st.write("Show the number of rows select.")
        df_up = df_reduce.groupby(list_labels).value_counts()

        for i in range(len(df_up)):
            df_up[i] = count_column[i]

        #st.write(df_up)

        plot(df_up, orientation='horizontal')
        plt.savefig("lama.svg")
        st.image("lama.svg")

    if select == "all":
        # ----------Save and Show all the dataframe------------------
        st.write("Show all rows available.")
        df_up_all = df.groupby(list_labels).value_counts()

        for i in range(len(df_up_all)):
            df_up_all[i] = count_column[i]

        #st.write(df_up_all)

        plot(df_up_all, orientation='horizontal')
        plt.savefig("lamacomplet.svg")
        st.image("lamacomplet.svg")
        st.write("finished.")


