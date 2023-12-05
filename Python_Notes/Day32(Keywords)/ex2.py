
# with out global Statement
# fruit = 'Apple'
# print('Before GV:',fruit)
#
# def Change():
#     fruit = 'Mango'
#     print('LV:',fruit)
# Change()
# print('After GV:',fruit)
# Before GV: Apple
# LV: Mango
# After GV: Apple






# using Global Statement
fruit = 'Apple'
print('Before GV:',fruit)

def Change():
    global fruit
    fruit = 'Mango'
    print('LV:',fruit)
Change()
print('After GV:',fruit)
# Before GV: Apple
# LV: Mango
# After GV: Mango
