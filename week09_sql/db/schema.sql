-- ============================================
-- Тестовая БД для практики SQL
-- Тема: интернет-магазин (users, products, orders)
-- ============================================

-- Очистка (если запускаем повторно)
DROP TABLE IF EXISTS order_items;
DROP TABLE IF EXISTS orders;
DROP TABLE IF EXISTS products;
DROP TABLE IF EXISTS users;

-- Пользователи
CREATE TABLE users (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    email TEXT,
    country TEXT,
    is_active INTEGER NOT NULL DEFAULT 1,
    created_at TEXT NOT NULL
);

-- Продукты
CREATE TABLE products (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    category TEXT NOT NULL,
    price REAL NOT NULL,
    stock INTEGER NOT NULL DEFAULT 0
);

-- Заказы
CREATE TABLE orders (
    id INTEGER PRIMARY KEY,
    user_id INTEGER NOT NULL,
    total REAL NOT NULL,
    status TEXT NOT NULL,
    created_at TEXT NOT NULL,
    FOREIGN KEY (user_id) REFERENCES users(id)
);

-- Позиции в заказах (для JOIN в будущем)
CREATE TABLE order_items (
    id INTEGER PRIMARY KEY,
    order_id INTEGER NOT NULL,
    product_id INTEGER NOT NULL,
    quantity INTEGER NOT NULL,
    price_at_purchase REAL NOT NULL,
    FOREIGN KEY (order_id) REFERENCES orders(id),
    FOREIGN KEY (product_id) REFERENCES products(id)
);

-- ============================================
-- Данные — users (10 пользователей)
-- ============================================
INSERT INTO users (name, email, country, is_active, created_at) VALUES
    ('Igor', 'igor@test.com', 'Russia', 1, '2025-01-15'),
    ('Anna', 'anna@test.com', 'USA', 1, '2025-02-20'),
    ('Sam', 'sam@test.com', 'Germany', 1, '2025-03-05'),
    ('Kate', NULL, 'UK', 0, '2025-03-10'),
    ('John', 'john@test.com', 'USA', 1, '2025-04-01'),
    ('Priya', 'priya@test.com', 'India', 1, '2025-05-12'),
    ('Marco', 'marco@test.com', 'Italy', 1, '2025-06-08'),
    ('Emma', NULL, 'UK', 1, '2025-06-25'),
    ('Yuki', 'yuki@test.com', 'Japan', 1, '2025-07-01'),
    ('Chen', 'chen@test.com', 'China', 0, '2025-07-15');

-- ============================================
-- Данные — products (15 продуктов)
-- ============================================
INSERT INTO products (name, category, price, stock) VALUES
    ('Laptop Pro 15', 'Electronics', 1499.99, 25),
    ('Wireless Mouse', 'Electronics', 29.99, 150),
    ('USB-C Hub', 'Electronics', 49.90, 80),
    ('Mechanical Keyboard', 'Electronics', 129.00, 45),
    ('Monitor 27"', 'Electronics', 399.00, 30),
    ('Coffee Maker', 'Home', 89.50, 60),
    ('Yoga Mat', 'Fitness', 25.00, 200),
    ('Running Shoes', 'Fitness', 120.00, 100),
    ('Bluetooth Speaker', 'Electronics', 79.99, 55),
    ('Backpack', 'Fashion', 65.00, 120),
    ('Water Bottle', 'Fitness', 15.00, 300),
    ('Desk Lamp', 'Home', 45.00, 40),
    ('Notebook Set', 'Office', 12.99, 500),
    ('Wireless Charger', 'Electronics', 35.00, 0),
    ('Winter Jacket', 'Fashion', 199.00, 10);

-- ============================================
-- Данные — orders (12 заказов)
-- ============================================
INSERT INTO orders (user_id, total, status, created_at) VALUES
    (1, 1499.99, 'completed', '2025-05-01'),
    (1, 59.98, 'completed', '2025-06-15'),
    (2, 249.00, 'completed', '2025-06-20'),
    (3, 89.50, 'shipped', '2025-07-01'),
    (5, 449.99, 'completed', '2025-07-05'),
    (2, 25.00, 'pending', '2025-07-10'),
    (6, 199.00, 'completed', '2025-07-12'),
    (7, 174.99, 'shipped', '2025-07-15'),
    (9, 120.00, 'pending', '2025-07-18'),
    (1, 45.00, 'completed', '2025-07-20'),
    (2, 12.99, 'cancelled', '2025-07-22'),
    (5, 79.99, 'shipped', '2025-07-23');

-- ============================================
-- Данные — order_items
-- ============================================
INSERT INTO order_items (order_id, product_id, quantity, price_at_purchase) VALUES
    (1, 1, 1, 1499.99),
    (2, 2, 2, 29.99),
    (3, 4, 1, 129.00),
    (3, 5, 1, 120.00),
    (4, 6, 1, 89.50),
    (5, 5, 1, 399.00),
    (5, 12, 1, 45.00),
    (5, 11, 1, 15.00),
    (6, 7, 1, 25.00),
    (7, 15, 1, 199.00),
    (8, 8, 1, 120.00),
    (8, 9, 1, 79.99),
    (9, 8, 1, 120.00),
    (10, 12, 1, 45.00),
    (11, 13, 1, 12.99),
    (12, 9, 1, 79.99);

-- ============================================
-- Проверка
-- ============================================
SELECT 'users' as tbl, COUNT(*) as cnt FROM users
UNION ALL
SELECT 'products', COUNT(*) FROM products
UNION ALL
SELECT 'orders', COUNT(*) FROM orders
UNION ALL
SELECT 'order_items', COUNT(*) FROM order_items;