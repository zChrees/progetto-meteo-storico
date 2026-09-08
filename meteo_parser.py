def analizza_dati_storici(dati):
    """
    Trasforma il JSON grezzo in una lista di dizionari
    """
    giornaliero = dati["daily"]
    date = giornaliero["time"]
    temp_max = giornaliero["temperature_2m_max"]
    temp_min = giornaliero["temperature_2m_min"]

    previsioni = []

    for i in range(len(date)):
        previsione = {
            "data" : date[i],
            "temp_max" : temp_max[i],
            "temp_min"  : temp_min[i]
        }
        previsioni.append(previsione)

        return previsioni


def calcola_statistiche(previsioni):
    """
    Calcola media delle temperature massime, giorno piu' caldo
    e giorno piu' freddo (basandosi su temp_max).
    Ritorna un dizionario con le statistiche. test
    """
    totale = 0
    giorno_piu_caldo = previsioni[0]
    giorno_piu_freddo = previsioni[0]
    for giorno in previsioni:
        #calcoliamo il totale per poi trovare la media
        totale = totale + giorno['temp_max']

        # troviamo il giorno piu caldo
        if giorno['temp_max'] > giorno_piu_caldo['temp_max']:
            giorno_piu_caldo=giorno

        # troviamo il giorno piu freddo
        if giorno['temp_max'] < giorno_piu_freddo['temp_max']:
            giorno_piu_freddo=giorno

    media = totale/len(previsioni)
    statistiche = {
        "media_max":media,
        "giorno_piu_caldo":giorno_piu_caldo,
        "giorno_piu_freddo":giorno_piu_freddo
    }
    return statistiche