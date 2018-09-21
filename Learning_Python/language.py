# Python 3.6.5 programming language - July ninth, 2018
# This script is about Python sintax and basic operations
# It was made by Erick Giffoni Felicíssimo
# contact : giffoni.erick@gmail.com
# github : https://github.com/ErickGiffoni
# linkedin : https://www.linkedin.com/in/erick-giffoni-022565167/
# instagram : @erick.giffoni
# Copyright © 2018 Erick Giffoni Felicíssimo. All rights reserved.

#*******************************************************************************

# MESSAGE TO THE READER :
    # Hi, there! WELCOME! Please, execute this script in your terminal before
    # you start reading and keep it running while you read this!
    # I hope you understand and learn!
    # Thank you, enjoy!

# execute : python language.py

#*******************************************************************************

# A brief perspective of numbers...
    # An integer:
num1 = 10
    # A float :
num2 = 10.1
    # Addition (+ or -):
num3 = num1 + num2 # this results in a float!
    # Multiplication (*):
num4 = num1 * num2 # this results in a float!
    # Division (/):
num5 = num1 / num2 # this results in a float!
        # NOTICE : if we divide two numbers and store the result in a variable,
        #          it'll result in a float, no matter what. Let's see :
num6 = 9 / 7
        # You can see in a calculator the result is 1.2857142857142858, a
        # periodical tithe, which is a float
    # Module (%):
        # it returns the remainder of a division, if that exists
num7 = 5%4  # the remainder is 1, and it's an integer!
num7 = 5.%4 # the remainder is 1.0, and it's a float!
            # NOTICE : we used dot(.) to say to Python that we want to generate
            #          a float number. 'Dot' could have been used on number 4,
            #  (4.)    insted, or on both numbers 5 and 4 (5.%4.)
    # Exponential (**):
num8 = 2**2 # the result is 4, and it's an integer. If we use dot, that'd be a
            # float

#*******************************************************************************

# A brief perspective of logical operators...
    # not :
        # this operator denies an operation, for example:
this_is = True # our variable is true
not this_is    # now it is false
    # and :
        # this operator results True only if both parameters are True :
        # Var1  Var2    Var1 and Var2
        #  T     T            T
        #  T     F            F
        #  F     T            F
        #  F     F            F
that_is = False
this_is and that_is # results False
    # or :
        # it's similar to operator 'and', but this results False only if both
        # parameters are False :
        # Var1  Var2    Var1 or Var2
        #  T     T           T
        #  T     F           T
        #  F     T           T
        #  F     F           F
this_is or that_is # results True
    # NOTICE : Logical Expressions
        # Logical operators can be used in the same expression. When that
        # happens, the operator 'not' is evaluated first, then Python evaluates
        # 'and'. At last, 'or' is evaluated. See further :
        #         True or False and not True
        #           True or False and False
        #                True or False
        #                    True

#*******************************************************************************

# How to print ?
print("*** This is the print() function! ***\n" +
      "\tIts parameters should be the same type!")
option = input("Press enter to continue: ")

    #You can convert diferent types to other types, you just have to use
    # a function like : int(), float(), srt(), etc
    # Example:
number = 3.2
int(number) #converts number, which is a float, to int
    #This should cause error :
        # print("The number is: " + number)
    # and it does, because we have in the same print both strings and float
    # To solve it,we can convert number to string, like this:
print("The number was converted to string! -> Number: " + str(number))

    # You can also print diferent types in the same print() by specifying
    # the type each variable is, like this :
text = "Hello!"
number = 792018
option = input("Press enter to continue: ")
print("This is a string: %s"%text + " And this is a number: %d"%number)
    # To confirm what was said, let's use the type() function to see
    # the types of our variables and print it :
type_text = type(text)
type_number = type(number)
option = input("Press enter to continue: ")
print(type_text); print("is the type of 'Hello'")
print(type_number); print("is the type of 'number'")
    # NOTICE : 1- what was done at line 99 (str(number)) didn't change the
    #             type of 'number' for real. But, for a moment, that variable
    #             was converted, so the print function could work.
    #          2- at lines 112 and 113 we used ';' to separate two comands on
    #             the same line. Without it, Python wouldn't understand what
    #             we wanted, and it would cause a sintax error.
print("*"*20 + '\n')
option = input("Press enter to continue: ")

#*******************************************************************************

# How to read something from the user ?
print('*** This is the input() function! ***\n' +
       "\tYou can pass as parameter a string and read\n\tsomething" +
       ' from the user at the same time!')
option = input("Press enter to continue: ")

    # Let's explain what was said with an example :
    # Let's read your age : (you must execute this script in your terminal
    #                        using 'python language.py')
