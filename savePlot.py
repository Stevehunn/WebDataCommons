import glob
import json
import os
import pandas as pd
from matplotlib import pyplot as plt

# Import Content Page
from upsetplot import plot


def save_all_plot():
    for subdir in ("before", "after"):
        for file in glob.glob(f"newData/{subdir}/*.json"):
            chemin_image_complet = f'./svgComplet/{file.replace("\\", "/").split("/")[-1].replace(".json", "")}{subdir}complet.svg'
            with open(file, 'r') as f:
                data_dict = json.load(f)
            if len(data_dict) != 0:
                if os.path.exists(chemin_image_complet):
                    pass
                else:
                    # get all labels
                    labels = set()
                    for item in data_dict:
                        labels.update(item["pset"])
                    # create bitmap from labels and counts
                    list_labels = list(labels)
                    df = pd.DataFrame(
                        [[e in item["pset"] for e in list_labels] + [item["count"]] for item in data_dict],
                        columns=list_labels + ["count"])
                    count_column = df.pop("count")
                    df_up_all = df.groupby(list_labels).value_counts()

                    for i in range(len(df_up_all)):
                        df_up_all[i] = count_column[i]

                    plot(df_up_all, orientation='horizontal')
                    plt.savefig(chemin_image_complet)
                    plt.close()
            else:
                pass


save_all_plot()
