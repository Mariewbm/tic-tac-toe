#initialisation du tableau
plateau = [" "] * 9  # 9 cases
#fonction d'affichage du tableau
def afficher_plateau() :
    print(f"""
    {plateau[0]} | {plateau[1]} | {plateau[2]}
    --|---|---
    {plateau[3]} | {plateau[4]} | {plateau[5]}
    --|---|---
    {plateau[6]} | {plateau[7]} | {plateau[8]}
    """)
afficher_plateau()


# verifier si le joueur a gagner
def verifie_victoire(joueur) :
    #listes combinaisons gagnantes
    combinaisons_gagnantes = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),  #lignes
        (0,  3, 6), (1, 4, 7), (2, 5, 8), #colonnes
        (0, 4, 8), (2, 4, 6)              #diagonales                   
    ]

#fonction qui verifie si une combinaison est remplis par le meme joueurs
    for comb in combinaisons_gagnantes :
        if plateau[comb[0]] == plateau[comb[1]] == plateau[comb[2]] == joueur:
            return True
        return False
    
#fonction pour verifier si le plateau est plein (match nul) 
def plateau_plein() :
    return " " not in plateau 

#definitio du joueur actuel ("X" commence)
joueur_actuel = "X"

#boucle principale du jeu
while True :
    #demander au joueur de choisir une case
    try: #introduire des exeptions
        case = int(input(f"joueur {joueur_actuel}, entrez un numéro entre 1 et 9 :")) -1
        if case < 0 or case > 8 or plateau[case] != " ":  #si la case n'est pas encore 0 et 8 ou la case est deja remplie
            print("Case invalide, essayer a nouveau")
            continue
    except ValueError: 
        print("Entrée invalide, veuillez entrer un chiffre entre 1 et 9.")
        continue    

    #placer le symbole du joueur sur le plateau
    plateau[case] = joueur_actuel
    afficher_plateau()

    #verifie si le joueur actuel a gagner
    if verifie_victoire(joueur_actuel) :
        print(f"Felicitation le joueur {joueur_actuel} a gagné !")
        break 
    
    #passer au joueur suivant
    joueur_actuel = "O" if joueur_actuel == "X" else "X"