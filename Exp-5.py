#Code for concept of union , intersection and difference
#Coder:Aliya Shaikh

CET={"daniel","john","emma","richa","rose"}
JEE={"mia","beth","emma","robert","rose"}
NEET={"mia","sophia","smith","richa","rose"}
print("CET:",CET)
print("JEE:",JEE)
print("NEET:",NEET)
#union
union=CET.union(JEE).union(NEET)
print("union:",union)
#intersection
intersection=CET.intersection(JEE).intersection(NEET)
print("intersection:",intersection)
#difference
difference=CET.difference(JEE).difference(NEET)
print("difference:",difference)

"""
OUTPUT:
CET: {'rose', 'richa', 'daniel', 'john', 'emma'}
JEE: {'rose', 'beth', 'robert', 'mia', 'emma'}
NEET: {'sophia', 'rose', 'smith', 'richa', 'mia'}
union: {'smith', 'beth', 'daniel', 'mia', 'emma', 'sophia', 'rose', 'richa', 'robert', 'john'}
intersection: {'rose'}
difference: {'daniel', 'john'}
"""
