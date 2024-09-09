def mainmenu():
    while True:
        print(
            f'Welkom bij de f1 data app\n'
            f'Je kan de volgende functionaliteiten kiezen:\n'
            f'\t1. Resultaten van de laatste race\n'
            f'\t2. Huidige standings coureurs\n'
            f'\t3. Huidige standings teams\n'
            f'\t4. Informatie over specifieke coureur\n'
            f'\t5. Informatie over specifiek team\n'
        )
        choice = input('Vul het nummer van uw keuze in: \n')

        if choice == '1':
            continue
        elif choice == '2':
            continue
        elif choice == '3':
            continue
        elif choice == '4':
            continue
        elif choice == '5':
            continue
        else:
            print(f'Keuze \'{choice}\' bestaat niet, vul een juiste keuze in')
            choice = input('Vul het nummer van uw keuze in: \n')
            continue

if __name__ == '__main__':
    mainmenu()