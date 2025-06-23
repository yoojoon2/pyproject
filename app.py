#import mod1
#from mod1 import PI, sub, add
#from mod1 import *
#import mod1 as mo
import mod.mod1 as mod


print('모듈 이름 : ', __name__)

print(mod.PI)
print(mod.add(100, 20))
print(mod.sub(10, 5))
mod.print_result()

#print(mo.PI)
#print(mo.add(100, 20))
#print(mo.sub(10, 5))

#print(PI)
#print(add(100, 20))
#print(sub(10, 5))

#print(mod1.PI)
#print(mod1.add(10, 20))
#print(mod1.sub(10, 3))