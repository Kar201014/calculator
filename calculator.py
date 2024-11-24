# def number():
#     while True:
#         try:
#             number = float(input("Type a number "))
#             return number
#         except ValueError:
#             print("Type only numbers")

# def choice():
#     ch = ('+', '-', '/', '*')
#     while True:
#         try:
#             c = input("'+', '-', '/', '*'")
#             if c not in ch:
#                 raise Exception
#         except Exception:
#             print("only", ch)
#         else:
#             return c

# def result():
#     x = number()
#     c = choice()
#     y = number()
    
#     if c == '+':
#         res = x + y
#         return f"{x} + {y} = {res}"
#     elif c == '-':
#         res = x - y
#         return f"{x} - {y} = {res}"
#     elif c == '*':
#         res = x * y
#         return f"{x} * {y} = {res}"
#     elif c == '/':
#         while True:
            
#             try:
#                 res = x / y
#                 return f"{x} / {y} = {res}"
#             except ZeroDivisionError:
#                 print( "y cant be 0:")
#                 y = number()
# print(result())