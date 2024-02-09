import interface
import game

def main_game() -> None:
    interface.print_start()
    interface.print_actions()
    game.game()


inp = ''
while inp == '':
    main_game()
    inp = input().lower()
