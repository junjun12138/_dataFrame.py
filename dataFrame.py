import pandas as pd 


table_b_path = "B.xlsx" 
df_b = pd.read_excel(table_b_path,sheet_name="Sheet1")

colum_b_2= df_b.iloc[:,2]

colum_b_3= df_b.iloc[:,3]


colum_b_4= df_b.iloc[:,4]

df_combined = pd.DataFrame({
    'column_2': colum_b_2,
    'column_3': colum_b_3,
    'column_4': colum_b_4
})
df_combine = df_combined[['column_2','column_3','column_4']]
df_combined.reset_index(drop=True, inplace=True)
df_combined.to_excel("combined_table.xlsx",sheet_name="Sheet1",index=False)
print("done")
