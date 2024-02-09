from data import *


def print_start() -> None:
    print(
        f"""---------------------- 
          {max_score}
----------------------
Диллер должен бросать 
пока его счёт < {dealer_stop_score}
----------------------"""
    )


def print_actions() -> None:
    print(
        """hit  | Бросить кости  
hold | Остановиться
----------------------"""
    )


def print_end_game(*args, pl: bool = False, dil: bool = False, tepm_scores: list[int | list[int]] | None = None) -> None:
    if tepm_scores is None:
        tepm_scores = []

    print(f"Игрок: {tepm_scores[0]}")
    if len(tepm_scores[2]) != 0:
        for score in tepm_scores[2]:
            print(f"Диллер* {score}")

        print("-" * 22)
        print(f"Диллер {tepm_scores[1]}")

    if len(args) == 1:
        print("-" * 22)
        print(f"{args[0]} победил!", "Диллер перебрал!" if dil else '', "Игрок перебрал!" if pl else '')
        print("Нажите enter чтобы начать заново", end=' ')

    elif len(args) < 1:
        print("-" * 22)
        print(f"Ничья!", "Диллер перебрал!" if dil else '', "Игрок перебрал!" if pl else '')
        print("Нажите enter чтобы начать заново", end=' ')
