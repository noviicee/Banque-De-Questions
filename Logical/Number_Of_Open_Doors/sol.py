def numberOfDoorsOpen(N):
    return int(N**1/2)

if __name__=="__main__":
    N=int(input("Enter nummber of doors: "))
    print("No. of doors open are: ", end=" ")
    print(numberOfDoorsOpen(N))
