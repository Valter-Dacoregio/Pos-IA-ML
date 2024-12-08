library(datasets)

df <- cars[1:6, ]

# Exemplo de concatenação de vetores
vetor1 = c(df$dist, 25, 30)


mediana <- function(vetor) {
  vetor <- sort(vetor)
  n     <- length(vetor)
  if(n %% 2 == 0) {
    pos <- (n) / 2
    return ((vetor[pos] + vetor[pos+1]) / 2) 
  } else {
    pos <- (n+1) / 2
    return (vetor[pos])
  }
}

mediana(df$dist)
median(df$dist)

mediana(df$speed)
median(df$speed)

medianas <- c()
nomes    <- c()

for(i in 1:ncol(cars)) {
  # print(mediana(cars[ , i]))
  nomes <- c(nomes, colnames(cars)[i])
  medianas <- c(medianas, mediana(cars[ , i]))
}

# Criando um dataframe
cars_medianas <- data.frame('Variaveis' = nomes, 'Medianas' = medianas)







