-- Создаем новую базу данных
CREATE DATABASE lesson_03;

-- Указываем на работу с новой базой
USE lesson_03;

-- Создаем новую таблицу staff
CREATE TABLE `staff`(`id` INT UNSIGNED PRIMARY KEY AUTO_INCREMENT,
					`firstname` VARCHAR(20) NOT NULL,
                    `lastname` VARCHAR(30) NOT NULL,
                    `post` VARCHAR(20) NOT NULL,
                    `seniority` INT NOT NULL,
                    `salary` DECIMAL(10,2) NOT NULL,
                    `age` INT NOT NULL);

-- Заполняем таблицу данными
INSERT INTO staff(firstname,lastname,post,seniority,salary,age) 
VALUES
('Вася', 'Петров', 'Начальник', '40', 100000, 60),
('Петр', 'Власов', 'Начальник', '8', 70000, 30),
('Катя', 'Катина', 'Инженер', '2', 70000, 25),
('Саша', 'Сасин', 'Инженер', '12', 50000, 35),
('Иван', 'Иванов', 'Рабочий', '40', 30000, 59),
('Петр', 'Петров', 'Рабочий', '20', 25000, 40),
('Сидр', 'Сидоров', 'Рабочий', '10', 20000, 35),
('Антон', 'Антонов', 'Рабочий', '8', 19000, 28),
('Юрий', 'Юрков', 'Рабочий', '5', 15000, 25),
('Максим', 'Максимов', 'Рабочий', '2', 11000, 22),
('Юрий', 'Галкин', 'Рабочий', '3', 12000, 24),
('Людмила', 'Маркина', 'Уборщик', '10', 10000, 49);

-- Сортировка по убыванию значенией в колонке salary
SELECT * FROM staff
ORDER BY salary DESC;

-- Сортировка по возрастанию значений в колонке salary
SELECT * FROM staff
ORDER BY salary;

-- Выведете 5 макисмальных зарплат из колонки salary
SELECT * FROM staff
ORDER BY salary DESC
LIMIT 5;

-- Посчитайте суммарную зарплату (salary) по каждой специальности (роst)
SELECT post, SUM(salary) AS result
FROM staff
GROUP BY post;

-- Найдите кол-во сотрудников с специальностью (post) «Рабочий» в возрасте от 24 до 49 лет включительно
SELECT COUNT(*)
FROM staff
WHERE post = 'Рабочий' AND age BETWEEN 24 AND 49;

-- Найдите количество уникальных специальностей
SELECT DISTINCT post
FROM staff;

-- Выведите специальности, у которых средний возраст сотрудников меньше 30 лет 
SELECT post, AVG(age)
FROM staff
GROUP BY post HAVING AVG(age) < 30;
