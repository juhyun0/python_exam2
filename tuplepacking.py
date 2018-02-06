#Tuple Packing
a=1,2,3
print(a)

#Tuple Unpacking
one,two,three=a
print(one)
print(two)
print(three)

print("")

city, latitude, longitude = 'Seoul', 37.541, 126.986
print(city)
print(latitude)
print(longitude)

print("")

a=('abc', 'def', 'ghi')
print(a.index('def')) #위치

print("")

a=(1, 100, 2, 100, 3, 100)
print(a.count(100)) 
print(a.count(200))
