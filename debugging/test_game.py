from mines import Minesweeper

def test_game():
    game = Minesweeper(width=5, height=5, mines=0)
    game.mines = {6, 12, 18}

    assert game.reveal(0, 0) == True
    assert game.revealed[0][0] == True

    assert game.reveal(1, 1) == False

    game.revealed = [[False]*5 for _ in range(5)]
    assert game.count_mines_nearby(2, 1) == 2

    game.revealed = [[True]*5 for _ in range(5)]
    for y in range(5):
        for x in range(5):
            if (y * 5 + x) in game.mines:
                game.revealed[y][x] = False
    assert game.check_win() == True

    print("All tests passed!")

if __name__ == "__main__":
    test_game()
