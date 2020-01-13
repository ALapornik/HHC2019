lower = 1137  
upper = 7731  
  
for num in range(lower,upper + 1):  
    if "2" in str(num) : continue       # discard the number if it contains a 2
    elif "4" in str(num) : continue     # discard the number if it contains a 4
    elif "5" in str(num) : continue     # discard the number if it contains a 5
    elif "6" in str(num) : continue     # discard the number if it contains a 6
    elif "8" in str(num) : continue     # discard the number if it contains a 8
    elif "9" in str(num) : continue     # discard the number if it contains a 9
    elif "0" in str(num) : continue     # discard the number if it contains a 0
    for i in range(2,num):  # check if prime
        if (num % i) == 0:  
            break
    else:
        print(num)






