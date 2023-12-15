import pandas

file = pandas.read_csv('data.txt')
txt_data = file.values.tolist()

"""Kurā gadā bija dibināts vecākais Omānas reģiona uzņēmums (informācija ir pieejama kolonnā Founded)?"""
founded = []
for row in txt_data:
    if row[4] == 'Oman':
        founded.append(row[6])
print(f'1.uzdevums: {min(founded)}')


"""Kāds ir darbinieku skaits, kas strādā Latvijā?"""
worker_count = 0
for row in txt_data:
    if row[4] == 'Latvia':
        worker_count += 1
print(f'2.uzdevums: {worker_count}')


"""Kāds ir darbinieku skaits kas strādā telekomunikācijas jomā Latvijā.  (Industry = Telecommunications, Country = Latvia) ?"""
worker_count = 0
for row in txt_data:
    if row[7] == 'Telecommunications' and row[4] == 'Latvia':
        worker_count += 1
print(f'3.uzdevums: {worker_count}')


"""Cik no datu bāze esošajiem Latvijas kompānijām ir SSL sertifikāts? (SSL sertifikāts ir kompānijām, kuram tīmekļa adrese sākas ar https://)"""
company_site = []
for row in txt_data:
    if row[4] == 'Latvia':
        company_site.append(row[3])

count = 0
for i in company_site:
    if i[0:5] == 'https':
        count += 1
print(f'4.uzdevums {count}')


"""Cik reizes datu bāzē tiek minēts domēna vārds .org reģionam Latvia?"""
site = []
for row in txt_data:
    if row[4] == 'Latvia':
        site.append(row[3])

count = 0
for i in site:
    if i[-5:-1] == '.org':
        count += 1
print(f'5.uzdevums {count}')