import requests

url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
r = requests.get(url)
print('Status code: {}'.format(r.status_code))

respose_dict = r.json()