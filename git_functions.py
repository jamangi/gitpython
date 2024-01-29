import git
from pathlib import Path
import json


database_filename = "entries.json"
all_potatoes = []


def pull_database():
    current_directory = Path.cwd()
    repo = git.Repo(str(current_directory))
    origin = repo.remote("origin")
    origin.fetch()

    repo.git.pull(origin, repo.head.ref)

    print("Database pulled")


def push_database(commit_message):
    current_directory = Path.cwd()
    repo = git.Repo(str(current_directory))
    origin = repo.remote("origin")
    origin.fetch()
    repo.index.add([database_filename])
    repo.index.commit(commit_message)
    repo.git.push(origin, repo.head.ref)
    print("database pushed")


def save_potatoes(potatoes,save_filename):
    with open(save_filename, 'w') as file:
        json.dump(potatoes,file)

    return potatoes


def load_potatoes(save_filename):
    with open(save_filename, 'r') as file:
        loaded_potatoes = json.load(file)

    return loaded_potatoes


if __name__ == '__main__':
    try:
        pull_database()
        all_potatoes = load_potatoes(database_filename)
    except:
        pass

    blob = {"blob": len(all_potatoes)}
    all_potatoes.append(blob)
    save_potatoes(all_potatoes, database_filename)
    push_database("commit from gitpython")
