import mysql.connector
import base62


def shorten_url(long_url):
    conn = mysql.connector.connect(
        host='your_host',
        user='your_user',
        password='your_password',
        database='your_database'
    )
    c = conn.cursor()

    c.execute('SELECT short_url FROM urls WHERE long_url = %s',
              (long_url,))
    existing_short_code = c.fetchone()

    if existing_short_code:
        short_url = existing_short_code[0]

    else:
        # Generate unique ID and base 62 code
        c.execute('INSERT INTO urls (long_url) VALUES (%s)', (long_url,))
        url_id = c.lastrowid
        short_url = base62.base62_encode(url_id)
        c.execute('UPDATE urls SET short_url = %s WHERE id = %s',
                  (short_url, url_id))

    conn.commit()
    conn.close()

    return f"www.tinyurl.com/{short_url}"


url = input("Enter the URL: ")
shortened_url = shorten_url(url)
print("Shortened URL:", shortened_url)
