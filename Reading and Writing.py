fob=open('c:/test/a.txt', 'r')
print(fob.readline())

print(fob.readlines())
fob.close()

fob=open('c:/test/a.txt', 'w') 
fob.write('this is a new line\nthis is line 2 \nthis is line 3\nthis is the last and final line')
fob.close()

