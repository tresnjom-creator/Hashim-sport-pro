import requests
from config import SUPPORTED_LEAGUES

def fetch_football_data():
    print("Sistem autonomno pretražuje sportske izvore...")
    
    active_leagues = []
    for league, info in SUPPORTED_LEAGUES.items():
        active_leagues.append({
            "league_name": league,
            "league_id": info["id"],
            "priority": info["priority"]
        })
    
    # Autonomno generisanje i filtriranje aktuelnih mečeva za analizu golova
    # U sljedećoj fazi ovo povezujemo direktno na live API
    live_analysed_matches = [
        {
            "match": "Arsenal vs Chelsea", 
            "league": "Premier League", 
            "avg_goals": 3.2, 
            "recommendation": "Over 2.5 Golova (Visoka vjerovatnoća)"
        },
        {
            "match": "Real Madrid vs Barcelona", 
            "league": "La Liga", 
            "avg_goals": 3.5, 
            "recommendation": "Over 2.5 Golova (Derbi meč)"
        },
        {
            "match": "Inter vs Milan", 
            "league": "Serie A", 
            "avg_goals": 2.7, 
            "recommendation": "Over 2.5 Golova (Tvrđi meč, oprez)"
        }
    ]
    
    return active_leagues, live_analysed_matches

if __name__ == "__main__":
    leagues, matches = fetch_football_data()
    print("Uspješno učitano.")

def fetch_football_data():
    print("Pokrećem automatsko prikupljanje podataka za fudbal...")
    
    active_leagues = []
    for league, info in SUPPORTED_LEAGUES.items():
        active_leagues.append({
            "league_name": league,
            "league_id": info["id"],
            "priority": info["priority"]
        })
    
    analysed_matches = [
        {
            "match": "Primjer: Tim A vs Tim B", 
            "league": "Premier League", 
            "avg_goals": 2.9, 
            "recommendation": "Over 2.5 (Automatski analizirano)"
        }
    ]
    
    return active_leagues, analysed_matches

if __name__ == "__main__":
    leagues, matches = fetch_football_data()
    print("Aktivne lige:", leagues)
    print("Pronađeni mečevi:", matches)
