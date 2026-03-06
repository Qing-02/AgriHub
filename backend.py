import json
import psycopg2

# Connect to PostgreSQL
conn = psycopg2.connect(
    host="localhost",
    database="metabase",
    user="metabase",
    password="metabase123",
    port=5432
)

cur = conn.cursor()

# Load JSON file
with open("agrihub data.json") as f:
    data = json.load(f)

# Insert data
for row in data:
    cur.execute(
        """
        INSERT INTO weather_data (temperature, humidity, pressure)
        VALUES (%s, %s, %s)
        """,
        (
            row["temperature"],
            row["humidity"],
            row["pressure"]
        )
    )

conn.commit()
cur.close()
conn.close()

print("Data inserted successfully")