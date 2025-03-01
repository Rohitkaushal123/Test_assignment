from faker import Faker
import random
import pandas as pd

fake = Faker()
categories = ["Food","Transportation","Bills","Groceries","Subscription","Entertainment"]
payment_mode = ["Cash","Online"]
data = []
for _ in range(100):
    data.append({
        "Date" : fake.date_this_year(),
        "Category": random.choice(categories),
        "Payment Mode": random.choice(payment_mode),
        "Description": fake.sentence(),
        "Amount Paid": round(random.uniform(100,1000),2),
        "Cashback": round(random.uniform(1,50),2),
    })

    df = pd.DataFrame(data)
    print(df)
    df.to_csv('expensee_data.csv', index=False)
    print("Data saved to expenses_data.csv")