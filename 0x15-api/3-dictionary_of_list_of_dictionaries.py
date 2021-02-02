#!/usr/bin/python3
'''Python script that, using this REST API to acces todo list '''
import json
import requests

if __name__ == "__main__":
    ids = [i for i in range(1, 11)]
    session = requests.Session()
    info = {}
    for id in ids:
        URL_user = "https://jsonplaceholder.typicode.com/users/{}".format(id)
        URL = "https://jsonplaceholder.typicode.com/users/{}/todos".format(id)
        feedback = session.get(URL_user).json()
        username = feedback['username']
        task = session.get(URL).json()
        tasks = []
        info[id] = tasks
        for content in task:
            tasks.append({"username": username,
                          "task": content['title'],
                          "completed": content['completed']})
    with open("todo_all_employees.json", "w") as file:
        json.dump(info, file)
