import re

from Bio import Entrez, Medline
from matplotlib import pyplot as plt


def get_retmax(term):
    Entrez.email = "akd.vaneersel@student.han.nl"
    handle = Entrez.egquery(term=term)
    record = Entrez.read(handle)
    retmax = 0
    for row in record["eGQueryResult"]:
        if row["DbName"] == "pubmed":
            retmax = (row["Count"])
    return retmax


def get_idlist(term, retmax):
    Entrez.email = "akd.vaneersel@student.han.nl"
    handle = Entrez.esearch(db="pubmed", term=term, retmax=int(retmax))
    record = Entrez.read(handle)
    handle.close()
    return record["IdList"]


def get_source(idlist):
    Entrez.email = "akd.vaneersel@student.han.nl"
    handle = Entrez.efetch(db="pubmed", id=idlist, rettype="medline", retmode="text")
    records = Medline.parse(handle)
    source = []
    for record in records:
        temp = ("source:", record.get("SO", "?"))
        source.append(temp)
    return source


def get_year(source):
    years = []
    for year in source:
        temp = (year[1].split(" "))
        for i in range(len(temp)):
            if re.match("^[1-2][089][0-9]{2}$", year[1].split(" ")[i]):
                years.append(year[1].split()[i])
    return list(map(int, years))


def make_plot(years):
    binlist = []
    for i in range(min(years), max(years), 5):
        binlist.append(i)
    print(binlist)
    plt.hist(sorted(years), bins=binlist)
    print(len(years))
    plt.show()


if __name__ == '__main__':
    term_ = input("Welk woord wil je gebruiken om te zoeken? ")
    retmax_ = get_retmax(term_)
    idlist_ = get_idlist(term_, retmax_)
    source_ = get_source(idlist_)
    year_ = get_year(source_)
    make_plot(year_)
