from flask import Flask
import json
import requests
# Setup flask server
app = Flask(__name__)

# Setup url route which will calculate
# total sum of array.


@app.route('/arraysum')
def sum_of_array():
    array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


# Data that we will send in post request.
    data = {'array': array}

# The POST request to our node server
    res = requests.post('http://192.168.254.111:3000/arraysum', json=data)

# Convert response data to json
    returned_data = res.json()

    print(returned_data)
    result = returned_data['result']
    return f'This is the sum of arrays {result}'


if __name__ == "__main__":
    app.run(port=8080)
