prices = {'Friday' : {12 : 250 ,16 : 350, 20 : 450},'Champions' : {10 : 250, 13: 350, 16 : 350}, 'Pernataya Banda' : {10 : 350, 14 : 450, 18 : 450}}
film = input('Choose your film:\nFriday\nChampions\nPernataya Banda\n')
while prices.get(film, False) == False:
    film = input('Choose film:\nFriday\nChampions\nPernataya Banda\n')
date = input('tomorrow or today:\n')
for i in list(prices[film].keys()):
    print(i, "-",  prices[film][i])
time = int(input('Choose time:\n'))
while prices[film].get(time, False) == False:
    time = int(input('Choose time:\n'))
number = int(input('Numbers of tickets:\n'))
k = 1.0
if date == 'tomorrow':
    k -= 0.05
if number >= 20:
    k -= 0.2
print(prices[film][time] * k * number)


