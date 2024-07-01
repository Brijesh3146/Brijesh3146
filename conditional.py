a=int(input("Enter mark1"))
b=int(input("Enter mark2"))
c=int(input("Enter mark3"))
d=int(input("Enter mark4"))
e=int(input("Enter mark5"))

avg=((a+b+c+d+e)/500)*100
if avg<0:
     print("what did you do?")
elif avg<35:
     print("fail")
elif avg<40:
     print("pass")
elif avg<60:
     print("second class")
elif avg<75:
     print("first class")
elif avg<101:
     print("distinction")
else:
     print ("how?")
print(avg)
