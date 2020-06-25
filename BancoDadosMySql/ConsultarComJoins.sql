--Explorando os tipos de joins


select * from prefeitos
select * from cidades

--Inner Join
select * from cidades c inner join prefeitos p on c.id = p.cidade_id

--Left Join
select * from cidades c left join prefeitos p on c.id = p.cidade_id

--Right Join
select * from cidades c right join prefeitos p on c.id = p.cidade_id

--Full join (não suportado pelo MySql - Alternativamente utilizar union)
select * from cidades c left join prefeitos p on c.id = p.cidade_id
union
select * from cidades c right join prefeitos p on c.id = p.cidade_id