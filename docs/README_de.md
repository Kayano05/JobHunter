# BOSS Direct Stelleninformationen Crawler und PDF-Generator

[简体中文](../README.md) | [English](README_en.md) | [日本語](README_ja.md) | [Français](README_fr.md) | [Deutsch](README_de.md)

Ein Python-Programm, das automatisch Stelleninformationen von der BOSS Direct-Website crawlt und formatierte PDF-Berichte generiert.

## Funktionen

- Automatisches Crawlen von BOSS Direct Stelleninformationen
- Unterstützung für benutzerdefinierte Suchkriterien (Position, Stadt, Seiten)
- Speicherung der Rohdaten im JSON-Format
- Generierung schöner PDF-Format-Berichte
- Unterstützung für chinesische Zeichendarstellung
- Automatische Seitenumbrüche
- Enthält Stellenbezeichnung, Unternehmen, Gehalt, Standort und weitere Informationen

## Systemanforderungen

- Python 3.7+
- Chrome-Browser (für Web-Crawling)
- macOS/Linux/Windows

## Installationsschritte

1. Klonen oder laden Sie dieses Projekt lokal herunter

2. Erstellen und aktivieren Sie eine virtuelle Umgebung (empfohlen):
```bash
# Virtuelle Umgebung erstellen
python -m venv .venv

# Virtuelle Umgebung aktivieren
# Windows:
.venv\Scripts\activate
# macOS/Linux:
source .venv/bin/activate
```

3. Installieren Sie die Abhängigkeiten:
```bash
pip install -r requirements.txt
```

4. Chinesische Schriftarten-Einstellungen (falls PDF unleserliche Zeichen anzeigt):

Für macOS-Benutzer:
- Das System enthält normalerweise die erforderlichen chinesischen Schriftarten
- Bei Problemen laden Sie Source Han Sans herunter und installieren Sie es:
```bash
curl -O https://github.com/adobe-fonts/source-han-sans/raw/release/OTF/SimplifiedChinese/SourceHanSansSC-Regular.otf
```

Für Windows-Benutzer:
- Stellen Sie sicher, dass chinesische Schriftarten installiert sind (wie Microsoft YaHei oder SimSun)
- Oder laden Sie Source Han Sans herunter und installieren Sie es

Für Linux-Benutzer:
```bash
# Ubuntu/Debian:
sudo apt-get install fonts-wqy-microhei

# CentOS/RHEL:
sudo yum install wqy-microhei-fonts
```

## Verwendung

1. Führen Sie das Crawler-Programm aus:
```bash
python main.py
```

2. Geben Sie die Suchkriterien wie aufgefordert ein:
```
Bitte geben Sie den zu suchenden Stellentitel ein: Python Entwickler
Bitte geben Sie den Stadtcode ein (z.B. Peking 101010100, Standard ist Peking): [Enter für Standardwert]
Bitte geben Sie die maximale Anzahl der zu crawlenden Seiten ein (Standard ist 5): [Enter für Standardwert]
```

3. Häufige Stadtcodes:
- Peking: 101010100
- Shanghai: 101020100
- Guangzhou: 101280100
- Shenzhen: 101280600
- Hangzhou: 101210100
- Chengdu: 101270100

## Ausgabedateien

Das Programm generiert zwei Dateien:

1. JSON-Datei: enthält Rohdaten
   - Dateinamenformat: `Stellentitel_Stadtcode_jobs_Zeitstempel.json`
   - Beispiel: `PythonEntwickler_101010100_jobs_20240223_172956.json`

2. PDF-Bericht: formatierter Stelleninformationsbericht
   - Dateinamenformat: `Stellentitel_Stadtcode_jobs_Zeitstempel.pdf`
   - Beispiel: `PythonEntwickler_101010100_jobs_20240223_172956.pdf`

## PDF-Berichtsinhalt

Der generierte PDF-Bericht enthält:
- Titelseite: zeigt "Stelleninformationsbericht"
- Statistiken: zeigt die Gesamtzahl der gefundenen Stellen
- Stellendetails:
  - Stellentitel (blau hervorgehoben)
  - Firmenname
  - Gehaltsbereich
  - Arbeitsort

## Hinweise

1. Hinweise zur Crawler-Nutzung:
   - Es wird empfohlen, Intervalle zwischen den Crawls einzuhalten
   - Vermeiden Sie häufiges Massen-Crawling
   - Es wird empfohlen, das Standard-5-Seiten-Limit zu verwenden

2. Hinweise zur PDF-Generierung:
   - Stellen Sie sicher, dass chinesische Schriftarten installiert sind
   - PDF-Dateien werden automatisch paginiert
   - Unterstützt Chinesisch und Sonderzeichen

3. Mögliche Probleme:
   - Wenn ein CAPTCHA erscheint, versuchen Sie es später erneut
   - Wenn das PDF unleserliche Zeichen anzeigt, folgen Sie den obigen Schriftarten-Installationsanweisungen
   - Bei Netzwerkverbindungsproblemen überprüfen Sie die Netzwerkeinstellungen

## Entwicklungspläne

- [ ] Unterstützung für weitere Suchkriterien hinzufügen
- [ ] PDF-Berichtsstil optimieren
- [ ] Datenanalysefunktionen hinzufügen
- [ ] Export in weitere Formate unterstützen

## Beitragsrichtlinien

Sie sind herzlich eingeladen, Issues und Pull Requests einzureichen, um dieses Projekt zu verbessern.

## Lizenz

MIT-Lizenz 