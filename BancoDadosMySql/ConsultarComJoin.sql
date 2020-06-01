--Consulta com joins (juntando a tabela de estados com tabelas de cidades)


select e.nome, c.nome, regiao  from estados e, cidades c
where e.id = estado_id

--Alternativa: INNER JOIN
select c.nome as Cidade, e.nome as Estado, regiao as Regiao
from estados e inner join cidades c
on e.id = c.estado_id
