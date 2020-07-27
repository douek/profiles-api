import requests


def client():
    # data = {'username':'testrest', 'password1':'changeme123','password2':'changeme123', 'email':'test@tset.com'}
    # response = requests.post('http://127.0.0.1:8000/api/rest-auth/registration/',
    # data=data)
    #from the response
    token_h = 'Token 2cdff4d69f51e204746d9a069ba0a0b2d0ac96e1'
    headers = {'Authorization': token_h}
    response = requests.get('http://127.0.0.1:8000/api/profiles/', headers=headers)

    print('status code: ', response.status_code)
    res_data = response.json()
    print(res_data)

if __name__ == '__main__':
    client()