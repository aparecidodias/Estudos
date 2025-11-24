import pandas as pd
dados_df = pd.read_excel('produtos_ficticios.xlsx')
#
# 
# liste os produtos acima de 50
mais_barato = dados_df.loc[dados_df ['Preço'].idxmin()]
print(mais_barato)