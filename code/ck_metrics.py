import csv
import math
import ast
import pandas as pd
import numpy as np

# CBO: Coupling between objects
def cbo_from_csv(file_path):
    df = pd.read_csv(file_path)
    
    total_cbo = pd.to_numeric(df['cbo'], errors='coerce').sum()
    return total_cbo

# DIT: Depth of Inheritance Tree
def dit_from_csv(file_path):
    df = pd.read_csv(file_path)
    
    total_dit = pd.to_numeric(df['dit'], errors='coerce').sum()
    return total_dit

# LCOM*: Lack of Cohesion of Methods
def lcom_from_csv(file_path):
    df = pd.read_csv(file_path)
    
    total_lcom = pd.to_numeric(df['lcom*'], errors='coerce').sum()
    return total_lcom

# Number of star
def star_count_from_csv(data):
    df = data
    total_stars_mean = df['stargazerCount'].mean()

    return total_stars_mean

# Number of releases
def releases_from_csv(data):
    total_releases = []

    for row in data['releases']:
        release_data = ast.literal_eval(row)
        total_releases.append(release_data['totalCount'])

    total_releases_mean = np.mean(total_releases)

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
    print("# of stars:", star_count_from_csv(repos_data))
