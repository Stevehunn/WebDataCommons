import glob


def get_plot_name(target_classes: list):
    for file in glob.glob("assets/plots/*.svg"):
        filename = file.replace('\\', '/')
        # Utilisez split pour séparer le chemin du fichier
        parts = filename.split("/")
        # Supprime l'extension ".svg"
        cname = parts[2].replace("_plot.svg", "")
        # Ajoute à la liste avec le préfixe "schema:"
        target_classes.append(f"schema:{cname}")


def get_name_from_json(target_classes_available: list, subdir: str):
    for file in glob.glob(f"newData/{subdir}/*.json"):
        filename = file.replace('\\', '/')
        # Utilisez split pour séparer le chemin du fichier
        parts = filename.split("/")
        # Supprime l'extension ".json"
        cname = parts[2].replace(".json", "")
        # Ajoute à la liste avec le préfixe "schema:"
        target_classes_available.append(f"schema:{cname}")


def getCheminForImage(nomfichier: str) -> str:
    # Utiliser split pour séparer la chaîne en fonction de ":"
    filename = nomfichier.split(":")[1]
    # Concaténer les parties avec le format souhaité
    return f"assets/plots/{filename}_plot.svg"
