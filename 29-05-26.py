# Slicing

# marks=[10,20,30,40,50,60,70,80,90,100]
# # [start-0:stop-1:step-1]
# sub_list=marks[3:7]
# print(sub_list)

# marks=[10,20,30,40,50,60,70,80,90,100]
# # [start-0:stop-1:step-1]
# sub_list=marks[2:9]
# print(sub_list)

# marks=[10,20,30,40,50,60,70,80,90,100]
# # [start-0:stop-1:step-1]
# sub_list=marks[2:9:2]
# print(sub_list)

# marks=[10,20,30,40,50,60,70,80,90,100]
# # [start-0:stop-1:step-1]
# sub_list=marks[2:9:2]
# print(sub_list)

# marks=[10,20,30,40,50,60,70,80,90,100]
# # [start-0:stop-1:step-1]
# # sub_list=marks[3:7]
# # sub_list=marks[2:9:2]
# sub_list=marks[:-1]
# print(sub_list)

# marks=[10,20,30,40,50,60,70,80,90,100]
# # [start-0:stop-1:step-1]
# # sub_list=marks[3:7]
# # sub_list=marks[2:9:2]
# sub_list=marks[:7]
# print(sub_list)

# marks=[10,20,30,40,50,60,70,80,90,100]
# # [start-0:stop-1:step-1]
# # sub_list=marks[3:7]
# # sub_list=marks[2:9:2]
# sub_list=marks[:-1]
# print(sub_list)

# marks=[10,20,30,40,50,60,70,80,90,100]
# # [start-0:stop-1:step-1]
# # sub_list=marks[3:7]
# # sub_list=marks[2:9:2]
# sub_list=marks[:]
# print(sub_list)

# marks=[10,20,30,40,50,60,70,80,90,100]
# # [start-0:stop-1:step-1]
# # sub_list=marks[3:7]
# # sub_list=marks[2:9:2]
# sub_list=marks[2:0:-1]
# print(sub_list)

# marks=[10,20,30,40,50,60,70,80,90,100]
# # [start-0:stop-1:step-1]
# # sub_list=marks[3:7]
# # sub_list=marks[2:9:2]
# sub_list=marks[2:0:]
# print(sub_list)

# marks=[10,20,30,40,50,60,70,80,90,100]
# # [start-0:stop-1:step-1]
# # sub_list=marks[3:7]
# # sub_list=marks[2:9:2]
# sub_list=marks[2:0:-1]
# print(sub_list)

# marks=[10,20,30,40,50,60,70,80,90,100]
# # [start-0:stop-1:step-1]
# # sub_list=marks[3:7]
# # sub_list=marks[2:9:2]
# sub_list=marks[5::-1]
# print(sub_list)

# marks=[10,20,30,40,50,60,70,80,90,100]
# # [start-0:stop-1:step-1]
# # sub_list=marks[3:7]
# # sub_list=marks[2:9:2]
# sub_list=marks[5:0:-1]
# print(sub_list)

# marks=[10,20,30,40,50,60,70,80,90,100]
# # [start-0:stop-1:step-1]
# # sub_list=marks[3:7]
# # sub_list=marks[2:9:2]
# sub_list=marks[:6:-1]
# print(sub_list)

# marks=[10,20,30,40,50,60,70,80,90,100]
# # [start-0:stop-1:step-1]
# # sub_list=marks[3:7]
# # sub_list=marks[2:9:2]
# sub_list=marks[::-1]
# print(sub_list)

# marks=[10,20,30,40,50,60,70,80,90,100]
# # [start-0:stop-1:step-1]
# # sub_list=marks[3:7]
# # sub_list=marks[2:9:2]
# sub_list=marks[5:3:-1]
# print(sub_list)

# marks=[10,20,30,40,50,60,70,80,90,100]
# # [start-0:stop-1:step-1]
# # sub_list=marks[3:7]
# # sub_list=marks[2:9:2]
# sub_list=marks[:3:-1]
# print(sub_list)

# marks=[10,20,30,40,50,60,70,80,90,100]
# # [start-0:stop-1:step-1]
# # sub_list=marks[3:7]
# # sub_list=marks[2:9:2]
# sub_list=marks[:3]
# print(sub_list)

# marks=[10,20,30,40,50,60,70,80,90,100]
# # [start-0:stop-1:step-1]
# # sub_list=marks[3:7]
# # sub_list=marks[2:9:2]
# sub_list=marks[:3:-2]
# print(sub_list)

# Question1
# Wap to swap the first value of list with last value of list
# [10,11,20,31,30,33,40,55,50,60,70,80]
# answer[80,11,20,31,30,33,40,55,50,60,70,10]

# my_list=[10,11,20,31,30,33,40,55,50,60,70,80]

# first_elm=my_list[0]
# last_elm=my_list[-1]

# my_list[-1]=first_elm
# my_list[0]=last_elm

# print(my_list)



# [10,20,30,40]
# [40,20,30,10]

# my_list=[10,20,30,40]

# first_elm=my_list[0]
# last_elm=my_list[-1]

# my_list[-1]=first_elm
# my_list[0]=last_elm

# print(my_list)

# Question2
# 1.Wap to find the sum of the all element in the list : [10,20,30,40].
# 2.Wap to find the sum of only even element in the list : [10,3,4,6,22,31,33,55,40].
# 3.Wap to find the sum of only odd element in the list : [10,3,4,6,22,31,33,55,40].
# 4.Wap to find the count of how many int value and how many str in the list.
# : [70, "aman", 50,10,20, "rohan", "iq-india"].

# Wap to find the sum of the all element in the list : [10,20,30,40].

# ..........................ignore
# numbers = [10, 20, 30, 40]
# print(sum(numbers[0:4]))  # slicing used here
# .............................................ignore

# List of numbers
# numbers = [10, 20, 30, 40]

# sliced_numbers = numbers[:]

# total = sum(sliced_numbers)

# print("Sum of all elements:", total)

# Q2

# numbers = [10, 3, 4, 6, 22, 31, 33, 55, 40]

# sum_even = 0

# for num in numbers:
#     if num % 2 == 0:   
#         sum_even = sum_even + num
# print("Sum of even numbers:", sum_even)