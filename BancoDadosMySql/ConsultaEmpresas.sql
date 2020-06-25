--Consultando tabela de empresas

select e.nome Empresa, c.nome Cidade from empresas e, empresa_unidades eu, cidades c
where e.id = eu.empresa_id
and c.id = eu.cidade_id
and sede = 1 