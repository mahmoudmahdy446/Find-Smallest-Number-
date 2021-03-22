smallest = None
largest=-1
x=input("enter values separated vy a comma :")
lis1=x.split(',')
print("your values is",lis1)
for itervar in lis1:
    if smallest is None or int(itervar) < smallest:
        smallest =int(itervar)
        
    if int(itervar)>largest:
        largest=int(itervar)
    print("Loop:", itervar,"smallest :",smallest)
    print("Loop:", itervar,"largest :" ,largest)
print('DONE!')
print(">>Smallest:", smallest)
print(">>largest:",largest)
