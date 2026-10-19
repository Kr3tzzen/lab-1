from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/api/data')
@app.route('/data')
def get_data():
    return jsonify({
        "message": "Привет от бэкенда второй лабораторной!",
        "status": "success"
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
