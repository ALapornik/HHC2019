import requests
def getToken():
    url = 'https://studentportal.elfu.org/validator.php'
    response = requests.get(url)
    token = response.text
    return token


