from flask import Flask, jsonify

app = Flask(__name__)

data = [
        {
            "id": 4,
            "frameworks": "Django",
            "year": 2005
        },
        {
            "id": 7,
            "frameworks": "Flask",
            "year": 2010
        },
        {
            "id": 8,
            "frameworks": "Web2Py",
            "year": 2007
        }
    ]


@app.route('/')
def home():
    return "Hello World"


@app.route('/api', methods=['GET'])
def get_api():
    return jsonify(data)  # Return web frameworks informationn


if __name__ == '__main__':
    app.run(debug=True)
