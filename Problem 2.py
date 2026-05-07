#Problem 2
#Find the range of numbers
numbers = []
#get first value from user
value = float(input("Enter value: "))
#loop until user enters 0
while value != 0:
    #add value to list
    numbers.append(value)
    #ask for next value
    value = float(input("Enter value (or 0 to end: "))
#display the list
print(numbers)
#assume first number is min and max
min_value = numbers[0]
max_value = numbers[0]
#loop through list to find min and max
for num in numbers:
    if num > max_value:
        max_value = num
    if num < min_value:
        min_value = num

#calculate range
range_value = max_value - min_value
#display range
print(f"Range= {range_value}")
