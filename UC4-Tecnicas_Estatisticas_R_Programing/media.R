## Exemplo

# Dados
library(datasets)

dados <- cars

# Média
media <- mean(cars$speed)

# Moda
# library(DescTools)
# moda <- mode(cars$speed)
moda_speed <- names(sort(-table(cars$speed)))[1]
moda_dist <- names(sort(-table(cars$dist)))[1]

# Mediana
mediana_speed <- median(cars$speed)
mediana_dist <- median(cars$dist)

# Desvio Padrão
desvio_padrao_speed <- sd(cars$speed)
desvio_padrao_dist <- sd(cars$dist)

# Correlação
correlacao <- cor(cars$speed, cars$dist)
correlacao_test <- cor.test(cars$speed, cars$dist)

# Amostra
amostra <- sample(cars$speed, 10, FALSE)
amostra <- sample(1:50, 10, replace = FALSE)

amostras <- dados[amostra, ]




# Regressão Linear
linear_model = lm(dist ~ speed, data = cars)
summary(linear_model)


# Predição
novos_dados <- data.frame("speed" = c(21, 24, 26))

predict(linear_model, newdata = novos_dados, interval = "confidence")




