# 1func:
#   citim de la tastatura si returnam int
# 2func:
#   2 nr, le comparam
#   daca n1 >= n2 => true daca nu false
#   return,
# 3func:
#   daca e true atunci cerem de la tastatura altul
# 4func
#   daca e false
#   sa il printui pe primul nr impar mai mic decat el

def cit_tast():
    numarul = input('alege numarul : ')  # LaMi - nu se returneaza int de numarul citit de la tastatura
    return int(numarul)

def compar():  # numerele cu care se face compare are trebui trimise ca si parametrii la functia de compare si nu folosite variabile globale
    if n1 >= n2:
        return True
    else:
        return False

def if_false():
    l = []
    for num in range(2, int(n1)):
        for i in range(2, num):
            if (num % i) == 0:
                break
            else:
                l.append(num)
    return l[-1]

def if_true():
    if r:
        numarul_nou = input('alege numarul nou: ')  # functia nu inlocuieste primul numar din cele citite initial ci citeste un numar nou si nu face nimic cu el, doar il printeaza la final
        return numarul_nou

n1 = cit_tast()
n2 = cit_tast()
r = compar()
# urmatoarele 2 linii se executa oricum ... nu tin cont de output-ul de la compare

z = if_false()
nou = if_true()

print('asta e primul numar prim mai mic decat n1', z)

print('ai ales un alt numar nou: ', nou)
