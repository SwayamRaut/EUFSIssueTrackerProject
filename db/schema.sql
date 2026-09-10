    /*
    CREATE TABLE issues (
        id UUID PRIMARY KEY,
        title VARCHAR(100) NOT NULL,
        description TEXT NOT NULL,
        priority VARCHAR(20) NOT NULL DEFAULT 'medium'
            CHECK (priority IN ('low', 'medium', 'high')),
        status VARCHAR(20) NOT NULL DEFAULT 'open'
            CHECK (status IN ('open', 'in_progress', 'closed')),
        created_at TIMESTAMP DEFAULT NOW()
    );
    */

    /*
    CREATE TABLE components (
        name UUID PRIMARY KEY,
        type VARCHAR(20) NOT NULL DEFAULT 'unknown',
        cost VARCHAR(20) NOT NULL
    );

    ALTER TABLE issues ADD COLUMN name UUID REFERENCES components(name)
    */

    SELECT issues.title, components.name AS COMPONENT
    FROM issues
    JOIN components ON issues.name = components

