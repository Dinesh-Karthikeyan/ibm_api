import requests


def get_data(api):
        response = requests.get(f"{api}")
        if response.status_code == 200:
            print("sucessfully fetched the data")
            print(response.json())
        else:
            print(f"Hello person, there's a {response.status_code} error with your request")

        return None

# get_data("http://127.0.0.1:8000")

url = "http://127.0.0.1:8000/getPred"

arr = 1,2
myobj = {"id": [1,2,4,5],"camName": "cam1"}

x = requests.post(url, json = myobj)

print(x.json())