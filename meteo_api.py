# meteo_api.py — STUDENTE 1 — branch: feature/api
# Funzioni: cerca_coordinate(nome_citta)
#           scarica_dati_storici(latitudine, longitudine, data_inizio, data_fine)
import requests

URL_GEOCODING = "https://geocoding-api.open-meteo.com/v1/search"
URL_ARCHIVIO = "https://archive-api.open-meteo.com/v1/archive"

def scarica_previsioni_multi_citta(lista_nomi_citta, data_inizio, data_fine):
    """
    Per ogni citta' nella lista, cerca le coordinate e scarica le
    previsioni. Ritorna un dizionario {nome_citta: dati_previsioni}.
    Se una citta' non viene trovata, la salta e continua con le altre.
    """
    dati_per_citta = {}

    for nome_citta in lista_nomi_citta:
        coordinate = cerca_coordinate(nome_citta)

        if coordinate is None:
            print(f"Città non trovata, salto: {nome_citta}")
            continue

        latitudine=coordinate[0]
        longitudine=coordinate[1]
        dati = scarica_dati_storici(latitudine, longitudine, data_inizio, data_fine)
        dati_per_citta[nome_citta] = dati

    return dati_per_citta

def cerca_coordinate(nome_citta):
    """
    Chiede all'API di geocoding le coordinate di una citta'.
    Ritorna una coppia (latitudine, longitudine), oppure None
    se la citta' non viene trovata.
    """
    parametri = {
        "name" : nome_citta, 
        "count" : 1,
        "language" : "it",
        "format" : "json"
    }
    risposta = requests.get(URL_GEOCODING, params=parametri, timeout=10)
    dati = risposta.json()

    if "results" in dati:
        primo_risultato = dati["results"][0]
        latitudine = primo_risultato["latitude"]
        longitudine = primo_risultato["longitude"]
        return latitudine, longitudine
    else:
        print("Citta' non trovata")
        return None

def scarica_dati_storici(latitudine, longitudine, data_inizio, data_fine):
    """
    Chiama l'API Open-Meteo Archive e ritorna il dizionario JSON
    con le temperature storiche nell'intervallo richiesto.
    Ritorna None se c'e' un errore.
    """
    parametri = {
        "latitude" : latitudine, 
        "longitude" : longitudine,
        "start_date" : data_inizio,
        "end_date" : data_fine,
        "daily" : "temperature_2m_max,temperature_2m_min",
        "timezone" : "Europe/Rome"
    }

    try:
        risposta = requests.get(URL_ARCHIVIO, params=parametri, timeout=10)
        if risposta.status_code == 200:
            return risposta.json()
        else:
            print("Errore: non so che errore sia")
            return None

    except requests.exceptions.Timeout:
        print("Errore: sia non che so errore")
        return None

    except requests.exceptions.ConnectionError:
        print("Errore: errore che sia non so")
        return None

    except Exception as e:
        print("Errore: Generale, qualcosa è andato storto, controlla meglio dentro il pc, togli la polvere, lava il processore con lo sgrassatore alla candegina, usa la carta vetrata per togliere la sporcizia incrostata, e riprova, scusa per il disagio e grazie per averci contattato :D")
        return None

if __name__ == "__main__":
    DATA_INIZIO = "2026-08-31"
    DATA_FINE = "2026-09-06"
    lista_nomi_citta=["palermo", "catania", "palermo", "bergamo"]
    previsioni=scarica_previsioni_multi_citta(lista_nomi_citta, DATA_INIZIO, DATA_FINE)
    print(previsioni)