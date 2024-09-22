CREATE DATABASE db_name;

USE db_name;

CREATE TABLE user (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(120) NOT NULL UNIQUE,
    password VARCHAR(200) NOT NULL
);

CREATE TABLE resource (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    category VARCHAR(100) NOT NULL
);

INSERT INTO resources (name, category) VALUES ('Recurso Exemplo', 'Categoria A');


-- Criar um novo usuário
CREATE USER 'novo_usuario'@'localhost' IDENTIFIED BY 'nova_senha';

-- Conceder permissões
GRANT ALL PRIVILEGES ON *.* TO 'novo_usuario'@'localhost' WITH GRANT OPTION;

-- Aplicar as alterações
FLUSH PRIVILEGES;

EXIT;

SHOW GRANTS FOR 'username'@'localhost';