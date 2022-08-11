import requests

from pprint import pprint


def diet_choice(x):
    query = x
    url = 'https://api.api-ninjas.com/v1/recipe?query={}'.format(query)
    response = requests.get(url, headers={'X-Api-Key': '4aMjDI71/zFUTVQgSk5Oow==59V4Rb7LfOul3ls3'})

    if response.status_code == requests.codes.ok:
        pprint(response.json())
    else:
        print("Error:", response.status_code, response.text)


def veggie_breakfast():
    diet_choice("shakshuka")


def veggie_dinner():
    diet_choice("spinach lasagne")


def vegan_breakfast():
    diet_choice("vegan pancakes")


def vegan_dinner():
    diet_choice("vegan pasta")


vegan_dinner()
