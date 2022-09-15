#   Scrivi una funzione che fornisca in output il nome del Sistema Operativo utilizzato con eventuali relative informazioni sulla release corrente.
#   utilizza libreria platform
import platform

def mySystem():
    print(platform.system())
    print(platform.release())
    print(platform.version())


mySystem()