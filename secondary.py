#author: Lynijah
# date: 07-1-2021

def blank():
    return print(" ")
# --------------- Section 3 --------------- #
#  String Duplication / Pattern Recognition #

# you may choose to use any symbol, it does not have to be the dollar sign

# create the following pattern using string duplication and print statments:
#
# $
# $$
# $$$
# $$$$
# $$$$$
print("String Duplication")
print("@"* 1)
print("@"* 2)
print("@"* 3)
print("@"* 4)
print("@"* 5)
blank()

# create the following pattern using string duplication and print statments:
#
# $$$$$
# $$$$
# $$$
# $$
# $
print("String Duplication going down")
print("@"* 5)
print("@"* 4)
print("@"* 3)
print("@"* 2)
print("@"*1)
blank()
blank()


# create the following pattern using string duplication and print statments:
#
#     $
#    $$
#   $$$
#  $$$$
# $$$$$
print("String Duplication with decreased indentation  ")
print(" "*4 + "@"*1)
print(" "*3 + "@"*2)
print(" "*2 + "@"*3)
print(" "*1 + "@"*4)
print("@"*5)


# create the following pattern using string duplication and print statments:
#
# $$$$$
#  $$$$
#   $$$
#    $$
#     $
print("String Duplication with increased indentation")
print( "@"*5)
print(" "*1 + "@"*4)
print(" "*2 + "@"*3)
print(" "*3 + "@"*2)
print(" "*4 + "@"*1)
blank()

