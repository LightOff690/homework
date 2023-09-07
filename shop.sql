CREATE TABLE ПОСТАВЩИКИ (
id INT PRIMARY KEY AUTO_INCREMENT,
название_компании VARCHAR(100) NOT NULL,
адрес VARCHAR(200) NOT NULL,
телефон VARCHAR(20) NOT NULL
);
CREATE TABLE ТОВАРЫ (
id INT PRIMARY KEY AUTO_INCREMENT,
название_товара VARCHAR(100) NOT NULL,
цена DECIMAL(10,2) NOT NULL,
количествo INT NOT NULL,
поставщик_id INT NOT NULL,
FOREIGN KEY (поставщик_id) REFERENCES ПОСТАВЩИКИ(id)
);

/* d (INT, PRIMARY KEY, AUTO_INCREMENT) - уникальный идентификатор
/*название (VARCHAR) - название поставщика
/*адрес (VARCHAR) - адрес поставщика
телефон (VARCHAR) - телефон поставщика
/*Мы определили уникальный идентификатор "id", который будет использоваться в качестве первичного ключа.
 Это позволяет нам однозначно идентифицировать каждую запись в таблице.
 Для хранения текстовых данных, таких как название, адрес и телефон, мы выбрали тип данных VARCHAR.
 VARCHAR является переменной длины типом данных,
 который может хранить строки переменной длины.*\