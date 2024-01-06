import base64
import json
import os.path

import pandas as pd
import streamlit as st
from matplotlib import pyplot as plt
from upsetplot import plot

from parse import setLink


def content_testplot(target_select, before):
    row = ["10", "15", "20", "30", "40", "50", "all"]
    if before is True:
        namekey = "before"
    else:
        namekey = "after"
    selectrow = st.selectbox("Select the number of column to display", row, index=0, key=namekey)
    result = target_select.split(":")[1]
    if before is True:
        cheminTarget = './newData/before/' + result + '.json'
        cheminImage = './tempSvg/' + selectrow + result + "before.svg"
        cheminImageComplet = './tempSvg/' + result + "beforecomplet.svg"
    else:
        cheminTarget = './newData/after/' + result + '.json'
        cheminImage = './tempSvg/' + selectrow + result + "after.svg"
        cheminImageComplet = './tempSvg/' + result + "aftercomplet.svg"

    with open(cheminTarget, 'r') as f:
        data_dict = json.load(f)
    if len(data_dict) != 0:
        if os.path.exists(cheminImage) and selectrow !="all":
            col1, col2 = st.columns(2)
            with col1:
                filename1 = cheminImage.replace('./tempSvg/', '')
                with open(cheminImage, "rb") as f:
                    contenu = f.read()
                f.close()
                st.markdown(
                    f'<a href="data:application/octet-stream;base64,{base64.b64encode(contenu).decode()}" download="{filename1}">Download plot</a>',
                    unsafe_allow_html=True, )

            with col2:
                filename2 = cheminImage.replace('./tempSvg/', '')
                with open(cheminImage, "rb") as f:
                    contenu = f.read()
                f.close()
                link = setLink(namekey,selectrow,filename2)
                st.markdown(
                    "[Show raw json file](%s)" %link,
                    unsafe_allow_html=True, )
            st.image(cheminImage)
            return
        if os.path.exists(cheminImageComplet) and selectrow =="all":
            col1, col2 = st.columns(2)
            with col1:
                filename1 = cheminImageComplet.replace('./tempSvg/', '')
                with open(cheminImageComplet, "rb") as f:
                    contenu = f.read()
                f.close()
                st.markdown(
                    f'<a href="data:application/octet-stream;base64,{base64.b64encode(contenu).decode()}" download="{filename1}">Download plot</a>',
                    unsafe_allow_html=True, )

            with col2:
                filename2 = cheminImageComplet.replace('./tempSvg/', '')
                with open(cheminImageComplet, "rb") as f:
                    contenu = f.read()
                f.close()
                link = setLink(namekey, selectrow, filename2)
                st.markdown(
                    "[Show raw json file](%s)" % link,
                    unsafe_allow_html=True, )
            st.image(cheminImageComplet)
            return
        else:
            # get all labels
            labels = set()
            for item in data_dict:
                labels.update(item["pset"])
            # create bitmap from labels and counts
            list_labels = list(labels)
            df = pd.DataFrame([[e in item["pset"] for e in list_labels] + [item["count"]] for item in data_dict],
                              columns=list_labels + ["count"])
            count_column = df.pop("count")
            if selectrow != "all":
                select = int(selectrow)
                df_reduce = df.head(select)
                column_to_remove = list()
                for column in df_reduce.columns:
                    canary = False
                    for item in df_reduce[column]:
                        canary |= item
                    if not canary:
                        column_to_remove.append(column)
                for column in column_to_remove:
                    df_reduce.pop(column)
                    list_labels.remove(column)

                # ----------Save and Show n row of the dataframe------------------
                df_up = df_reduce.groupby(list_labels).value_counts()

                for i in range(len(df_up)):
                    df_up[i] = count_column[i]

                plot(df_up, orientation='horizontal')
                plt.savefig(cheminImage)
                plt.close()

                col1, col2 = st.columns(2)
                with col1:
                    filename1 = cheminImage.replace('./tempSvg/', '')
                    with open(cheminImage, "rb") as f:
                        contenu = f.read()
                    f.close()
                    st.markdown(
                        f'<a href="data:application/octet-stream;base64,{base64.b64encode(contenu).decode()}" download="{filename1}">Download plot</a>',
                        unsafe_allow_html=True, )

                with col2:
                    filename2 = cheminImage.replace('./tempSvg/', '')
                    with open(cheminImage, "rb") as f:
                        contenu = f.read()
                    f.close()
                    link = setLink(namekey, selectrow, filename2)
                    st.markdown(
                        "[Show raw json file](%s)" % link,
                        unsafe_allow_html=True, )
                st.image(cheminImage)
            else:
                # ----------Save and Show all the dataframe------------------
                df_up_all = df.groupby(list_labels).value_counts()

                for i in range(len(df_up_all)):
                    df_up_all[i] = count_column[i]

                plot(df_up_all, orientation='horizontal')
                plt.savefig(cheminImageComplet)
                plt.close()

                col1, col2 = st.columns(2)
                with col1:
                    filename1 = cheminImageComplet.replace('./tempSvg/', '')
                    with open(cheminImageComplet, "rb") as f:
                        contenu = f.read()
                    f.close()
                    st.markdown(
                        f'<a href="data:application/octet-stream;base64,{base64.b64encode(contenu).decode()}" download="{filename1}">Download plot</a>',
                        unsafe_allow_html=True, )

                with col2:
                    filename2 = cheminImageComplet.replace('./tempSvg/', '')
                    with open(cheminImageComplet, "rb") as f:
                        contenu = f.read()
                    f.close()
                    link = setLink(namekey, selectrow, filename2)
                    st.markdown(
                        "[Show raw json file](%s)" % link,
                        unsafe_allow_html=True, )
                st.image(cheminImageComplet)
    else:
        st.write("The file you selected is not available")
