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

def clean(value):
    if value == "N/A" or value == "":
        return None
    return value

count = 0

with open("agrihub data.json", "r", encoding="utf-8") as f:
    for line in f:
        row = json.loads(line)

        cur.execute("""
            INSERT INTO agrihub_data (
                timestamp,
                ec_value,
                ph_value,
                water_temp,
                lux_value,
                humidity,
                surround_temp,
                water_level,
                dosing_pump
            )
            VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)
        """,
        (
            row["timestamp"],
            clean(row["ec_value"]),
            clean(row["ph_value"]),
            clean(row["water_temp"]),
            clean(row["lux_value"]),
            clean(row["humidity"]),
            clean(row["surround_temp"]),
            row["water_level"],
            row["dosing_pump"]
        ))

        count += 1

conn.commit()
cur.close()
conn.close()

print(f"{count} rows inserted successfully")
