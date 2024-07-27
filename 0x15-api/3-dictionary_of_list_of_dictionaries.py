#!/usr/bin/python3
""" Script that, using a REST API, for a given employee ID,
returns information about his/her todo list progress.
"""
import csv
import json
import requests
import sys

if __name__ == "__main__":
    URL = "https://jsonplaceholder.typicode.com/"

    user_response = requests.get(f"{URL}users")
    if user_response.status_code != 200:
        print("Error: User not found")
        sys.exit(1)

    users = user_response.json()

    all_tasks = {}
    for user in users:
        user_id = user['id']
        username = user['username']

        todo_response = requests.get(f"{URL}todos", params={"userId": user_id})
        if todo_response.status_code != 200:
            print(f"Error: Could not retrieve todos for user {user_id}")
            sys.exit(1)

        todos = todo_response.json()

        tasks_list = []
        for task in todos:
            task_info = {
                "username": username,
                "task": task['title'],
                "completed": task['completed']
            }
            tasks_list.append(task_info)

        all_tasks[user_id] = tasks_list

    json_filename = "todo_all_employees.json"
    with open(json_filename, mode="w") as json_file:
        json.dump(all_tasks, json_file)
