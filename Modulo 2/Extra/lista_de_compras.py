import csv

with open('lista_de_compras.tsv','w', newline='', encoding='utf-8') as csvFile:
    csvWriter = csv.writer(csvFile,delimiter='\t',lineterminator='\n')  

    csvWriter.writerow(['maçãs','bananas','morangos'])
    csvWriter.writerow(['leite','iogurte','queijo'])
    csvWriter.writerow(['sabão','detergente','esponja'])