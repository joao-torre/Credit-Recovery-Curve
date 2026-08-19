# Credit Recovery Curve

Projeto de **Data Analytics aplicado à recuperação de crédito**, desenvolvido para analisar a evolução dos valores recuperados após o default e comparar a performance por produto, perfil de risco, coorte e vintage.

> Todos os dados utilizados são sintéticos e foram gerados exclusivamente para fins educacionais e de portfólio. Nenhum dado representa clientes ou informações reais.

## 🎯 Objetivo

Responder perguntas como:

- Como a recuperação evolui ao longo do tempo?
- Quais produtos apresentam maior recuperação?
- Como o risco influencia a recuperação?
- Quais coortes apresentam melhor performance?
- Em quanto tempo a carteira atinge 50% de recuperação?
- As novas vintages estão melhorando ou piorando?

## 📊 Principais análises

- **Recovery Rate**
- **Recovery Curve**
- Recovery Rate @ 30d, 60d, 90d, 120d, 180d e 360d
- Recuperação por produto
- Recuperação por perfil de risco
- **Cohort Analysis**
- **Vintage Analysis**

### Estrutura
Credit-Recovery-Curve/
├── README.md
├── requirements.txt
├── main.py
├── data/
│   ├── raw/
│   └── processed/
├── src/
│   ├── data_generator.py
│   ├── data_cleaning.py
│   ├── recovery_metrics.py
│   ├── cohort_analysis.py
│   └── analysis.py
├── notebooks/
├── outputs/
└── tests/

### Dados sintéticos

A base contém aproximadamente:

10.000 clientes
15.000 contratos
150.000 parcelas
Eventos de recuperação

Produtos analisados:

Personal Loan
Vehicle Finance
Credit Card
Payroll Loan

Perfis de risco:

LOW
MEDIUM
HIGH
🛠️ Tecnologias
Python
Pandas
NumPy
Matplotlib
Seaborn
Pytest

Evolução planejada:

SQL / DuckDB
Power BI
AWS S3 + Athena
