#creare un dizionario e estrarre il voto di matematica
d = {"classe": {
        "studente":{
            "nome": "Marco",
            "voti": {
                "italiano": 7.5,
                "matematica": 8
            }
        }
    }
}
print(d["classe"]["studente"]["voti"]["matematica"]);