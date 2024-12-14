import re
import csv

def txt_to_csv(input_file,output_file)->str:

    """
    La fonction txt_to_csv nous permet de convertir nos résultats obtenus sous forme de fichier txt vers un fichier csv.
    Le format csv nous permettra de comparer ligne par ligne notre résultat avec notre référence.
    """

    try:
        with open(input_file,'r',encoding='utf-8') as f:
            lines=f.readlines()

        with open(output_file,'w',newline='',encoding='utf-8') as csvfile:
            writer=csv.writer(csvfile)
            writer.writerow(['Chunk','Cat'])

            for line in lines:
                matches=re.findall(r'\d+\[(\w+)\s([^0-9]+)',line) #regex pour détecter les "2[SN blabla" avec le pattern numéro+[+lettre+espace
                chunk=""
                category=""

                for match in matches:
                    #si on trouve un chunk, on écrit son contenu et sa catégorie
                    if chunk:
                        writer.writerow([chunk.strip(),category])
                        chunk=""
                        category=""

                    chunk+=match[1]
                    category=match[0]

                #cas du dernier chunk
                if chunk:
                    writer.writerow([chunk.strip(),category])

        process=f"\nLe fichier {output_file} a bien été créé."

    except FileNotFoundError:
        process=f"\nFichier {input_file} introuvable"

    return process

def read_csv(csv_file):
    """
    La fonction read_csv sera appelée dans notre fonction evaluation pour lire nos deux fichiers (test et reference)
    """

    with open(csv_file, 'r', encoding='utf-8') as f:
        reader=csv.reader(f)
        #On skippe la première ligne (en-tête)
        next(reader)
        data=[row for row in reader]
    return data



def evaluation(ref_file,test_file):
    ref_data=read_csv(ref_file)
    test_data=read_csv(test_file)

    vp=0
    fn=0
    fp=0

    for ref_row,test_row in zip(ref_data,test_data):
        ref_chunk,ref_cat=ref_row
        test_chunk,test_cat=test_row

        #Le meilleur des cas : bon découpage et bonne catégorie : +1 vrai positif
        if ref_chunk==test_chunk and ref_cat==test_cat:
            vp+=1

        #Cas où découpage OK mais mauvaise catégorie : +1 faux positif
        elif ref_chunk==test_chunk and ref_cat!=test_cat:
            fp+=1

        #Cas où rien n'est bon : +1 faux négatif
        elif ref_chunk!=test_chunk and ref_cat!=test_cat:
            fn+=1

    if (vp+fp)==0:
        precision=0
    else:
        precision=vp/(vp+fp)

    if (vp+fn)==0:
        rappel=0
    else:
        rappel=vp/(vp+fn)

    if precision!=0 and rappel!=0:
      fmesure=((precision*rappel)/(precision+rappel))*2

    results=print((f"Pour notre chunker, nous estimons :\n"
    f"\tPrécision : {precision}\n"
    f"\tDécision : {rappel}\n"
    f"\tF-mesure : {fmesure}"
    ))
    return results
