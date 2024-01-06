import glob


def get_plot_name(target_classes: list):
    for file in glob.glob("assets/plots/*.svg"):
        filename = file.replace('\\', '/')
        parts = filename.split("/")
        cname = parts[2].replace("_plot.svg", "")
        target_classes.append(f"schema:{cname}")


def get_name_from_json(target_classes_available: list, subdir: str):
    for file in glob.glob(f"newData/{subdir}/*.json"):
        filename = file.replace('\\', '/')
        parts = filename.split("/")
        cname = parts[2].replace(".json", "")
        target_classes_available.append(f"schema:{cname}")


def getCheminForImage(nomfichier: str) -> str:
    # Use split to split the string based on ":"
    filename = nomfichier.split(":")[1]
    return f"assets/plots/{filename}_plot.svg"

def setLink(namekey,selectcol,filename: str) -> str:
    filename = filename.replace("complet", "")
    filename = filename.replace(selectcol, "")
    filename = filename.replace("before.svg", "")
    filename = filename.replace("after.svg", "")
    return 'https://raw.githubusercontent.com/Stevehunn/WebDataCommonsStreamlit/main/newData/' + namekey + '/' + filename + '.json'