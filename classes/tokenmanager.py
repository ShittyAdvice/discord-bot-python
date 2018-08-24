from os.path import isfile
from classes.console import Console

class TokenManager:
  @classmethod
  def getTokenFromFile(self, tokenPath, default=None):
    if default:
      return default

    if not isfile(tokenPath):
      return None

    with open(tokenPath, 'r') as f:
      return f.readline()


  @classmethod
  def saveToken(self, tokenPath, token):
    if self.getTokenFromFile(tokenPath) == token:
      return

    if not Console.yesOrNo('WARNING: Token is saved in plain text and will override any existing token\nSave token?'):
      return

    with open(tokenPath, 'w') as file:
        file.write(token)
