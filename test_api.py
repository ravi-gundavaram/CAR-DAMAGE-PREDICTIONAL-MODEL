import requests

def test_predict():
    url = "http://localhost:5000/predict"
    with open("test_images/sample_damaged.jpg", "rb") as img:
        response = requests.post(url, files={"image": img})
    assert response.status_code == 200
    assert response.json()['classification'] in ['damaged', 'not_damaged']
