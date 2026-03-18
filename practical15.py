import pandas as pd
from tabulate import tabulate

file = "sample_excel.xlsx"  
df = pd.read_excel(file)

print(tabulate(df, headers="keys", tablefmt="grid", showindex=False))