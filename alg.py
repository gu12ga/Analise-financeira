import pandas as pd

errors = []
rows = []

with open('indicadores-continuidade-coletivos-2020-2029.csv', 'rb') as fz:
    data = fz.readlines()

for row in data:
    try:
        decoded = row.decode('utf-8')
    except Exception as e:
        errors.append(row)
        continue

    # Assuming you want to replace 'Vrin' with an empty string and split by ';'
    cleaned_row = decoded.replace('Vrin', '').split(';')
    
    rows.append(cleaned_row)

#print('Errors:', len(errors))
#print('Rows:', len(rows))

clean_errors = []

for error in errors:
    row = ''.join(chr(i) for i in error[:-2])
    clean_errors.append(row.split(';'))

#print('Number of cleaned errors:', len(clean_errors))
#print('First cleaned error:', clean_errors[0])

columns = rows.pop(0)

print(columns)

df = pd.DataFrame(data=clean_errors, columns=columns)
print(df)
