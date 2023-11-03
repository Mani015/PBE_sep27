
# How to get the value by using key
# syn: dict[key]

technology = {'python':'Serverside','Html':'Clientside','Django':'Webdevelopment',"mechanical":'Hardware'}
print(technology)

print(technology['python'])
# {'python': 'Serverside', 'Html': 'Clientside', 'Django': 'Webdevelopment', 'mechanical': 'Hardware'}
# Serverside

print(technology['Html'])
# Clientside

print(technology['mechanical'])

# Hardware

print(technology['javascript'])
# KeyError: 'javascript'
