Ce projet répond aux exigences, aux restrictions et à des consignes d'un travail demandé dans le cadre d'un cours.

# Projet : Développement d'un moteur à base de règles pour la segmentation en chunks

Ce projet consiste à développer un moteur à base de règles (MBR) pour segmenter un texte brut en chunks. Il a été réalisé dans le cadre d'un cours **Formalismes pour le TAL** en avril 2024.
Ce chunker a été réalisée sur la base d'[un texte spécifique](https://www.legorafi.fr/2024/01/23/il-meurt-de-vieillesse-en-tentant-de-fermer-tous-les-onglets-ouverts-par-ses-parents/) venant du Gorafi (texte.txt). **Nos règles et nos lexiques ont été construits sur la base spécifique de ce texte.** Nous avons testé ce moteur sur [un autre texte](https://www.legorafi.fr/2023/09/19/astrologie-mercure-percute-accidentellement-un-semi-remorque-sur-la6-en-retrogradant-trop-tot/) du Gorafi (texte_test.txt).

## Fonctionnalités

- **Tokenisation** : Segmentation du texte en unités basée sur des règles et un lexique.
- **Segmentation en chunks** : Application de règles morphosyntaxiques pour regrouper les tokens en chunks.
- **Évaluation des performances** : Calcul de la précision, du rappel et de la F-mesure.


## Structure du projet

### 1. Formalismes

#### Linguistique

Un chunk est défini comme une portion de phrase naturelle à l'oral. Chaque chunk contient une "tête" (mot lexical) entouré de mots grammaticaux. La ponctuation est traitée comme des chunks séparés.

#### Traitement

Les étapes principales du traitement sont :
1. **Tokenisation** du texte brut.
2. **Association des catégories morphosyntaxiques** aux tokens via un lexique.
3. **Application des règles** pour déterminer les chunks.
4. **Écriture du résultat** dans un fichier 'chunks.txt'.
5. **Évaluation des performances** via comparaison avec une référence manuelle.

#### Règles

Le moteur applique 11 règles basées sur :
- Les catégories morphosyntaxiques.
- Les combinaisons de tokens successifs.
- Des motifs morphologiques (regex).

#### Lexique

Le lexique contient des mots grammaticaux classés par catégories (PRON, DET, PUNCT, etc.).


### 2. Expérimentations

Deux textes ont été testés :
1. **Texte initial** :
   - Précision : 75%
   - Rappel : 10%
   - F-mesure : 18%
   - Problème principal : Surdécoupage causé par des règles trop générales.

2. **Second texte** :
   - Avec le lexique initial : F-mesure de 3%.
   - Avec un lexique enrichi :
     - Précision : 80%
     - Rappel : 8%
     - F-mesure : 16%.
   - Problème : Catégories de chunks limitées.


### 3. Pistes d'amélioration

#### Limites

- Surdécoupage des chunks.
- Non-reconnaissance de certains types de chunks (SV, SVc, etc.).
- Règles et lexique trop simples.

#### Améliorations possibles

1. Ajout de règles spécifiques basées sur le contexte.
2. Extension du lexique pour inclure des verbes et noms communs.
3. Révision des règles existantes pour éviter le surdécoupage.


## Textes utilisés 

- "Il meurt de vieillesse en tentant de fermer tous les onglets ouverts par ses parents", publié le 23/01/2024 par La Rédaction, https://www.legorafi.fr/2024/01/23/il-meurt-de-vieillesse-en-tentant-de-fermer-tous-les-onglets-ouverts-par-ses-parents/
- "Astrologie – Mercure percute accidentellement un semi-remorque sur l’A6 en rétrogradant trop tôt", publié le 19/09/2023 par La Rédaction, https://www.legorafi.fr/2023/09/19/astrologie-mercure-percute-accidentellement-un-semi-remorque-sur-la6-en-retrogradant-trop-tot/

