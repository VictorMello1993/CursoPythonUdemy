--Inserindo estados com Id
insert into estados (id, nome, sigla, regiao, populacao)
values (1000, 'Novo', 'NV', 'Sul', 2.54)

select * from estados

--Inserindo estados sem id (no caso, como a PK é auto-incremento, em vez de incrementar em relação ao último registro 
insert into estados (nome, sigla, regiao, populacao)
values ('Mais Novo', 'MN', 'Norte', 2.51)

select * from estados