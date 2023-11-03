
# The copy() method returns a copy of the specified dictionary.
#
# Syntax
# dictionary.copy()


player = {'sachin':25000,'virat':15000,'rohit':18000,'dhoni':5000,'Galye':10000}
print(player)
# {'sachin': 25000, 'virat': 15000, 'rohit': 18000, 'dhoni': 5000, 'Galye': 10000}
runs = {}
print('before dict:',runs)

runs = player.copy()
print('After dict:',runs)
# before dict: {}
# After dict: {'sachin': 25000, 'virat': 15000, 'rohit': 18000, 'dhoni': 5000, 'Galye': 10000}
