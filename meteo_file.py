import json

def salva_json(previsioni, percorso):
    with open(percorso, "w", encoding="utf-8") as f:
        json.dump(previsioni, f, indent=2, ensure_ascii=False)
    print(f"File JSON salvato in: {percorso}")
    print(f"Record salvati: {len(previsioni)}")


def scrivi_report(previsioni, statistiche, citta, percorso):
        with open(percorso, "w", encoding="utf-8") as f:
            f.write(f"PREVISIONI STORICHE — {citta}\n")
            f.write("=" * 40 + "\n")
            f.write("GIORNO      | MAX (°C) | MIN (°C)\n")
            f.write("-" * 40 + "\n")

        for previsione in previsioni:
            f.write(
                f"{previsione['data']:<12}| "
                f"{previsione['temp_max']:>8.1f} | "
                f"{previsione['temp_min']:>8.1f}\n"
            )
        f.write("\nSTATISTICHE\n")
        f.write("-" * 40 + "\n")
        f.write(f"Temperatura massima media: {statistiche['media_max']:.1f} °C\n")
        caldo = statistiche["giorno_piu_caldo"]
        freddo = statistiche["giorno_piu_freddo"]
        f.write(
            f"Giorno piu' caldo: {caldo['data']} "
            f"({caldo['temp_max']:.1f} °C)\n"
        )
        f.write(
            f"Giorno piu' freddo: {freddo['data']} "
            f"({freddo['temp_min']:.1f} °C)\n"
        )
        print(f"Report scritto: {percorso}")