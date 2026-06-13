#Coder:Aliya Shaikh
#Code for Gross Salary 

print("Gross salary")
BS=float(input("Enter basic salary:"))
DA=0.70*BS
TA=0.30*BS
HRA=0.10*BS
GS=BS+DA+TA+HRA
print("BS:", BS)
print("DA(70%):", DA)
print("TA(30%):", TA)
print("HRA(10%):", HRA)
print("Gross salary:", GS)

"""
OUTPUT:
Gross salary
Enter basic salary: 40000
BS: 40000.0
DA(70%): 28000.0
TA(30%): 12000.0
HRA(10%): 4000.0
Gross salary: 84000.0
"""
