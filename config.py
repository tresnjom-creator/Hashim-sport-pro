# Konfiguracija za autonomno praćenje fudbalskih liga
SUPPORTED_LEAGUES = {
    "Champions League": {"id": "CL", "priority": 1},
    "Premier League": {"id": "EPL", "priority": 1},
    "La Liga": {"id": "LL", "priority": 2},
    "Serie A": {"id": "SA", "priority": 2},
    "Bundesliga": {"id": "BL", "priority": 2}
}

DATA_SOURCES = {
    "auto_scrape": True,
    "target_markets": ["over_2.5_goals", "h2h_stats", "team_form"]
}
