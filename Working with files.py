fob=open('c:/test/a.txt', 'w')
fob.write('hey now brown cow')
fob.close()

fob=open('c:/test/a.txt', 'r')
print(fob.read(3))

print(fob.read())
fob.close()