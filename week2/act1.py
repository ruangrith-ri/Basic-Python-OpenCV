# Test OpenCV2 Version 4.2.0

import cv2 as cv
print("OpenCV Version : ", cv.__version__)

# Boolean Operation

a = 5
b = 10
c = 15
d = 20

print("a = b", a == b)
print("a < b", a < b)
print("a - b = c", (a - b) == c)

print("Result", a == b and c < d)
print("Result", a < b and c < d)
print("Result", a > b or c < d)
print("Result", a > (not b) or c < d)

# Aritermic Operation

fanta = 10
milinda = 12
oishi = 18
yenyen = 15

print("total", fanta+milinda+oishi+yenyen)
print("vat", (fanta+milinda+oishi+yenyen)*0.07)
print("service", (fanta+milinda+oishi+yenyen)*0.10)
print("sum", (fanta+milinda+oishi+yenyen)*1.17)

# Structor Variable

x = ['A', 'B', 'C', 'DEFG']

print(x[0])
print(x[0] + x[3])

#condition control

if fanta > oishi:
    print("fanta")
else:
    print("oishi")

#Repettive Control

while a < 10:
    a = a+1
    print("a : ",a)

x = "ABCD"

for i in x:
    print(i)

for i in range (5,10):
    print(i)