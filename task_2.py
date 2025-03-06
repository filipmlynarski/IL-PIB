import sqlite3

conn = sqlite3.connect(":memory:")
cursor = conn.cursor()

cursor.execute(
    """
    CREATE TABLE tree (
        N INTEGER,
        P INTEGER
    )
"""
)

test_data = [(1, 2), (3, 2), (6, 8), (9, 8), (2, 5), (8, 5), (5, None)]

cursor.executemany("INSERT INTO tree (N, P) VALUES (?, ?)", test_data)

query = """
WITH nodes AS (
    SELECT 
        t1.N,
        CASE 
            WHEN t1.P IS NULL THEN 'root'
            WHEN NOT EXISTS (SELECT 1 FROM tree t2 WHERE t2.P = t1.N) THEN 'leaf'
            ELSE 'inner'
        END AS type
    FROM tree t1
)
SELECT N, type
FROM nodes
ORDER BY N;
"""

cursor.execute(query)
results = cursor.fetchall()

print("\nResults:")
print("N | type")
print("-" * 15)
for row in results:
    print(f"{row[0]} | {row[1]}")

conn.close()
