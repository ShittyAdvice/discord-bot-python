class Console:
  @classmethod
  def yesOrNo(self, question):
    '''
      Ask a yes/no question via raw_input() and return their answer.
    '''
    choices = {
      'yes': True,
      'y': True,
      'no': False,
      'n': False
    }

    while True:
      print(question + ' (y/n): ', end='')
      choice = input().lower()
      if choice in choices:
          return choices[choice]
      else:
          print("Please respond with 'yes' or 'no' (or 'y' or 'n').")