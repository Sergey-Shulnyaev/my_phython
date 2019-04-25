from math import pi


def solve(radius):  
    try:
        out = 4 / 3 * pi * float(radius) ** 3
        return str(out)
    except NameError:
        return "Радиус не задан"
    except TypeError:
        return "Не тот тип данных у радиуса"
    except Exception:
        return "Какая-то ошибка" 
        
        
def save_file(radius):
    value = solve(radius)
    with open("output.txt",'a') as outfile:
        outfile.write(str(radius) + ' - ' +value+"\n")

def save_html(radius):
    value = solve(radius)
    try:
        with open("output.html",'r') as infile:
            solves = infile.readlines()
            solves = solves[1:-1]
            solves.append(str(radius) + ' - ' + value + '<br />\n')
    except:
        solves = [str(radius) + ' - ' + value + '<br />\n']
        
    with open("output.html",'w') as htmlfile:
        htmlfile.write('<html><head></head><body><h1>Volume</h1>\n')
        for i in solves:
            htmlfile.write(i)
        htmlfile.write('</body>'+'</html>')
        
def save(radius,par):
    print(radius)
    if par == 'Текст':
        save_file(radius)
    else:
        save_html(radius)
