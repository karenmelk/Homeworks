
# ex 1
# first_number = int(input('Arajin tiv -- > '))
# second_number = int(input('Erkrord tiv -- >'))
# c = input("Nermuceq gorcoxutyuny '+' '-' '/' '*'")
# def calculator(a,b,c):
#     if c == '+':
#         return a+b
#     elif c == '-':
#         return a-b
#     elif c == '/':
#         return a / b
#     elif c == '*':
#         return a * b
#     else:
#         text = 'Nman gorcoxutyun goyutyun chuni'
#         return text
# print(calculator(first_number,second_number,c))

# ex 2
# def maxf(a,b):
#     return max(a,b)
# first_number = int(input('Arajin tiv -- > '))
# second_number = int(input('Erkrord tiv -- >'))
# print(maxf(first_number,second_number))

#ex 3
# def numbers(*a):
#     z = 0
#     for i in a :
#         z += i
#     return z 
# print((numbers(4,5,6,8,5)))

# ex 4

# def numbers(*a):
#     z = 1
#     for i in a :
#         z *= i
#     return z 
# print((numbers(4,5,6,8,5)))


# ex 5
# def func(text):
#     count_tar = 0
#     count_tiv = 0
#     for i in text:
#         if i.isdigit():
#             count_tiv += 1
#         elif i.isalpha():
#             count_tar += 1
#     print(count_tar, count_tiv)
# func(input('Enter text-->'))