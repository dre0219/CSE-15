from logic import TruthTable

#functions
#or (∨), and (∧), - (¬), -> (→), <-> (↔).

#Problem 1
negTable = TruthTable(["a"],["-a"])
andTable = TruthTable(["a", "b"], ["a and b"])
orTable  = TruthTable(["a", "b"],["a or b"])
ifTable  = TruthTable(["a", "b"], ["a -> b"])
biTable  = TruthTable(["a", "b"],["a <-> b"])

negTable.display()
andTable.display()
orTable.display()
ifTable.display()
biTable.display()
