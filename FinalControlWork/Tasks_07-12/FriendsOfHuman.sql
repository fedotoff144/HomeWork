-- 7. В подключенном MySQL репозитории создать базу данных “Друзья человека”
CREATE DATABASE friends_of_human;
USE friends_of_human;


-- 8. Создать таблицы с иерархией из диаграммы в БД
DROP TABLE IF EXISTS animals;
CREATE TABLE animals (animals_id INT AUTO_INCREMENT PRIMARY KEY,
                    type_of_animal VARCHAR(25));
INSERT INTO animals (type_of_animal)
VALUES ('Домашние'), ('Вьючные');
SELECT * FROM animals;


DROP TABLE IF EXISTS wild_animals;
CREATE TABLE wild_animals (wild_animals_id INT AUTO_INCREMENT PRIMARY KEY,
                            group_of_animals VARCHAR(25),
                            type_id INT,
                            FOREIGN KEY (type_id) REFERENCES animals (animals_id) ON UPDATE CASCADE ON DELETE CASCADE);

INSERT INTO wild_animals (group_of_animals, type_id)
VALUES ('Лошади', 2), ('Верблюды', 2), ('Ослы', 2);
SELECT * FROM wild_animals;


DROP TABLE IF EXISTS pet_animals;
CREATE TABLE pet_animals (pet_animals_id INT AUTO_INCREMENT PRIMARY KEY,
                            group_of_animals VARCHAR(25),
                            type_id INT,
                            FOREIGN KEY (type_id) REFERENCES animals (animals_id) ON UPDATE CASCADE ON DELETE CASCADE);
INSERT INTO pet_animals (group_of_animals, type_id)
VALUES ('Собаки', 1), ('Кошки', 1), ('Хомяки', 1);
SELECT * FROM pet_animals;


/* 9. Заполнить низкоуровневые таблицы именами(животных), командами
   которые они выполняют и датами рождения
 */
DROP TABLE IF EXISTS dogs;
CREATE TABLE dogs (dogs_id INT AUTO_INCREMENT PRIMARY KEY,
                    name VARCHAR(25),
                    commands VARCHAR(25),
                    birthday DATE,
                    group_id INT,
                    FOREIGN KEY (group_id) REFERENCES pet_animals (pet_animals_id) ON UPDATE CASCADE ON DELETE CASCADE);
INSERT INTO dogs (name, commands, birthday, group_id)
VALUES ('Бобик', 'лежать', '2020-01-01', 1),
       ('Шарик', 'сидеть', '2019-01-01', 1);


DROP TABLE IF EXISTS cats;
CREATE TABLE cats (cats_id INT AUTO_INCREMENT PRIMARY KEY,
                    name VARCHAR(25),
                    commands VARCHAR(25),
                    birthday DATE,
                    group_id INT,
                    FOREIGN KEY (group_id) REFERENCES pet_animals (pet_animals_id) ON UPDATE CASCADE ON DELETE CASCADE);
INSERT INTO cats (name, commands, birthday, group_id)
VALUES ('Барсик', 'служить', '2020-12-12', 2),
       ('Пушок', 'голос', '2018-10-10', 2);


DROP TABLE IF EXISTS hamsters;
CREATE TABLE hamsters (hamsters_id INT AUTO_INCREMENT PRIMARY KEY,
                    name VARCHAR(25),
                    commands VARCHAR(25),
                    birthday DATE,
                    group_id INT,
                    FOREIGN KEY (group_id) REFERENCES pet_animals (pet_animals_id) ON UPDATE CASCADE ON DELETE CASCADE);
INSERT INTO hamsters (name, commands, birthday, group_id)
VALUES ('Хома', 'сидеть', '2020-11-11', 3),
       ('Комок', 'голос', '2018-09-09', 3);


DROP TABLE IF EXISTS horses;
CREATE TABLE horses (horses_id INT AUTO_INCREMENT PRIMARY KEY,
                    name VARCHAR(25),
                    commands VARCHAR(25),
                    birthday DATE,
                    group_id INT,
                    FOREIGN KEY (group_id) REFERENCES wild_animals (wild_animals_id) ON UPDATE CASCADE ON DELETE CASCADE);
INSERT INTO horses (name, commands, birthday, group_id)
VALUES ('Молния', 'бегом', '2016-11-11', 1),
       ('Бурка', 'голопом', '2018-08-08', 1);


DROP TABLE IF EXISTS camels;
CREATE TABLE camels (camels_id INT AUTO_INCREMENT PRIMARY KEY,
                    name VARCHAR(25),
                    commands VARCHAR(25),
                    birthday DATE,
                    group_id INT,
                    FOREIGN KEY (group_id) REFERENCES wild_animals (wild_animals_id) ON UPDATE CASCADE ON DELETE CASCADE);
INSERT INTO camels (name, commands, birthday, group_id)
VALUES ('Руфат', 'сидеть', '2016-07-07', 2),
       ('Бурак', 'лежать', '2017-06-06', 2);


