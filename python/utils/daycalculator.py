def findDay(d, m, a):
    c_months = [1, 4, 4, 0, 2, 5, 0, 3, 6, 1, 4, 6]
    names= [ "Samedi","Dimanche", "Lundi", "Mardi", "Mercredi", "Jeudi", "Vendredi"]
    n = (d + c_months[m-1]+cYear(a))%7
    return names[n]
def cCentury(c):
    if c%3==0:
        c_century=2
    elif c%3==1:
        c_century=0
    else:
        c_century=6
    return c_century
def cYear(a):
    a_year = a%100
    a_century = a//100
    c_century = cCentury(a_century)
    return (c_century+a_year+a_year//4)%7
        
