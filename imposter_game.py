import numpy as np
import pandas as pd

def get_num_players():
  '''Returns number of players'''
  while True:
    try:
      num_players = int(input("Enter the Nummber of Players: "))
      if num_players < 3:
        print('You need atleast 3 players to play')
        continue
      return num_players
    except ValueError:
        print('Please enter a valid integer')

def collect_players(num_players: int) -> list[str]:
  '''Return list of players'''
  players = []
  for i in range(num_players):
    while True:
      player = input('Enter Player Name: ')
      if player in players:
        print('No duplicate names. Please try again.')
        continue
      break
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


def reveal_roles(game_dict: dict) -> None:
  '''Reveal roles, nba player, and hints to game players'''
  for player in game_dict['player_list']:
    print('\n' * 40)
    input(f'Pass to {player} and Press Enter When Ready')

    print('\n' * 40)
    if player == game_dict['imposter']:
      print('You are the IMPOSTER')
      print('\nHint: ', game_dict['hint'])
    else:
      print('You are a NORMAL player\n')
      print(game_dict['nba_player'])
    
    input('Press ENTER when done')
  
  print('\n' * 40)
  print('Begin the Game')


      


def main():
  player_num = get_num_players()
  player_list = collect_players(player_num)
  imposter = choose_imposter(player_list)
  nba_player, hint = random_nba_player()
  player_roles = assign_roles(player_list, imposter)

  game_dict = {'player_num':player_num, 'player_list':player_list, 'imposter':imposter,'nba_player':nba_player, 'hint':hint}

  reveal_roles(game_dict)
  


if __name__ == "__main__":
    main()


