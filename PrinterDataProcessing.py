import pandas as pd
import os

print("Hello, You will be asked to write the name of the 1st month, and then the previous month.")
print()
# Get the file names from the user
file1_name = input("Enter the file name from the current Month. (e.g., Maio.csv): ")
file2_name = input("Enter the file name from the previous Month. (e.g., Abril.csv): ")

# Get the current working directory
folder_path = os.getcwd() + os.sep

# Read the first CSV file into a DataFrame
df1 = pd.read_csv(folder_path + file2_name, encoding='utf-8')
df2 = pd.read_csv(folder_path + file1_name, encoding='utf-8')

# Read the CSV file into a DataFrame
#df = pd.read_csv('C:\\Users\\tmart\\Desktop\\EDU\\CONTAGENS\\XSAreport2024_03.csv', encoding='utf-8')

# Read the Excel file into a DataFrame
#df = pd.read_excel('C:\\Users\\tmart\\Desktop\\CONTAGENS\\XSAreport2024_05_01.xlsx')

# Print all the columns in df1 and df2
print("Columns in first CSV file:")
print(df1.columns)

print("\nColumns in second CSV file:")
print(df2.columns)

''' 
---
UTF-8 Columns:
---
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
       'Hora do Relatório'


---
Non UTF-8 Columns
---
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
'''

'''
---
Important columns
---

'Contador: Total de cÃ³pias e impressÃµes em preto e branco',
       'Contador: Total de cÃ³pias e impressÃµes em cores',
       'Contador: Total de impressÃµes de cÃ³pias em cores',
       'Contador: Total de impressÃµes de cÃ³pias em preto e branco',
       'Contador: Total de impressÃµes em cores',
       'Contador: Total de impressÃµes em preto e branco',

'''




# List of columns you want to delete
columns_to_delete = [
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
       'Hora do Relatório'
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

'''
Remove 0 columns in UTF-8 and Not UTF_8

df1 = df1[(df1['Contador: Total de cópias e impressões em preto e branco'] != 0) & (df1['Contador: Total de cópias e impressões em cores'] != 0)]
df1 = df1[(df1['Contador: Total de impressÃµes de cÃ³pias em preto e branco'] != 0) & (df1['Contador: Total de cÃ³pias e impressÃµes em cores'] != 0)]
'''

# Filter rows where both column X and column Y are not equal to 0
df1 = df1[(df1['Contador: Total de cópias e impressões em preto e branco'] != 0) & (df1['Contador: Total de cópias e impressões em cores'] != 0)]
df2 = df2[(df2['Contador: Total de cópias e impressões em preto e branco'] != 0) & (df2['Contador: Total de cópias e impressões em cores'] != 0)]
print("\nFiltered values with 0 in both .csvs!")

'''
Subtractions in UTF-8 and Not UTF_8

df1 = df1[(df1['Contador: Total de cópias e impressões em preto e branco'] != 0) & (df1['Contador: Total de cópias e impressões em cores'] != 0)]
df1 = df1[(df1['Contador: Total de impressÃµes de cÃ³pias em preto e branco'] != 0) & (df1['Contador: Total de cÃ³pias e impressÃµes em cores'] != 0)]
'''

# Create an empty DataFrame with desired columns
result_columns = [
    'Nome da Conta',
    'C: Diferença Total',
    'C: Diferença Só Cópias',
    'C: Diferença Só Impressões',
    'PB: Diferença Total',
    'PB: Diferença Só Cópias', 
    'PB: Diferença Só Impressões'
]
dfResult = pd.DataFrame(columns=result_columns)

# Perform subtraction of columns from df1 and df2
dfResult['Nome da Conta'] = df1['Nome da Conta']
#Cores
dfResult['C: Diferença Total'] = df2['Contador: Total de cópias e impressões em cores'] - df1['Contador: Total de cópias e impressões em cores']
dfResult['C: Diferença Só Cópias'] = df2['Contador: Total de impressões em cores'] - df1['Contador: Total de impressões em cores']
dfResult['C: Diferença Só Impressões'] = df2['Contador: Total de impressões de cópias em cores'] - df1['Contador: Total de impressões de cópias em cores']
#Preto e Branco
dfResult['PB: Diferença Total'] = df2['Contador: Total de cópias e impressões em preto e branco'] - df1['Contador: Total de cópias e impressões em preto e branco']
dfResult['PB: Diferença Só Cópias'] = df2['Contador: Total de impressões em preto e branco'] - df1['Contador: Total de impressões em preto e branco']
dfResult['PB: Diferença Só Impressões'] = df2['Contador: Total de impressões de cópias em preto e branco'] - df1['Contador: Total de impressões de cópias em preto e branco']
print("\nSubtracted values to new .csv!")

# Calculate the sum of each column
sum_row = dfResult[result_columns[1:]].sum().to_frame().T
sum_row['Nome da Conta'] = 'TOTAL'

# Append the sum row to the DataFrame
dfResult = pd.concat([dfResult, sum_row], ignore_index=True)


# Filter out users who didn't do any copies
dfResult = dfResult[(dfResult['C: Diferença Total'] != 0) | 
                    (dfResult['C: Diferença Só Cópias'] != 0) | 
                    (dfResult['C: Diferença Só Impressões'] != 0) | 
                    (dfResult['PB: Diferença Total'] != 0) | 
                    (dfResult['PB: Diferença Só Cópias'] != 0) | 
                    (dfResult['PB: Diferença Só Impressões'] != 0)]
print("\nSubtracted users with 0 copies this month.")


# Ask the user for the output file name
output_file_name = input("Enter the desired name for the output file (e.g., result.xlsx): ")


# TODO: CONFIRMAR SE ESTA A APAGAR EM CASOS EM QUE SÓ TEM UM 0 NUM DOS SITIOS

#print(result.columns)


# Save the modified DataFrame to an Excel file
dfResult.to_excel(folder_path + output_file_name, index=False)

print(f"\nGreat Success Bolachinha! \nCreated new Excel file called: {output_file_name}\n")