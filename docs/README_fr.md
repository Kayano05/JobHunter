# Crawler d'Informations d'Emploi BOSS Direct et Générateur PDF

[简体中文](../README.md) | [English](README_en.md) | [日本語](README_ja.md) | [Français](README_fr.md) | [Deutsch](README_de.md)

C'est un programme Python qui extrait automatiquement les informations d'emploi du site web BOSS Direct et génère des rapports PDF formatés.

## Caractéristiques

- Extraction automatique des informations d'emploi de BOSS Direct
- Prise en charge des conditions de recherche personnalisées (poste, ville, pages)
- Sauvegarde des données brutes au format JSON
- Génération de rapports PDF élégants
- Prise en charge de l'affichage en chinois
- Pagination automatique
- Inclut le titre du poste, l'entreprise, le salaire, l'emplacement et d'autres informations

## Exigences Système

- Python 3.7+
- Navigateur Chrome (pour l'extraction web)
- macOS/Linux/Windows
- Environnement réseau pouvant accéder aux services Google (VPN requis en Chine continentale car le programme dépend du téléchargement de ChromeDriver)

## Étapes d'Installation

1. Cloner ou télécharger ce projet localement

2. Créer et activer un environnement virtuel (recommandé) :
```bash
# Créer un environnement virtuel
python -m venv .venv

# Activer l'environnement virtuel
# Windows:
.venv\Scripts\activate
# macOS/Linux:
source .venv/bin/activate
```

3. Installer les dépendances :
```bash
pip install -r requirements.txt
```

4. Configuration des polices chinoises (si l'affichage chinois est incorrect dans le PDF) :

Pour les utilisateurs macOS :
- Le système inclut généralement les polices chinoises requises
- Si des caractères sont incorrects, télécharger et installer Source Han Sans :
```bash
curl -O https://github.com/adobe-fonts/source-han-sans/raw/release/OTF/SimplifiedChinese/SourceHanSansSC-Regular.otf
```

Pour les utilisateurs Windows :
- S'assurer que les polices chinoises sont installées (comme Microsoft YaHei ou SimSun)
- Ou télécharger et installer Source Han Sans

Pour les utilisateurs Linux :
```bash
# Ubuntu/Debian:
sudo apt-get install fonts-wqy-microhei

# CentOS/RHEL:
sudo yum install wqy-microhei-fonts
```

## Utilisation

1. Exécuter le programme d'extraction :
```bash
python main.py
```

2. Entrer les conditions de recherche selon les invites :
```
Veuillez entrer le titre du poste à rechercher : Ingénieur Python
Veuillez entrer le code de la ville (ex : Pékin 101010100, par défaut Pékin) : [Appuyez sur Entrée pour utiliser la valeur par défaut]
Veuillez entrer le nombre maximum de pages à extraire (par défaut 5) : [Appuyez sur Entrée pour utiliser la valeur par défaut]
```

3. Codes de ville courants :
- Pékin : 101010100
- Shanghai : 101020100
- Guangzhou : 101280100
- Shenzhen : 101280600
- Hangzhou : 101210100
- Chengdu : 101270100

## Fichiers de Sortie

Le programme génère deux fichiers :

1. Fichier JSON : contient les données brutes
   - Format du nom de fichier : `titre_poste_code_ville_jobs_horodatage.json`
   - Exemple : `Ingénieur Python_101010100_jobs_20240223_172956.json`

2. Rapport PDF : rapport d'informations d'emploi formaté
   - Format du nom de fichier : `titre_poste_code_ville_jobs_horodatage.pdf`
   - Exemple : `Ingénieur Python_101010100_jobs_20240223_172956.pdf`

## Contenu du Rapport PDF

Le rapport PDF généré comprend :
- Page de titre : affiche "Rapport d'Informations d'Emploi"
- Statistiques : montre le nombre total d'emplois trouvés
- Détails des emplois :
  - Titre du poste (mis en évidence en bleu)
  - Nom de l'entreprise
  - Fourchette de salaire
  - Lieu de travail

## Notes Importantes

1. Notes sur l'Environnement Réseau :
   - Le programme doit télécharger ChromeDriver au démarrage, ce qui nécessite l'accès aux serveurs Google
   - Si vous l'utilisez en Chine continentale, assurez-vous de pouvoir accéder aux services Google (par exemple, en utilisant un VPN)
   - Le programme ne démarrera pas et ne fonctionnera pas correctement sans accès aux services Google

2. Notes sur l'Utilisation du Crawler :
   - Il est recommandé d'avoir des intervalles entre chaque extraction
   - Éviter les extractions massives fréquentes
   - Il est recommandé d'utiliser la limite par défaut de 5 pages

3. Notes sur la Génération PDF :
   - S'assurer que les polices chinoises sont installées dans le système
   - Les fichiers PDF seront automatiquement paginés
   - Prend en charge le chinois et les caractères spéciaux

4. Problèmes Possibles :
   - Si un CAPTCHA apparaît, veuillez réessayer plus tard
   - Si les caractères chinois sont incorrects dans le PDF, suivez les instructions d'installation des polices ci-dessus
   - Si la connexion réseau échoue, vérifiez les paramètres réseau
   - Si le téléchargement de ChromeDriver échoue, vérifiez si vous pouvez accéder aux services Google

## Plan de Développement

- [ ] Ajouter plus de support pour les conditions de recherche
- [ ] Optimiser le style des rapports PDF
- [ ] Ajouter des fonctionnalités d'analyse de données
- [ ] Prendre en charge l'exportation vers plus de formats

## Guide de Contribution

Bienvenue pour soumettre des Issues et des Pull Requests pour aider à améliorer ce projet.

## Licence

Licence MIT 