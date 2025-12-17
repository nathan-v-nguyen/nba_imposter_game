import numpy as np

def collect_players(num_players: int) -> list[str]:
  '''Return list of players'''
  players = np.array([])
  for i in np.arange(num_players):
    player = input('Enter Player Name: ')
    players = np.append(players, player)

  return players


def choose_imposter(player_list: list[str]) -> str:
  '''Choose random imposter from list of players'''
  imposter = np.random.choice(player_list)
  return imposter


def random_nba_player() -> str:
  '''Returns random nba player'''



def main():
  player_num = int(input("Enter the Nummber of Players: "))
  player_list = collect_players(player_num)
  imposter = choose_imposter(player_list)

  


if __name__ == "__main__":
    main()


