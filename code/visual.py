import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import pearsonr


def plot_stars_vs_quality(CBO, DIT, LCOM, stars):
    data = pd.DataFrame({
        'CBO': CBO,
        'DIT': DIT,
        'LCOM': LCOM,
        'Stars': stars
    })

    # Create the plots
    fig, axs = plt.subplots(1, 3, figsize=(18, 5))

    for i, metric in enumerate(['CBO', 'DIT', 'LCOM']):
        sns.scatterplot(data=data, x='Stars', y=metric, ax=axs[i])

        if np.std(data['Stars']) == 0 or np.std(data[metric]) == 0:
            correlation = np.nan
        else:
            correlation, _ = pearsonr(data['Stars'], data[metric])

        axs[i].set_title(f'Stars vs {metric} (r = {correlation:.2f})')
        axs[i].set_xlabel('Stars')
        axs[i].set_ylabel(metric)

    plt.tight_layout()
    plt.savefig('./plots/stars_vs_quality.jpg')
    plt.show()


def plot_age_vs_quality(CBO, DIT, LCOM, ages):
    data = pd.DataFrame({
        'CBO': CBO,
        'DIT': DIT,
        'LCOM': LCOM,
        'Age': ages
    })

    fig, axs = plt.subplots(1, 3, figsize=(18, 5))

    for i, metric in enumerate(['CBO', 'DIT', 'LCOM']):
        sns.scatterplot(data=data, x='Age', y=metric, ax=axs[i])

        if np.std(data['Age']) == 0 or np.std(data[metric]) == 0:
            correlation = np.nan
        else:
            correlation, _ = pearsonr(data['Age'], data[metric])

        axs[i].set_title(f'Age vs {metric} (r = {correlation:.2f})')
        axs[i].set_xlabel('Age (years)')
        axs[i].set_ylabel(metric)

    plt.tight_layout()
    plt.savefig('./plots/age_vs_quality.jpg')
    plt.show()


def plot_activity_vs_quality(CBO, DIT, LCOM, releases):
    data = pd.DataFrame({
        'CBO': CBO,
        'DIT': DIT,
        'LCOM': LCOM,
        'Releases': releases
    })

    fig, axs = plt.subplots(1, 3, figsize=(18, 5))

    for i, metric in enumerate(['CBO', 'DIT', 'LCOM']):
        sns.scatterplot(data=data, x='Releases', y=metric, ax=axs[i])

        if np.std(data['Releases']) == 0 or np.std(data[metric]) == 0:
            correlation = np.nan
        else:
            correlation, _ = pearsonr(data['Releases'], data[metric])

        axs[i].set_title(f'Releases vs {metric} (r = {correlation:.2f})')
        axs[i].set_xlabel('Number of Releases')
        axs[i].set_ylabel(metric)

    plt.tight_layout()
    plt.savefig('./plots/activity_vs_quality.jpg')
    plt.show()


def plot_size_vs_quality(CBO, DIT, LCOM, LOC):
    data = pd.DataFrame({
        'CBO': CBO,
        'DIT': DIT,
        'LCOM': LCOM,
        'LOC': LOC
    })

    fig, axs = plt.subplots(1, 3, figsize=(18, 5))

    for i, metric in enumerate(['CBO', 'DIT', 'LCOM']):
        sns.scatterplot(data=data, x='LOC', y=metric, ax=axs[i])

        if np.std(data['LOC']) == 0 or np.std(data[metric]) == 0:
            correlation = np.nan
        else:
            correlation, _ = pearsonr(data['LOC'], data[metric])

        axs[i].set_title(f'LOC vs {metric} (r = {correlation:.2f})')
        axs[i].set_xlabel('Total Lines of Code (LOC)')
        axs[i].set_ylabel(metric)

    plt.tight_layout()
    plt.savefig('./plots/size_vs_quality.jpg')
    plt.show()
