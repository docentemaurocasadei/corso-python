# gestire i presenti nel campo di una partita di Calcio
# all'inizio partita entrano 11 giocatori (creare una lista di 11 nomi)
# al 35" minuto esce 1 giocatore e ne entra un altro, quindi sostituirlo
# al 50" minuto c'è un infortunio e entrano i 2 massaggiatori
# al 52" minuto escono i 2 massaggiatori
# al 80" minuto viene espulso uno dei giocatori
# gestire le presenze nel campo con una lista e stampare nei diversi minuti
# il numero dei giocatori e le persone nel campo

in_campo = ['carlo', 'giovanni', 'sergio', 'marco', 'patrizio', 'simone', 'stefano', 'luca', 'paolo', 'mirko', 'michele']
print('al 1" minuto in campo ci sono', len(in_campo), 'persone', in_campo)

in_campo[9] = 'andrea'
print('al 35" minuto in campo ci sono', len(in_campo), 'persone', in_campo)

in_campo.extend(['silvia', 'martina'])
print('al 50" minuto in campo ci sono', len(in_campo), 'persone', in_campo)

in_campo.remove('silvia')
in_campo.remove('martina')
print('al 52" minuto in campo ci sono', len(in_campo), 'persone', in_campo)

in_campo.remove('simone')
print('al 80" minuto in campo ci sono', len(in_campo), 'persone', in_campo)

