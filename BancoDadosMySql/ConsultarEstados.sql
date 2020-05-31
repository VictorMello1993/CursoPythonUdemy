--Consultando estados
select * from estados
select nome as 'Nome do sstado', sigla from estados
select sigla, nome from estados 

select sigla, nome as 'Nome do estado' from estados --Alias (apelidando colunas)
where regiao = 'Sul'

--Consultando nomes dos estados com regiões correspondentes cuja população é maior do que 10 milhões de habitantes
select nome, regiao from estados 
where populacao >= 10 
order by populacao

--Consultando nomes dos estados com regiões correspondentes cuja população é maior do que 10 milhões de habitantes em ordem descrescente de habitantes
select nome, regiao from estados 
where populacao >= 10 
order by populacao desc

