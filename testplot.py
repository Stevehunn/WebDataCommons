import streamlit as st
from streamlit_option_menu import option_menu
import plotly.express as px
import pandas as pd
import json
import glob
import re
from matplotlib import pyplot as plt

from upsetplot import plot, from_memberships, UpSet


def content_testplot():
    st.write("genere plot")
    with open('./newData/after/Action.json', 'r') as f:
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
    df_up = df.groupby(list_labels).value_counts()
    for i in range(len(df_up)):
        df_up[i] = count_column[i]

    st.write(df_up)
    plot(df_up, orientation='horizontal')
    plt.savefig("lama.svg")
    st.image("lama.svg")
    st.write("finished.")
