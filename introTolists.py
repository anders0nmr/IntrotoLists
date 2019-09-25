# #simple code to count the number of periods in a string
# ipAddress = input('Please Enter an IP Address')
# print(ipAddress.count('.'))

# #list can be sequence of many things including a list of lists
# parrot_list = ['non pinin', 'no more', 'a stiff', 'bereft of life']
# #appending a value to a list
# parrot_list.append('cool')
# #for loop with list
# for state in parrot_list:
#     print('This parrot is ' + state)
#
# #simple loop through 2 lists to do addition
# even = [2,4,6,8]
# odd = [1, 3, 5, 7, 9]
# #Numbers concatonates lists
# numbers = even + odd
# #simple code to print sorted numbers
# numbers.sort()
# print(numbers)
# for x in odd:
#     for y in even:
#         addition = x + y
#         print(addition)

#creating a list using a constructor
list_1 = []
list_2 = list()
#prints out a list, char by char
# print(list('The lists are equal'))

#even and another even refer to the same list, so if we reverse one, the other is also reversed
# even = [2, 4, 6, 8]
# another_even = even
# another_even.sort(reverse=True)
# print (even)

#example creating list of lists and printing values from list of lists and each lists contents
# even = [2, 4, 6]
# odd = [1, 3, 5]
# numbers = [even, odd]
#
# for number_set in numbers:
#     print(number_set)
#
#     for value in number_set:
#         print(value)

menu = []
menu.append(['eggs', 'spam', 'bacon'])
menu.append(['egg', 'sausage', 'bacon'])
menu.append(['egg', 'spam'])
menu.append(['egg', 'bacon', 'spam'])
menu.append(['egg', 'bacon', 'sausage', 'spam'])
menu.append(['spam', 'bacon', 'sausage', 'spam'])
menu.append(['spam', 'egg', 'spam', 'spam', 'bacon', 'spam'])
menu.append(['spam', 'egg', 'sausage', 'spam'])

#for loop searches each list in Menu and returns a value where the value Spam isn't locatted
for meal in menu:
    if not 'spam' in meal:
        for ingredient in meal:
            #print ingredients individually
            print(ingredient)