import requests
import json
import matplotlib.pyplot as plt

response = requests.get('API_ENDPOINT_URL')

if response.status_code == 200:
    print('Successful request')
else:
    print('Request failed with status code', response.status_code)

data = json.loads(response.text)

# This is just an example, replace with actual data extraction
x_data = [item['x'] for item in data]
y_data = [item['y'] for item in data]

plt.plot(x_data, y_data)
plt.show()
