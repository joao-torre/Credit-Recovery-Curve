# Credit Recovery Curve

Projeto de **Data Analytics aplicado à recuperação de crédito**, desenvolvido para analisar a evolução dos valores recuperados após o default e comparar a performance por **produto, perfil de risco, coorte e vintage**.

> **Dados 100% sintéticos:** todos os dados foram gerados exclusivamente para fins educacionais e de portfólio. Nenhuma informação representa clientes, contratos ou estratégias reais.

---

## 🎯 Problema

Após um contrato entrar em default, a recuperação do saldo não ocorre de forma uniforme ao longo do tempo.

A análise da **Recovery Curve** permite entender quanto da exposição é recuperada em diferentes períodos e identificar diferenças de performance entre produtos, perfis de risco e cohorts.

## Objetivo

Investigar:

* Como a recuperação evolui após o default?
* Quais produtos apresentam maior recuperação?
* Como o perfil de risco influencia a recuperação?
* Quais cohorts apresentam melhor performance?
* Em quanto tempo a carteira atinge 50% de recuperação?
* As novas vintages apresentam evolução de performance?

---

## 📊 Principais métricas

### Recovery Rate

Percentual do saldo originalmente em default que foi recuperado ao longo do tempo.

### Recovery Curve

Evolução acumulada da recuperação após o default.

### Recovery Rate por período

Comparação da recuperação acumulada em:

**30d · 60d · 90d · 120d · 180d · 360d**

### Cohort Analysis

Comparação da recuperação entre grupos de contratos que entraram em default em diferentes períodos.

### Vintage Analysis

Avaliação da evolução da performance entre diferentes vintages de default.

---

## 🔎 Dimensões analisadas

### Produtos

* Personal Loan
* Vehicle Finance
* Credit Card
* Payroll Loan

### Perfil de risco

* LOW
* MEDIUM
* HIGH

### Outras dimensões

* Cohort
* Vintage
* Dias desde o default
* Valor em default
* Valor recuperado

---

## 🧠 Perguntas de negócio

O projeto foi estruturado para responder perguntas como:

> **Qual produto apresenta a melhor recuperação acumulada após 180 dias?**

> **Clientes de maior risco apresentam recuperação significativamente menor?**

> **Qual cohort atinge 50% de recuperação mais rapidamente?**

> **As vintages mais recentes apresentam melhora ou deterioração na curva de recuperação?**

> **Em qual período ocorre a maior concentração dos eventos de recuperação?**

---

## 📈 Insights

Os resultados das análises são apresentados por meio de curvas de recuperação, comparações entre produtos, perfis de risco, cohorts e vintages.

> **Os insights apresentados são baseados exclusivamente nos dados sintéticos gerados pelo projeto e não representam comportamento real de carteiras de crédito.**

---

## 🏗️ Estrutura do projeto

```text
Credit-Recovery-Curve/
│
├── README.md
├── requirements.txt
├── main.py
│
├── data/
│   ├── raw/
│   └── processed/
│
├── src/
│   ├── data_generator.py
│   ├── data_cleaning.py
│   ├── recovery_metrics.py
│   ├── cohort_analysis.py
│   └── analysis.py
│
├── notebooks/
├── outputs/
└── tests/
```

---

## 📦 Dados sintéticos

O projeto trabalha com aproximadamente:

* **10.000 clientes**
* **15.000 contratos**
* **150.000 parcelas**
* Eventos de recuperação

Os dados foram gerados artificialmente para reproduzir uma estrutura semelhante à encontrada em análises de recuperação de crédito, sem utilizar informações reais.

---

## 🛠️ Tecnologias

**Python · Pandas · NumPy · Matplotlib · Seaborn · Pytest**

### Em evolução

**SQL / DuckDB · Power BI · AWS S3 · Amazon Athena**

---

## 🚀 Evolução planejada

O projeto foi estruturado para evoluir de uma análise local em Python para uma solução analítica mais completa:

```text
Dados sintéticos
       ↓
Python / Pandas
       ↓
SQL / DuckDB
       ↓
AWS S3
       ↓
Amazon Athena
       ↓
Power BI
```

Essa evolução permitirá separar as etapas de **geração, armazenamento, transformação, análise e visualização dos dados**.

---

## ⚠️ Disclaimer

Este projeto possui finalidade exclusivamente educacional e de portfólio.

Os dados, resultados e padrões apresentados são sintéticos e não devem ser utilizados para decisões reais de crédito, cobrança ou recuperação.
