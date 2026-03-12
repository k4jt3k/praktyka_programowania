def Add(numbers):
    if not numbers:
        return 0
    
    if(",,") in numbers:
        return ValueError

    liczby = numbers.replace("\n",",")
    liczby = liczby.split(",")

    suma=0
    for i in liczby:
        suma+=int(i)
    return suma