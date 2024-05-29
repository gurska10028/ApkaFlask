from flask import Flask, jsonify, request
app = Flask(__name__)

@app.route('/')
def index():
    return jsonify({"message": "Witaj w aplikacji!"})

@app.route('/fetch', methods=['POST'])
def fetch_data():
    from scraper import process_data
    url = request.json['url']
    asyncio.run(process_data(url))
    return jsonify({"message": "Dane są przetwarzane"})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
