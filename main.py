import random
from dao import DAO
from flask_cors import CORS
from aioflask import Flask, request, redirect

app = Flask(__name__)
CORS(app)
db = DAO()
db.create_database()


@app.route('/')
def home():
    return '1'


@app.route("/create_shortened_url", methods=["POST"])
def create_shortened_url():
    original_url = request.json["url"]
    generated_code = code_generator_for_url()
    new_url = 'https://uvvszaca6s.us-west-2.awsapprunner.com/' + generated_code

    response = db.insert_data(original_url, new_url, generated_code)
    if response == 1:
        return new_url
    else:
        return 'Erro ao encurtar url'


def code_generator_for_url():
    ids = 'ABCDEFGHIJKLMNOPQRSTUVXZabcdefghijklmnopqrstuvxz0123456789'
    generated_id = ''.join(random.choice(ids) for _ in range(5))
    return generated_id


@app.route("/<string:code_url>", methods=["GET", "POST"])
def validate_shortened_url(code_url):
    original_url = ''
    data = db.select_data(code_url)
    for row in data:
        original_url = str(row[1])

    return redirect(original_url)


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8080)
