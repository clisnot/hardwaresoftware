def user_selection(num):
      ans = input("Enter selection:")
      if ans == "q":
           return False
      return True

def main():
     run_me = True
     while run_me:
          run_me = user_selection()
