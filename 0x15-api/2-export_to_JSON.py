#!/usr/bin/python3
""" Script that, using a REST API, for a given employee ID,
returns information about his/her todo list progress.
"""
import csv
import json
import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python 0-gather_data_from_an_API.py <employee_id>")
        sys.exit(1)

    employee_id = sys.argv[1]
    URL = "https://jsonplaceholder.typicode.com/"

    user_response = requests.get(f"{URL}users/{employee_id}")
    if user_response.status_code != 200:
        print("Error: User not found")
        sys.exit(1)

    user = user_response.json()
    employee_name = user.get('username')

    print(employee_name)

    todos_response = requests.get(f"{URL}todos",
                                  params={"userId": employee_id})
    if todos_response.status_code != 200:
        print("Error: Todos not found")
        sys.exit(1)
    todos = todos_response.json()

    json_file = f"{employee_id}.json"

    tasks_list = []
    for task in todos:
        task_info = {
            "task": task['title'],
            "completed": task['completed'],
            "username": employee_name,
        }
        tasks_list.append(task_info)

    user_task = {employee_id: tasks_list}

    with open(json_file, mode="w") as json_file:
        json.dump(user_task, json_file)

    print(f"Data exported to {json_file}")
