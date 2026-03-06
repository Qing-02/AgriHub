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

print("Connected successfully!")

cur = conn.cursor()

# Open JSON file
with open("agrihub data.json", "r") as f:
    lines = f.readlines()

# Insert first 10 rows
for line in lines[:10]:
    data = json.loads(line)

    cur.execute("""
        INSERT INTO weather_data
        (timestamp, ec_value, ph_value, water_temp, lux_value,
         humidity, surround_temp, water_level, dosing_pump)
        VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)
    """, (
        data["timestamp"],
        data["ec_value"],
        data["ph_value"],
        data["water_temp"],
        data["lux_value"],
        data["humidity"],
        data["surround_temp"],
        data["water_level"],
        data["dosing_pump"]
    ))

conn.commit()
cur.close()
conn.close()

print("✅ 10 rows inserted successfully")