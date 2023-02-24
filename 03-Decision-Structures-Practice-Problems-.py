#!/usr/bin/env python
# coding: utf-8

# 1) Write a program to calculate and print weekly pay for an hourly employee.  The employee gets paid $15/hour if he/she works 40 hours or less.  If the employee works for more than 40 hours, the employee gets overtime pay (which is 50% more than regular pay). 

# In[4]:


hours=int(input("how many hours did you work?: "))
pay = int(input("How much are you paid per hour?: "))
if hours<=40:
    print(f'you are paid ${hours*pay}')
else:
    print(f'you are paid ${hours*(pay*1.5)}')


# 2) Write a program to check whether a number is odd or even. Ask the user for the number.

# In[7]:


num=int(input("Please input a number: "))
if num%2==0:
    print("This number is even.")
else:
    print("This number is odd")


# 3) Write a program to take in two numbers (say num1 and num2) from the user and determine whether num1 is greater than or less than or equal to num2. <br>

# In[9]:


num1=int(input("Please enter a number: "))
num2=int(input("Please enter another number: "))
if num1<num2:
    print(f'{num1} is smaller than {num2}')
else:
    print(f'{num1} is greater than {num2}')


# 4) Write a program to check whether a number is between 90 and 100. Ask the user for the number.

# In[13]:


num=int(input("Input a number: "))
if 90<=num<=100:
    print(f'{num} is between 90 and 100')
else:
    print(f"{num} isn't between 90 and 100")


# 5) Write a program that determines whether a number is outside the range of 9 to 51. If the variable’s value is outside this range it should display “Invalid points.” Otherwise, it should display “Valid points.”  Ask the user for the number.

# In[15]:


num=int(input("Please input a number: "))
if not 9<=num<=51:
    print("Invalid points")
else:
    print("Valid points")


# 6) Determine if a customer qualifies for credit using salary and employment length as criteria. The customer qualifies for credit if he/she meets the following two conditions. i) salary is greater than 40,000, ii) the number of years of work experience is more than 2 years  <br>

# In[21]:


salary=float(input("Please enter your salary: "))

if salary>40000:
    years=int(input("Please enter your years of experience: "))
    if years>2:
        print(f'You are qualified for credit')
    else:
        print(f'You are not qualified for credit. You need {2-years} more years of experience')
else:
    print(f'You are not qualified for credit. You need ${40000-salary} more to qualify')


# 7) (Optional) Write a program to assign test score to a letter grade)<br>
# <li>Assign A grade if score >90
# <li>Assign B grade if score is between 81 and 90
# <li>Assign C grade if score is between 71 and 80
# <li>Assign F grade if score is less than or equal to 70

# In[34]:


grade=int(input("Please input your grade: "))
if grade>90:
    print("Grade A")
elif 81<grade<90:
    print("Grade B")
elif 71<grade<80:
    print("Grade C")
else:
    print("Grade F")

