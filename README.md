# java-repos-insights
A data-driven analysis of Java GitHub repositories, exploring correlations between repository stats and CK (Chidamber and Kemerer) code quality metrics.

---

## Examined metrics and summarization

### RQ 01: "What is the correlation between a repository popularity and its quality characteristics?"
*"Qual a relação entre a popularidade dos repositórios e as suas características de qualidade?"*  
`stars_vs_quality`: Correlation between the total amount of stars and quality metrics (CBO, DIT, LCOM) across repositories.

### RQ 02: "What is the correlation between a repository maturity and its quality characteristics?"
*"Qual a relação entre a maturidade dos repositórios e as suas características de qualidade?"*  
`age_vs_quality`: Correlation between repository age (in years) and quality metrics (CBO, DIT, LCOM) across repositories.

### RQ 03: "What is the correlation between a repository activity and its quality characteristics?"
*"Qual a relação entre a atividade dos repositórios e as suas características de qualidade?"*  
`activity_vs_quality`: Correlation between the number of releases and quality metrics (CBO, DIT, LCOM) across repositories.

### RQ 04: "What is the correlation between a repository size and its quality characteristics?"
*"Qual a relação entre o tamanho dos repositórios e as suas características de qualidade?"*  
`size_vs_quality`: Correlation between the total lines of code (LOC) and lines of comments with quality metrics (CBO, DIT, LCOM) across repositories.



### Process Metrics

| Metric           | Definition                                            | Summarization Method |
|------------------|-------------------------------------------------------|----------------------|
| **Repository popularity**| Total amount of stars                         | Total |
| **Codebase size**        | Lines of code (LOC) and lines of comments     | Total |
| **Project activity**     | Number of releases                            | Total |
| **Repository age**       | Age (in years) of each collected repository   | Total |

### Quality Metrics

| Metric | Definition | Summarization Method |
|--------|------------|----------------------|
| **CBO: Coupling between objects** | Number of dependencies a class has | Mean |
| **DIT: Depth Inheritance Tree** | Number of levels a class is from the root of the inheritance hierarchy | Maximum |
| **LCOM: Lack of Cohesion of Methods** | Degree of method cohesion in a class, normalized between 0 and 1 | Mean |



---


## Getting started

## 1. Virtual Environment setup

1.1 Navigate to "code" directory
```bash
cd code
```

1.2. Create a virtual environment in the root directory of your project
```bash
python3 -m venv .venv
```

1.3. Activate the virtual environment to use the isolated Python environment
```bash
# On Windows:
source .venv/bin/activate
```

```bash
# On Linux or MacOS:
.venv/Scripts/activate
```

1.4. With the virtual environment active, install the required packages
```bash
pip install -r requirements.txt
```
```bash
ck pull repo:ck-win
```

## 2. Run

2.1 Navigate to "code" directory
```bash
cd code
```

2.2. Activate the virtual environment
- Instructions can be found in step 1.3

2.3. Run program
```bash
python main.py
```
