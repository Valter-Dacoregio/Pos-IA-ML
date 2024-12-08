library(readxl)

caminho <- '/home/valter/Documentos/DEV/Estudos/Pos-IA-ML/UC4-Tecnicas_Estatisticas_R_Programing/dadosPratica.xlsx'
dados <- read_excel(caminho, col_types = c('text', 'numeric', 'text', 'numeric', 'text'), na = 'NA')

View(dados)

# mostra a média, mediana, moda dos dados
summary(dados)

# mostre estatísticas da coluna sexo, mostre a quantidade de ocorrencia de cada valor
table(dados$Sexo)
table(dados$Classe_social)
table(dados$Escolaridade)

# mostre o tanto que cada valor da coluna sexo representa em porcentagem
prop.table(table(dados$Sexo))
prop.table(table(dados$Classe_social))
prop.table(table(dados$Escolaridade))

library(funModeling)
df_status(dados)

# mostre histogramas para todas as colunas
hist(dados$Idade)
hist(dados$N_Filhos)

# crie um novo dataframe só com as colunas numéricas
dados_num <- dados[, c(2, 4)]

# mostre a correlação entre as colunas numéricas
cor(dados_num)

# mostre a correlação entre as colunas numéricas com um gráfico
library(corrplot)
corrplot(cor(dados_num))


# Distribuição de Bernouli e Binomial
# Probabilidade de obter 0 sucessos em 3 lançamentos com probabilidade de ganho igual a probabilidade de perda é de exatamente 1/8=0.125
dbinom(x = 0, size = 3, prob = 0.5)
