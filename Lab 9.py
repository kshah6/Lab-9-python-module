# Kunal Shah
# Date 02/10/2022

# Problem 1
# While loop to print Infinite
while True:
    print("Infinite")


# Problem 2

L = []
i=0
# While i is less than or equal to 10 append function is used to add the number
while i<=10:
    L.append(i)
    i=i+1
print(L)

# Problem 3

L=[]
# While loop if sum of L is less than equal to 100 append L
while(sum(L)<=100):
        n = int(input())
        L.append(n)


# Problem 4

counter = 0
tens=[]
# While loop to check if counter is less than equal to 50
while(counter<=50):
    # If Counter is divisble by 10 than append the counter 
    if counter % 10 == 0:
        tens.append(counter)
    counter = counter + 1

print(tens)
