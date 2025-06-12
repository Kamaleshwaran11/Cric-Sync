from flask import Blueprint, render_template
from flask import render_template, request
from app.scraper import player_id,player_name
from bs4 import BeautifulSoup
import requests

bp = Blueprint('main', __name__)

@bp.route('/')
def home():
    return render_template('index.html')

player_list = [
    {
        "name": "Parthi",
        "role": "Captain - All rounder",
        "image": "static/images/parthi.jpg",
        "flag": "static/images/cc-flag.png",
        "jersey": 21,
        "player-profile": "https://cricheroes.com/player-profile/19059417/parthii/profile",
        "Player-stats" : "https://cricheroes.com/player-profile/19059417/parthii/stats",
        "player-teams": "https://cricheroes.com/player-profile/19059417/parthii/teams"
    },
    {
        "name": "Madhan",
        "role": "All rounder",
        "image": "static/images/madhan.jpg",
        "flag": "static/images/cc-flag.png",
        "jersey": 16,
        "profile_url": "madhan.html"
    },
    {
        "name": "Kamalesh",
        "role": "All rounder",
        "image": "static/images/kamalesh.jpg",
        "flag": "static/images/cc-flag.png",
        "jersey": 3,
        "profile_url": "kamalesh.html"
    },
    {
        "name": "Madhava",
        "role": "All rounder",
        "image": "static/images/madhava.jpg",
        "flag": "static/images/cc-flag.png",
        "jersey": 1,
        "profile_url": "player-history/madhava.html"
    },
    {
        "name": "Lokesh",
        "role": "All rounder",
        "image": "static/images/lokesh.jpg",
        "flag": "static/images/cc-flag.png",
        "jersey": 19,
        "profile_url": "player-history/lokesh.html"
    },
    {
        "name": "Thiru",
        "role": "All rounder",
        "image": "static/images/thiru.jpg",
        "flag": "static/images/cc-flag.png",
        "jersey": 333,
        "profile_url": "player-history/thiru.html"
    },
    {
        "name": "Aravind",
        "role": "All rounder",
        "image": "static/images/aravind.jpg",
        "flag": "static/images/cc-flag.png",
        "jersey": 46,
        "profile_url": "player-history/aravind.html"
    },
    {
        "name": "Dinesh",
        "role": "All rounder",
        "image": "static/images/dinesh.jpg",
        "flag": "static/images/cc-flag.png",
        "jersey": 14,
        "profile_url": "player-history/dinesh.html"
    },
    {
        "name": "Vetri",
        "role": "All rounder",
        "image": "static/images/vetri.jpg",
        "flag": "static/images/cc-flag.png",
        "jersey": 333,
        "profile_url": "player-history/vetri.html"
    },
    {
        "name": "Tharun",
        "role": "All rounder",
        "image": "static/images/tharun.jpg",
        "flag": "static/images/cc-flag.png",
        "jersey": 17,
        "profile_url": "player-history/tharun.html"
    },
    {
        "name": "Santha",
        "role": "All rounder",
        "image": "static/images/santha.jpg",
        "flag": "static/images/cc-flag.png",
        "jersey": 5,
        "profile_url": "player-history/santha.html"
    }
]

@bp.route('/squad')
def players():
    return render_template('player.html', players=player_list)


@bp.route('/squad/player/<name>')
def player_profile(name):
    for player in player_list:
        if player['name'].lower() == name.lower():
            return render_template('profile.html', player=player)
    return "Player not found", 404

@bp.route('/player/<player_id>/<player_name>')
def show_player(player_id, player_name):
    base_url = f"https://cricheroes.com/player-profile/{player_id}/{player_name}"

    urls = {
        "profile": f"{base_url}/profile",
        "stats": f"{base_url}/stats",
        "teams": f"{base_url}/teams"
    }

    headers = {"User-Agent": "Mozilla/5.0"}
    player_data = {}

    # --- Profile Info ---
    response = requests.get(urls["profile"], headers=headers)
    if response.ok:
        soup = BeautifulSoup(response.text, "html.parser")
        player_data["name"] = soup.select_one("h1").text.strip()
        player_data["role"] = soup.select_one(".player-role").text.strip() if soup.select_one(".player-role") else "N/A"
        player_data["city"] = soup.select_one(".player-location").text.strip() if soup.select_one(".player-location") else "N/A"

    # --- Teams ---
    response = requests.get(urls["teams"], headers=headers)
    if response.ok:
        soup = BeautifulSoup(response.text, "html.parser")
        teams = soup.select(".team-card .team-name")
        player_data["teams"] = [team.text.strip() for team in teams]

    # --- Stats ---
    response = requests.get(urls["stats"], headers=headers)
    player_data["stats"] = {}
    if response.ok:
        soup = BeautifulSoup(response.text, "html.parser")
        stat_cards = soup.select(".card-body .d-flex.flex-column.align-items-center")

        for card in stat_cards:
            label = card.select_one(".text-muted")
            value = card.select_one("h5")
            if label and value:
                player_data["stats"][label.text.strip()] = value.text.strip()

    return render_template("player.html", player=player_data)

@bp.route('/about')
def about():
    return render_template('about.html') 

@bp.route('/contact')
def contact():
    return render_template('contact.html')

@bp.route('/gallery')
def gallery():
    return render_template('gallery.html')

@bp.route('/privacy-policy')
def privacy_policy():
    return render_template('privacy-policy.html')

@bp.route('/disclaimer')
def disclaimer():
    return render_template('disclaimer.html')

@bp.route('/terms')
def terms_of_service():
    return render_template('terms.html')

