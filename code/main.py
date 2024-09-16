from data_collector import run_query
from cloner import start_clonage
from stats import calculate_metrics
from ck_runner import run_ck

import pandas as pd
import os

batch_size = 20
repos_quantity = 1000

# For each repository fetched from the API and stored in results.csv, 
# creates a new folder, named after the repo's name, to later store ck outputs
def create_folders(fetched_repos):
    for index, row in fetched_repos.iterrows():
            repo_name = row['name']

            path = f"./ck/output/{repo_name}"

            if not os.path.exists(path):
                os.makedirs(path)


if __name__ == '__main__':
    with open("query/query.gql", "r") as file:
        query = file.read()

    variables = {'num_repos': repos_quantity}

    print('''
    1- Fetch repository data and clone repos 
    2- Get CK metrics
    ''')
    
    option = input("Action: ")
    match term:
        case "1":
            run_query(batch_size, query, variables)
            start_clonage('query/results/results-0.csv')
        case "2":
            create_folders(pd.read_csv('query/results/results-0.csv'))
            # calculate_metrics()
            run_ck()


