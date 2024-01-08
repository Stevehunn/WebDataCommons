import base64
import json
import os.path

import pandas as pd
import streamlit as st
from matplotlib import pyplot as plt
from upsetplot import plot

from parse import setLink, setLinkSchema


def content_testplot(target_select, before, subdir: str):
    row = ["10", "15", "20", "30", "40", "50", "all"]
    select_column = st.selectbox("Select the number of column to display", row, index=0, key=subdir)
    result = target_select.split(":")[1]
    if before is True:
        chemin_target = './newData/before/' + result + '.json'
        chemin_image = './tempSvg/' + select_column + result + "before.svg"
        chemin_image_complet = './tempSvg/' + result + "beforecomplet.svg"
    else:
        chemin_target = './newData/after/' + result + '.json'
        chemin_image = './tempSvg/' + select_column + result + "after.svg"
        chemin_image_complet = './tempSvg/' + result + "aftercomplet.svg"

    with open(chemin_target, 'r') as f:
        data_dict = json.load(f)
    if len(data_dict) != 0:
        if os.path.exists(chemin_image) and select_column != "all":
            col1, col2, col3 = st.columns(3)
            with col1:
                filename1 = chemin_image.replace('./tempSvg/', '')
                with open(chemin_image, "rb") as f:
                    contenu = f.read()
                f.close()
                st.markdown(
                    f'<a href="data:application/octet-stream;base64,{base64.b64encode(contenu).decode()}" download="{filename1}">Download plot</a>',
                    unsafe_allow_html=True, )

            with col2:
                filename2 = chemin_image.replace('./tempSvg/', '')
                with open(chemin_image, "rb") as f:
                    contenu = f.read()
                f.close()
                link = setLink(subdir, select_column, filename2)
                st.link_button("Show raw json file of this plot", link)

            with col3:
                filename2 = chemin_image.replace('./tempSvg/', '')
                link = setLinkSchema(select_column, filename2)
                st.link_button("Access to Schema.org for this Type", link)

            st.image(chemin_image)
            return

        if os.path.exists(chemin_image_complet) and select_column == "all":
            col1, col2, col3 = st.columns(3)
            with col1:
                filename1 = chemin_image_complet.replace('./tempSvg/', '')
                with open(chemin_image_complet, "rb") as f:
                    contenu = f.read()
                f.close()
                st.markdown(
                    f'<a href="data:application/octet-stream;base64,{base64.b64encode(contenu).decode()}" download="{filename1}">Download plot</a>',
                    unsafe_allow_html=True, )

            with col2:
                filename2 = chemin_image_complet.replace('./tempSvg/', '')
                with open(chemin_image_complet, "rb") as f:
                    contenu = f.read()
                # f.close()
                link = setLink(subdir, select_column, filename2)
                st.link_button("Show raw json file of this plot", link)
            with col3:
                filename2 = chemin_image.replace('./tempSvg/', '')
                link = setLinkSchema(select_column, filename2)
                st.link_button("Access to Schema.org for this Type", link)

            st.image(chemin_image_complet)
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
            if select_column != "all":
                select = int(select_column)
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
                plt.savefig(chemin_image)
                plt.close()

                col1, col2, col3 = st.columns(3)
                with col1:
                    filename1 = chemin_image.replace('./tempSvg/', '')
                    with open(chemin_image, "rb") as f:
                        contenu = f.read()
                    f.close()
                    st.markdown(
                        f'<a href="data:application/octet-stream;base64,{base64.b64encode(contenu).decode()}" download="{filename1}">Download plot</a>',
                        unsafe_allow_html=True, )

                with col2:
                    filename2 = chemin_image.replace('./tempSvg/', '')
                    with open(chemin_image, "rb") as f:
                        contenu = f.read()
                    f.close()
                    link = setLink(subdir, select_column, filename2)
                    st.link_button("Show raw json file of this plot", link)
                with col3:
                    filename2 = chemin_image.replace('./tempSvg/', '')
                    link = setLinkSchema(select_column, filename2)
                    st.link_button("Access to Schema.org for this Type", link)

                st.image(chemin_image)

            else:
                # ----------Save and Show all the dataframe------------------
                df_up_all = df.groupby(list_labels).value_counts()

                for i in range(len(df_up_all)):
                    df_up_all[i] = count_column[i]

                plot(df_up_all, orientation='horizontal')
                plt.savefig(chemin_image_complet)
                plt.close()

                col1, col2, col3 = st.columns(3)
                with col1:
                    filename1 = chemin_image_complet.replace('./tempSvg/', '')
                    with open(chemin_image_complet, "rb") as f:
                        contenu = f.read()
                    f.close()
                    st.markdown(
                        f'<a href="data:application/octet-stream;base64,{base64.b64encode(contenu).decode()}" download="{filename1}">Download plot</a>',
                        unsafe_allow_html=True, )

                with col2:
                    filename2 = chemin_image_complet.replace('./tempSvg/', '')
                    with open(chemin_image_complet, "rb") as f:
                        contenu = f.read()
                    f.close()
                    link = setLink(namekey, select_column, filename2)
                    st.link_button("Show raw json file of this plot", link)
                with col3:
                    filename2 = chemin_image.replace('./tempSvg/', '')
                    link = setLinkSchema(select_column, filename2)
                    st.link_button("Access to Schema.org for this Type", link)
                st.image(chemin_image_complet)
    else:
        st.write("The file you selected is not available")
