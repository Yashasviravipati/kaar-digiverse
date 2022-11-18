from flask import Flask, jsonify, request

app = Flask(__name__)
stores = [
    {
        'name': 'Movies',
        'list': [
            {
                'name': 'KGF',
                'price': 100
            }
        ]
    },
    {
        'name': 'Fruits',
        'list': [
            {
                'name': 'apple',
                'price': 100
            }
        ]
    }
]


@app.route('/')
def home():
    return "Hello world"

@app.route('/store', methods=['POST'])
def create_store():
    request_data = request.get_json()
    new_store = {
        'name': request_data['name'],
        'list': []
    }
    stores.append(new_store)
    return jsonify(new_store)


@app.route('/store/<string:name>')
def get_store_name(name):
    for store in stores:
        if(store['name'] == name):
            return jsonify(store)
    return jsonify({'message': 'store not found'})


@app.route('/store')
def get_all_store_name():
    return jsonify({'stores': stores})


@app.route('/store/<string:name>/item', methods=['POST'])
def create_store_item(name):
    request_data = request.get_json()
    for store in stores:
        if(store['name'] == name):
            new_item = {
                'name': request_data['name'],
                'price': request_data['price']
            }
            stores['list'].append(new_item)
            return jsonify(new_item)
    return jsonify({'message':'store not found'})


@app.route('/store/<string:name>/item')
def get_store_item(name):
    for store in stores:
        if(store['name'] == name):
            return jsonify(store['items'])
    return jsonify({'message': 'store not found'})



if __name__ == '__main__':
    app.run(debug=True)