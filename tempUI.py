import proj
check = proj.checkUserPass("hello", "boi")
if check is None:
	print("Not a valid userName or Password")
		
else:
	print (check)