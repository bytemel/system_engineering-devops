#!/usr/bin/python3
"""
Script using REST API
Exports all employee data to_do data in JSON format
"""

import json
import requests


if __name__ == "__main__":

    base_url = "https://jsonplaceholder.typicode.com"
    users = requests.get(base_url + "/users").json()

    with open("todo_all_employees.json", "w") as json_file:
        json.dump({u.get("id"): [{
            "username": u.get("username"),
            "task": t.get("title"),
            "completed": t.get("completed")}
            for t in requests.get(base_url + "/todos",
                                  params={"userId": u.get("id")}).json()]
            for u in users}, json_file)
