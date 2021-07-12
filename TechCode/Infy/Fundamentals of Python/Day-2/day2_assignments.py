#13-02-2021

#Day-2

"""7. Write a python program that displays a message as follows for a given
number:
● If it is a multiple of three, display "Zip"
● If it is a multiple of five, display "Zap".
● If it is a multiple of both three and five, display "Zoom".
● If it does not satisfy any of the above given conditions, display "Invalid"."""

def disp_msg(n:int):
	if n%3==0 and n%5!=0:
		print("Zip")
	elif n%5==0 and n%3!=0:
		print("Zap")
	elif n%3==0 and n%5==0:
		print("Zoom")
	else:
		print("Invalid")
disp_msg(30)
disp_msg(39)
disp_msg(67)
disp_msg(25)

#8. ->Kindly refer to the md file for this day for the question..
def grade(g):
	if 80<=g<=100:
		res="A"
	elif 73<=g<=79:
		res="B"
	elif 65<=g<=72:
		res="C"
	elif 0<=g<=64:
		res="D"
	else:
		res="Z"
	return res
print(grade(100))
print(grade(3687))
print(grade(52))

#9. ->Kindly refer to the md file for this day for the question..
def prod_of_three_nos(n1,n2,n3):
	if n1!=7 and n2!=7 and n3!=7:
		product=n1*n2*n3
	elif n1==7 and n2!=7 and n3!=7:
		product=n2*n3
	elif n1!=7 and n2==7 and n3!=7:
		product=n3
	elif n3==7:
		product=-1
	return product
print(prod_of_three_nos(1,5,3))
print(prod_of_three_nos(3,7,8))
print(prod_of_three_nos(7,4,3))
print(prod_of_three_nos(1,5,7))

#10. ->Kindly refer to the md file for this day for the question..
def coins(x,y,z):
	if (x*5)+y<z:
		print(-1)
	else:
		print("5 rupees coins needed={}, 1 rupee coins needed={}".format(z//5,z%5))
coins(4,2,21)
coins(2,11,11)
coins(3,3,19)


#You can check the output by running the code on your device :)









