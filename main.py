import re
import csv

from tokenizer import Tokeniseur, read_lexicon
from chunker import read_rules, chunker
from evaluate import txt_to_csv, evaluation

def main():
    # 1. Chargement des ressources
    lexicon_path = "ressources/lexique.txt"
    rules_path = "ressources/regles.txt"
    text_path = "ressources/texte.txt"
    reference_path = "ressources/reference.csv"
    grammar_path = "ressources/grammar.txt"

    try:
        lexicon = read_lexicon(lexicon_path)
        rules = read_rules(rules_path)
        tokenizer = Tokeniseur(grammar_path)

        # 2. Lecture et tokenisation du texte
        print("Lecture du texte...")
        input_text = tokenizer.read_file(text_path)
        print(f"Texte lu :\n{input_text}\n")

        print("Tokenisation...")
        tokenized_text = tokenizer.tokenize(input_text)
        print(f"Texte tokénisé :\n{tokenized_text}\n")

        # 3. Processus de segmentation (chunking)
        print("Segmentation (chunking)...")
        rule_usage = chunker(tokenized_text, lexicon, rules)
        print(f"Règles utilisées :\n{rule_usage}\n")

        # 4. Conversion en CSV pour évaluation
        chunks_file = "outputs/chunks.txt"
        chunks_csv = "outputs/chunks.csv"
        print(txt_to_csv(chunks_file, chunks_csv))

        # 5. Évaluation des performances
        print("Évaluation des performances...")
        evaluation(reference_path, chunks_csv)

    except FileNotFoundError as e:
        print(f"Erreur : {e}")
    except Exception as e:
        print(f"Une erreur s'est produite : {e}")

if __name__ == "__main__":
    main()

