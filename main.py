import pandas as pd

def read_excel(excel_file):   # Load excel statistics into list of dictionaries

    dataframe = pd.read_excel(excel_file)

    ocorrencias = []
    for i in range(1, 61):
        dictionary = {key: 0 for key in range(1, 61)}
        ocorrencias.append(dictionary)

    for index, row in dataframe.iterrows():
        # 'index' is the row index, and 'row' is a Pandas Series representing the current row
        # You can access individual elements in the row using column names
        bola1 = row['Bola1']
        bola2 = row['Bola2']
        bola3 = row['Bola3']
        bola4 = row['Bola4']
        bola5 = row['Bola5']
        bola6 = row['Bola6']

        ocorrencias[int(bola1)-1][bola1]+=1
        ocorrencias[int(bola1)-1][bola2]+=1
        ocorrencias[int(bola1)-1][bola3]+=1
        ocorrencias[int(bola1)-1][bola4]+=1
        ocorrencias[int(bola1)-1][bola5]+=1
        ocorrencias[int(bola1)-1][bola6]+=1

        ocorrencias[int(bola2)-1][bola1]+=1
        ocorrencias[int(bola2)-1][bola2]+=1
        ocorrencias[int(bola2)-1][bola3]+=1
        ocorrencias[int(bola2)-1][bola4]+=1
        ocorrencias[int(bola2)-1][bola5]+=1
        ocorrencias[int(bola2)-1][bola6]+=1

        ocorrencias[int(bola3)-1][bola1]+=1
        ocorrencias[int(bola3)-1][bola2]+=1
        ocorrencias[int(bola3)-1][bola3]+=1
        ocorrencias[int(bola3)-1][bola4]+=1
        ocorrencias[int(bola3)-1][bola5]+=1
        ocorrencias[int(bola3)-1][bola6]+=1

        ocorrencias[int(bola4)-1][bola1]+=1
        ocorrencias[int(bola4)-1][bola2]+=1
        ocorrencias[int(bola4)-1][bola3]+=1
        ocorrencias[int(bola4)-1][bola4]+=1
        ocorrencias[int(bola4)-1][bola5]+=1
        ocorrencias[int(bola4)-1][bola6]+=1

        ocorrencias[int(bola5)-1][bola1]+=1
        ocorrencias[int(bola5)-1][bola2]+=1
        ocorrencias[int(bola5)-1][bola3]+=1
        ocorrencias[int(bola5)-1][bola4]+=1
        ocorrencias[int(bola5)-1][bola5]+=1
        ocorrencias[int(bola5)-1][bola6]+=1

        ocorrencias[int(bola6)-1][bola1]+=1
        ocorrencias[int(bola6)-1][bola2]+=1
        ocorrencias[int(bola6)-1][bola3]+=1
        ocorrencias[int(bola6)-1][bola4]+=1
        ocorrencias[int(bola6)-1][bola5]+=1
        ocorrencias[int(bola6)-1][bola6]+=1

    return ocorrencias

def start_bets():   # Start bets and include first number
    apostas = []
    for i in range(1, 61):
        aposta = []
        aposta.append(i)
        apostas.append(aposta)
    return apostas

ocorrencias = read_excel('Mega-Sena.xlsx')

apostas = start_bets()

for aposta in apostas:
    while len(aposta) < 6:
        current_game = ocorrencias[aposta[-1]-1] # Take game of last number
        self_appeared = current_game[aposta[-1]]-1 # Take the same appeared times and reduce 1

        bet_found = False
        keys = []
        while bet_found == False:
            for j in range(1, 61):
                if current_game[j] == self_appeared:
                    if j not in aposta:
                        keys.append(j)
                        bet_found = True
            self_appeared -= 1

        aposta_original = aposta[:]
        aposta.append(keys[0])
        if len(keys) > 1:
            for key in keys:
                if key != keys[0]:
                    aposta_clonada = aposta_original[:]
                    aposta_clonada.append(key)
                    apostas.append(aposta_clonada)

print ("Encontrados " + str(len(apostas)) + " jogos")

def remove_duplicate_lists(apostas):
    unique_lists = []
    seen_tuples = set()

    for inner_list in apostas:
        tuple_representation = tuple(sorted(inner_list))
        if tuple_representation not in seen_tuples:
            seen_tuples.add(tuple_representation)
            unique_lists.append(inner_list)
        else:
            print ("Jogo repetido: " + str(tuple_representation))

    return unique_lists

apostas_filtradas = remove_duplicate_lists(apostas)

print ("Encontrados " + str(len(apostas_filtradas)) + " jogos depois de filtrar")

for aposta in apostas_filtradas:
    print(str(sorted(aposta)))