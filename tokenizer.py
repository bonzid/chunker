import re

class Tokeniseur:
  def __init__(self, grm_path="/content/grammar.txt",file_path="/content/texte.txt"):
    self.grm_path=grm_path

  @staticmethod
  def read_grammar(grm_path:str)->str:
    """
    Cette fonction lit un fichier de grammaire et renvoie à une chaîne de caractères
    Entrée :
      arg: chemin vers le fichier grammaire
    Sortie :
      str: contenu du fichier grammaire
    """
    #On charge le contenu de notre grammaire
    try:
      with open(grm_path,'r',encoding='utf-8') as file:
        print("Contenu de la grammaire : ")
        grm_content=file.read()
    except FileNotFoundError:
      print(f"Fichier grammaire introuvable à l'adresse {grm_path}")

    return grm_content

  def read_file(self,file_path:str)->str:
    with open(file_path, 'r', encoding='utf-8') as file:
      texte=file.read()
    return texte


  def tokenize(self,text:str,lang:str="fr",keep_space:bool=False)->list:
    """
    Tokéniseur
    Entrées :
      arg1 : la chaine à tokeniser
      arg2 : la langue
    Sortie :
      la liste des tokens du texte donné

    Nécessite les modules suivants : re
    """
    grm_content=self.read_grammar(self.grm_path)
    grm={
        "fr": grm_content,
        "default": r"\d{1,2}[-/]\d{1,2}[-/]\d{2,4}| \d+(?:[,.]\d+)?| [\w-]+'?+| \S"
    }

    #On tokénise selon les expressions régulières définies dans notre grammaire
    space=""
    if keep_space:
      space=r"|\s"
    if lang in grm:
      regex=re.compile(grm[lang]+space,flags=re.I|re.X)
    else:
      regex=re.compile(grm["default"]+space)

    tokens=regex.findall(text)

    return tokens


def read_lexicon(lex_path:str)->dict:
    #Ici on prend notre chemin de lexique en entrée, on lit le fichier et on associe chaque token du lexique à sa catégorie grammaticale
    lexique={}
    with open(lex_path, 'r', encoding='utf-8') as file:
      lexicon=file.read()
      lines=lexicon.split('\n')
      for line in lines:
        parts=line.strip().split('\t')
        if len(parts)==2:
            category,tokens=parts
            tokens_list=tokens.split(', ')
            for token in tokens_list:
                lexique[token]=category

    return lexique


def process_tokens(tokenized_text:list,lexicon:dict):
  """
  Cette fonction associe chaque token à une catégorie grammaticale si ce token est dans le lexique. Sinon, "Catégorie: Inconnue".
  """
  for token in tokenized_text:
    if token in lexicon:
      print(f"Token: {token}, Catégorie: {lexicon[token]}")
    else:
      print(f"Token: {token}, Catégorie: Inconnue")
