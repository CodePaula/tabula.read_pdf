import tabula
from tabula import read_pdf

df = tabula.read_pdf('nome_do_arquivo.pdf', pages = 5, lattice = True) 
tabela = df[0]
tabela = tabela.dropna(how = "all")
tabela = tabela.dropna(how = "all", axis = 1)
tabela.columns = tabela.iloc[0]
tabela = tabela.drop(tabela.index[0])
tabela = tabela.reset_index(drop = True)
print(tabela)
