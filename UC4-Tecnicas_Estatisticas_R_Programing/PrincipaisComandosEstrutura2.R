
caminho <- '/home/valter/Documentos/DEV/Estudos/Pos-IA-ML/UC4-Tecnicas_Estatisticas_R_Programing/dados.csv'
df <- read.csv(caminho, sep = ';', dec = ',')

library(jsonlite)

#Lista de todas as escolas em funcionamento que não tenham energia, água nem esgoto, e que tenham cozinha.
# http://educacao.dadosabertosbr.org
url <- 'http://educacao.dadosabertosbr.org/api/escolas/buscaavancada?situacaoFuncionamento=1&energiaInexistente=on&aguaInexistente=on&esgotoInexistente=on&cozinha=on'
df <- fromJSON(url)

