def is_year_lip(a):
    if ((a%4==0) and (a%100!=0))or (a%400 == 0):
        a="True"
    else:
        a="False"
    return(a)
a = input("year = ")
a = int(a)
print (is_year_lip(a))