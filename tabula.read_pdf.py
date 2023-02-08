import tabula
from tabula import read_pdf

# reading the file (the parameter "pages" is the page that you want to read)
df = tabula.read_pdf('file_name.pdf', pages = 2, lattice = True) 
tabela = df[0]
# organizing data in the file, using methods
tabela = tabela.dropna(how = "all") 
tabela = tabela.dropna(how = "all", axis = 1)
tabela.columns = tabela.iloc[0]
tabela = tabela.drop(tabela.index[0])
tabela = tabela.reset_index(drop = True)
print(tabela)
