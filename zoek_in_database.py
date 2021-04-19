import mysql.connector


def query(zoekwoord):
    conn = mysql.connector.connect(host="ensembldb.ensembl.org", user="anonymous", db="homo_sapiens_core_95_38")
    cursur = conn.cursor()
    cursur.execute("select description from gene where description like('%" + zoekwoord + "%')")
    rows = cursur.fetchall()
    cursur.close()
    conn.close()
    results = list()
    for i in range(len(rows)):
        results.append(rows[i][0])
    return results
