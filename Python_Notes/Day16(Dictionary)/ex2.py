
# In the dictionary keys are immutable

d2 = {'Ramu':'Python','Mark':'Facebook','Musk':'Twitter','Google':'sundar','microsoft':'sathyanadenlla'}

print(d2)
# {'Ramu': 'Python', 'Mark': 'Facebook', 'Musk': 'Twitter', 'Google': 'sundar', 'microsoft': 'sathyanadenlla'}

# How to change the keys

# We need to take a one value

founder = 'Guido'

print(d2['Ramu'])
# Python


d2[founder] = d2.pop('Ramu')

print(d2)
# {'Mark': 'Facebook', 'Musk': 'Twitter', 'Google': 'sundar', 'microsoft': 'sathyanadenlla', 'Guido': 'Python'}

d2['Gangadharam'] = d2.pop('Google')
print(d2)
# {'Mark': 'Facebook', 'Musk': 'Twitter', 'microsoft': 'sathyanadenlla', 'Guido': 'Python', 'Gangadharam': 'sundar'}
