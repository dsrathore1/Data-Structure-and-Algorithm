'''
1. Let us say your expense for every month are listed below,
	1. January -  2200
 	2. February - 2350
    3. March - 2600
    4. April - 2130
    5. May - 2190

Create a list to store these monthly expenses and using that find out,

1. In Feb, how many dollars you spent extra compare to January?
2. Find out your total expense in first quarter (first three months) of the year.
3. Find out if you spent exactly 2000 dollars in any month
4. June month just finished and your expense is 1980 dollar. Add this item to our monthly expense list
5. You returned an item that you bought in a month of April and
got a refund of 200$. Make a correction to your monthly expense list
based on this

'''
months = [2200, 2350, 2600, 2130, 2190]

#1

print ("\n\nAns1:")
print ("1: In feb I spent",months[1] - months[0], "extra compare to January")

#2

print ("\n2: The total expense in first quater of the year is", months[0] + months [1] + months[2])

#3

print ("\n3 : Did I spent 2000$ in any months ?", 2000 == months)  #You can use 'or' in between 2000 and months

# or

if months == 2000 :

    print("3: You spent exactly 2000 dollars in one of them months")

else :

    print("\n3.1: No you do not spent exactly 2000 dollars in any months")


# 4

months.append(1980)

''' Append is use for adding items in lists REMEMBER THAT!!!!  '''

print ("\n4: In June my expense is 1980")

print (months)

#5

exe = months[3] - 200

print ("\n5: I got the discount on April so the expense is ", exe)

print(months, "\n\n")


''' ****************  END  **************** '''

print ("\n\n****************  END1  ****************\n\n")

'''
You have a list of your favourite marvel super heros.

heros=['spider man','thor','hulk','iron man','captain america']

Using this find out,

1. Length of the list
2. Add 'black panther' at the end of this list
3. You realize that you need to add 'black panther' after 'hulk',
   so remove it from the list first and then add it after 'hulk'
4. Now you don't like thor and hulk because they get angry easily :)
   So you want to remove thor and hulk from list and replace them with doctor strange (because he is cool).
   Do that with one line of code.
5. Sort the heros list in alphabetical order (Hint. Use dir() functions to list down all functions available in list)

'''

heros = ['spider man','thor','hulk','iron man','captain america']

print ("Ans2:")
#1

print ("1: ",len(heros))

#2

heros.append("black panther")

print ("2: ",heros)

#3

heros.remove("black panther")
heros.insert(3, "black panther")

print ("3: ",heros)

#4

heros[1:3] = ["doctor strange"]

print ("4: ",heros)

heros.sort ()

print("5: ",heros)

print ("\n\n****************  END2  ****************\n\n")

'''Create a list of all odd numbers between 1 and a max number.
Max number is something you need to
take from a user using input() function '''

j = int(input("Ans3: Enter the range of the number which you want between 1 to "))

f = []

for i in range (j):

    if (i % 2) != 0:

        f.append(i)

print (f)

print ("\n\n****************  END3  ****************\n\n")
