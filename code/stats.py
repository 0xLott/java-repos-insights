from datetime import datetime, timezone

import csv
import math
import ast
import os
import pandas as pd
import numpy as np

def calculate_metrics():
    root_path = 'ck/output'

    for dirpath, dirs, files in os.walk(root_path):
        for dir in dirs:
            # Gather this repository's data from results.csv
            repos_data = pd.read_csv('query/results/results-0.csv')   
            row = repos_data[repos_data["name"] == dir]

            # Gather this repository's data from ck outputs
            classes_data = pd.read_csv('ck/output/' + dir +  '/class.csv')
            methods_data = pd.read_csv('ck/output/' + dir + '/method.csv')

            cbo = cbo_from_csv(classes_data)
            dit = dit_from_csv(classes_data)
            lcom = lcom_from_csv(classes_data)
            loc = loc_from_csv(methods_data)
            [age, stars, releases] = process_row(row)

            print("\n" + dir + " metrics:")
            display_metrics(cbo, dit, lcom, loc, age, stars, releases)

def process_row(row):   
    row = row.iloc[0]
    age = calculate_age(row['createdAt'])
    stars = row['stargazerCount']
    releases = calculate_releases(row['releases'])

    return age, stars, releases

def display_metrics(cbo, dit, lcom, loc, age, stars, releases):
    print(f"\t CBO: {cbo}")
    print(f"\t DIT: {dit}")
    print(f"\t LCOM*: {lcom}")
    print(f"\t # of releases: {releases}")
    print(f"\t LOC: {loc}")
    print(f"\t # of stars: {stars}")
    print(f"\t Age (in days): {age}")

# CBO: Coupling between objects
def cbo_from_csv(data):
    df = data
    
    total_cbo = pd.to_numeric(df['cbo'], errors='coerce').mean()
    return total_cbo

# DIT: Depth of Inheritance Tree
def dit_from_csv(data):
    df = data
    
    total_dit = pd.to_numeric(df['dit'], errors='coerce').max()
    return total_dit

# LCOM*: Lack of Cohesion of Methods
def lcom_from_csv(data):
    df = data
    
    total_lcom = pd.to_numeric(df['lcom*'], errors='coerce').mean()
    return total_lcom

# Number of releases
def calculate_releases(data):
    try:
        releases_dict = eval(data)
        return int(releases_dict.get('totalCount', 0))
    except (SyntaxError, ValueError, AttributeError):
        return 0

# LOC: Lines of Code
def loc_from_csv(data):
    df = data
    
    total_loc = pd.to_numeric(df['loc'], errors='coerce').sum()
    return total_loc

# Age
def calculate_age(data):
    created_date = datetime.fromisoformat(data.replace('Z', '+00:00'))
    current_date = datetime.now(timezone.utc)
    age = (current_date - created_date).days
    return age