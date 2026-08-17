# Online Retail Sales Analysis
## Project Overview
This project analyzes transaction records from a UK-based online retailer to understand and detect the main contributors to product sales and the effect of recorded cancellations.

## Objective:
The main objective is to identify opportunities to increase and protect Net Product Sales by answering two broad questions:
1. Which identified customers, products, and time periods contribute most to gross product sales?
2. Where are recorded cancellations most concentrated by customer, product, and time?

The analysis concludes by recommending a set of monthly KPIs for monitoring gross sales, cancellations, net sales, order activity, and identified-customer retention.

## Analytical Definitions
For this project:

- Gross Product Sales: the value of positive merchandise transactions before recorded cancellations.
- Cancelled Sales Value: the absolute value of recorded merchandise cancellations.
- Net Product Sales: Gross Product Sales minus Cancelled Sales Value.

Postage, discounts, fees, commissions, inventory adjustments, and other non-product entries are outside the primary analytical scope. Consequently, these measures represent product sales recorded in the dataset rather than the retailer’s complete accounting revenue.

## Key Findings

- The retailer generated approximately £10.27 million in gross product sales and £9.79 million in net product sales during the observed period.
- Units ordered showed a substantially stronger association with product sales than product price.
- Product sales were concentrated: the top 20% of products generated approximately 78.2% of gross product sales.
- Among identified customers, 65.27% placed at least two orders and repeat buyers generated 92.82% of identified-customer sales.
- Cancellation value represented 4.66% of gross product sales and was heavily influenced by a small number of extreme transactions.
- There was a big drop at the end of December 2010 where daily purchases, cancellations, and value all reached 0 for a few days.
- December 2011 is incomplete, so it was excluded from direct comparisons with complete months.

See the [full analysis report](reports/analysis%20report.pdf) for detailed findings, limitations, and recommendations.

---
## Analysis Workflow
1. Initial exploration of the raw dataset
2. Data cleaning
3. Exploratory data analysis
4. Final insights and recommendations reporting

---
## Dataset
The data contains transactions from 01/12/2010 to 09/12/2011 of a UK-based non-store online retail which sells mainly unique all-occasion gifts. Many customers in the dataset are wholesalers.

### Columns
- **InvoiceNo** (Nominal): Invoice number. A 6-digit integral number uniquely assigned to each order. Codes starting with "C" indicate a cancellation.
- **StockCode** (Nominal): Product code. A code uniquely assigned to each product.
- **Description** (Nominal): Product name.
- **Quantity** (Numeric, Discrete): Number of items bought per transaction.
- **InvoiceDate** (Datetime): Date and time of the generation of each transaction. Ranged from 01/12/2010 to 09/12/2011.
- **UnitPrice** (Numeric, Continuous): Product price per unit (in sterling).
- **CustomerID** (Nominal): A 5-digit code assigned uniquely to each customer.
- **Country** (Nominal): Country name. The country where each customer resides.

Data source: [Online Retail | Kaggle](https://www.kaggle.com/datasets/tunguz/online-retail)

## Tools

- Python
- NumPy
- pandas
- Matplotlib
- seaborn
- Jupyter
- Git and GitHub

---
## Limitations and Assumptions

This project uses a public dataset without access to the retailer’s stakeholders, source systems, or internal business documentation. Several decisions must therefore be based on the evidence available within the dataset and documented analytical assumptions.

Important limitations include:
- The dataset does not contain a unique invoice-line identifier, making the legitimacy of exact duplicate rows uncertain.
- A substantial proportion of records has no CustomerID, so customer-level findings apply only to identified customers.
- Cancellation reasons are unavailable.
- It is not specified whether cancellations are done on whole orders or if they can be done partially on each order transaction.
- The data does not confirm payment, fulfilment, delivery, or refund status.
- Product catalogue, inventory, cost, and historical pricing references are unavailable.
- Some stock codes represent non-product financial or operational entries.
- The dataset covers only one year, limiting conclusions about long-term and annual trends.
- The final month (December 2011) is incomplete and should not be compared directly with complete months.
- The data is heavily concentrated in the United Kingdom, so geographic comparison is outside the primary project scope.
- Cleaning and analytical decisions are documented in their respective notebooks. Findings should be interpreted as evidence-based observations from the available transaction data, not definitive statements about the retailer’s complete business performance.

---
## How to Reproduce the Analysis

### 1. Clone the repository

```bash
git clone https://github.com/ahmed-nassr/online-retail.git
cd online-retail
```

### 2. Create and activate a virtual environment

```bash
python -m venv .venv
```

Activation On Windows:

```bash
.venv\Scripts\activate
```

Activation On macOS or Linux:

```bash
source .venv/bin/activate
```

### 3. Install the required packages

```bash
python -m pip install -r requirements.txt
```

### 4. Add the dataset

Download `Online_Retail.csv` from the [Kaggle dataset page (click here)](https://www.kaggle.com/datasets/tunguz/online-retail) and place it in:

```text
data/raw/Online_Retail.csv
```

Skip this step if the raw dataset is already included in the repository.

### 5. Run the notebooks

Open the repository in a Jupyter-compatible environment, such as VS Code, JupyterLab, or Jupyter Notebook.

Run the notebooks in the following order:

1. `notebooks/01_raw_data_exploration.ipynb`
2. `notebooks/02_data_cleaning.ipynb`
3. `notebooks/03_eda.ipynb`

The cleaning notebook creates the processed dataset used by the EDA notebook, so the notebooks should be run sequentially.

### 6. View the final report

The final analysis report is available in:

```text
reports/online_retail_report.pdf
```

---