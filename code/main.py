from data_collector import run_query
from cloner import start_clonage
from ck_metrics import calculate_metrics

batch_size = 20
repos_quantity = 1000

if __name__ == '__main__':
    with open("query/query.gql", "r") as file:
        query = file.read()

    # variables = {'num_repos': repos_quantity}
    # run_query(batch_size, query, variables)
    start_clonage('query/results/results-0.csv')
    # calculate_metrics()
