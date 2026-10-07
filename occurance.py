names = ["Aarav","Anoop","abhi","Arjun"]

count = sum(name.lower().count('a') for name in names)

print('occurence of a :', count)
