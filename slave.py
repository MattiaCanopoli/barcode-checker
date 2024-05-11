listaBarcode = [] #lista in cui inserire i barcode da input

dbList=[] #lista per database barcode


#importa un csv con elenco di barcode

import csv

#aggiunge tutti i barcode del file alla lista dbList
with  open("csv/db-barcode.csv", mode='r') as dbBarcode:
    csv_reader = csv.reader(dbBarcode,delimiter=";")
    valore=True
    for riga in csv_reader:
        if valore:
            #saltiamo la prima riga, quella di intestazione
            valore = False
            continue
        dbList.append(riga[0])

# print(dbList)

def aggiuntaBarcode():
    #inserire if che verifica che il barcode inserito sia nel csv importato. se true appende barcode alla lista, se false restiuisce messaggio di errore
    bcode = (input('inserisci barcode\n')) #aggiunge barcode da input. inserire in funzione richiamata ad ogni inserimento
    if bcode in dbList:
        listaBarcode.append(bcode)
    else:
        print('barcode sconosciuto')


def creaFile():
    if listaBarcode:
        nomeFile= 'output file/' + input('come vuoi chiamare il file?\n') + '.txt' #richiede il nome file all'utente
        file=open(nomeFile,'w') #crea il file con il nome scelto
        
        #scrive tutti i barcode salvati in lista barcode nel nuovo file
        for barcode in listaBarcode:
            file=open(nomeFile, 'a')
            file.write(barcode)
            file.write('\n') 
        file.close()
        #stampa messaggio di avvenuta scrittura del file
        print('file ' + nomeFile + ' creato')
    else:
        print('nessun barcode da salvare')
