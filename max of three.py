def function(firs, second, third):
	if firs[:] > second[:] and firs[:] > third[:]:
		print(firs)
	elif second[:] > firs[:] and second[:] > third[:]:
		print(second)
	elif third[:] > firs[:] and third[:] > second[:]:
		print(third)

function('Pavle', 'Maja', 'Ivannnnn')


def function2(firs, second, third):
	if len(firs) > len(second) and len(firs) > len(third):
		print(firs)
	elif len(second) > len(firs) and len(second) > len(third):
		print(second)
	elif len(third) > len(firs) and len(third) > len(second):
		print(third)
function2('Pavleeeeeee', 'Maja', 'Vedran')