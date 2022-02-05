import requests

def test_server_is_alive():
     response = requests.get("http://myServ:80/")
     assert response.status_code == 200
