import psycopg2

def create_table():
    # 1. Make connection
    conn = psycopg2.connect("dbname='database1' user='postgres' password='postgres1234' port='5432' host='localhost'")

    # 2. Craete a cursor object
    cur = conn.cursor()

    # 3. Crate the table
    cur.execute("CREATE TABLE IF NOT EXISTS store (item TEXT, quantity INTEGER, price REAL)")

    # 4. Commit
    conn.commit()

    # 5. Close the connection
    conn.close()

# Create function to avoid duplicate entry
def insert(item, quantity, price):
    conn = psycopg2.connect("dbname='database1' user='postgres' password='postgres1234' port='5432' host='localhost'")
    cur = conn.cursor()
    cur.execute("INSERT INTO store VALUES (%s, %s, %s)", (item, quantity, price))
    conn.commit()
    conn.close()

def delete(item):
    conn = psycopg2.connect("dbname='database1' user='postgres' password='postgres1234' port='5432' host='localhost'")
    cur = conn.cursor()
    cur.execute("DELETE FROM store WHERE item = %s ", (item,))
    conn.commit()
    conn.close()

def update(quantity, price, item):
    conn = psycopg2.connect("dbname='database1' user='postgres' password='postgres1234' port='5432' host='localhost'")
    cur = conn.cursor()
    cur.execute("UPDATE store SET quantity = %s, price = %s WHERE item = %s", (quantity, price, item))
    conn.commit()
    conn.close()

#Display the data
def view():
    conn = psycopg2.connect("dbname='database1' user='postgres' password='postgres1234' port='5432' host='localhost'")
    cur = conn.cursor()
    cur.execute("SELECT * FROM store")
    rows = cur.fetchall()
    conn.close()
    return rows

create_table()
insert("Apple", 10, 15)
insert("Orange", 10, 15)
delete("Orange")
update(15, 15, "Apple")
print(view())