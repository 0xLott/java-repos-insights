# java-repos-insights

A data-driven analysis of Java GitHub repositories, exploring correlations between repository stats and CK (Chidamber and Kemerer) code quality metrics.

---

## Examined metrics and summarization

#### RQ 01: "What is the correlation between a repository popularity and its quality characteristics?"

_"Qual a relação entre a popularidade dos repositórios e as suas características de qualidade?"_  
`stars_vs_quality`: Correlation between the total amount of stars and quality metrics (CBO, DIT, LCOM) across repositories.

#### RQ 02: "What is the correlation between a repository maturity and its quality characteristics?"

_"Qual a relação entre a maturidade dos repositórios e as suas características de qualidade?"_  
`age_vs_quality`: Correlation between repository age (in years) and quality metrics (CBO, DIT, LCOM) across repositories.

#### RQ 03: "What is the correlation between a repository activity and its quality characteristics?"

_"Qual a relação entre a atividade dos repositórios e as suas características de qualidade?"_  
`activity_vs_quality`: Correlation between the number of releases and quality metrics (CBO, DIT, LCOM) across repositories.

#### RQ 04: "What is the correlation between a repository size and its quality characteristics?"

_"Qual a relação entre o tamanho dos repositórios e as suas características de qualidade?"_  
`size_vs_quality`: Correlation between the total lines of code (LOC) and lines of comments with quality metrics (CBO, DIT, LCOM) across repositories.

### Process Metrics

| Metric                    | Definition                                  | Summarization Method |
| ------------------------- | ------------------------------------------- | -------------------- |
| **Repository popularity** | Total amount of stars                       | Total                |
| **Codebase size**         | Lines of code (LOC) and lines of comments   | Total                |
| **Project activity**      | Number of releases                          | Total                |
| **Repository age**        | Age (in years) of each collected repository | Total                |

### Quality Metrics

| Metric                                | Definition                                                             | Summarization Method |
| ------------------------------------- | ---------------------------------------------------------------------- | -------------------- |
| **CBO: Coupling between objects**     | Number of dependencies a class has                                     | Mean                 |
| **DIT: Depth Inheritance Tree**       | Number of levels a class is from the root of the inheritance hierarchy | Maximum              |
| **LCOM: Lack of Cohesion of Methods** | Degree of method cohesion in a class, normalized between 0 and 1       | Mean                 |

---

## Getting started

## 1. Environment setup

1.1 Navigate to "code" directory

```bash
cd code
```

1.2. Install the required packages

```bash
pip install -r requirements.txt
```

## 2. Run

2.1 Navigate to "code" directory

```bash
cd code
```

2.2. Run program

```bash
python main.py
```
