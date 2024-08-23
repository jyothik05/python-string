#COUNT()  
#The count() method returns the number of times a specified value appears in the string.


txt = "I love apples, apple are my favorite fruit"

x = txt.count("apple")

print(x)


#CAPTILIZE()

#The capitalize() method returns a string where the first character is upper case, and the rest is lower case.
# Syntax
# string.capitalize()


txt = "hello, and welcome to my world."

x = txt.capitalize()

print (x)


txt = "36 is my age."

x = txt.capitalize()

print (x)


#CASEFOLD()
#The casefold() method returns a string where all the characters are lower case
# Syntax
# string.casefold()


txt = "Hello, And Welcome To My World!"

x = txt.casefold()

print(x)


#CENTER()
#The center() method will center align the string, using a specified character (space is default) as the fill character.
# Syntax
# string.center(length, character)


string = "pythonlearning"
print(len(string))
print(string.center(22))


#ENDS WITH()
# The endswith() method returns True if the string ends with the specified value, otherwise False.

# Syntax
# string.endswith(value)


txt = "Hello, welcome to my world."

x = txt.endswith("my world.")

print(x)



#EXPANDTABS()
#The expandtabs() method sets the tab size to the specified number of whitespaces.
# Syntax
# string.expandtabs(tabsize)


txt = "H\te\tl\tl\to"

x =  txt.expandtabs(2)

print(x)



txt = "H\te\tl\tl\to"

print(txt)
print(txt.expandtabs())
print(txt.expandtabs(2))
print(txt.expandtabs(4))
print(txt.expandtabs(10))



#FIND() AND INDEX()
#The find() method finds the first occurrence of the specified value.   (indexing value)

# The find() method returns -1 if the value is not found.

# The find() method is almost the same as the index() method, the only difference is that the index() method raises an exception if the value is not found. (See example below)

# Syntax
# string.find(value, start, end)


txt = "Hello, welcome to my world."

x = txt.find("m")

print(x)




#ISALNUM()
# The isalnum() method returns True if all the characters are alphanumeric, meaning alphabet letter (a-z) and numbers (0-9).

# Example of characters that are not alphanumeric: (space)!#%&? etc.
# Syntax
# string.isalnum()

tx= "Company12"

x = tx.isalnum()

print(x)


tt = "Company 12"

x = tt.isalnum()

print(x)


#ISALPHA()
# The isalpha() method returns True if all the characters are alphabet letters (a-z).

# Example of characters that are not alphabet letters: (space)!#%&? etc.

# Syntax
# string.isalpha()

t = "Company10"

x = t.isalpha()

print(x)


tx2t = "Company"

x = tx2t.isalpha()

print(x)


#ISASCII()
# The isascii() method returns True if all the characters are ascii characters  (a-z) and 0-9.
# Syntax
# string.isascii()


txt3 = "visualcode056"

x = txt3.isascii()

print(x)



#ISDECIMAL()
# The isdecimal() method returns True if all the characters are decimals (0-9).
# Syntax 
# string.isdecimal()


num = "123ms"
print(num.isdecimal())


#ISDIGIT
# The isdigit() method returns True if all the characters are digits, otherwise False.

# Syntax 
# string.isdigit()
 

date = "2402"
print(date.isdigit())



#ISIDENTIFIER
# The isidentifier() method returns True if the string is a valid identifier, otherwise False.

# A string is considered a valid identifier if it only contains alphanumeric letters (a-z) and (0-9), or underscores (_). A valid identifier cannot start with a number, or contain any spaces.

# syntax 
# string.isidentifier()

a = "MyFolder"
b = "Demo002"
c = "2bring"
d = "my demo"

print(a.isidentifier())
print(b.isidentifier())
print(c.isidentifier())
print(d.isidentifier())


#ISLOWER
# The islower() method returns True if all the characters are in lower case, otherwise False.

# Numbers, symbols and spaces are not checked, only alphabet characters.
# Syntax
# string.islower()

a = "Hello world!"
b = "hello 123"
c = "mynameisPeter"

print(a.islower())
print(b.islower())
print(c.islower())


#JOIN
# The join() method takes all items in an iterable and joins them into one string.

# A string must be specified as the separator.

# Syntax
# string.join(iterable)

myTuple = ("John", "Peter", "Vicky")

x = "#".join(myTuple)

print(x)


# When using a dictionary as an iterable, the returned values are the keys, not the values.

myDict = {"name": "John", "country": "Norway"}
mySeparator = "TEST"

x = mySeparator.join(myDict)

print(x)


#SPLIT
# The split() method splits a string into a list.

# You can specify the separator, default separator is any whitespace.

# Syntax
# string.split(separator, maxsplit)

txt = "welcome to the jungle"

x = txt.split()

print(x)


txt = "apple#banana#cherry#orange"

x = txt.split("#")

print(x)


#Note: When maxsplit is specified, the list will contain the specified number of elements plus one.

txt = "apple#banana#cherry#orange"
x = txt.split("#", 1)

print(x)


#LJUST
#The ljust() method will left align the string, using a specified character (space is default) as the fill character.
# Syntax
# string.ljust(length, character)

txt = "banana"

x = txt.ljust(20)

print(x, "is my favorite fruit.")


txt = "banana"

x = txt.ljust(20, "O")

print(x)


#LOWER
# The lower() method returns a string where all characters are lower case.
# Symbols and Numbers are ignored.

# Syntax
# string.lower()


txt = "Hello my FRIENDS"

x = txt.lower()

print(x)


# The lstrip() method removes any leading characters (space is the default leading character to remove)

# Syntax
# string.lstrip(characters)

name = "python is a programming language"
str = name.lstrip("python")
print(str)


#MAKETRANS  and  TRANSLATE
#The maketrans() method returns a mapping table that can be used with the translate() method to replace specified characters.
# Syntax
# str.maketrans(x, y, z)
# x = given string
# y = replacing value having same length of given string
# z = removing characters from original string


txt = "Hello Sam!"
mytable = str.maketrans("S", "P")
print(txt.translate(mytable))

txt = "Good night Sam!"
x = "mSa"
y = "eJo"
z = "odnght"
mytable = str.maketrans(x, y, z)
print(txt.translate(mytable))


#PARTITION
#The partition() method searches for a specified string, and splits the string into a tuple
# Syntax
# string.partition(value)

txt = "I could eat bananas all day"

x = txt.partition("bananas")

print(x)

#If the specified value is not found, the partition() method returns a tuple containing: 1 - the whole string, 2 - an empty string, 3 - an empty string:

txt = "I could eat bananas all day"

x = txt.partition("apples")

print(x)



#REMOVEPREFIX
#removeprefix() function removes the prefix and returns the rest of the string. If the prefix string is not found, then it returns the original string.
# syntax
# str.removeprefix()


txt = "visualcode"
str = txt.removeprefix("v")
print(str)
print(txt.removeprefix("k"))


#REMOVESUFFIX
#removesuffix() functions removes the suffix and returns the rest of the string If the suffix is not found, then it returns the original string.
# syntax
# str.removesuffix()


txt = "practicing"
print(txt.removesuffix("ing"))


#REPLACE
# #The replace() method replaces a specified phrase with another specified phrase.
# Syntax
# string.replace(oldvalue, newvalue, count)

txt = "one one was a race horse, two two was one too."

x = txt.replace("one", "three")

print(x)


txt = "one one was a race horse, two two was one too."

x = txt.replace("one", "three", 2)

print(x)


