n = int(input("Enter the number : "));
primelist = []
def prime(n):
    if (n == 0):
        return
    for i in range(2,n):
        for j in range(1,i):
            count = 0
            if(j%i == 0):
                count += 1
            if (count == 2):
                primelist.append(i)
    return primelist
result = prime(n)
print("Prime numbers upto given number are : ")
print(result)


#lower_red2 = np.array([170,50,50])
#upper_red2 = np.array([180,255,255])