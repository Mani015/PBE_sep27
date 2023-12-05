g1 = 'velu'
def fun1():
    en = 'gangadharam'
    print('EV:' ,en)
    def fun2():
        nonlocal en
        en = 'ramu'
        print('LV:' ,en)

    print('EV:', en)
    print('gloval var:', g1)
    fun2()
    print('EV:', en)
print('gloval var:',g1)
fun1()
print('gloval var:',g1)

# gloval var: velu
# EV: gangadharam
# EV: gangadharam
# gloval var: velu
# LV: ramu
# EV: ramu
# gloval var: velu
