CurrentYear = int(input("What is year now? - "))
Age = int(round(float(input("How old are you ? - "))))
FutureYear = int(input("Chose your period - "))
a = FutureYear - CurrentYear
print("You will be " + str(a + Age) + " in " + str(FutureYear) )

