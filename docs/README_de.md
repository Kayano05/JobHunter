# BOSS Direct Stelleninformationen Crawler und PDF-Generator

[简体中文](../README.md) | [English](README_en.md) | [日本語](README_ja.md) | [Français](README_fr.md) | [Deutsch](README_de.md)

Dies ist ein Python-Programm, das automatisch Stelleninformationen von der BOSS Direct Website crawlt und formatierte PDF-Berichte generiert.

## Funktionen

- Automatisches Crawlen von BOSS Direct Stelleninformationen
- Unterstützung für benutzerdefinierte Suchkriterien (Position, Stadt, Seiten)
- Speicherung der Rohdaten im JSON-Format
- Generierung schöner PDF-Berichte
- Unterstützung für chinesische Anzeige
- Automatische Seitennummerierung
- Enthält Stellenbezeichnung, Unternehmen, Gehalt, Standort und weitere Informationen

## Systemanforderungen

- Python 3.7+
- Chrome Browser (für Web-Crawling)
- macOS/Linux/Windows
- Netzwerkumgebung mit Zugriff auf Google-Dienste (VPN erforderlich in Festland-China, da das Programm von ChromeDriver-Download abhängig ist)

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

3. Abhängigkeiten installieren:
```bash
pip install -r requirements.txt
```

4. Chinesische Schriftarten-Einstellungen (falls chinesische Zeichen im PDF nicht korrekt angezeigt werden):

Für macOS-Benutzer:
- Das System enthält normalerweise die erforderlichen chinesischen Schriftarten
- Bei fehlerhafter Darstellung Source Han Sans herunterladen und installieren:
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

1. Crawler-Programm ausführen:
```bash
python main.py
```

2. Suchkriterien gemäß den Aufforderungen eingeben:
```
Bitte geben Sie die zu suchende Stellenbezeichnung ein: Python Entwickler
Bitte geben Sie den Stadtcode ein (z.B. Peking 101010100, Standard ist Peking): [Enter für Standardwert]
Bitte geben Sie die maximale Seitenzahl zum Crawlen ein (Standard ist 5): [Enter für Standardwert]
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
   - Dateinamenformat: `stellenbezeichnung_stadtcode_jobs_zeitstempel.json`
   - Beispiel: `Python Entwickler_101010100_jobs_20240223_172956.json`

2. PDF-Bericht: formatierter Stelleninformationsbericht
   - Dateinamenformat: `stellenbezeichnung_stadtcode_jobs_zeitstempel.pdf`
   - Beispiel: `Python Entwickler_101010100_jobs_20240223_172956.pdf`

## PDF-Berichtsinhalt

Der generierte PDF-Bericht enthält:
- Titelseite: zeigt "Stelleninformationsbericht"
- Statistiken: zeigt die Gesamtzahl der gefundenen Stellen
- Stellendetails:
  - Stellenbezeichnung (blau hervorgehoben)
  - Firmenname
  - Gehaltsbereich
  - Arbeitsort

## Wichtige Hinweise

1. Hinweise zur Netzwerkumgebung:
   - Das Programm muss beim Start ChromeDriver herunterladen, was Zugriff auf Google-Server erfordert
   - Wenn Sie es in Festland-China verwenden, stellen Sie sicher, dass Sie auf Google-Dienste zugreifen können (z.B. durch Verwendung eines VPN)
   - Das Programm wird ohne Zugriff auf Google-Dienste nicht ordnungsgemäß starten und ausgeführt werden können

2. Hinweise zur Crawler-Nutzung:
   - Es wird empfohlen, Intervalle zwischen den Crawl-Vorgängen einzuhalten
   - Vermeiden Sie häufiges massenhaftes Crawlen
   - Es wird empfohlen, das Standard-Limit von 5 Seiten zu verwenden

3. Hinweise zur PDF-Generierung:
   - Stellen Sie sicher, dass chinesische Schriftarten im System installiert sind
   - PDF-Dateien werden automatisch paginiert
   - Unterstützt Chinesisch und Sonderzeichen

4. Mögliche Probleme:
   - Wenn ein CAPTCHA erscheint, versuchen Sie es später erneut
   - Wenn chinesische Zeichen im PDF nicht korrekt angezeigt werden, folgen Sie den obigen Anweisungen zur Schriftarteninstallation
   - Bei Netzwerkverbindungsproblemen überprüfen Sie die Netzwerkeinstellungen
   - Wenn der ChromeDriver-Download fehlschlägt, überprüfen Sie, ob Sie auf Google-Dienste zugreifen können

## Entwicklungsplan

- [ ] Weitere Suchkriterien-Unterstützung hinzufügen
- [ ] PDF-Berichtsstil optimieren
- [ ] Datenanalysefunktionen hinzufügen
- [ ] Export in weitere Formate unterstützen

## Beitragsrichtlinien

Sie sind herzlich eingeladen, Issues und Pull Requests einzureichen, um dieses Projekt zu verbessern.

## Lizenz

MIT-Lizenz 