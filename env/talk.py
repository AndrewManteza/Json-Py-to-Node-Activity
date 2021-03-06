import requests

# Sample array
array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Data that we will send in post request.
data = {'array': array}

# The POST request to our node server
res = requests.post('http://192.168.254.110:8080/arraysum', json=data)

# Convert response data to json
returned_data = res.json()

print(returned_data)
result = returned_data['result']
print("Sum of Array from Node.js:", result)
