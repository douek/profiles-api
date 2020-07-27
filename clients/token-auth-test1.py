import requests


def client():
    token_h = 'Token f7fa8b73a9082d35ddad9a528c9a7538a090e60d'
    # credentials = {'username':'test', 'password':'changeme123'}
    # response = requests.post('http://127.0.0.1:8000/api/rest-auth/login/',
    # credentials)
    headers = {'Authorization': token_h}
    response = requests.get('http://127.0.0.1:8000/api/profiles/', headers=headers)

    print('status code: ', response.status_code)
    res_data = response.json()
    print(res_data)

if __name__ == '__main__':
    client()