# a=10
# b=0
# c=a/b
# print(c)
# print("program ended")
# print("program started")

# try:
#     a=10
#     b=10
#     c=a/b
#     print(c)
# except ZeroDivisionError:
#     print("we can divide any num with 0")
# print("program ended")


# valuError:--
# TypeError :--
# NameError :---
# ZeroDivisionError :--

# print("pr started")
# try:
#     marks1=input("enter your marks :--")
#     marks2=int(input("enter marks 3 here :---"))
#     totalmarks=marks1+marks2
#     print(totalmarks)
#     print(a)
# except ValueError:
#     print("enter proper value")
# except TypeError:
#     print("give proper datatypes to do proper opea")
# except NameError:
#     print("try to access the name is which is defined")
# except  ZeroDivisionError:
#     print("can t divide with zero")
# except IndexError:
#     print("try to correct index")
# print("pr ended")


# try:
#     num = int(input("Enter a number"))
#     print("Square is:",num)
# except:
#     print("except valu")
# else:
#     print("enter a else vale")

# class lowAmountEnterNeeded(Exception):
#     pass
# try:
#     bal=4000
#     withD=int(input("enter amount to withdraw :---"))
#     if withD>bal:
#         raise lowAmountEnterNeeded("you are trying to drwa more amount....!")
#     elif withD<bal:
#         raise 
# except lowAmountEnterNeeded as l:
#     print(l)

