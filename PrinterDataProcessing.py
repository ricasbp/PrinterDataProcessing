import pandas as pd

# Get the file names from the user
file1_name = input("Enter the file name for the first CSV file. The Last Month. (e.g., 1.csv): ")
file2_name = input("Enter the file name for the second CSV file. The Previous Month. (e.g., 2.csv): ")

folder_path = "C:\\Users\\tmart\\Desktop\\EDU\\CONTAGENS\\"

# Read the first CSV file into a DataFrame
df1 = pd.read_csv(folder_path + file1_name, encoding='utf-8')
df2 = pd.read_csv(folder_path + file2_name, encoding='utf-8')

# Read the CSV file into a DataFrame
#df = pd.read_csv('C:\\Users\\tmart\\Desktop\\EDU\\CONTAGENS\\XSAreport2024_03.csv', encoding='utf-8')

# Read the Excel file into a DataFrame
#df = pd.read_excel('C:\\Users\\tmart\\Desktop\\CONTAGENS\\XSAreport2024_05_01.xlsx')

# Print all the columns in df1 and df2
print("Columns in first CSV file:")
print(df1.columns)

print("\nColumns in second CSV file:")
print(df2.columns)

''' UTF-8 Columns
'ID da Conta',
       'Tipo de Conta',
       'Limite: Limite de Cópia em Cores', 
       'Limite: Cópias em Cores usadas',
       'Limite: Cópias em Cores Remanescentes',
       'Subcontador: Impressões de cópias grandes em cores',
       'Limite: Limite de Cópias em Preto e Branco',
       'Limite: Cópias em Preto e Branco usadas',
       'Limite: Cópias em Preto e Branco remanescentes',
       'Subcontador: Impressões de cópias grandes em P/B',
       'Limite: Limite de Impressões em Cores',
       'Limite: Impressões em Cores usadas',
       'Limite:Impressões em Cores Remanescentes',
       'Subcontador: Impressões grandes em cores',
       'Limite: Limite de Impressões em Preto e Branco',
       'Limite: Impressões em Preto e Branco usadas',
       'Limite: Impressões em Preto e Branco remanescentes',
       'Subcontador: Impressões grandes em preto e branco',
       'Última Reinicialização', 
       'Número de série da máquina',
       'Data do Relatório',
         'Hora do Relatório',

'''

''' Important Columns
'Contador: Total de cÃ³pias e impressÃµes em preto e branco',
       'Contador: Total de cÃ³pias e impressÃµes em cores',
       'Contador: Total de impressÃµes de cÃ³pias em cores',
       'Contador: Total de impressÃµes de cÃ³pias em preto e branco',
       'Contador: Total de impressÃµes em cores',
       'Contador: Total de impressÃµes em preto e branco',

       df1 = df1[(df1['Contador: Total de cópias e impressões em preto e branco'] != 0) & (df1['Contador: Total de cópias e impressões em cores'] != 0)]

'''

# List of columns you want to delete
columns_to_delete = [
         'Nome da Conta', 'ID da Conta', 'Tipo de Conta',
       
       'Limite: Limite de CÃ³pia em Cores', 'Limite: CÃ³pias em Cores usadas',
       'Limite: CÃ³pias em Cores Remanescentes',
       'Subcontador: ImpressÃµes de cÃ³pias grandes em cores',
       'Limite: Limite de CÃ³pias em Preto e Branco',
       'Limite: CÃ³pias em Preto e Branco usadas',
       'Limite: CÃ³pias em Preto e Branco remanescentes',
       'Subcontador: ImpressÃµes de cÃ³pias grandes em P/B',
       'Limite: Limite de ImpressÃµes em Cores',
       'Limite: ImpressÃµes em Cores usadas',
       'Limite:ImpressÃµes em Cores Remanescentes',
       'Subcontador: ImpressÃµes grandes em cores',
       'Limite: Limite de ImpressÃµes em Preto e Branco',
       'Limite: ImpressÃµes em Preto e Branco usadas',
       'Limite: ImpressÃµes em Preto e Branco remanescentes',
       'Subcontador: ImpressÃµes grandes em preto e branco',
       'Ãšltima ReinicializaÃ§Ã£o', 'NÃºmero de sÃ©rie da mÃ¡quina',
       'Data do RelatÃ³rio', 'Hora do RelatÃ³rio'
         ]

# drop the columns
df1.drop(columns=columns_to_delete, inplace=True)
df2.drop(columns=columns_to_delete, inplace=True)
print("\nDropped Columns in both .csvs!")

# print new columns
print("New Columns in first CSV file:")
print(df1.columns)

print("\n New Columns in second CSV file:")
print(df2.columns)

# Filter rows where both column X and column Y are not equal to 0
df1 = df1[(df1['Contador: Total de impressÃµes de cÃ³pias em preto e branco'] != 0) & (df1['Contador: Total de cÃ³pias e impressÃµes em cores'] != 0)]
df2 = df2[(df2['Contador: Total de impressÃµes de cÃ³pias em preto e branco'] != 0) & (df2['Contador: Total de cÃ³pias e impressÃµes em cores'] != 0)]
print("\nFiltered values with 0 in both .csvs!")


# Create an empty DataFrame with desired columns
result_columns = ['Diferença dos totais de impressões em preto e branco', 'Diferença dos totais de impressões em cores']
result = pd.DataFrame(columns=result_columns)

# Perform subtraction of column from df1 and df2
result['Diferença dos totais de impressões em preto e branco'] = df2['Contador: Total de impressÃµes de cÃ³pias em preto e branco'] - df1['Contador: Total de impressÃµes de cÃ³pias em preto e branco']
result['Diferença dos totais de impressões em cores'] = df2['Contador: Total de cÃ³pias e impressÃµes em cores'] - df1['Contador: Total de cÃ³pias e impressÃµes em cores']
print("\nSubtracted values to new .csv!")


# TODO: CONFIRMAR SE ESTA A APAGAR EM CASOS EM QUE SÓ TEM UM 0 NUM DOS SITIOS

#print(result.columns)

result_name = "modified_file.csv"

# Save the modified DataFrame back to a CSV file
result.to_csv(folder_path + result_name, index=False)

print("\nGreat Sucess Bolachinha! \nCreated new .csv called: " + result_name + "\n")
