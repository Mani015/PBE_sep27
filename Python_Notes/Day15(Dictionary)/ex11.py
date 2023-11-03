
# The setdefault() method returns the value of the item with the specified key.
# syn : dict.setdefault(key,value)
dc2 = {1:'aa',2:'bb',3:"cc"}
print(dc2)
# {1: 'aa', 2: 'bb', 3: 'cc'}


dc2.setdefault(4,'dd')
print(dc2)
# {1: 'aa', 2: 'bb', 3: 'cc', 4: 'dd'}

dc2.setdefault(5)
print(dc2)
# {1: 'aa', 2: 'bb', 3: 'cc', 4: 'dd', 5: None}


print(dc2.get(5))
# None
