from datetime import datetime, timezone

import csv
import math
import ast
import pandas as pd
import numpy as np

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

# Number of stars
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

# LOC: Lines of Code
def loc_from_csv(data):
    df = data
    
    total_loc = pd.to_numeric(df['loc'], errors='coerce').sum()
    return total_loc

# Age
def age_from_csv(data):
    repo_age = []
    today = datetime.today().date()

    for row in data['createdAt']:
        date_obj = datetime.fromisoformat(row.replace('Z', '+00:00')).date()
        age_in_days = today - date_obj
        repo_age.append(age_in_days.days)

    created_at_median = np.median(repo_age)
    
    return created_at_median


def calculate_metrics():
    classes_data = pd.read_csv('ck/output/class.csv')
    methods_data = pd.read_csv('ck/output/method.csv')
    repos_data = pd.read_csv('query/results/results-0.csv')

    print("CBO:", cbo_from_csv(classes_data))
    print("DIT:", dit_from_csv(classes_data))
    print("LCOM*:", lcom_from_csv(classes_data))
    print("# of releases:", releases_from_csv(repos_data))
    print("LOC:", loc_from_csv(methods_data))
    print("# of stars:", star_count_from_csv(repos_data))
    print("Age (in days):", age_from_csv(repos_data))
