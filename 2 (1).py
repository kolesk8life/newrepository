print("Hello")
x = "Bro" #String valuable
y = 21 # int valuable
z = False
# String + String (OK). String = str
print("Fuck you " + x) #Example
print(type(x)); #write down type() to get type of variable
#types of variables str(name or smth else), int(number), bool(True, False), float (int + 0.0001)
age = 21
age += 1 # Computer deduces(выводит) the lastest value of variable
print(age)
# String + ing = Error/ Float == int
# To make int variable become string use str()
print("Your age is " + str(age));

a, b, c = 50, "shit","bag";
print(c + " of " + b + " number " + str(a))

SpongeBob = SquidWard = Patric = Sandy = 30;
print(Sandy)

d = "favourite Slavic's number is " + str(len(b))
print(d);
# len helps us to measure valuable's amount of numbers

print(d.find("S")); # To find letter in sentece or word use nameofvariable + .find()

print(d.upper())# To make entire sentece up (add nameofvariable.upper() )

print(d.lower())# To make entire sentece down (add nameofvariable.lower() )

print(d.lower().count("s")) # to count hw many same letters there are in the word (add nameofvariable.count() )

print(d.lower().replace("s", "b")) # to replace letters

print((d + " ") * 3) # to write smth 3 times

# 26.24 https://www.youtube.com/watch?v=XKHEtdqhLK8&ab_channel=BroCode

x = 1 # int
y = 2.0 # float
z = "3" # string
print(int(z))
print(int(y))
print(int(z)*3)