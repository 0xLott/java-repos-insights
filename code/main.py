from data_collector import run_query
from cloner import start_clonage
from stats import calculate_metrics
from ck_runner import run_ck

batch_size = 20
repos_quantity = 1000

if __name__ == '__main__':
    with open("query/query.gql", "r") as file:
        query = file.read()

    variables = {'num_repos': repos_quantity}

    print('''
    1- Fetch repository data and clone repos 
    2- Get CK metrics
    ''')
    
    option = input("Action: ")
    match option:
        case "1":
            run_query(batch_size, query, variables)
            start_clonage('query/results/results-0.csv')
        case "2":
            run_ck()
            # calculate_metrics()
            


