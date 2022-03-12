def stringing(s, n): 

    # if offset is 1 
    if (n == 1): 

        # simply print the 
        # string and return 
        print(s)              
        return

    # Get length of the string 
    l = len(s) 

    # Create a 2d character array 
    a = [[" " for x in range(l)] for y in range(l)]  

    # for counting the  
    # rows of the ZigZag 
    row = 0
    for i in range(l): 

        # put characters in the matrix 
        a[row][i] = s[i];  

        # You have reached the bottom 
        if row == n - 1: 
            down = False    
        elif row == 0: 
            down = True
        if down == True: 
            row = row + 1
        else: 
            row = row - 1

    # Print the Zig-Zag String 
    for i in range(n): 
        for j in range(l): 
            print(str(a[i][j]), end = " ") 
        print() 



# to define stars for intended number of rows
def mul_star(n):
    
    if n==3:
        star = '*' * 9
    
    elif n==2:
        star = '*' * 5
    
    else:
        temp = n-3
        star = '*' * (9+4*temp)

    return star


# driver code
n = int(input('enter the row '))#represents the number of rows you want the wave to be
x = mul_star(n)
stringing(x, n) 