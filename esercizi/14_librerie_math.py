#creare 2 funzioni 1 che calcola la radice quadrata e 1 che calcola il fattoriale di un numero
#aggiungere un try in modo da gestire eventuali errori
import math

def sqrt2(num):
    try:
        return math.sqrt(num)
    except Exception as e:
        print(e)
        print(f"errore {e}")
def factorial2(num):
    try:
        return math.factorial(num)
    except Exception as e:
        print(f"errore {e}")
print(sqrt2(-9))
print(factorial2(5))