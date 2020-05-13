import ImportModules
ImportModules.testmod()

baby=ImportModules.testmod
baby()

reload(ImportModules)
ImportModules.testmod()