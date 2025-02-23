# Crawler d'Offres d'Emploi BOSS Direct et Générateur PDF

[简体中文](../README.md) | [English](README_en.md) | [日本語](README_ja.md) | [Français](README_fr.md) | [Deutsch](README_de.md)

Un programme Python qui extrait automatiquement les informations d'emploi du site BOSS Direct et génère des rapports PDF formatés.

## Fonctionnalités

- Extraction automatique des offres d'emploi de BOSS Direct
- Prise en charge des critères de recherche personnalisés (poste, ville, pages)
- Sauvegarde des données brutes au format JSON
- Génération de rapports PDF élégants
- Prise en charge de l'affichage en chinois
- Pagination automatique
- Inclut le titre du poste, l'entreprise, le salaire, l'emplacement et d'autres informations

## Configuration Requise

- Python 3.7+
- Navigateur Chrome (pour l'extraction web)
- macOS/Linux/Windows

## Étapes d'Installation

1. Clonez ou téléchargez ce projet localement

2. Créez et activez un environnement virtuel (recommandé) :
```bash
# Créer un environnement virtuel
python -m venv .venv

# Activer l'environnement virtuel
# Windows :
.venv\Scripts\activate
# macOS/Linux :
source .venv/bin/activate
```

3. Installez les dépendances :
```bash
pip install -r requirements.txt
```

4. Configuration des polices chinoises (si le PDF affiche des caractères illisibles) :

Pour les utilisateurs macOS :
- Le système inclut généralement les polices chinoises requises
- En cas de problème, téléchargez et installez Source Han Sans :
```bash
curl -O https://github.com/adobe-fonts/source-han-sans/raw/release/OTF/SimplifiedChinese/SourceHanSansSC-Regular.otf
```

Pour les utilisateurs Windows :
- Assurez-vous que les polices chinoises sont installées (comme Microsoft YaHei ou SimSun)
- Ou téléchargez et installez Source Han Sans

Pour les utilisateurs Linux :
```bash
# Ubuntu/Debian :
sudo apt-get install fonts-wqy-microhei

# CentOS/RHEL :
sudo yum install wqy-microhei-fonts
```

## Utilisation

1. Exécutez le programme d'extraction :
```bash
python main.py
```

2. Saisissez les critères de recherche comme demandé :
```
Veuillez saisir le titre du poste à rechercher : Ingénieur Python
Veuillez saisir le code de la ville (ex : Pékin 101010100, par défaut Pékin) : [Entrée pour la valeur par défaut]
Veuillez saisir le nombre maximum de pages à extraire (par défaut 5) : [Entrée pour la valeur par défaut]
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
   - Format du nom de fichier : `titre-poste_code-ville_jobs_horodatage.json`
   - Exemple : `IngenieurPython_101010100_jobs_20240223_172956.json`

2. Rapport PDF : rapport d'information d'emploi formaté
   - Format du nom de fichier : `titre-poste_code-ville_jobs_horodatage.pdf`
   - Exemple : `IngenieurPython_101010100_jobs_20240223_172956.pdf`

## Contenu du Rapport PDF

Le rapport PDF généré comprend :
- Page de titre : affiche "Rapport d'Informations d'Emploi"
- Statistiques : montre le nombre total d'emplois trouvés
- Détails des emplois :
  - Titre du poste (surligné en bleu)
  - Nom de l'entreprise
  - Fourchette de salaire
  - Lieu de travail

## Remarques

1. Notes sur l'utilisation du crawler :
   - Il est recommandé d'avoir des intervalles entre chaque extraction
   - Évitez les extractions massives fréquentes
   - Il est recommandé d'utiliser la limite par défaut de 5 pages

2. Notes sur la génération PDF :
   - Assurez-vous que les polices chinoises sont installées
   - Les fichiers PDF sont automatiquement paginés
   - Prend en charge le chinois et les caractères spéciaux

3. Problèmes possibles :
   - Si un CAPTCHA apparaît, veuillez réessayer plus tard
   - Si le PDF affiche des caractères illisibles, suivez les instructions d'installation des polices ci-dessus
   - Si la connexion réseau échoue, vérifiez les paramètres réseau

## Plans de Développement

- [ ] Ajouter la prise en charge de plus de critères de recherche
- [ ] Optimiser le style des rapports PDF
- [ ] Ajouter des fonctionnalités d'analyse de données
- [ ] Prendre en charge l'exportation vers plus de formats

## Directives de Contribution

N'hésitez pas à soumettre des Issues et des Pull Requests pour aider à améliorer ce projet.

## Licence

Licence MIT 