CREATE TABLE `mobile_phones`(`id` INT PRIMARY KEY AUTO_INCREMENT, `product_name` VARCHAR(50), `manifacturer` VARCHAR(50), `product_count` INT, `price` INT);

INSERT INTO `mobile_phones` (`product_name`,`manifacturer`,`product_count`,`price`) VALUES ('iPhone X','Apple','3','76000'),('iPhone 8','Apple','2','51000'),('Galaxy S9','Samsung','2','56000'),('Galaxy S8','Samsung','1','41000'),('P20 Pro','Huawei','5','36000');

SELECT product_name, manifacturer, price FROM mobile_phones WHERE product_count > 2;

SELECT * FROM mobile_phones WHERE manifacturer = 'Samsung';