# The union() method returns a set that contains all items from the original set,
# and all items from the specified set(s).

# syntax:-set.union(set1, set2...)

s2={1,3,45,6,8,0}
print(s2)
# {0, 1, 3, 6, 8, 45}
s1={'java','c','c++','python','php','DBMS'}
# print(s1)
# {'c++', 'java', 'c', 'php', 'python', 'DBMS'}
s3=s1.union(s2)
# print(s3)
# {0, 1, 3, 6, 'c', 8, 'DBMS', 'java', 45, 'php', 'c++', 'python'}


s={5,10,15,17,'Ramesh','Madhu'}
print(s)
{17, 'Ramesh', 'Madhu', 5, 10, 15}
s5={1+5j,5.0,-2.2}
s6=s5.union(s)
print(s6)
# {5.0, 'Madhu', 10, 15, (1+5j), 17, 'Ramesh', -2.2}

