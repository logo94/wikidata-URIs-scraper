![](https://img.shields.io/badge/OS-Linux-blueviolet.svg)
[![it](https://img.shields.io/badge/lang-it-blue.svg)](https://github.com/logo94/excel2text-key/blob/main/README.md)
![](https://img.shields.io/badge/Python-3.8%2B-green.svg)


# wikidata-URIs-scraper

Scritto a supporto della preparazione di un vocabolario completo per l'addestramento di Annif, software per l'indicizzazione automatica per soggetto di testi; partendo da un foglio di calcolo, lo scraper automatizza la procedura lato web browser di ricerca di ogni termine, riga per riga, su Wikipedia o Wikidata. 

Per riprodurre un vocabolario strutturato secondo la forma supportata da Annif, l'URI di ogni Elemento Wikidata trovato viene copiato, per la stessa riga del foglio di calcolo, nella colonna precedente rispetto al termine ricercato.   

>L'automazione avviene esclusivamente lato client, l'attività di scraping non riuslta quindi invasiva.

## Installazione ##
Per l'utilizzo degli scripts è necessario aver scaricato `Python 3.8+` sul proprio dispositivo, per installare Python seguire le istruzioni riportate al seguente [link](https://www.python.org/downloads/).

Una volta eseguito il download è possibile verificare le versioni di `Python` e `pip` tramite i comandi:

```
python --version
```
```
pip --version
```

### Ambiente virtuale ###
Per non compromettere l'installazione di Python e le relative librerie è consigliabile creare un ambiente virtuale indipendente dal proprio sistema; per la creazione di un ambiente virtuale procedere come segue:

Creare l'ambiente virtuale
```
python3 -m venv pyenv
```

Attivare l'ambiente virtuale:
```
source pyenv/bin/activate
```

### Librerie ###
Una volta attivato l'ambiente virtuale è possibile procedere con l'installazione delle librerie necessarie:

```
pip install openpyxl
```
```
pip install selenium
```
```
pip install webdriver-manager
```

## Preparazione ##
Il foglio di calcolo di partenza deve essere così strutturato:

* **Colonna 1**: vuota; 
* **Colonna 2**: termine da ricercare per l'ottenimento del relativo URI 

## Utilizzo ##
Una volta scaricate le librerie necessarie e scaricato il repository, per avviare lo script sarà sufficiente eseguire il comando:
```
python3 wikipedia.py
```
Ogni termine viene ricercato su Wikipedia, se il termine ricercato coincide esattamente con il nome della voce Wikipedia, viene seguito il link che rimanda al relativo elemento Wikidata e l'URI viene copiato all'interno del foglio di calcolo tra parentesi uncinate `<` `>`

oppure

```
python3 wikidata.py
```
Ogni termine viene ricercato su Wikidata, se il termine ricercato esiste, viene selezionara la prima voce dell'elenco e il relativo URI viene copiato all'interno del foglio di calcolo tra parentesi uncinate `<` `>`. 

>wikidata.py non è in grado di gestire automaticamente la selezione del termine perfettamente coincidente, seleziona invece il primo termine proposto da Wikidata, è quindi necessaria una supervisione.
