CREATE TABLE CUSTOMER(
    id INTEGER CONSTRAINT pk_customer PRIMARY KEY AUTOINCREMENT,
    firstname VARCHAR(15),
    name VARCHAR(40),
    mail VARCHAR(50),
    password VARCHAR(10)
);

CREATE TABLE REVENUE(
    id INTEGER CONSTRAINT pk_revenue PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(50),
    amount DECIMAL(15,2),
    id_customer INTEGER NOT NULL,
    CONSTRAINT fk_revenue_customer FOREIGN KEY(id_customer) REFERENCES CUSTOMER(id)
);

CREATE TABLE CATEGORY(
    id INTEGER CONSTRAINT pk_category PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(50),
    forecast DECIMAL(15,2),
    id_customer INTEGER NOT NULL,
    CONSTRAINT fk_category_customer FOREIGN KEY(id_customer) REFERENCES CUSTOMER(id)
);

CREATE TABLE EXPENSE(
    id INTEGER CONSTRAINT pk_expense PRIMARY KEY AUTOINCREMENT,
    label TEXT,
    amount DECIMAL(15,2),
    id_category INTEGER NOT NULL,
    id_customer INTEGER NOT NULL,
    CONSTRAINT fk_expense_category FOREIGN KEY(id_category) REFERENCES CATEGORY(id),
    CONSTRAINT fk_expense_customer FOREIGN KEY(id_customer) REFERENCES CUSTOMER(id)
);
