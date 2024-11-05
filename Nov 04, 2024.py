'''
Number: 153
Task: You're given a table called userActivityLogs.
This table contains data on each time a user opens into Application X.
You can assume this table has all the historical data one would expect
(this table will be large assuming Application X has a number of loyal users).
Application X defines an active user as one that has opened the application within
the last 30 days. Using SQL, can you write a query that outputs users who are inactive?
Your output should have userid and the number of days since the last login.
'''

import sqlite3
from datetime import datetime, timedelta

#Connect to the SQLLite database
#Replace 'your_database.db' with the actual database file or connection string
conn = sqlite3.connect('your_database.db')
cursor = conn.cursor()

#Define the SQL query
query = """
WITH LastLogin AS (
    SELECT
        userid,
        MAX(date) AS last_login_date
    FROM
        userActivityLogs
    GROUP BY
        userid 
)

SELECT
    userid,
    julianday('now') - julianday(last_login_date) AS days_since_last_login
FROM 
    LastLogin
WHERE
    julianday('now') - julianday(last_login_date) > 30;
"""

#Execute the query
cursor.execute(query)
inactive_users = cursor.fetchall()

#Output the results
print("Inactive Users (No login in the last 30 days):")
for user in inactive_users:
    print(f"UserID:{user[0]}, Days Since Last Login: {int(user[1])}")

#Close the database connection
conn.close()