#creare una delle variabili di tipo list, tuple, set, dict e analizzare
#se modificabile
#se accetta duplicati
#
#stampare:
#il tipo  <class 'list'>  è modificabile
#il tipo  <class 'list'>  accetta duplicati
#***********************
#il tipo  <class 'tuple'>  non è modificabile
#il tipo  <class 'tuple'>  non accetta duplicati
#***********************
#il tipo  <class 'set'>  non è modificabile
#il tipo  <class 'set'>  non accetta duplicati
#***********************
#il tipo  <class 'dict'>  è modificabile
#il tipo  <class 'dict'>  non accetta duplicati
#***********************


def analisi(p):
    try:
        p[0] = 1
        print(f"il tipo ", type(p), " è modificabile")
    except Exception as ex:
        print(f"il tipo ", type(p), " non è modificabile")

    try:
        p.append(p[0])
        print(f"il tipo ", type(p), " accetta duplicati")
    except Exception as ex:
        print(f"il tipo ", type(p), " non accetta duplicati")
    finally:
        print("***********************")

analisi([1,2,3])
analisi((1,2,3))
analisi({1,2,3})
analisi({"a" : 1,"b" : 2, "c": 3})