# ! python3

import argparse, os
from classes.tokenmanager import TokenManager
from rocketbot import client

def run(args):
  tokenPath = os.path.abspath('TOKEN.txt')
  token = TokenManager.getTokenFromFile(tokenPath, args.token)

  if not token:
    print('Token is required. Usage: --token SuperSecretToken')
    return

  TokenManager.saveToken(tokenPath, token)
  client.owner_id = 178070750048157696
  client.run(token)


if __name__ == '__main__':
  parser = argparse.ArgumentParser(description='Discord bot')
  parser.add_argument('--token', help='Discord Bot Token')
  args = parser.parse_args()
  run(args)
