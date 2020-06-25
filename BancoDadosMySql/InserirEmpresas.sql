--Inserindo registros na tabela de empresas
alter table empresas MODIFY cnpj varchar(14)

insert into empresas (nome, cnpj)
values ('Bradesco', 38570679000127),
       ('Vale', 48372551000102),
       ('Cielo', 57556239000160);


desc empresas;
desc prefeitos;
select * from empresas
select * from estados;

--Inserindo registros na tabela N para N
insert into empresa_unidades
    (empresa_id, cidade_id, sede)
values
    (1, 1, 1),    
    (1, 2, 0),    
    (2, 1, 0),    
    (2, 2, 1)    


select * from empresa_unidades    