CREATE TABLE IF NOT EXISTS external_links (
    link TEXT
);
CREATE TABLE IF NOT EXISTS website_categories (
            domain VARCHAR(255) PRIMARY KEY,
            domain_frequency INTEGER,
            paths TEXT,
            country TEXT
        );