import numpy as np
import pandas as pd

def collect_players(num_players: int) -> list[str]:
  '''Return list of players'''
  players = []
  for i in range(num_players):
    player = input('Enter Player Name: ')
    players.append(player)

  return players


def choose_imposter(player_list: list[str]) -> str:
  '''Choose random imposter from list of players'''
  imposter = np.random.choice(player_list)
  return imposter


def random_nba_player() -> tuple[str, str]:
  '''Returns random nba player'''
  nba_players = 'nba_players.csv'
  df = pd.read_csv(nba_players)
  row = df.sample(1).iloc[0]
  player = row['name']
  hint = row['hint']
  return player, hint
  

def assign_roles(player_list: list[str], imposter: str) -> dict:
  '''Assign roles to every player and return dictionary'''
  player_dict = {}
  for player in player_list:
    if player == imposter:
      player_dict[player] = {'role':'imposter'}
    else:
      player_dict[player] = {'role':'normal'}
  return player_dict



def main():
  player_num = int(input("Enter the Nummber of Players: "))
  player_list = collect_players(player_num)
  imposter = choose_imposter(player_list)
  nba_player, hint = random_nba_player()
  player_roles = assign_roles(player_list, imposter)

  game_dict = {'player_num':player_num, 'player_list':player_list, 'imposter':imposter,'nba_player':nba_player, 'hint':hint}
  print(game_dict)
  



if __name__ == "__main__":
    main()


