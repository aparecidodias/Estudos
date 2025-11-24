import pandas as pd
dados_df = pd.read_excel('produtos_ficticios.xlsx')
mais_caro = dados_df.loc[dados_df ['Preço'].idxmax()]
print(mais_caro)


import pandas as pd
dados_df = pd.read_excel('produtos_ficticios.xlsx')

mais_barato = dados_df.loc[dados_df ['Preço'].idxmin()]
print(mais_barato)