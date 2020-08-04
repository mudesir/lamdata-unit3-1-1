
# my_lamdata/my_mod.py

def enlarge(n):
    """
    Parma n is a number
    Function will enlarge the number
    """
    return n*100
# this code breaks our ablity to import enlarge from other files, 
#


if __name__ == "__main__":

    print("Hello")
y = int(input("please choose a number"))
print(y, enlarge(y))