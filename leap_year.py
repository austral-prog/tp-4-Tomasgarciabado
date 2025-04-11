def leap_year():
    año = int(input(""))
    bi = ((año%4) == 0 and (año%100) != 0) or (año%400) == 0
    if bi == True:
        print(f"El año {año} es bisiesto")
    else:
        print(f"El año {año} no es bisiesto")
