import json
import os.path

import pandas as pd
import streamlit as st
from matplotlib import pyplot as plt
from upsetplot import plot


def content_testplot(target_classes, target_select, before):
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
        namekey = "before"
    else:
        cheminTarget = './newData/after/' + result + '.json'
        cheminImage = './tempSvg/' + selectrow + result + "after.svg"
        cheminImageComplet = './tempSvg/' + result + "aftercomplet.svg"
        namekey = "after"

    with open(cheminTarget, 'r') as f:
        data_dict = json.load(f)
        # st.write(data_dict)
    if len(data_dict) != 0:
        if os.path.exists(cheminImage):
            st.image(cheminImage)
            return
        if os.path.exists(cheminImageComplet):
            st.image(cheminImageComplet)
            return
        else:
            # récuperer tous les labels
            labels = set()
            for item in data_dict:
                labels.update(item["pset"])
            # creer bitmap a partir des labels et des counts
            list_labels = list(labels)
            # st.write(list_labels)
            # st.write([[e in item["pset"] for item in data_dict] for e in list_labels])
            # df = pd.DataFrame([[e in item["pset"] for e in list_labels] for item in data_dict], columns=list_labels)
            df = pd.DataFrame([[e in item["pset"] for e in list_labels] + [item["count"]] for item in data_dict],
                              columns=list_labels + ["count"])
            count_column = df.pop("count")
            # st.write(df)
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
                # print(column_to_remove)
                for column in column_to_remove:
                    df_reduce.pop(column)
                    list_labels.remove(column)
                # st.write(df_reduce)

                # ----------Save and Show n row of the dataframe------------------
                df_up = df_reduce.groupby(list_labels).value_counts()

                for i in range(len(df_up)):
                    df_up[i] = count_column[i]

                # st.write(df_up)

                plot(df_up, orientation='horizontal')
                plt.savefig(cheminImage)
                st.image(cheminImage)

            else:
                # ----------Save and Show all the dataframe------------------
                df_up_all = df.groupby(list_labels).value_counts()

                for i in range(len(df_up_all)):
                    df_up_all[i] = count_column[i]

                # st.write(df_up_all)

                plot(df_up_all, orientation='horizontal')
                plt.savefig(cheminImageComplet)
                st.image(cheminImageComplet)
                # st.write("finished.")
    else:
        st.write("The file you selected is not available")
