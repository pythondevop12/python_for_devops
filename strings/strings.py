var = "hello world"
print(var)

# loop on string 
# for i in var:
#     print(i)

# reversed the string 
print(var[::-1])

rev_str = ""
for i in var:
    rev_str = i + rev_str
print(rev_str)

# in built function uses
print(var.upper())
print(var.lower())
print(var.capitalize())
print(var.casefold())

text = "I love Java. Java is fun!"
new_text = text.replace("Java", "Python")
print(new_text)
