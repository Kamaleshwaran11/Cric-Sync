from flask import Blueprint, render_template
from flask import render_template, request
from app.scraper import player_stats

bp = Blueprint('main', __name__)

@bp.route('/')
def home():
    return render_template('index.html')

@bp.route('/players')
def players():
    players = [
        {
            "name": "Parthi",
            "role": "Captain - All rounder",
            "image": "static/images/parthi.jpg",
            "flag": "static/images/cc-flag.png",
            "jersey": 21,
            "profile_url": "templates/parthi.html"
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
            "jersey": 16,
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
            "jersey": 333,
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
    return render_template('player.html', players=players)


@bp.route("/liveplayer", methods=["GET"])
def live_player():
    player_url = request.args.get("url")
    if not player_url:
        return "No URL provided", 400

    data = player_stats(player_url)
    return render_template("live_player.html", player=data)

@bp.route('/squad')
def squad():
    return render_template('squad.html')

@bp.route('/about')
def about():
    return render_template('about.html') 

@bp.route('/contact')
def contact():
    return render_template('contact.html')

@bp.route('/gallery')
def gallery():
    images = [
        {"url": "static/images/image1.jpg", "caption": "Image 1"},
        {"url": "static/images/image2.jpg", "caption": "Image 2"},
    ]
    return render_template('gallery.html', images=images)

