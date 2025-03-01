SELECT * FROM expenses_tracker.expensee_data;

##What is the total amount spent in each category?

SELECT Category, SUM(`Amount Paid`) as total_spent
FROM expensee_data
group by Category;

##What is the total amount spent using each payment mode (Cash/Online)?

SELECT `Payment Mode`, SUM(`Amount Paid`) as The_payment
FROM expensee_data
WHERE `Payment Mode` IN ('Cash','Online')
group by `Payment Mode`;

##What is the total cashback received across all transactions?

SELECT `Payment Mode`, SUM(Cashback) as Total_cashback_return
FROM expensee_data
group by `Payment Mode`;

##Which are the top 5 most expensive categories in terms of spending?

SELECT Category, SUM(`Amount Paid`) as Total_payment
FROM expensee_data
group by Category
Order by Total_payment DESC
LIMIT 5;

##How much was spent on transportation using different payment modes?

SELECT Category, SUM(`Amount Paid`) as Total_Transport
FROM expensee_data
WHERE Category = 'Transportation'
group by Category;









