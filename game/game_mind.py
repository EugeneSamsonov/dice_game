from random import randint
from data import *
import interface


def game() -> None:
    global player_score, dealer_score, dealer_scores
    player_score = 0
    dealer_score = 0
    dealer_scores = []

    while player_score < max_score and dealer_score < max_score:
        player_action = input(f"{player_score} > ").lower()

        if player_action == "hit":

            player_score += randint(1, 11)
            dealer_score += randint(1, 11)
            if not is_gameover():
                dealer_scores.append(dealer_score)
                print(f"Игрок* {player_score}")
                interface.print_actions()



        elif player_action == "hold":
            is_gameover()

            if player_score > dealer_score:
                interface.print_end_game("Игрок", tepm_scores=[player_score, dealer_score, dealer_scores])
                return None
            elif player_score < dealer_score:
                interface.print_end_game("Диллер", tepm_scores=[player_score, dealer_score, dealer_scores])
                return None
            elif player_score == dealer_score:
                interface.print_end_game("Игрок", "Диллер", tepm_scores=[player_score, dealer_score, dealer_scores])
                return None


def is_gameover() -> bool:
    if player_score == max_score and dealer_score == max_score:
        interface.print_end_game(tepm_scores=[player_score, dealer_score, dealer_scores])
        return True

    elif player_score == max_score and dealer_score < max_score:
        interface.print_end_game("Игрок", tepm_scores=[player_score, dealer_score, dealer_scores])
        return True

    elif player_score < max_score and dealer_score == max_score:
        interface.print_end_game("Диллер", tepm_scores=[player_score, dealer_score, dealer_scores])
        return True

    elif player_score == max_score and dealer_score > max_score:
        interface.print_end_game("Игрок", dil=True, tepm_scores=[player_score, dealer_score, dealer_scores])
        return True

    elif player_score > max_score and dealer_score == max_score:
        interface.print_end_game("Диллер", pl=True, tepm_scores=[player_score, dealer_score, dealer_scores])
        return True

    elif player_score > max_score and dealer_score > max_score:
        interface.print_end_game(pl=True, dil=True, tepm_scores=[player_score, dealer_score, dealer_scores])
        return True

    elif player_score > max_score and dealer_score < max_score:
        interface.print_end_game("Диллер", pl=True, tepm_scores=[player_score, dealer_score, dealer_scores])
        return True

    elif player_score < max_score and dealer_score > max_score:
        interface.print_end_game("Игрок", dil=True, tepm_scores=[player_score, dealer_score, dealer_scores])
        return True

    else:
        return False
