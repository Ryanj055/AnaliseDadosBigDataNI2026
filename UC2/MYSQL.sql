#id_produtocreate database vendas_online;
CREATE database vendas_online;
USE vendas_online;

CREATE TABLE produtos (
id_produto INT auto_increment PRIMARY KEY ,
nome VARCHAR(100),
 categoria VARCHAR(50),
 preco DECIMAL(10, 2),categoria
 estoque INT
);
select * from produtospreco

-- CLIENTE
CREATE TABLE clientes (
id_cliente INT PRIMARY KEY NOT NULL ,
NOME VARCHAR(255) NOT NULL,
email VARCHAR(255) NOT NULL
);
select * from CLIENTES;
ALTER table Clientes RENAME column nome to nome_cliente; -- my sql v.5.0 inferior
alter table clientes change nome nome_cliente varchar(255); -- mysql v. 5.0 superior 


-- Pedidos
create table pedidos (
	id_pedido INT PRIMARY KEY,
	id_cliente INT,
    data_pedido DATE,
	valor_total DECIMAL(10, 2),
	id_produto INT,
	quantidade INT
); 

ALTER TABLE pedidos
ADD CONSTRAINT fk_pedidos_clientes
foreign key (id_cliente) references clientes(id_cliente);

ALTER TABLE pedidos
ADD CONSTRAINT fk_pedidos_produtos
foreign key (id_produto) references produtos(id_produto);
select * from pedidos;

truncate table pedidos;
select * from pedidos;

select data_pedido, valor_total
from pedidos
where data_pedido < "2024-02-24";

select nome_cliente, email
from clientes
where nome_cliente = "daniela ferreira";

select nome_produto, preco
from produtos
where preco > 1000;


