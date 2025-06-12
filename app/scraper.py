import requests
from bs4 import BeautifulSoup

player_id = "19059417"
player_name = "parthii"

base_url = f"https://cricheroes.com/player-profile/{player_id}/{player_name}"

urls = {
    "player-profile": f"{base_url}/profile",
    "player-stats": f"{base_url}/stats",
    "player-teams": f"{base_url}/teams"
}

headers = {
    "User-Agent": "Mozilla/5.0"
}

for key, url in urls.items():
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        print(f"\n--- {key.upper()} ---")
        soup = BeautifulSoup(response.text, 'html.parser')

        if key == "player-profile":
            name = soup.select_one("h1").text.strip()
            role = soup.select_one(".player-role").text.strip() if soup.select_one(".player-role") else "N/A"
            city = soup.select_one(".player-location").text.strip() if soup.select_one(".player-location") else "N/A"
            print(f"Name: {name}\nRole: {role}\nCity: {city}")

        elif key == "player-stats":
            stats = soup.select("div.stats-card")
            for stat in stats:
                label = stat.select_one(".label").text.strip()
                value = stat.select_one(".value").text.strip()
                print(f"{label}: {value}")

        elif key == "player-teams":
            teams = soup.select(".team-card .team-name")
            print("Teams:")
            for team in teams:
                print("-", team.text.strip())
    else:
        print(f"Failed to fetch {key}. Status code: {response.status_code}")