DROP TABLE IF EXISTS donkeys;
CREATE TABLE donkeys (donkeys_id INT AUTO_INCREMENT PRIMARY KEY,
                    name VARCHAR(25),
                    commands VARCHAR(25),
                    birthday DATE,
                    group_id INT,
                    FOREIGN KEY (group_id) REFERENCES wild_animals (wild_animals_id) ON UPDATE CASCADE ON DELETE CASCADE);
INSERT INTO donkeys (name, commands, birthday, group_id)
VALUES ('Иа', 'сидеть', '2016-05-05', 3),
       ('Мак', 'голос', '2015-04-04', 3);


/* 10. Удалив из таблицы верблюдов, т.к. верблюдов решили перевезти в другой
питомник на зимовку. Объединить таблицы лошади, и ослы в одну таблицу.
 */
DELETE FROM wild_animals
WHERE group_of_animals = 'Верблюды';

SELECT * FROM horses
UNION
SELECT * FROM donkeys;


/* 11.Создать новую таблицу “молодые животные” в которую попадут все
животные старше 1 года, но младше 3 лет и в отдельном столбце с точностью
до месяца подсчитать возраст животных в новой таблице
 */
DROP TABLE IF EXISTS all_animals_temp;
CREATE TEMPORARY TABLE all_animals_temp AS
SELECT name, birthday, 'Лошадь' AS name_animal FROM horses
UNION SELECT name, birthday, 'Осел' AS name_animal FROM donkeys
UNION SELECT name, birthday, 'Собака' AS name_animal FROM dogs
UNION SELECT name, birthday, 'Кошка' AS name_animal FROM cats
UNION SELECT name, birthday, 'Хомяк' AS name_animal FROM hamsters;


DROP TABLE IF EXISTS yang_animals;
CREATE TABLE yang_animals (yang_animals_id INT AUTO_INCREMENT PRIMARY KEY,
                            type_of_animal VARCHAR(25),
                            name VARCHAR(25),
                            birthday DATE,
                            cuantity_of_month INT);

INSERT INTO yang_animals(type_of_animal, name, birthday, cuantity_of_month)
SELECT name_animal, name, birthday, TIMESTAMPDIFF(MONTH, birthday, CURDATE()) AS cuantity_of_month
FROM all_animals_temp WHERE birthday BETWEEN ADDDATE(CURDATE(), INTERVAL -3 YEAR) AND ADDDATE(CURDATE(), INTERVAL -1 YEAR);

SELECT * FROM yang_animals;


/* 12. Объединить все таблицы в одну, при этом сохраняя поля, указывающие на
прошлую принадлежность к старым таблицам.
 */
DROP TABLE IF EXISTS all_animals;
CREATE TABLE all_animals (all_id INT AUTO_INCREMENT PRIMARY KEY,
                    name VARCHAR(25),
                    commands VARCHAR(25),
                    birthday DATE,
                    group_id INT,
                    group_of_animals VARCHAR(25),
                    type_of_animals VARCHAR(25));
INSERT INTO all_animals (name, commands, birthday, group_id, group_of_animals, type_of_animals)
SELECT d.name, d.commands, d.birthday, d.group_id, pa.group_of_animals, a.type_of_animal
FROM dogs AS d
LEFT JOIN pet_animals AS pa ON d.group_id = pa.pet_animals_id
LEFT JOIN animals AS a ON pa.type_id = a.animals_id

UNION ALL
SELECT c.name, c.commands, c.birthday, c.group_id, group_of_animals, a.type_of_animal
FROM cats AS c
LEFT JOIN pet_animals AS pa ON c.group_id = pa.pet_animals_id
LEFT JOIN animals AS a ON pa.type_id = a.animals_id

UNION ALL
SELECT h.name, h.commands, h.birthday, h.group_id, group_of_animals, a.type_of_animal
FROM hamsters AS h
LEFT JOIN pet_animals AS pa ON h.group_id = pa.pet_animals_id
LEFT JOIN animals AS a ON pa.type_id = a.animals_id

UNION ALL
SELECT h.name, h.commands, h.birthday, h.group_id, wa.group_of_animals, a.type_of_animal
FROM horses AS h
LEFT JOIN wild_animals AS wa ON h.group_id = wa.wild_animals_id
LEFT JOIN animals AS a ON wa.type_id = a.animals_id

UNION ALL
SELECT cm.name, cm.commands, cm.birthday, cm.group_id, wa.group_of_animals, a.type_of_animal
FROM camels AS cm
LEFT JOIN wild_animals AS wa ON cm.group_id = wa.wild_animals_id
LEFT JOIN animals AS a ON wa.type_id = a.animals_id

UNION ALL
SELECT d.name, d.commands, d.birthday, d.group_id, wa.group_of_animals, a.type_of_animal
FROM donkeys AS d
LEFT JOIN wild_animals AS wa ON d.group_id = wa.wild_animals_id
LEFT JOIN animals AS a ON wa.type_id = a.animals_id;

SELECT * FROM all_animals;
