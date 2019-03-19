
k = 0
l ={}
key = 0
while k != 3:
    print("Usl")
    k = int(input())
    if k == 1:
        s1 = input("Formulirovka zadachi:")
        s2 = input("Kategoria:")
        s3 = input("Time:")   
        l.update({key : [s1,s2,s3]})
        key += 1
    elif k == 2:
        for i in range(len(l)): 
            print("Zadacha", l[i][0], "Category" , l[i][1], "Time", l[i][2])
