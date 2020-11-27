# DB Analyse for DB Tracker
Dies ist das Tool zum Auswerten der erstellten Datenbank in dem Projekt DB Tracker

## Requirements
- Python3.8 or greater
- SOON

## Instalation
Git Repo Downloaden
```shell
git clone <GIT-ROPOSITORY>
```
In den Gedownloadeten Ordner Navigieren
```
cd DB_Analyse
```

## Usage
### Sample
Um die Instalation zu Prüfen die Main.py ausführen
```shell 
python Main.py
```

### CLI
In der Commandline die Main Datei importieren
```python
import Main
```

Danach inizialisieren
```python
data = Main.init()
```

Datenbankbefehle direkt ausführen
```python
data._execute("SQL COMMAND")
```