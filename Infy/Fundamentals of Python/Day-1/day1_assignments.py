#11-02-2021

#Day-1

#1. Write a code to find the minimum among three given numbers.
def min_of_three(a,b,c):
	if a<b:
		if a<c:
			return a
		return c
	else:
		if b<c:
			return b
		return c

print(min_of_three(1,2,3)) #1
print(min_of_three(11,2,34)) #2
print(min_of_three(177,26,3)) #3

#2.  Write a code to check whether a given number is a palindrome.
def check_palindrome(num):
	s=str(num)
	if s==s[::-1]:
		return True
	return False

print(check_palindrome(6283782)) #False
print(check_palindrome(62833826)) #True
print(check_palindrome(628373826)) #True
print(check_palindrome(6283782.556)) #False #It works for floating-point numbers as well. This is because we are converting it into string.
#If we would have used another method (like %,/,or//), it would face some issues while working with floating-point numbers.

#The above code for checking palindrome won't work if we provide a negative number.
#To make it work even for negative numbers, we can run the below code-
def check_palindrome(num):
	s=str(abs(num)) #abs #open("link.html", "r").read('<a href="http://www.example.com"> Link </a>')
	if s==s[::-1]:
		return True
	return False

print(check_palindrome(-1737371)) #True

"""3.Write a code to find the sum of numbers divisible by 4.The code must allow the user to accept a number and add it to the
sum if it is divisible by 4. It should continue accepting numbers as long as the user wants to provide an input and should
display the final sum."""
s=0
l=[int(ele) for ele in input().split()]
for i in l:
	if i%4==0:
		s+=i
print(s)

"""4. A three digit number is said to be an “Armstrong number” if the sum of the third power of its individual digits is equal to
the number itself.Write a program to check whether a number is armstrong or not."""
n=int(input("Enter a three digit number:"))
o=n%10
t1=n//10
t=t1%10
h=t1//10
s1=n
s2=(o**3)+(t**3)+(h**3)
print(h,t,o)
print(s1,s2)
if s1==s2:
	print("Armstrong")
else:
	print("Not Armstrong")

#Fun-fact: Armstrong numbers are also known as Narcissistic numbers

#5. #open("link.html", "r").read('<a href="http://www.example.com"> Link </a>')
def student_total_fee(branch,score,coursefee):
	
	if branch=="Arts":
		if score>90:
			scholarship=0.50*coursefee
			final_fee=coursefee-scholarship
			return final_fee
		elif score%2!=0:
			scholarship=0.05*coursefee
			final_fee=coursefee-scholarship
			return final_fee
		elif score>90 and score%2!=0:
			scholarship=0.50*coursefee
			final_fee=coursefee-scholarship
			return final_fee
	elif branch=="Engineering":
		if score>85:
			scholarship=0.50*coursefee
			final_fee=coursefee-scholarship
			return final_fee
		elif score%7==0:
			scholarship=0.05*coursefee
			final_fee=coursefee-scholarship
			return final_fee
		elif score>85 and score%7==0:
			scholarship=0.50*coursefee
			final_fee=coursefee-scholarship
			return final_fee

print(student_total_fee("Arts",79,12000))

"""6. The flight ticket rates for a round-trip (Mumbai->Dubai) were as
follows:
● Rate per Adult: Rs. 37550.0
● Rate per Child: 1/3rd of the rate per adult
● Service Tax: 7% of the ticket amount (including all passengers)
● As it was a holiday season, the airline also offered a 10%
discount on the final ticket cost (after inclusion of the service
tax).
● Find and display the total ticket cost for a group which had
adults and children."""

def flight_ticket_rate(numofAdults,numofChildren):
	rate_per_adult=37550.0
	rate_per_Child=1/3*(rate_per_adult)
	rate_adults=numofAdults*rate_per_adult        #262850
	rate_children=numofChildren*rate_per_Child    #12516.6*3 -> 37550.0
	total_cost=(rate_adults+rate_children)        #300400
	tax=7/100*(total_cost)                        #21028
	total_ticket_cost=total_cost+tax              #321428
	discount=0.1*(total_ticket_cost)              #32124.8
	final_ticket_cost=total_ticket_cost-discount  #289285.2
	return final_ticket_cost

print(flight_ticket_rate(7,3))

