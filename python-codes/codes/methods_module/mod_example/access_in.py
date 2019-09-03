import mod_example.test_mod

# where ever you type a function name
# it means you are calling the function

print(mod_example.test_mod.add(12,3))
print(mod_example.test_mod.mul(12,3))


print("-----------------------")
# importing with alias

import mod_example.test_mod as m

print(m.add(12,3))
print(m.mul(12,3))

print("-----------------------")

from mod_example.test_mod import add,mul

print(add(34,3))
print(mul(34,3))

print("-----------------------")

from mod_example.test_mod import * # import all the modules

print(add(34,3))
print(mul(34,3))

# calling function without return
name()