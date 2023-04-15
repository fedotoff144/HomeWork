# создаем новую базу данных
create database `lesson_02`;

# перпеходим к работе к новой базой данных
use lesson_02;

# создаем таблицу и указываем значения для колонок
CREATE TABLE sales (id INT PRIMARY KEY AUTO_INCREMENT,
					order_date DATE,
                    count_product INT NOT NULL);

# вводим данные в новую таблицу
INSERT INTO sales (order_date, count_product) VALUES ('2022-01-01', '156'),
													('2022-01-02', '180'),
                                                    ('2022-01-03', '21'),
                                                    ('2022-01-04', '124'),
                                                    ('2022-01-05', '341');

# выводим значения в соответствии с числовым показателем                                                 
SELECT id,
CASE
WHEN count_product > 0 AND count_product < 100 THEN 'Маленький заказ'
WHEN count_product >= 100 AND count_product < 300 THEN 'Средний заказ'
WHEN count_product >= 300 THEN 'Большой заказ'
END AS Тип_заказа
FROM sales;


# создаем еще одну таблицу
CREATE TABLE orders (id INT PRIMARY KEY AUTO_INCREMENT,
					employee_id VARCHAR(5),
                    amount DOUBLE,
                    order_status VARCHAR(15));
       
# вставляем значения
INSERT INTO orders (employee_id,amount,order_status) VALUES ('e03', 15.00, 'OPEN'),
															('e01', 25.50, 'OPEN'),
                                                            ('e05', 100.70, 'CLOSED'),
                                                            ('e02', 22.18, 'OPEN'),
                                                            ('e04', 9.50, 'CANCELLED');
               
# выводим столбец согласно условиям
SELECT employee_id, amount, 
CASE order_status
WHEN "OPEN" THEN "Order is an open state"
WHEN "CLOSED" THEN "Order is closed"
WHEN "CANCELLED" THEN "Order is cancelled"
END AS full_order_status
FROM orders;


/*NULL обозначает, что в поле таблице не задано никакое значение, 0 же является конкретным значением поля таблицы
и тем самым координально отличается от NULL*/
