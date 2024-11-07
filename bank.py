Greet = input("Input a Greeting for $$$:")

if Greet.lower().strip().startswith("hello"):
    print("$0")
elif Greet.lower().strip().startswith("h"):
    print("$20")
else:
    print("$100")
