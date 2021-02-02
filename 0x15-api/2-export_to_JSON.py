#!/usr/bin/python3
'''Python script that
using this REST API to acces todo list and export it to json'''
import json
import requests
from sys import argv

if __name__ == "__main__":
    if argv[1]:
        id = argv[1]
    URL_user = "https://jsonplaceholder.typicode.com/users/{}".format(id)
    URL = "https://jsonplaceholder.typicode.com/users/{}/todos".format(id)
    session = requests.Session()
    feedback = session.get(URL_user)
    username = feedback.json()['username']
    feedback = session.get(URL)
    task = feedback.json()
    tasks = []
    info = {id: tasks}
    for content in task:
        tasks.append({"task": content['title'],
                      "completed": content['completed'],
                      "username": username})
    with open("{}.json".format(id), "w") as file:
        json.dump(info, file)
