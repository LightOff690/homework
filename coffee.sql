CREATE TABLE КОФЕ (
id INT PRIMARY KEY,
название VARCHAR(255),
размер_чашки VARCHAR(20),
цена DECIMAL(6,2),
количество INT
);
CREATE TABLE БАРИСТА (
id INT PRIMARY KEY,
имя VARCHAR(255)
);
CREATE TABLE СМЕНА (
id INT PRIMARY KEY,
дата DATE,
id_бариста INT,
FOREIGN KEY (id_бариста) REFERENCES БАРИСТА(id)
);
SELECT БАРИСТА.имя
FROM БАРИСТА
JOIN СМЕНА ON БАРИСТА.id = СМЕНА.id_бариста
WHERE СМЕНА.дата = '07.09.2023';
SELECT КОФЕ.название, КОФЕ.размер_чашки
FROM КОФЕ
JOIN СМЕНА ON КОФЕ.id = СМЕНА.id_кофе
WHERE СМЕНА.дата = '07.09.2023';
SELECT БАРИСТА.имя
FROM БАРИСТА
JOIN СМЕНА ON БАРИСТА.id = СМЕНА.id_бариста
JOIN КОФЕ ON КОФЕ.id = СМЕНА.id_кофе
WHERE СМЕНА.дата = '07.09.2023' AND КОФЕ.название = 'капучино' AND КОФЕ.размер_чашки = '200 мл';