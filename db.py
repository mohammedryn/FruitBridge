import psycopg2
from psycopg2 import sql

# Replace with your actual connection string
connection = psycopg2.connect(
    "postgresql://export_management_owner:M9m4XrsQhgNj@ep-bitter-salad-a1fgi0js.ap-southeast-1.aws.neon.tech/export_management?sslmode=require",
    sslmode='require'  # Use 'require' if Neon enforces SSL
)

try:
    cursor = connection.cursor()
    print("Connected to Neon PostgreSQL Database!")
    cursor.execute("SELECT NOW();")
    print("Current time from database:", cursor.fetchone())
except Exception as error:
    print("Error connecting to PostgreSQL:", error)
finally:
    if connection:
        cursor.close()
        connection.close()
