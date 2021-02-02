#!/usr/bin/python3
'''Python script that
 using this REST API to acces todo list and export it to csv'''
import csv
import requests
from sys import argv

if __name__ == "__main__":
    id = argv[1]
    URL_user = "https://jsonplaceholder.typicode.com/users/{}".format(id)
    URL = "https://jsonplaceholder.typicode.com/users/{}/todos".format(id)
    session = requests.Session()
    feedback = session.get(URL_user)
    username = feedback.json()['username']
    feedback = session.get(URL)
    task = feedback.json()
    tasks = []
    for content in task:
        tasks.append([id, username, content['completed'], content['title']])
    with open("{}.csv".format(id), "w") as file:
        writer = csv.writer(file, quoting=csv.QUOTE_ALL)
        writer.writerows(tasks)
