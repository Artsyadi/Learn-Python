def greet(name):
    print("Hello!")
    print("Good Morning!")
    print(f"Have a nice day {name}")

# greet("Aditya")

def greet1(name, location):
    print(f"Hello {name}, How was your day?")
    print(f"You have been to the location {location}")

# greet1("Aditya", "Pune")

def calculate_love_score(name1,name2):
    lower1 = name1.lower()
    lower2 = name2.lower()
    
    combine = lower1+lower2
    t = combine.count("t")
    r = combine.count("r")
    u = combine.count("u")
    e = combine.count("e")
    digit1 = t+r+u+e
    
    l = combine.count("l")
    o = combine.count("o")
    v = combine.count("v")
    e = combine.count("e")
    digit2 = l+o+v+e
    
    print(int(str(digit1)+str(digit2)))

calculate_love_score("Kanye West", "Kim Kardashian")