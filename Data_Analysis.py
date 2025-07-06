import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv("Clean_data.csv")

print(df)

# Total revenue per city 

City_revenue = df.groupby("City")["Price"].sum()
print(City_revenue)

# Most ordered food overall 

Most_ordered = df["Food"].value_counts()
print(Most_ordered)

# City with highest average rating 

City_Rating = df.groupby("City")["Rating"].mean()
print(City_Rating)

# Average delivery time by city 

Avg_time = df.groupby("City")["DeliveryTime"].mean()
print(Avg_time)

# Top 5 expensive orders 

Expensive_order = df.sort_values(by="Price", ascending=False).head(5)
print(Expensive_order)

# Count of each payment method 

Payment_method = df["PaymentMethod"].value_counts().sort_values(ascending=False)
print(Payment_method)



# PIE CHART 

Payment_method.plot(
    kind="pie",
    autopct="%1.1f%%",
    title="Payment Methods",
)

plt.ylabel("")
plt.show()

# Bar chart: Revenue by city  

City_revenue.plot(
    kind="bar",
    xlabel="CITY",
    ylabel="Revenue Price (Rupees)",
    title = "City Revenue",
    color="orange"
)

plt.show()

