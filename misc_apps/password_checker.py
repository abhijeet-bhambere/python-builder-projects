# A verry basic app that will heck if user-entered passwrd fits all the criteria.
# All checks are registered into respective flags, which will be clubbed into a list.
# At the end, show the password strength depending on how many conditions are met.

# Take user input
password = input(">>>Enter a password: ")
# Initiate a list to store the checks; append all checks and declare final result at end
results=[]

# Condition 1 -- check password length
is_len = False
if len(password)>=8:
    is_len=True
results.append(is_len)

# Condition 2 -- check if contains atleast one numeric
is_digit = False
for each in password:
    if each.isdigit():
        is_digit = True       
results.append(is_digit)

# Condition 3 -- check if contains atleast one upper case
is_upper = False
for each in password:
    if each.isupper():
        is_upper = True
results.append(is_upper)

# Condition 4 -- check if contains a special character
is_spechar = False
for each in password:
    # condition will return False if contain special character
    if each.isalnum()==False:
        is_spechar=True
results.append(is_spechar)

print(results)

# Combining results of all 3 conditions
# Method 1 - Using sum() method -- sums up all true values
# check the difference with length of the list
# ****************************the working method****************************
strength = len(results) - sum(results)
if strength==0:
    print("🟩  Strong password")
elif strength<3:
    print("🟧  Moderate password")
elif strength==3:
    print("🟥  Weak password")

print("===============================")
# print(results)
# Collecting all details for display
details = []
# Print condition-1 result
if results[0]==True:
    result_len = "✔️ Password has 8️⃣ chars"
else:
    result_len = "❌ Password does not have 8️⃣  chars"

details.append(result_len)

# Print condition-2 result
if results[1]==True:
    result_digit = "✔️ Password has atleast 1 digit"
else:
    result_digit = "❌ Password does not have even 1 digit"

details.append(result_digit)

# Print condition-3 result
if results[2]==True:
    result_upper = "✔️ Password has atleast 1 Uppercase character"
else:
    result_upper = "❌ Password does not have even 1 Uppercase character"

details.append(result_upper)

# Print condition-4 result
if results[3]==True:
    result_upper = "✔️ Password has atleast 1 special character"
else:
    result_upper = "❌ Password does not have even 1 special character"

details.append(result_upper)

# Print the details --
for each in (details):
    print(each)
# ****************************the working method****************************



# Alternate method -- using the counter module
# from collections import Counter

# lst = [True, False, True, True, False]
# counts = Counter(lst)

# print(f"True: {counts[True]}, False: {counts[False]}")


