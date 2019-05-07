#cette fonction va permetre de recup recuprer le max de la ligne


def recupMaxRow(df , columns):
    #pour effecture les itération de chaque boucles
    iter = 0

    for valeur in df[Columns]:

        if valeur == df[Columns].max():

            print(iter)
            valeur = iter

        iter = iter + 1

    return valeur
