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

# Ensure the 'Nome da Conta' column exists in both DataFrames
if 'Nome da Conta' not in df1.columns or 'Nome da Conta' not in df2.columns:
    raise ValueError("Both CSV files must contain the 'Nome da Conta' column.")

# Merge the two DataFrames on 'Nome da Conta'
df_merged = pd.merge(df1, df2, on='Nome da Conta', suffixes=('_prev', '_curr'))

print(df_merged)

# List of columns you want to delete from both DataFrames
columns_to_delete = [
    'ID da Conta', 'Tipo de Conta', 'Limite: Limite de Cópia em Cores', 
    'Limite: Cópias em Cores usadas', 'Limite: Cópias em Cores Remanescentes',
    'Subcontador: Impressões de cópias grandes em cores', 'Limite: Limite de Cópias em Preto e Branco',
    'Limite: Cópias em Preto e Branco usadas', 'Limite: Cópias em Preto e Branco remanescentes',
    'Subcontador: Impressões de cópias grandes em P/B', 'Limite: Limite de Impressões em Cores',
    'Limite: Impressões em Cores usadas', 'Limite:Impressões em Cores Remanescentes',
    'Subcontador: Impressões grandes em cores', 'Limite: Limite de Impressões em Preto e Branco',
    'Limite: Impressões em Preto e Branco usadas', 'Limite: Impressões em Preto e Branco remanescentes',
    'Subcontador: Impressões grandes em preto e branco', 'Última Reinicialização', 
    'Número de série da máquina', 'Data do Relatório', 'Hora do Relatório'
]

# Drop the columns from the merged DataFrame
df_merged.drop(columns=[col + '_prev' for col in columns_to_delete] + [col + '_curr' for col in columns_to_delete], inplace=True)
print("\nDropped Columns in merged DataFrame!")

# Save the modified DataFrame to an Excel file
#df_merged.to_excel("df_filtered.xlsx", index=False)


# Create an empty DataFrame with desired columns
result_columns = [
    'Nome da Conta', 'C: Diferença Total', 'C: Diferença Só Cópias', 'C: Diferença Só Impressões',
    'PB: Diferença Total', 'PB: Diferença Só Cópias', 'PB: Diferença Só Impressões'
]

dfResult = pd.DataFrame(columns=result_columns)

# Perform subtraction of columns from df1 and df2
dfResult['Nome da Conta'] = df_merged['Nome da Conta']
# Cores
dfResult['C: Diferença Total'] = df_merged['Contador: Total de cópias e impressões em cores_curr'] - df_merged['Contador: Total de cópias e impressões em cores_prev']
dfResult['C: Diferença Só Cópias'] = df_merged['Contador: Total de impressões em cores_curr'] - df_merged['Contador: Total de impressões em cores_prev']
dfResult['C: Diferença Só Impressões'] = df_merged['Contador: Total de impressões de cópias em cores_curr'] - df_merged['Contador: Total de impressões de cópias em cores_prev']
# Preto e Branco
dfResult['PB: Diferença Total'] = df_merged['Contador: Total de cópias e impressões em preto e branco_curr'] - df_merged['Contador: Total de cópias e impressões em preto e branco_prev']
dfResult['PB: Diferença Só Cópias'] = df_merged['Contador: Total de impressões em preto e branco_curr'] - df_merged['Contador: Total de impressões em preto e branco_prev']
dfResult['PB: Diferença Só Impressões'] = df_merged['Contador: Total de impressões de cópias em preto e branco_curr'] - df_merged['Contador: Total de impressões de cópias em preto e branco_prev']
print("\nSubtracted values to new DataFrame!")



# Filter out rows with any negative values
dfResult = dfResult[
    (dfResult['C: Diferença Total'] >= 0) & 
    (dfResult['C: Diferença Só Cópias'] >= 0) & 
    (dfResult['C: Diferença Só Impressões'] >= 0) & 
    (dfResult['PB: Diferença Total'] >= 0) & 
    (dfResult['PB: Diferença Só Cópias'] >= 0) & 
    (dfResult['PB: Diferença Só Impressões'] >= 0)
]
print("\nFiltered out rows with negative values.")

# Filter out rows where all relevant columns are 0
dfResult = dfResult[
    (dfResult['C: Diferença Total'] != 0) | 
    (dfResult['C: Diferença Só Cópias'] != 0) | 
    (dfResult['C: Diferença Só Impressões'] != 0) | 
    (dfResult['PB: Diferença Total'] != 0) | 
    (dfResult['PB: Diferença Só Cópias'] != 0) | 
    (dfResult['PB: Diferença Só Impressões'] != 0)
]
print("\nFiltered out rows with all zero values.")


# Calculate the sum of each column
sum_row = dfResult[result_columns[1:]].sum().to_frame().T
sum_row['Nome da Conta'] = 'TOTAL'

# Append the sum row to the DataFrame
dfResult = pd.concat([dfResult, sum_row], ignore_index=True)

print(dfResult)

# Ask the user for the output file name
output_file_name = input("Enter the desired name for the output file (e.g., result.xlsx): ")

# Save the modified DataFrame to an Excel file
dfResult.to_excel(folder_path + output_file_name, index=False)

print(f"\nGreat Success! Created new Excel file called: {output_file_name}\n")
