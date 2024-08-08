import json
from datetime import date
from decimal import Decimal

from fr_date import conv


def all_data():
    with open("./src/seuils/seuils.json", "r") as f:
        seuils = json.loads(f.read())
    return seuils


def liens():
    with open("./src/seuils/avis.json", "r") as f:
        avis = json.loads(f.read())
    return avis


def get_trimestre(jour):
    vigueur = conv(jour, True)
    if type(vigueur) is not date:
        raise ValueError
    elif vigueur.year == 2023:
        return vigueur.replace(day=1).isoformat()
    else:
        mois = {}
        for m in range(1, 13):
            mois[m] = m - (m - 1) % 3
        return vigueur.replace(month=mois[vigueur.month], day=1).isoformat()


def get_lien(jour):
    trimestre = get_trimestre(jour)
    avis = liens()
    return avis[trimestre]


def get_taux(jour, montant=None, categorie=None):
    trimestre = get_trimestre(jour)
    data = all_data()
    seuils = data[trimestre]["seuils"]
    if montant:
        for s in seuils:
            if Decimal(s["min"]) < montant <= Decimal(s["max"]):
                if categorie and "categorie" in s:
                    if categorie == s["categorie"]:
                        return Decimal(s["taux"])
                elif "categorie" in s:
                    return seuils
                else:
                    return Decimal(s["taux"])
    return seuils
