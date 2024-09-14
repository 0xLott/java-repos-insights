from data_collector import run_query

if __name__ == '__main__':

    with open("query/query.gql", "r") as file:
        query = file.read()

    variables = {}
    variables['num_repos'] = 1
    run_query(query, variables)