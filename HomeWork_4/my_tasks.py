
k = 0
l =[]
while k != 3:
    print("Usl")
    k = int(input())
    if k == 1:
        s1 = input("Formulirovka zadachi:")
        s2 = input("Kategoria:")
        s3 = input("Time:")
        l.append([s1,s2,s3])
    elif k == 2:
        for i in l: 
            print("Zadacha", i[0], "Category" , i[1], "Time", i[2])
