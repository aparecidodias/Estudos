#criar a coluna status
import pandas as pd

dados_df= pd.read_excel("produtos_ficticios.xlsx")

dados_df['imposto']= dados_df['Valor em estoque']= 0.03
dados_df['Valor final'] = dados_df['Valor em estoque']* dados_df['imposto']
dados_df['Status'] = dados_df.loc[:,'status'] = 'Esgotado'



dados_df.loc[dados_df['Quantidade em estoque'] > 0,'status']= 'Disponivel'
esgotado=dados_df.loc[dados_df['Status']=='Esgotado']
print(esgotado)
