import csv
import json

fechas = {}

fieldNames = []

with open('bvc.csv') as csvfile:
  readCSV = csv.reader(csvfile, delimiter=',')
  for row in readCSV:
    fecha = row[0].strip()
    nemo= row[1].strip()
    razonSocial = row[2].strip()
    volumen = row[3].strip()
    if fecha.endswith("02/2016"):
      if fecha not in fechas:
        fechas[fecha] = {}
      f = fechas[fecha]

      if nemo not in fieldNames:
        fieldNames.append(nemo)

      f[nemo] = volumen

with open('names.csv', 'w') as csvfile:
  fieldNames.append('year')
  writer = csv.DictWriter(csvfile, fieldnames=fieldNames)
  writer.writeheader()
  for key in fechas:
    row = {}
    for fn in fieldNames:
      if fn != 'year':
        row[fn] = fechas[key][fn]
    row['year'] = key
    writer.writerow(row)