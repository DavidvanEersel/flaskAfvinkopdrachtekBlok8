from Bio import Entrez
from Bio import Medline


def getinfo(idlist, t1, t2, t3):
    Entrez.email = "akd.vaneersel@student.han.nl"
    handle = Entrez.efetch(db="pubmed", id=idlist, rettype="medline", retmode="text")
    records = Medline.parse(handle)
    au = []
    ab = []
    for record in records:
        au.append(("AU:", record.get("SO", "?")))
        ab.append(("AB", record.get("SO", "?")))
    combi = t1, t2, t3
    print("De meest voorkomende combinatie is: {}.\nAuteurs zijn: {}.\nAbstracts zijn: {}".format(combi, au, ab))


def search(term1, term2, term3, high, idlist):
    Entrez.email = "akd.vaneersel@student.han.nl"
    term = "(" + term1 + ") AND (" + term2 + ") AND (" + term3 + ")"
    handle = Entrez.esearch(db="pubmed", term=term, field="tiab")
    record = Entrez.read(handle)
    handle.close()
    if high < int(record["Count"]):
        high = int(record["Count"])
        idlist = record["IdList"]
        print(record["Count"])
        return high, idlist, term, term2, term3
    return high, idlist, term, term2, term3


def read():
    genes = []
    compounds = []
    molecular_effects = []

    for f in open("genes.txt"):
        genes.append(f.strip())
    for f in open("compounds.txt"):
        compounds.append(f.strip())
    for f in open("molecular_effects.txt"):
        molecular_effects.append(f.strip())
    return genes, compounds, molecular_effects


def make_terms(g, c, me):
    high = 0
    idlist = []
    term1 = ''
    term2 = ''
    term3 = ''
    for i in g:
        for j in c:
            for k in me:
                high, idlist, term1, term2, term3 = search(i, j, k, high, idlist)
    getinfo(idlist, term1, term2, term3)
    print("done")


if __name__ == '__main__':
    g, c, me = read()
    make_terms(g, c, me)
