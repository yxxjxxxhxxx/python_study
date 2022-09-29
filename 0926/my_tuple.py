t1 = (1,2,3)
t2 = 4,5,6
t3 = tuple([6,7,8])
t4 = (4,)

print("t1=", t1)
print("t2=", t2)
print("t3=", t3)
print("t4=", t4)

for i in t1:
    print(i)

print("t1[0]=", t1[0])

# 튜플은 요소 변경시 에러 발생
# t1[0] = 10

def test():
    a = 10
    b = 20
    c = 30
    return a, b, c

res = test()
print(res)
print(type(res))

x, y, z = test()
print(x, y, z)
