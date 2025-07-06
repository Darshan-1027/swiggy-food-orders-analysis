# 🍕 Swiggy Food Orders Analysis

This project analyzes food order data from Swiggy using Python (Pandas, Matplotlib, Seaborn). It provides insights into city-wise revenue, food preferences, delivery efficiency, and customer behavior.

---

## 📁 Dataset Overview

| Column         | Description                              |
|----------------|------------------------------------------|
| OrderID        | Unique order identifier                  |
| City           | City where the order was placed          |
| Food           | Food item ordered                        |
| Price          | Total price of the order                 |
| Rating         | Customer rating (out of 5)               |
| DeliveryTime   | Time taken to deliver the order (minutes)|
| PaymentMethod  | UPI, Card, or Cash                       |
| OrderDate      | Date of the order                        |

---

## 🧼 Data Cleaning Steps

- Removed duplicates  
- Checked and dropped missing values  
- Standardized column names (City, Food, etc.)  
- Converted `OrderDate` to datetime format  

---

## 🔍 Key Insights

| 🔎 Business Question                          | 📊 Analysis Performed                        |
|----------------------------------------------|----------------------------------------------|
| Total revenue per city                       | `groupby + sum`                              |
| Most ordered food items                      | `value_counts()`                             |
| City with highest average rating             | `groupby + mean`                             |
| Average delivery time by city                | `groupby + mean`                             |
| Top 5 most expensive orders                  | `sort_values(by="Price")`                    |
| Count of each payment method                 | `value_counts()`                             |

---

## 📊 Visualizations

- 📊 Pie Chart: Payment method distribution  
- 📈 Bar Chart: Revenue by city  
- 📉 Line Chart: Weekly order trend  
- 📦 Box Plot: Delivery time spread

---

## 💡 Bonus Features

- Calculated **Profit** = 20% of Price  
- Added **Discount** column (₹30 if price > ₹300)

---

## 🛠️ Tools Used

- Python
- Pandas
- Matplotlib
- Seaborn
- Jupyter Notebook

---



