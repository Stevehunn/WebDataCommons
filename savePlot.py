import glob
import json
import os

import pandas as pd
from matplotlib import pyplot as plt
from upsetplot import plot


def save_all_plot():
    for subdir in ("before", "after"):
        for file in glob.glob(f"newData/{subdir}/*.json"):
            cheminImageComplet = f'./svgComplet/{file.replace("\\", "/").split("/")[-1].replace(".json", "")}{subdir}complet.svg'
            with open(file, 'r') as f:
                data_dict = json.load(f)
            if len(data_dict) != 0:
                if os.path.exists(cheminImageComplet):
                    pass
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
                    df = pd.DataFrame(
                        [[e in item["pset"] for e in list_labels] + [item["count"]] for item in data_dict],
                        columns=list_labels + ["count"])
                    count_column = df.pop("count")
                    # st.write(df)
                    df_up_all = df.groupby(list_labels).value_counts()

                    for i in range(len(df_up_all)):
                        df_up_all[i] = count_column[i]

                    try:
                        plot(df_up_all, orientation='horizontal')
                    except Exception as err:
                        print(err)
                        print(file)
                    plt.savefig(cheminImageComplet)
                    plt.close()
            else:
                pass


save_all_plot()