age = input("Tap out your age here: ")
print("Nice! You are " + "%d" %int(age))

    # NOTICE : at line 135, if we didn't use the int() function to convert
    # 'age' as integer, it would go wrong. This fact tells us that Python
    # interprets our variable as a string, even though it's a number.
    # BUT HEY ! What if, for some reason, the user taps out a string instead of
    # a number ? Let's see...
    # Execute this script again and tap out anything that's not a number!
    # Well, you may have seen that it caused an error, an ValueError for
    # int() on the print(). What can we do?  We learned how to convert things
    # above, so let's do it : (execute the script again)
option = input("Press enter to continue: ")
age = int(input("Now we convert: Tap out your age here: "))
print("Nice! You are " + "%d" %age)
    # Now, what we did at line 147 was to say to Python that :
    # 1- if the user taps out a float number, Python will generate a ValueError
    #    on the age (line 147)
    # 2- if he taps out something else, the error will continue.
    # So what we did at all ? We basicly changed where our code would generate
    # an error. It generates an error on the validation of the age (line 147),
    # instead of generating an error on the print() (line 148), and that might
    # be useful somehow later.

    # Until now we just read numbers from the user. Let's read your name, then :
option = input("Press enter to continue: ")
name = input("Tell me what is your name? ")
print("Hi, " + name.upper() + ". I'm glad you're enjoying!")
    # That's cool! Now, NOTICE :
    #                   1- if you execute this script again and, instead of
    #                      tapping out a string, you tap out a number, nothing
    #                      will go wrong! That fact confirms what we assumed
    #                      at line 139. WOWWW :p
    #                   2- at line 161, on the print(), we used '.upper()'on our
    #                      variable name. You should know that Python is an
    #                      Object Oriented programming language, so 'name' is an
    #                      object of class str and 'upper()' is a method of
    #                      that class. A method is like a function, and this
    #                 specific method converts our string to upper case letters.
    #                 We use '.' (dot) to access a class method.
print("*"*20 + '\n')
option = input("Press enter to continue: ")

#*******************************************************************************

# How to use IF ?
print("*** This is the 'IF' condition ! ***")
option = input("Press enter to continue: ")

    # The structure to use IF is quite simple:

    # if <condition> :
    #   instructions

    # Let's do an example : imagine we want to read two numbers and say which
    # one is the bigger. We can do like this :
number1 = input("Tap out a number: ")
number2 = input("Tap out another number: ")
bigger = False # let's use this boolean operator to say there isn't a bigger
if number1 > number2 :
    bigger = number1
if number1 < number2 :
    bigger = number2
if number1 == number2:
    print("The numbers are equal !")
    # and then we print 'bigger'
if bigger : # this means : if there is a bigger number!
    print(str(bigger) + " is bigger!")
    # NOTICE : if you execute this script again and tap out letters instead of
    # numbers, nothing will go wrong. That's problably because Python works with
    # chart ASCII, which means that every letter has a corresponding number
    # Simple simple, yeah ?
print("*"*20 + '\n')
option = input("Press enter to continue: ")

#*******************************************************************************

# How to use ELSE ?
print("*** This is the 'ELSE' condition ! ***")
option = input("Press enter to continue: ")

    # To ilustrate how simple and easy ELSE is, let's use this example : we want
    # to know whether a camera is ON or OFF. So...
print("Is that camera ON or OFF ?\n\tTap 1 for ON\n\tTap anything for OFF")
camera = input()
if camera == str(1) : # which means : if the camera is on
    print("It seens it's ON!")
else : # which means : if any option is true
    print("It seens it's OFF...")

    # Without ELSE, we'd have to use two IF's, but ELSE summarises what we want!
    # NOTICE : remember Python understands our variables as strings, even though
    #          if they're numbers? So, that's why we had to convert '1' using
    #          srt() function at line 219
    # Structure :

    # if <condition> :
    #   instructions
    # else :
    #   instructions

    # Both IF and ELSE must be even, differently it'll cause a sintax error
    # Simple simple, yeah ?
print("*"*20 + '\n')
option = input("Press enter to continue: ")

#*******************************************************************************

# How to use ELIF ?
print("*** This is the 'ELIF' condition ! ***\n\t"
       + "It can replace a pair ELSE IF and it has the same meaning !")

    # Let's understand this...
    # Imagine we have a store and we sell four different types of bags. We
    # want to know which type of bag the customer has choosen. So...
    # let's aks him :
option = input("Press enter to continue: ")
print("Welcome to our store! which bag do you want?\n\t"
      "Tap 1 for red\n\tTap 2 for blue\n\tTap 3 for black\n\tTap 4 for green")
bag = input()
if bag == str(1) :
    print("Bag 1 coming up! Thank you!")
elif bag == str(2) :
    print("Bag 2 coming up! Thank you!")
elif bag == str(3) :
    print("Bag 3 coming up! Thank you!")
elif bag == str(4) :
    print("Bag 4 coming up! Thank you!")
else :
    print("Sorry! This is not an option...")

    # This is how we do it...
print("*"*20 + '\n')
option = input("Press enter to continue: ")

#*******************************************************************************

