class Mom:
	var1='hey im mom'

class Dad:
	var2='hey there son im dad'

class Child(Mom, Dad):
	var3='im a new variable'

childObject=Child()
print(childObject.var1)
print(childObject.var2)
print(childObject.var3)