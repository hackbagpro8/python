theboard={'7': ' ' , '8': ' ' , '9': ' ' ,
          '4': ' ' , '5': ' ' , '6': ' ' ,
          '1': ' ' , '2': ' ' , '3': ' ' ,}

board_keys=[]

for key in theboard:
    board_keys.append(key)

print(board_keys)

def printboard(board):
    print(board['7'] , '|' , board['8'] , "|" + board['9'])
    print('-+-+-')
    print(board['4'] , '|' , board['5'] , "|" , board['6'])
    print('-+-+-')
    print(board['1'] , '|' , board['2'] , "|" , board['3'])
    print('-+-+-')


def game():

    turn= 'X'
    count=0


    for i in range(10):
        printboard(theboard)
        print("It's your turn," , turn , ".Move to which place?")

        move=input()

        if theboard[move] == ' ':
            theboard[move] = turn
            count += 1
        else:
            print("That place is already filled. \nMOve to to which place")

        if count >= 5:
            if theboard['7'] == ['8'] == ['9'] != ' ':
                printboard(theboard)
                print("\n Game over.\n")
                print(" **** " +turn + "won. ****")
                break
            elif theboard['4'] == ['5'] == ['6'] != ' ':
                printboard(theboard)
                print("\n Game over.\n")
                print(" **** " +turn + "won. ****")
                break
            elif theboard['1'] == ['2'] == ['3'] != ' ':
                printboard(theboard)
                print("\n Game over.\n")
                print(" **** " +turn + "won. ****")
                break
            elif theboard['7'] == ['4'] == ['1'] != ' ':
                printboard(theboard)
                print("\n Game over.\n")
                print(" **** " +turn + "won. ****")
                break
            elif theboard['8'] == ['5'] == ['2'] != ' ':
                printboard(theboard)
                print("\n Game over.\n")
                print(" **** " +turn + "won. ****")
                break
            elif theboard['9'] == ['6'] == ['3'] != ' ':
                printboard(theboard)
                print("\n Game over.\n")
                print(" **** " +turn + "won. ****")
                break
            elif theboard['7'] == ['5'] == ['3'] != ' ':
                printboard(theboard)
                print("\n Game over.\n")
                print(" **** " +turn + "won. ****")
                break
            elif theboard['9'] == ['5'] == ['1'] != ' ':
                printboard(theboard)
                print("\n Game over.\n")
                print(" **** " +turn + "won. ****")
                break
        if count == 9:
            print("\nGame over.\n")
            print("Its a tie")


        if turn=='X':
            turn= 0
        else:
            turn= 'X'

    restart= input("DO you want to play again? (y/n)")
    if restart == "y" or restart == "Y":
        for key in board_keys:
            theboard[key] = " "

        game()


if __name__ == "__main__":
    game()
