
insert into cidades (nome, area, estado_id)
values('Campinas', 795, 21)

insert into cidades (nome, area, estado_id)
values('Niterói', 795, 15)

insert into cidades (nome, area, estado_id)
values('Gramado', 395, (select id from estados where sigla = 'RS'))

insert into cidades (nome, area, estado_id)
values('Balneário Camboriú', 590, (select id from estados where sigla = 'SC'))

select * from cidades