import requests

url = 'http://localhost:65322/raw/dictionary'
obj = {'imagePath': 'D:\\Users\\chiawei\\konduit\\Github\\Keras_mnist_python\\mnist-test.png'}

response = requests.post(url, json=obj)

if response.status_code == 200:

    content = response.json()
    output = content['output']
    output_class = content['output_class']

    print(output)
    print(output_class)

else:
    print(response)
