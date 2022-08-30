#1
# with open('test.txt','w') as x:
#     x.write('Barev dzez')

#2
# with open('test.txt','w') as x:
#     c = 0
#     while c < 5:
#         x.write(input('miban -- > '))
#         x.write('\n')
#         c += 1
    
# with open('test.txt','rt') as k:
#     res = k.readlines()
#     print(k.read())
# c = int(input('Number of lines -- > '))
# p = 0
# for i in res:
#     print(i)
#     p += 1
#     if p == c:
#         break

#3
# with open('test.txt', 'w') as x:
#     x.write('Hello world')
# with open('test.txt', 'rt') as k:
#     print(k.read())

#4
# with open('users.txt','rt') as x:
#     res = x.readlines()
# print(res)
# word = res[0]
# max = len(res[0])
# for i in range(0,len(res)):
#     if len(res[i]) > max:
#         max = len(res[i])
#         word = res[i]
# print(word)

#5

# with open('test.txt','rt') as x:
#     res = x.read()
# for i in res:
#     if i.isdigit():
#         print(i)

#6
# s = 'qwertyuiopasdfghjklzxcvbnm'
# a = 'login'
# b = 'pass'
# with open('test.txt','rt') as x:
#     res = x.readlines()
# for i in range(0,len(res)):
#     if a in res[i] or b in res[i]:
#         print(res[i])


#####################################SLAYD####################################################

#1
# mylist1 = [1, 2, 3]
# mylist2 = ['a', 'b', 'c']
# mydict = {}
# for i, j in zip(mylist1, mylist2):
#     mydict[j] =i
# with open('test.txt','w') as x:
#     for i in mydict:
#         x.write(i+':'+str(mydict[i])+'\n')
# with open('test.txt','rt') as k:
#     res = k.read()
#     print(res)

#2?
#3
# mylist = []
# x = int(input('number -- > '))
# for i in range(1,x):
#     if i % 5 == 0 or i % 3 == 0 :
#         mylist.append(i)
# sum = 0
# for i in mylist:
#     sum += i
# with open('test.json','w') as x:
#    res = x.write(str(sum))
# print(res)

#4
# vowels = 'aeyuio'
# x = input('word -- > ')
# count = 0
# for i in range(0,len(x)):
#     if x[i] in vowels:
#         count += 1
# print(count)
# with open('test.json','w') as x :
#     res = x.write(str(count))
# print(res)

#5
# with open('test.txt','rt') as x:
#     res = x.read()
# mylist = res.split(' ')
# mydict = {}
# x = mylist.count(mylist[2])
# for i in range(0,len(mylist)):
#     mydict[mylist[i]] = mylist.count(mylist[i]) 
# print(mydict)

#6
# mylist = ['a','b','a','c','b']
# myset = set(mylist)
# print(myset)

#7
upper = 0
lower = 0
with open('word.txt','rt') as x:
    res = x.read()
for i in res:
    if i.isupper():
        upper += 1
    if i.islower():
        lower += 1
print(f'Upper -- > {upper}\nLower -- > {lower}')