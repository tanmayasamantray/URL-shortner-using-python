import mysql.connector
conn = mysql.connector.connect(
    host="your_host",
    user="your_user",
    password="your_password",
    database="your_database"
)

c = conn.cursor()

c.execute("""
    CREATE TABLE IF NOT EXISTS urls (
        id INT AUTO_INCREMENT PRIMARY KEY,
        long_url VARCHAR(255),
        short_url VARCHAR(255)
    )
""")

conn.commit()
conn.close()
