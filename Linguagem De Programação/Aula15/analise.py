import pandas as pd
dados_df = pd.read_excel('produtos_ficticios.xlsx')
#string mostra todas as linhas da tabela
#print(dados_df.to_string())
#mostra apenas as colunas
#print(dados_df.columns)
#print(dados_df.shape)


#produto = dados_df['Quantidade em estoque']
#print(produto)
#Roupas = dados_df.loc[dados_df['Categoria']=='Roupas ']
#print(Roupas)
#Roupas = dados_df.loc[dados_df['Categoria'] == 'Roupas' , ['Categoria' ,'Código do produto', 'Preço'] ]
#print(Roupas)
#produto_cor_df = dados_df.loc[
#    (dados_df['Cor'] == 'Preto') &
   #  (dados_df['Categoria']  == 'Roupas'),
   # ['Categoria','Código do produto','Preço']
#]

#mostrar resultado Filtrando
#print(produto_cor_df)
print(dados_df.loc[5,'Código do produto'])


