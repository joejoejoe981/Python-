# # ex01
import requests
response = requests.get(url='http://pokemondb.net/pokedex/national')
# if response.ok:
#     print('反應成功')
# else:
#     print('回應失敗')
#
# print(response.status_code)
# print(response.headers)
#
for k,v in response.headers.items():
    print('{:35s}{}'.format(k,v))

# ex02

# import requests
# response = requests.get(url='http://pokemondb.net/pokedex/national')
# if response.ok:
#     print('反應成功')
#     print(response.text)
# else:
#     print('回應失敗')
#     print(response.status_code)
#     print(response.reason)
#
