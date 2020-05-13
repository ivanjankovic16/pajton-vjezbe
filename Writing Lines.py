fob=open('c:/test/a.txt', 'r')
listme=fob.readlines()
print(listme)
fob.close()

listme[2]='mmm i sure love bacon\n'
print(listme)

fob=open('c:/test/a.txt', 'w')
fob.writelines(listme)
fob.close()