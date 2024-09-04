from Calculadora import *
from Lambda import *

class Main:
    x=int(input("Escolha a sua operação:\n1 - adição\n2 - subtração\n3 - multiplicação\n4 - divisão\n"))
    a=int(input("Digite o n1: "))
    b=int(input("Digite o n2: "))
    if(x==1): print(Lambda.adi(a,b))
    if(x==2): print(Lambda.sub(a,b))
    if(x==3): print(Lambda.mul(a,b))
    if(x==4): print(Lambda.div(a,b))

