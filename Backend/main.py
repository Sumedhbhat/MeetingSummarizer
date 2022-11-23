from flask import Flask, jsonify, request
from PIL import Image

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def home():
    if (request.method == 'GET'):
        return jsonify({'home': 'something'})


def process_image():
    if request.method == 'POST':
        file = request.files['image']
        img = Image.open(file.stream)
        return jsonify({'message': 'Success', 'size': img.width})


@app.route('/get-summary', methods=['GET', 'POST'])
def getSummary():
    return jsonify({'msg': 'something'})


def getImage():
    if (request.method == 'POST'):
        sound = request.files['audioFile']


def getItDone():
    return jsonify({'msg': "Something else"})
