#Introduction to procedural programming
def greeting(msg = "Hello", name = "user"):
    name  = name.replace("e","3")
    msg = msg.replace("e","3")
    print(msg, name)


greeting("José","Python Learning")

greeting(name = "Julio Cesar",msg="Python Learning")