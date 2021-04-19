from Bio import Entrez, Medline


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


if __name__ == '__main__':
    term_ = input("Welk woord wil je gebruiken om te zoeken? ")
    retmax_ = get_retmax(term_)
    idlist_ = get_idlist(term_, retmax_)
    get_source(idlist_)
