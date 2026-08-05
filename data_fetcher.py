import requests
from config import SUPPORTED_LEAGUES, DATA_SOURCES

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
