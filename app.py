
from flask import Flask, request

app = Flask(__name__)

data = {
    1: {'name': 'John', 'age': '20'},
    2: {'name': 'Mary', 'age': '30'},
    3: {'name': 'Bob', 'age': '40'}
}



@app.route('/', methods=['GET', 'POST'])
def home():
    return {'message': 'Hello World'}

# get route to get all data


@app.route('/all-data', methods=['GET'])
def get_all_data():
    return data

# get route to get a specific data by id


@app.route('/data/<int:id>', methods=['GET'])
def get_data(id):
    return data[id]

# post route to add new data


@app.route('/add-data', methods=['POST'])
def add_data():
    new_data = request.get_json()
    data[len(data)+1] = new_data
    return data


# put request to update data by id
@app.route('/update-data/<int:id>', methods=['PUT'])
def update_data(id):
    if id in data.keys():
        new_data = request.get_json()
        data[id] = new_data
        return data
    else:
        return {'message': 'You can not update data that does not exist'}

# delete request to delete data by id


@app.route('/delete-data/<int:id>', methods=['DELETE'])
def delete_data(id):
    if id in data.keys():
        del data[id]
        return data
    else:
        return {'message': 'You can not delete data that does not exist'}


if __name__ == '__main__':
    app.run(debug=True)