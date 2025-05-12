
import psycopg2
import os
from werkzeug.security import generate_password_hash

def init_db():
    schema = """
    CREATE TABLE IF NOT EXISTS users (
        id SERIAL PRIMARY KEY,
        username TEXT UNIQUE NOT NULL,
        password TEXT NOT NULL,
        prestige INTEGER DEFAULT 0,
        argent INTEGER DEFAULT 0,
        niveau INTEGER DEFAULT 1,
        ip TEXT,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );

    CREATE TABLE IF NOT EXISTS invites (
        code TEXT PRIMARY KEY,
        used BOOLEAN DEFAULT FALSE,
        used_by TEXT
    );
    """

    conn = psycopg2.connect(os.environ.get("DATABASE_URL"), sslmode="require")
    cur = conn.cursor()
    cur.execute(schema)

    # Insère Topaz si non existant
    cur.execute("SELECT * FROM users WHERE username = 'Topaz'")
    if not cur.fetchone():
        password = generate_password_hash("azertyuiop")
        cur.execute("INSERT INTO users (username, password, prestige, argent, niveau) VALUES (%s, %s, %s, %s, %s)", 
                    ("Topaz", password, 9999, 999999, 666))
        conn.commit()
    cur.close()
    conn.close()
    print("✔️ Base PostgreSQL initialisée avec compte Topaz.")

if __name__ == "__main__":
    init_db()
