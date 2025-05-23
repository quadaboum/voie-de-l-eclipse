
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
