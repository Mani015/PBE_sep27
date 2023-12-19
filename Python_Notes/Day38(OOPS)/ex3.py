
# creation object for class

class Product_Details(object):
    product_name = 'Samsung'
    product_price = 12000
    product_color = 'black'
    product_camera = '20MP'

# object Instantiation
Product_Details()

# we have to assign new variable name , when After  object Instantiation

x1 = Product_Details()

# How to call Attributes by using objectname
# sy : objectname.Attribute

print(x1.product_name)
print(x1.product_price)
print(x1.product_camera)
print(x1.product_color)
# Samsung
# 12000
# 20MP
# black

