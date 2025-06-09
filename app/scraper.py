from flask import Flask, request, jsonify
from bs4 import BeautifulSoup
import requests

app = Flask(__name__)

def get_player_data(url):
    try:
        response = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})
        soup = BeautifulSoup(response.text, "html.parser")

        tables = soup.find_all("table")

        def extract_table_data(table):
            rows = table.find_all("tr")
            headers = [th.text.strip() for th in rows[0].find_all("th")]
            total_row = rows[-1]
            values = [td.text.strip() for td in total_row.find_all("td")]
            return dict(zip(headers, values))

        data = {}

        if len(tables) >= 1:
            data["overall_batting"] = extract_table_data(tables[0])
        if len(tables) >= 2:
            data["leather_ball_batting"] = extract_table_data(tables[1])
        if len(tables) >= 3:
            data["tennis_ball_batting"] = extract_table_data(tables[2])

        return data
    except Exception as e:
        return {"error": str(e)}


@app.route("/player_stats")
def player_stats():
    url = request.args.get("url")
    if not url:
        return jsonify({"error": "No URL provided"}), 400

    try:
        response = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})
        soup = BeautifulSoup(response.text, "html.parser")

        tables = soup.find_all("table")

        def extract_table_data(table):
            rows = table.find_all("tr")
            headers = [th.text.strip() for th in rows[0].find_all("th")]
            total_row = rows[-1]
            values = [td.text.strip() for td in total_row.find_all("td")]
            return dict(zip(headers, values))

        result = {}

        # First table: Overall Batting
        if len(tables) >= 1:
            result["overall_batting"] = extract_table_data(tables[0])

        # Second table: Leather Ball Batting
        if len(tables) >= 2:
            result["leather_ball_batting"] = extract_table_data(tables[1])

        # Third table: Tennis Ball Batting
        if len(tables) >= 3:
            result["tennis_ball_batting"] = extract_table_data(tables[2])

        return jsonify(result)

    except Exception as e:
        return jsonify({"error": str(e)}), 500
