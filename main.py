# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

lower_name1 = name1.lower()
lower_name2 = name2.lower()

#variable to store the count of indiviual instances of each letter
true_t = 0
true_r = 0
true_u = 0
true_e = 0

love_l = 0
love_o = 0
love_v = 0
love_e = 0


#code for counting tens

true_t += (lower_name1.count("t"))

true_r += (lower_name1.count("r"))

true_u += (lower_name1.count("u"))

true_e += (lower_name1.count("e"))



true_t += (lower_name2.count("t"))

true_r += (lower_name2.count("r"))

true_u += (lower_name2.count("u"))

true_e += (lower_name2.count("e"))

# #code for counting units

love_l +=  lower_name1.count("l")

love_o +=  lower_name1.count("o")

love_v +=  lower_name1.count("v")

love_e +=  lower_name1.count("e")


love_l +=  lower_name2.count("l")

love_o +=  lower_name2.count("o")

love_v +=  lower_name2.count("v")

love_e +=  lower_name2.count("e")

#displays total iteration of each letter for boths names

print(f"T occurs {true_t} times")
print(f"R occurs {true_r} times")
print(f"U occurs {true_u} times")
print(f"E occurs {true_e} times")

#adds count for "TRUE" 
print(f"Total = {true_t + true_r + true_u + true_e}")

#displays total iteration of each letter for boths names

print(f"L occurs {love_l} times")
print(f"O occurs {love_o} times")
print(f"V occurs {love_v} times")
print(f"E occurs {love_e} times")

#adds count for "LOVE"
print(f"Total = {love_l + love_o + love_v + love_e}")

#Add the value of each letter and convert the value of "love" to tens and add it to units

count_units = love_l + love_o + love_v + love_e
total_count = ((true_t + true_r + true_u + true_e) * 10 + count_units)

#condition to print score and messages

if total_count < 10 or total_count > 90:
  print(f"Your score is {total_count}, you go together like coke and mentos.")
elif total_count >= 40 and total_count < 50:
  print(f"Your score is {total_count}, you are alright together")
else:
  print(f"Your score is {total_count}.")


# "Your score is **x**, you go together like coke and mentos."

# "Your score is **y**, you are alright together."

# "Your score is **z**."



###############
#Angela's code
###############

#Write your code below this line 👇

# combined_names = name1 + name2
# lower_names = combined_names.lower()
# t = lower_names.count("t")
# r = lower_names.count("r")
# u = lower_names.count("u")
# e = lower_names.count("e")
# first_digit = t + r + u + e

# l = lower_names.count("l")
# o = lower_names.count("o")
# v = lower_names.count("v")
# e = lower_names.count("e")
# second_digit = l + o + v + e

# score = int(str(first_digit) + str(second_digit))

# if (score < 10) or (score > 90):
#   print(f"Your score is {score}, you go together like coke and mentos.")
# elif (score >= 40) and (score <= 50):
#   print(f"Your score is {score}, you are alright together.")
# else:
#   print(f"Your score is {score}.")