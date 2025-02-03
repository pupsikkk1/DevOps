import requests

def test_hello_api():
    url = "http://127.0.0.1:5000/hello"
    response = requests.get(url)
    
    assert response.status_code == 200
    assert response.json() == {"message": "Hello, world!"}
    
    print("Test passed!")

if __name__ == "__main__":
    test_hello_api()