# How to use WHILE ?
print("*** This is the 'While' loop ! ***\n\t"
        + "It is used when we want our code to be repeated sometimes")
    # Its sintax is simple and very useful :

    # while <condition> :
    #   instructions

    # Using WHILE can save your time and also save some computer memory, as
    # we don't need to repeat same instructions, because it executes the code
    # for how many times we want.
    # Think about this : what would you do if you had to read the names of
    # four people from your family? Well, you could code four input() functions
    # and store the names into diferent variables.
    # Now, I propound you a better solution...
option = input("Press enter to continue: ")
family_names = list(range(0,4))
i = 0
while i <= 3 :
  family_names[i] = input("What is the name? ")
  i += 1
i=0
while i<= 3 :
  print("\t" + "Family name %d: "%i + family_names[i])
  i+=1
print("That's AMAZING !!! :)")
    # As you can see, our code starts at line 287, where we declare a list,
    # 'family_names'. A list is variable type that allows us to store many
    # values accessed by an index. In Python, the first element on a list is
    # indexed by 0(zero) and so on. Then, as a parameter of list() function we
    # called another function, 'range()', and as a parameter of range() function
    # we used two numbers. The first number (0) tells Python where our list
    # begin and also tells it to store number 0 at the first position on our
    # list. Then, the second number (4) tells Python two things : 1- our list
    # has four positions indexed 0-3, and 2- the following numbers on our list
    # are 1,2,3(NOTICE that number 4 is not included). So by then we have a list
    # like this [0,1,2,3] and this is not gonna be a problem.
    # Next, we created a variable 'i' to control iterations, as you can see at
    # lines 289 and 293. What we did at line 289 was say to Python : execute
    # lines 290 and 291 until 'i' is up to 3. Then, 'family_names[i]' is how we
    # access each index of our list and we store a name on it. At line 291 we
    # had to increase 'i'. If we didn't, that while loop would not stop being
    # executed.
    # Hereunder, we want to print all the names on 'family_names', from index 0
    # to 3. So, at line 292 we reset 'i' and below that we start a new while
    # loop just to do the print of the names. The operator '\t' on the print has
    # the same function as 'tab' on your keyboard.

    # Nice, yeah?
print("*"*20 + '\n')
option = input("Press enter to continue: ")

#*******************************************************************************

# How to use LISTS ?
print("\t* LISTS *")
print("*** We already know about lists ! ***\n\t"
      + "But let's learn a bit more !")
    # As we know, lists are like vectors and matrixes, and they may contain
    # different types on the same list. No harm done !

    # Slicing lists !
        # You can get elements from a list by applying a range, like this :
date = [7,10,2018] # a list of 3 numbers
date[0:2] # this returns [7, 10] ; [0:2] is our range !
date[:]   # this returns the hole list
date[-2]  # this returns [10], which means the last element from a list is
          # indexed by -1 and so on
date[1:3] # this returns [10, 2018]
date[1:-2]; date[0:0] # both return empty
        # Did you get the ideia ? [where it begins : where it ends]
        #                                           (not included)
    # 'len()' function
        # it returns the length of a list
len(date) # this returns 3
    # Some methods !
        # .append()
          # this method is used to add a new element on a list, like :
date.append('it works!')
          # as a parameter of .append() we pass what we want to add to our list
          # and that can be an int or float or string or even another list !
option = input("Press enter to continue: ")
print("This is our list: " + str(date))
        # .pop()
          # this method is used when we want to remove a element from a list,
          # but it also return a value : the element we removed.
          # We can use 'del' to remove something from a list, but it doesn't
          # have a return. We can do 'del date[3]' for example, and it will
          # remove '[it works!]' from 'date'. But let's use .pop() :

          # Simple example : remember our family_names list ? All right...
          # let's say that everyone on that list was home together,
          # but somebody left...
option = input("Press enter to continue: ")
print("\nWait a second... it seems somebody from the family left...")
print("Who left ? - options(0, 1, 2 or 3)")
this_person_left = input("It was option ")
if this_person_left != str(0) and this_person_left != str(1) and this_person_left != str(2) and this_person_left!= str(3) :
    print("It seems that you don't know...")
else :
    print("How pity! " + family_names.pop(int(this_person_left)) + " left !")
          # Wooow ! How nice. Now, I think you have known enough to be able to
          # understand what is happening above. Although, I'll explain just line
          # 371. Remember what was said about '.pop()' and its return ? So, we
          # did 'family_names.pop' because we wanted it to return who had left
          # from our 'family_names' list. But just that is incomplete, we have
          # to pass a number as parameter and this number will be the index from
          # the person on family_names list that had left. So, as
          # 'this_person_left' is a string, we used int() function to convert it
          # to an integer, and this was our parameter to .pop() method, which
          # returned the name we wanted.
print("*"*20 + '\n')
option = input("Press enter to continue: ")

#*******************************************************************************
