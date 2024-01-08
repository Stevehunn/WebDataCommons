import os


def content_delete_svg():
    directory = "tempSvg/"
    elements_to_keep = ["10Productafter.svg", "10Productbefore.svg", "15Productafter.svg", "15Productbefore.svg",
                        "20Productafter.svg", "20Productbefore.svg", "30Productafter.svg", "30Productbefore.svg",
                        "40Productafter.svg", "40Productbefore.svg", "50Productafter.svg", "50Productbefore.svg"]
    try:
        # List of all files and folders in the directory
        content_dossier = os.listdir(directory)
        # Scanning all items in the directory
        for element in content_dossier:
            element_path = os.path.join(directory, element)

            # Checking if the element is not part of the list to keep
            if element not in elements_to_keep:
                os.remove(element_path)

        print(f"Contenu du directory '{directory}' supprimé sauf les éléments de la liste.")
    except Exception as e:
        print(f"Une erreur s'est produite : {e}")
