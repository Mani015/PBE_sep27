# slicing : It means you have to find out the sub-string
# syntax: string[start : end :step=1]

# start and ending values
name = 'Ravikumar'
print(name[0:5:])
# Ravik


# starting value:
print(name[0::])
# Ravikumar
print(name[1::])
# avikumar

print(name[2::])
# vikumar

y = 'python developer'
print(y[0:7])
print(y[3:6])
print(y[5:10])
print(y[2:8])
print(y[9:10])
print(y[1:7])
print(y[3::])

# python
# hon
# n dev
# thon d
# v
# ython

# hon developer

print(y[0::2])
# pto eeoe
