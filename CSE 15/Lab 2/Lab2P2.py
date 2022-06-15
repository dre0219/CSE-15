from logic import TruthTable

#functions
#or (∨), and (∧), - (¬), -> (→), <-> (↔).

#Problem2

# 1. enter 2 propositions
# 2. show truth tables
# 3. output if equal or not

def checkEqual(propTableList1, propTableList2):
    l1 = []
    l2 = []

    #add each value from the truthtables to the l1 and l2
    for row in propTableList1:
        l1.append(row[1][0])

    for row in propTableList2:
        l2.append(row[1][0])

    #iterate through the length of the lists(l1 length should equal l2 length) if there is anything inequal between the lists that means they are not equal.
    for x in range(len(l1) - 1):
        if(l1[x] != l2[x]):
            return False
    #if iterated through the entire list without returning false, then it is true
    return True


#inputs
prop1 = input("Enter proposition 1: ")

prop2 = input("Enter proposition 2: ")
print("\n")

#var11 should be the 0 index of the string from prop1 (ex: prop1 = "p and q": prop1[0] = p, [1] = and (not a var), [2] = q)
var11 = (prop1.split())[0]
#var12 should be the 2 index of the string from prop1
var12 = (prop1.split())[2]

#same for prop2
var21 = (prop2.split())[0]
var22 = (prop2.split())[2]

#create truth tables for both prop1 and prop2 to compare
prop1Table = TruthTable([var11, var12], [prop1])
prop2Table = TruthTable([var21, var22], [prop2])

#display the truthtables
prop1Table.display()
print("\n")
prop2Table.display()

#create list of all the values from both prop1 and prop2 truth tables
prop1TableList = prop1Table.table
prop2TableList = prop2Table.table

#compare truth table values
equal = checkEqual(prop1TableList, prop2TableList)

if(equal == True):
    print("The propositions are equivalent")
if(equal == False):
    print("The propositions are not equivalent")
