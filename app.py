import streamlit as st
import mysql.connector
import pandas as pd
import matplotlib.pyplot as plt

# Function to connect to MySQL
def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="@rohitGamer#3092",
        database="expenses_tracker"
    )

conn = get_connection()
cursor = conn.cursor()

## all Queries
query1 = """
SELECT `Category`, SUM(`Amount Paid`) AS Total_Spent
FROM expensee_data 
GROUP BY `Category`;
"""
cursor.execute(query1)
data1 = cursor.fetchall()
df1 = pd.DataFrame(data1, columns=["Category", "Total_Spent"])

## Query 2
query2 = """
SELECT `Payment Mode`, SUM(`Amount Paid`) AS Total_Spent 
FROM expensee_data 
GROUP BY `Payment Mode`;
"""
cursor.execute(query2)
data2 = cursor.fetchall()
df2 = pd.DataFrame(data2, columns=["Payment Mode", "Total_Spent"])

### Query 3
query3 = """
SELECT Category, SUM(`Amount Paid`) as Total_payment
FROM expensee_data
GROUP BY Category
ORDER BY Total_payment DESC
LIMIT 5;
"""
cursor.execute(query3)
data3 = cursor.fetchall()
df3 = pd.DataFrame(data3, columns=["Category", "Total_payment"])

### Query 4:
query4 = """
SELECT Category, SUM(`Amount Paid`) AS Main_category
FROM expensee_data
GROUP BY Category
ORDER BY Main_category DESC;
"""
cursor.execute(query4)
data4 = cursor.fetchall()
df4 = pd.DataFrame(data4, columns=["Category", "Main_category"])

### Query 5
query5 = """
SELECT DATE_FORMAT(Date, '%Y-%m') AS Month, SUM(`Amount Paid`) AS Total_Spent
FROM expensee_data
GROUP BY Month
ORDER BY Month;
"""
cursor.execute(query5)
data5 = cursor.fetchall()
df5 = pd.DataFrame(data5, columns=["Month", "Total_Spent"])

#Streamlit UI
st.title("📊 Expense Tracker Dashboard")

##query 1
st.subheader("💰 Total Spending by Category")
st.dataframe(df1.style.format({"Total_Spent": "₹{:.2f}"}))
fig, ax = plt.subplots()
ax.bar(df1["Category"], df1["Total_Spent"], color="skyblue")
plt.xticks(rotation=45)
plt.xlabel("Category")
plt.ylabel("Total Spent")
plt.title("Spending by Category")
st.pyplot(fig)

## query 2
st.subheader("💳 Payment Mode Distribution")
st.dataframe(df2.style.format({"Total_Spent": "₹{:.2f}"}))
fig, ax = plt.subplots()
ax.pie(df2["Total_Spent"], labels=df2["Payment Mode"], autopct="%1.1f%%", colors=["blue", "orange"])
ax.set_title("Spending by Payment Mode")
st.pyplot(fig)

## query 3
st.subheader("🔥 Top 5 Expensive Categories")
st.dataframe(df3.style.format({"Total_payment": "₹{:.2f}"}))
fig, ax = plt.subplots()
ax.plot(df3["Category"], df3["Total_payment"], marker="o", linestyle="-", color="red")
plt.xlabel("Category")
plt.ylabel("Total Payment")
plt.title("Top 5 Expensive Categories")
st.pyplot(fig)

## query 4
st.subheader("🏆 Categories with Highest Priority")
st.dataframe(df4.style.format({"Main_category": "₹{:.2f}"}))
fig, ax = plt.subplots()
ax.bar(df4["Category"], df4["Main_category"], color="green")
plt.xticks(rotation=45)
plt.xlabel("Category")
plt.ylabel("Total Spending")
plt.title("Categories with Highest Priority")
st.pyplot(fig)

##### query 5
st.subheader("📈 Monthly Spending Trend")
st.dataframe(df5.style.format({"Total_Spent": "₹{:.2f}"}))
fig, ax = plt.subplots()
ax.plot(df5["Month"], df5["Total_Spent"], marker="o", linestyle="-", color="purple")
plt.xticks(rotation=45)
plt.xlabel("Month")
plt.ylabel("Total Spending")
plt.title("Monthly Spending Trend")
st.pyplot(fig)


cursor.close()
conn.close()
