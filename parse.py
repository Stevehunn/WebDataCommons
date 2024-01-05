import glob
import re


# Version Window
def parseWindow(target_classes):
    for file in glob.glob("assets/plots/*.svg"):
        # Utilisez split pour séparer le chemin du fichier
        parts = file.split("/")

        # Extrait le premier élément après "assets"
        fname = parts[1]  # parts[0] est "assets", parts[1] est "plots"

        parts2 = fname.split("plots")
        # Extrait le premier élément après "plots"
        newFname = parts2[1]

        # Utiliser split pour séparer la chaîne en fonction de "\"
        parts = newFname.split("\\")

        # Concaténer les parties avec "schema:"
        newFname = "".join(parts[1:])

        # Supprime l'extension ".svg"
        cname = newFname.split("_plot.svg")[0]

        # Ajoute à la liste avec le préfixe "schema:"
        target_classes.append(f"schema:{cname}")


# Version Mac
def parseMac(target_classes):
    for file in glob.glob("assets/plots/*.svg"):
        # Utilisez split pour séparer le chemin du fichier
        parts = file.split("/")

        fname = parts[2]
        parts2 = fname.split(".")
        # Extrait le premier élément après "plots"
        newFname = parts2[0]

        cname = newFname.split("_plot")[0]
        if cname != "Intangible":
            target_classes.append(f"schema:{cname}")


def parseAfterJsonAvailableWindow(target_classes_available):
    for file in glob.glob("newData/after/*.json"):
        # Utilisez split pour séparer le chemin du fichier
        parts = file.split("/")
        # print(parts)
        # Extrait le premier élément après "assets"
        fname = parts[1]  # parts[0] est "assets", parts[1] est "plots"
        # print(fname)
        # print("Fname")
        parts2 = fname.split("plots")
        # print(parts2)
        # print("parts2")
        # Extrait le premier élément après "plots"
        newFname = parts2[0]
        # print(newFname)
        # Utiliser split pour séparer la chaîne en fonction de "\"
        parts = newFname.split("\\")
        # print(parts)
        # Concaténer les parties avec "schema:"
        newFname = "".join(parts[1:])
        # print(newFname)
        # Supprime l'extension ".svg"
        cname = newFname.split(".json")[0]

        # Ajoute à la liste avec le préfixe "schema:"
        target_classes_available.append(f"schema:{cname}")
        # print("target_classes_available")
        # print(target_classes_available)


def parseAfterJsonAvailableMac(target_classes_available):
    for file in glob.glob("newData/after/*.json"):
        # Utilisez split pour séparer le chemin du fichier
        parts = file.split("/")

        fname = parts[2]
        parts2 = fname.split(".")
        # Extrait le premier élément après "plots"
        newFname = parts2[0]

        cname = newFname.split("_plot")[0]
        if cname != "Intangible":
            target_classes_available.append(f"schema:{cname}")


def parseBeforeJsonAvailableWindow(target_classes_available):
    for file in glob.glob("newData/before/*.json"):
        # Utilisez split pour séparer le chemin du fichier
        parts = file.split("/")
        # print(parts)
        # Extrait le premier élément après "assets"
        fname = parts[1]  # parts[0] est "assets", parts[1] est "plots"
        # print(fname)
        # print("Fname")
        parts2 = fname.split("plots")
        # print(parts2)
        # print("parts2")
        # Extrait le premier élément après "plots"
        newFname = parts2[0]
        # print(newFname)
        # Utiliser split pour séparer la chaîne en fonction de "\"
        parts = newFname.split("\\")
        # print(parts)
        # Concaténer les parties avec "schema:"
        newFname = "".join(parts[1:])
        # print(newFname)
        # Supprime l'extension ".svg"
        cname = newFname.split(".json")[0]

        # Ajoute à la liste avec le préfixe "schema:"
        target_classes_available.append(f"schema:{cname}")
        # print("target_classes_available")
        # print(target_classes_available)


def parseBeforeJsonAvailableMac(target_classes_available):
    for file in glob.glob("newData/before/*.json"):
        # Utilisez split pour séparer le chemin du fichier
        parts = file.split("/")

        fname = parts[2]
        parts2 = fname.split(".")
        # Extrait le premier élément après "plots"
        newFname = parts2[0]

        cname = newFname.split("_plot")[0]
        if cname != "Intangible":
            target_classes_available.append(f"schema:{cname}")


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
