CREATE DATABASE nutrif;

CREATE TABLE `tb_campus` (
  `id_campus` int(10) UNSIGNED NOT NULL AUTO_INCREMENT,
  `cidade` varchar(60) NOT NULL,
  `sigla` varchar(3) NOT NULL,
  PRIMARY KEY (`id_campus`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

CREATE TABLE `tb_aluno` (
  `id_aluno` int UNSIGNED NOT NULL AUTO_INCREMENT,
  `fk_id_campus` int UNSIGNED NOT NULL,
  `matricula_aluno` varchar(12) NOT NULL,
  `nome` text NOT NULL,
  `nascimento` date NOT NULL,
  `altura` double NOT NULL,
  `peso` double NOT NULL,
  PRIMARY KEY (`id_aluno`),
  UNIQUE KEY `matricula_aluno` (`matricula_aluno`),
  FOREIGN KEY(fk_id_campus) REFERENCES tb_campus(id_campus)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

CREATE TABLE `tb_dia` (
  `id_dia` int(10) NOT NULL AUTO_INCREMENT,
  `nome_dia` text NOT NULL,
  PRIMARY KEY (`id_dia`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

CREATE TABLE `tb_nutricionista` (
  `id_nutricionista` int UNSIGNED NOT NULL AUTO_INCREMENT,
  `fk_id_campus` int UNSIGNED NOT NULL,
  `nome` text NOT NULL,
  `siape` varchar(10) NOT NULL,
  `CRN` text NOT NULL,
  PRIMARY KEY (`id_nutricionista`),
  FOREIGN KEY(`fk_id_campus`) REFERENCES tb_campus(`id_campus`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

CREATE TABLE `tb_dia_refeicao` (
  `id_dia_refeicao` int UNSIGNED NOT NULL AUTO_INCREMENT,
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

CREATE TABLE `tb_refeicao_realizada` (
  `id_dia_refeicao` int UNSIGNED NOT NULL AUTO_INCREMENT,
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
