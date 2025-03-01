CREATE TABLE expenses_tracker.expenses(
id int auto_increment primary key,
Date DATE,
Category VARCHAR(50),
Payment_Mode  VARCHAR(50),
Description TEXT,
Amount_Paid DECIMAL(10, 2),
Cashback DECIMAL(10, 2)
);

