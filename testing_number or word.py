name = input("Enter your name : ")
num1 = (name.lower().strip().replace(" ",""))
print("HI << {} >> the total number of your name is : {}".format(name.title() , len(num1)))
name2 =input("Enter Your name again toh find it Reverse,Capital or small : ")
print("Reverse is :"+name2[::-1].title())
print("Capital is :"+name2.upper())
print("Small is   :"+name2.lower())

#start with number\
num1 , num2 =(input("Enter two Big number For it (+ , - or / and avarage )and [separate them with comma] :").split(","))

print("As (+) ="+str(int(num1)+int(num2)))
print("As (*) ="+str(int(num1)*int(num2)))
print("As (/) ="+str(int(num1)/int(num2)))
print("As (avg) ="+str(int(num1)+int(num2)/2))

#count
counts =input("Enter Your Full name to conunt a word form your Name :")
word =input ("Enter a letter form YOur name to count it :")
print(f"Result is : {counts.lower().strip().count(word.lower().strip())}")


