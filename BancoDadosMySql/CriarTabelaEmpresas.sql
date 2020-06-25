--Criando tabela de empresas
create table if not exists empresas (
    id int unsigned not null auto_increment,
    nome varchar(255) not null,
    cnpj int unsigned,
    primary key (id),
    unique key (cnpj)
);


--cidades_empresas (relação muitos para muitos - N para N)
create table if not exists empresa_unidades (
    empresa_id int unsigned not null,
    cidade_id int unsigned not null,
    sede tinyint(1) not null,
    primary key (empresa_id, cidade_id)
)
