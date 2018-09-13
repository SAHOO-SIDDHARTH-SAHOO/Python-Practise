#define a printPicnic() method that will take in a dictionary of information and use center(),
#ljust()and rjust()to display that information in a neatly aligned table-like format.

"""
Like this:

---PICNIC ITEMS--
sandwiches..    4
apples......   12
cups........    4
cookies..... 8000

-------PICNIC ITEMS-------
sandwiches..........     4
apples..............    12
cups................     4
cookies.............  8000

"""
#============================================================================================

def printPicnic(itemDict,leftwidth,rightwidth):
    print("PICNIC ITEMS".center(leftwidth+rightwidth,"-"))
    for k,v in itemDict.items():
        print(k.ljust(leftwidth,".")+ str(v).rjust(rightwidth))

Dict=dict()
def Dictionary():
    n = int(input())               #n is the number of items you want to enter into dictionary.
    for i in range(0,n):
        word=input().split()
        key=word[0]
        value=word[1]
        Dict[key]=value
    print(Dict)
    
Dictionary()
printPicnic(Dict,12,12)
printPicnic(Dict,24,10)
