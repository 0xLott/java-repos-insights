import csv
import math
import ast
import pandas as pd

# CBO: Coupling between objects
def cbo_from_csv(file_path):
    total_cbo = 0
    with open(file_path, mode='r') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            try:
                cbo_value = float(row['cbo'])
                total_cbo += cbo_value
            except ValueError:
                continue
    return total_cbo

# DIT: Depth of Inheritance Tree
def dit_from_csv(file_path):
    total_dit = 0
    with open(file_path, mode='r') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            try:
                dit_value = float(row['dit'])
                total_dit += dit_value
            except ValueError:
                continue
    return total_dit

# LCOM*: Lack of Cohesion of Methods
def lcom_from_csv(file_path):
    total_lcom = 0
    with open(file_path, mode='r') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            try:
                lcom_value = float(row['lcom*'])
                if not math.isnan(lcom_value):
                    total_lcom += lcom_value
            except ValueError:
                continue
    return total_lcom

# Releases
def releases_from_csv(data):
    total_releases = []

    for row in data['releases']:
        release_data = ast.literal_eval(row)
        total_releases.append(release_data['totalCount'])

    total_releases_mean = np.mean(total_releases)

    plt.clf()

    plt.hist(total_releases, bins=30, color='salmon', edgecolor='black')
    plt.axvline(total_releases_mean, color='red', linestyle='dashed', linewidth=1)
    plt.title('Distribuição do Total de Releases')
    plt.xlabel('Número de Releases')
    plt.ylabel('Frequência')

    plt.savefig('./plots/rq_03.jpg')
    plt.show()

    return total_releases_mean

def metrics():
    classes_file_path = 'ck/output/class.csv'
    fields_file_path = 'ck/output/field.csv'
    methods_file_path = 'ck/output/method.csv'
    variables_file_path = 'ck/output/variable.csv'

    repos_data = pd.read_csv('query/results/results-0.csv')

    print("CBO:", cbo_from_csv(classes_file_path))
    print("DIT:", dit_from_csv(classes_file_path))
    print("LCOM*:", lcom_from_csv(classes_file_path))
    print("# of releases:", releases_from_csv(repos_data))
