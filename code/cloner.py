import csv
import os
import subprocess

repos_dir = 'clones'


def clone_repo(repo_url):
    repo_url += '.git'
    try:
        subprocess.run(['git', 'clone', repo_url], cwd=repos_dir, check=True)
        print(f'Repository {repo_url} cloned')
    except subprocess.CalledProcessError as e:
        print(f'Error cloning repo: {repo_url}: {e}')


def start_clonage(result_file):
    if not os.path.exists(repos_dir):
        os.makedirs(repos_dir)

    with open(result_file, mode='r') as file:
        reader = csv.reader(file)
        for row in reader:
            repo_url = row[2]
            clone_repo(repo_url)
