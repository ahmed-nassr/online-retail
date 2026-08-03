# Online Retail Sales Analysis
## Project Overview
This project analyzes transaction records from a UK-based online retailer to understand and detect the main contributors to product sales and the effect of recorded cancellations.

## Objective:
The main objective is to identify opportunities to increase and protect Net Product Sales by answering two broad questions:
1. Which identified customers, products, and time periods contribute most to gross product sales?
2. Where are recorded cancellations most concentrated by customer, product, and time?

Even though EDA will start with initial candidate KPIs that are very likely to be valuable toward sales, credible KPIs that will should be tracked in order to measure success toward this goal will be decided as a result of this project.

## Analytical Definitions
For this project:

- Gross Product Sales: the value of positive merchandise transactions before recorded cancellations.
- Cancelled Sales Value: the absolute value of recorded merchandise cancellations.
- Net Product Sales: Gross Product Sales minus Cancelled Sales Value.

Postage, discounts, fees, commissions, inventory adjustments, and other non-product entries are outside the primary analytical scope. Consequently, these measures represent product sales recorded in the dataset rather than the retailer’s complete accounting revenue.

## Project Life-cycle Phases
1. Initial exploration of the raw dataset
2. Data cleaning
3. Exploratory data analysis
4. Final insights and recommendations report

---
## Dataset
The data contains transactions from 01/12/2010 to 09/12/2011 of a UK-based non-store online retail which sells mainly unique all-occasion gifts. Many customers in the dataset are wholesalers.

### Columns
- **InvoiceNo** (Nominal): Invoice number. A 6-digit integral number uniquely assigned to each order. Codes starting with "C" indicate a cancellation.
- **StockCode** (Nominal): Product code. A code uniquely assigned to each product.
- **Description** (Nominal): Product name.
- **Quantity** (Numeric, Discrete): Number of items bought per transaction.
- **InvoiceDate** (Time, Continuous): Date and time of the generation of each transaction. Ranged from 01/12/2010 to 09/12/2011.
- **UnitPrice** (Numeric, Continuous): Product price per unit (in sterling).
- **CustomerID** (Nominal): A 5-digit code assigned uniquely to each customer.
- **Country** (Nominal): Country name. The country where each customer resides.

Data source: [Online Retail | Kaggle](https://www.kaggle.com/datasets/tunguz/online-retail)

---
## Limitations and Assumptions

This project uses a public dataset without access to the retailer’s stakeholders, source systems, or internal business documentation. Several decisions must therefore be based on the evidence available within the dataset and documented analytical assumptions.

Important limitations include:
- The dataset does not contain a unique invoice-line identifier, making the legitimacy of exact duplicate rows uncertain.
- A substantial proportion of records has no CustomerID, so customer-level findings apply only to identified customers.
- Cancellation reasons are unavailable.
- The data does not confirm payment, fulfilment, delivery, or refund status.
- Product catalogue, inventory, cost, and historical pricing references are unavailable.
- Some stock codes represent non-product financial or operational entries.
- The dataset covers only one year, limiting conclusions about long-term and annual trends.
- The final month (December 2011) is incomplete and should not be compared directly with complete months.
- The data is heavily concentrated in the United Kingdom, so geographic comparison is outside the primary project scope.
- Cleaning and analytical decisions are documented in their respective notebooks. Findings should be interpreted as evidence-based observations from the available transaction data, not definitive statements about the retailer’s complete business performance.

---