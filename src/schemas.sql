-- FinTech Risk Lab
-- Oracle-friendly schema design
-- Focus: clarity, constraints, portability

CREATE TABLE customers (
  customer_id NUMBER PRIMARY KEY,
  full_name   VARCHAR2(120) NOT NULL,
  age         NUMBER,
  country     VARCHAR2(60),
  created_at  DATE DEFAULT SYSDATE
);

CREATE TABLE loans (
  loan_id        NUMBER PRIMARY KEY,
  customer_id    NUMBER NOT NULL,
  principal      NUMBER(12,2) NOT NULL,
  interest_rate  NUMBER(5,2) NOT NULL,
  term_months    NUMBER NOT NULL,
  status         VARCHAR2(30) DEFAULT 'active',
  created_at     DATE DEFAULT SYSDATE,
  CONSTRAINT fk_loans_customer
    FOREIGN KEY (customer_id)
    REFERENCES customers(customer_id)
);

CREATE TABLE transactions (
  txn_id       NUMBER PRIMARY KEY,
  customer_id  NUMBER NOT NULL,
  amount       NUMBER(12,2) NOT NULL,
  txn_type     VARCHAR2(30) NOT NULL,
  channel      VARCHAR2(30),
  txn_time     DATE DEFAULT SYSDATE,
  CONSTRAINT fk_txn_customer
    FOREIGN KEY (customer_id)
    REFERENCES customers(customer_id)
);
