from schema import get_all_company
import pandas as pd
accounts = get_all_company()
print(len(accounts))
lists = {}
for i in accounts:
    lists.setdefault(i.Tax_code, i.to_string())
list_ex = []
for acc in lists.items():
    list_ex.append(acc[1])
# #
df = pd.DataFrame(list_ex)

df = pd.DataFrame(list_ex, columns=['Tax_code', 'Link', 'Company_name', 'Trading_name', 'Issued_date', 'Status', 'Registered_office',
                  'Address', 'Commune', 'District', 'Provincial', 'Head_office_address', 'Owner', 'Director', 'Business_lines', 'Note'])
df.to_excel("company_DONGNAI_27042023.xlsx",
            sheet_name='Page')
