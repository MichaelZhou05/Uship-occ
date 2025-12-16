CREATE EXTENSION IF NOT EXISTS pgcrypto;

CREATE TABLE orders (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),

    customer_name TEXT NOT NULL,
    customer_email TEXT NOT NULL,

    address TEXT NOT NULL,
    latitude DOUBLE PRECISION,
    longitude DOUBLE PRECISION,

    box_count INTEGER CHECK (box_count >= 0),

    status TEXT NOT NULL DEFAULT 'UNCONFIRMED',

    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);