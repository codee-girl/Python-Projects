#learning to import python packages and using them 

from prettytable import PrettyTable

table=PrettyTable()
table.add_column("Pokemon Name",["Pikachu","Squirrle","Combee"])
table.add_column("Type",["Fire","Water","Earth"])

table.align

print(table)




