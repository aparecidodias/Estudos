import pandas as pd
dados_df = pd.read_excel('produtos_ficticios.xlsx')
caros = dados_df[dados_df['Preço']>300]['Nome do produto']
['Preço']
print(caros)


