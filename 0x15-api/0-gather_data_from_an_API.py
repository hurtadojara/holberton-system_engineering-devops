#!/usr/bin/python3
''' takes data from an API '''
import requests
from sys import argv


if __name__ == "__main__":
    if argv[1]:
        id = argv[1]
    URL_user = "https://jsonplaceholder.typicode.com/users/{}".format(id)
    URL = "https://jsonplaceholder.typicode.com/users/{}/todos".format(id)
    session = requests.Session()
    feedback = session.get(URL_user)
    name = feedback.json()['name']
    feedback = session.get(URL)
    json_t = feedback.json()
    task = []
    for content in json_t:
        if content['completed']:
            task.append('\t ' + content['title'])
    print("Employee", end=" ")
    print("{} is done with tasks({}/{}):".format(name, len(task), len(json_t)))
    print(*task, sep='\n')
