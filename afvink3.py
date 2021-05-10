from Bio import Entrez
import itertools


def search(term1, term2, term3):
    Entrez.email = "akd.vaneersel@student.han.nl"
    term = "(" + term1 + ") AND (" + term2 + ") AND (" + term3 + ")"
    handle = Entrez.esearch(db="pubmed", term=term, field="tiab")
    record = Entrez.read(handle)
    handle.close()
    if int(record["Count"]) > 0:
        print(record["Count"])


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
    for i in g:
        for j in c:
            for k in me:
                search(i, j, k)
    print("done")


if __name__ == '__main__':
    g, c, me = read()
    make_terms(g,c,me)