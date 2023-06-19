# 1) Создать массив на 5 ячеек и вывести его

# required_fruits = ["peach", "watermelon", "apple", "grapes", "melon"]
# fruits = ["apple", "watermelon", "melon", "peach", "grapes"]
#
# if len(fruits) == 5:
#     all_fruits_present = True
#     for fruit in required_fruits:
#         if fruit not in fruits:
#             all_fruits_present = False
#             break
#     if all_fruits_present:
#         print("Fruits -> " + str(fruits))
#     else:
#         print("CHECK! You have incorrect data in your array!")
# else:
#     print("Your array hasn't five values")

# 2) Создать массив на 5 ячеек и инициализировать его с клавиатуры пользователя
# names_of_students = ["Alya", "Kamila", "Roman", "Vitya", "Rostik"]
# ages_of_students = []
#
# print("Enter ages of students 5 times -> ")
# for i in names_of_students:
#     print("Age of student -> " + i + " -> ", end=" ")
#     age_of_student = abs(int(input()))
#     if age_of_student >= 15 and age_of_student <= 80:
#         ages_of_students.append(age_of_student)
#     else:
#         print("We are sorry! Your age doesn't match! ")
#         break
# if len(ages_of_students) == 5 and len(names_of_students) == 5:
#     for i in range(len(names_of_students)):
#         student = names_of_students[i]
#         age = ages_of_students[i]
#         if isinstance(student, str):
#            if isinstance(age, int):
#                 print(str(student) + ", " + str(age), end = " years old; ")

# 3) Создать массив пользовательской длины и инициализировать его с клавиатуры
#
# print("Let's fill in an array with float values -> ")
# float_val = []
# len_float_val = abs(int(input("Enter the length of your array -> ")))
#
# for i in range(len_float_val):
#     float_val_tmp = input("Enter float values for your array -> ")
#     try:
#         float_val_tmp = float(float_val_tmp)
#         if float_val_tmp.is_integer():
#             raise ValueError
#         float_val.append(float_val_tmp)
#     except ValueError:
#         print("We are sorry! Your values are incorrect! You need to enter just float values")
#         break
#
# if len(float_val) == len_float_val:
#     for i in range(len(float_val)):
#         f_val = float_val[i]
#         if isinstance(f_val, float):
#             print(str(f_val), end=" ; ")

# 4) Принять у пользователя массив на 10 чисел и вывести их сумму
# nums_sum = []
# i = 0
# while i < 10:
#     number = abs(int(input("Enter a number -> ")))
#     nums_sum.append(number)
#     i += 1
#
# sum_of_numbers = 0
#
# if len(nums_sum) != 10:
#     print("Error! Your array hasn't length of 10 vals! ")
# else:
#     for num in nums_sum:
#         sum_of_numbers += num
#     print("Sum of numbers -> ", sum_of_numbers)


# 5) Принять у пользователя массив на 10 чисел и вывести сумму четных ячеек массива
nums_even_i = []
even_sum = 0

for i in range(10):
    number = abs(int(input("Enter a number -> ")))
    nums_even_i.append(number)
    if number % 2 == 0:
        nums_even_i += number

print("Sum of even numbers -> ", even_sum)

# 6) Принять у пользователя массив на 10 чисел и вывести сумму четных значений
nums_even = []
for i in range(10):
    number = int(input("Enter a number -> "))
    nums_even.append(number)

even_numbers = []
for number in nums_even:
    if number % 2 == 0:
        even_numbers.append(number)

even_sum = sum(even_numbers)
print("Sum of even values -> ", even_sum)

# 7) Принять у пользователя массив на 10 чисел и вывести максимальное и минимальное число
num_min_max = []
for i in range(10):
    number = int(input("Enter a number -> "))
    num_min_max.append(number)

max_number = max(num_min_max)
min_number = min(num_min_max)

print("Maximum number ->", max_number)
print("Minimum number ->", min_number)

# 8) Принять у пользователя массив на 10 чисел и вывести сумму чисел между минимальным и максимальным значением
nums_min_max_val = []
for i in range(10):
    number = int(input("Enter a number -> "))
    nums_min_max_val.append(number)

max_number = max(nums_min_max_val)
min_number = min(nums_min_max_val)

if nums_min_max_val.index(min_number) < nums_min_max_val.index(max_number):
    sum_between = sum(nums_min_max_val[nums_min_max_val.index(min_number) + 1:nums_min_max_val.index(max_number)])
    print("Sum between the minimum and maximum numbers -> ", sum_between)
else:
    print("The minimum number appears after the maximum number in the array.")

# 9) Принять у пользователя массив на 10 чисел и вывести сумму ячеек между максимальным и минимальным \
nums_min_max_i = []
for i in range(10):
    num = abs(int(input("Enter a number -> ")))
    nums_min_max_i.append(num)

max_i = nums_min_max_i.index(max(nums_min_max_i))
min_i = nums_min_max_i.index(min(nums_min_max_i))

if min_i < max_i:
    sum_between = sum(nums_min_max_i[min_i + 1:max_i])
    print("Sum of values between the minimum and maximum numbers -> ", sum_between)
else:
    print("The minimum number appears after the maximum number in the array.")

# 10) Принять у пользователя массив на 10 чисел и вывести сумму разниц от центра до конца массива с от начала до центра
numbers_count_diff = []
for i in range(10):
    number = int(input("Enter a number -> "))
    numbers_count_diff.append(number)

center = len(numbers_count_diff) // 2

if len(numbers_count_diff) % 2 == 0:
    sum_from_center_to_end = sum(numbers_count_diff[center:])
    sum_from_start_to_center = sum(numbers_count_diff[:center])
else:
    sum_from_center_to_end = sum(numbers_count_diff[center + 1:])
    sum_from_start_to_center = sum(numbers_count_diff[:center])

print("Sum of differences from center to end -> ", sum_from_center_to_end)
print("Sum of differences from start to center -> ", sum_from_start_to_center)

# 11) Принять у пользователя массив на 10 логических значений и вывести количество правды

boolean_vals = []
for i in range(10):
    boolean = bool(input("Enter a boolean False, or True -> "))
    boolean_vals.append(boolean)

count_true = sum(boolean for boolean in boolean_vals if boolean)

print("Amount of True values -> ", count_true)

# 12) Принять у пользователя массив на 10 чисел и посчитать количество пар с шагом в 1
#
# numbers = []
# print("Enter integer values 10 times ->  ")
# for i in range(10):
#     while True:
#         try:
#             number = abs(int(input("Enter integer value ->  ")))
#             numbers.append(number)
#             break
#         except ValueError:
#             print("Invalid input. Please enter an integer.")

# count = 0
# for i in range(len(numbers) - 1):
#     if  numbers[i] == numbers[i+1] + 1 or numbers[i] == numbers[i+1] - 1:
#         print("Array values with step 1 -> " + str(numbers[i]) + " - " + str(numbers[i+1]) + " ;")
#         count += 1
#
# print("Your array with numbers -> " + str(numbers))
# print("Amount of pairs with step 1 -> ", count)