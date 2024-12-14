import re

def read_rules(rules_path:str)->dict:
    rules={}

    with open(rules_path, 'r', encoding='utf-8') as file:
        for line in file:
            print(line.strip().split('\t'))
            parts=line.strip().split('\t')

            if len(parts)==3:
                rule_number,category,pattern=parts
                rule_number=int(rule_number.strip())
                category=category.strip()
                pattern=pattern.strip()
                if category.startswith("r'") and category.endswith("'"):
                    category=category[2:-1]
                    rules[rule_number]=(re.compile(category),pattern)
                else:
                    rules[rule_number]=(category,pattern)
    return rules


def chunker(tokenized_text:list,lexicon:dict,rules:dict)->dict:
    #On initie un compteur pour le nombre de fois où une règle a été utilisée
    rule_usage={rule_number:0 for rule_number in rules}

    #On extrait les expressions régulières de nos règles
    regexes={}
    for key,(category,pattern) in rules.items():
        #print(f"Règle : {key}, Catégorie: {category}, Motif: {pattern}")
        if isinstance(category,re.Pattern):
            #print(f"Expression régulière compilée : {category}")
            regexes[key]=category

    with open('outputs/chunks.txt','w',encoding='utf-8') as file:

        #On initie un compteur pour nos règles de type A+B->C et certaines regex
        i=0

        while i<len(tokenized_text):
            token=tokenized_text[i]
            if token in lexicon:
                cat=lexicon[token]

                for key,pattern in rules.items():

                    #Si la catégorie du token correspond à une règle:
                    if cat==pattern[0]:
                        #on applique simplement la règle
                        #Règle de type A->[B
                        file.write(f" {key}{pattern[1]} {token}")
                        # On incrémente le compteur des règles utilisées
                        rule_usage[key]+=1
                        break

                    #Si la catégorie du token correspond au "début" d'une règle (et n'est pas une regex):
                    #Règle de type A+B->[C
                    elif isinstance(pattern[0],str) and pattern[0].startswith(cat):
                        if '+' in pattern[0]:
                            #Si le token suivant match le pattern, on applique la règle
                            if (tokenized_text[i+1] in lexicon and
                                    (lexicon[tokenized_text[i+1]]==pattern[0].split('+')[1])):
                                file.write(f" {key}{pattern[1]} {token} {tokenized_text[i+1]}")
                                # On incrémente le compteur des règles utilisées
                                rule_usage[key]+=1
                                i+=1
                                break

                #Si le token est dans le lexique mais que aucune règle ne s'applique, on le réécrit
                else:
                    file.write(f" {token}")

            #Si le token n'est pas dans le lexique,
            else:
                #On vérifie s'il match une expression régulière
                for rule_number,regex in regexes.items():
                    if regex.match(token):
                        key,pattern=rules[rule_number]
                        file.write(f" {rule_number}{pattern[0]}{pattern[1]}{pattern[2]} {token}")
                        #On incrémente le compteur des règles utilisées
                        rule_usage[rule_number]+=1
                        break

                #Sinon, on le réécrit simplement
                else:
                    file.write(f" {token}")
            i+=1

    print("\nUn fichier chunks.txt a été créé.\nNombre de fois où nos règles ont été utilisées :")
    print(rule_usage)
    return rule_usage
