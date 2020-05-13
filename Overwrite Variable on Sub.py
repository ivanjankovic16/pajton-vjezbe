class parent:
	var1='bacon'
	var2='snausage'

class child(parent):
	var2='toast'

pob=parent()
cob=child()

print(pob.var1)
print(pob.var2)
print(cob.var1)
print(cob.var2)