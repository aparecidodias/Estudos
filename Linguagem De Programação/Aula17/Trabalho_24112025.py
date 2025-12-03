"""
Vamos praticar Pandas usando o dataset Titanic.csv.
Este trabalho vale 15 pontos.

Lembre-se: o semestre está acabando e a prova está chegando.
Aprenda!!
"""

#--------------------------------------------------
# 1. Importação da biblioteca e carregamento
#--------------------------------------------------
import pandas as pd
dados_df = pd.read_csv('titanic.csv')#importe aqui a planilha

print(dados_df.head())


#--------------------------------------------------
# 2. Explorando o dataset
#--------------------------------------------------
print(dados_df.info())
print(dados_df.describe())

#--------------------------------------------------
# 3. Exercícios (RESPONDA USANDO CÓDIGO EM PYTHON)
#--------------------------------------------------

# 1) Quantas linhas e colunas o dataset possui?
print (dados_df.shape)


# 2) Qual é a idade média dos passageiros?
print(dados_df['Age'].mean())


# 3) Trazer apenas as colunas 'Name' e 'Age'
Name = dados_df.loc[dados_df ['Name']]
print(Name)



# 4) Trazer apenas os passageiros do sexo feminino
mulher = dados_df.loc[dados_df['Sex'] == 'female']
print(mulher)

# 5) Trazer apenas passageiros do sexo masculino com idade > 30
Masculino_maior_30 = dados_df.loc[(dados_df['sex'] == 'male') &
(dados_df['Age']>30)]

# 6) Mostrar apenas mulheres sobreviventes
mulheres_sobreviventes = dados_df.loc[(dados_df['sex'] == 'female') &
(dados_df['Survived'] == 1)]
print(mulheres_sobreviventes)

# 7) Mostrar passageiros da 1ª classe com menos de 18 anos
passageiros_1classe_menor_18 =dados_df.loc[(dados_df['Pclass'] == 1) & (dados_df['Age'] < 18)]
print(passageiros_1classe_menor_18)

# 8) Criar uma coluna chamada 'Faixa' com:
#       - CRIANCA para idade < 18
#       - ADULTO para idade >= 18

dados_df.loc[dados_df['Age'] < 18, 'Faixa'] = 'crianca'
dados_df.loc[dados_df['Age'] >= 18, 'Faixa'] = 'adulto'
print(dados_df)

# 9) Agrupar e mostrar taxa de sobrevivência por sexo
dados_df = pd.read_csv('titanic.csv')
print(dados_df.groupby('sex')['Survived'].mean())

# 10) Mostrar a tarifa média por classe
dados_df= pd.read_csv('titanic.csv')
print(dados_df.groupby('Pclass')['Fare']. mean())

# 11) Qual é a idade da pessoa mais velha do Titanic?
#     Dica: df['Age'].max()
dados_df= pd.read_csv('titanic.csv')
print(dados_df['Age'].max())

# 12) Qual foi a tarifa mais alta paga no Titanic?
#     Dica: df['Fare'].max()
dados_df= pd.read_csv('titanic.csv')
print(dados_df['Age'].max())


# 13) Qual classe tinha mais passageiros?
#     Dica: use value_counts()
dados_df= pd.read_csv('titanic.csv')
print(dados_df['Pclass'].value_counts())


#--------------------------------------------------
# 5. Exportação
#--------------------------------------------------

# 14) Exportar apenas os sobreviventes para um arquivo CSV
#     Nome sugerido: sobreviventes.csv
dados_df= pd.read_csv('titanic.csv')
Sobreviventes=dados_df[dados_df['Survived']==1]
Sobreviventes.to_csv('sobreviventes.csv', index=False)
