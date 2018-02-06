#리스트=배열

a=['김개똥', '박짱구', '이멍충']
print(a)
print(a[0])
print(a[1])
print(a[2])

print("")

a=[1,2,3,4]
print(a)

print("")

a=[1,2,3,4,5,6,7,8,9,10]
print(a[0:5])
print(a[5:])
print(a[:3])

print("")

a=[1,2,3,4]
b=[5,6,7]
print(a+b)

a=[1,2,3,4,5]
a[2]=30
print(a)
a[3]=40
print(a)
print(len(a))

print("")

a=[1,2,3]

a.append(4) #끝에 추가
print(a)

a.extend([6,7,8]) #다른 리스트 이어붙이기
print(a)

a.insert(0,9) #리스트 내의 위치에새 요소 삽입
print(a)
a.insert(5,9)
print(a)

print("")

a=['BMW', 'DENZ', 'VOLKSWAGEN', 'AUDI']
a.remove('BMW') #제거
print(a)
a.remove('VOLKSWAGEN') 
print(a)

print("")

a=[1,2,3,4,5]
a.pop() #마지막 제거
print(a)
a.pop()
print(a)

a=[1,2,3,4,5]
a.pop(2) #3번째 요소 제거
print(a)

print("")

a=['abc', 'def', 'ghi']
print(a.index('def')) #찾는배열위치

print("")

a=[1, 100, 2,100, 3, 100]
print(a.count(100)) #개수

print("")

a=[3,4,5,1,2]
a.sort() #정렬
print(a)
a.reverse() #반대로 뒤집기
print(a)
