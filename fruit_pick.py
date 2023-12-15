def display_menu():
  menu_dict = {
     '1':'apples',
     '2':'bananas',
     '3':'cherries',
     'X':'pick your own'
 }
 for items, values in menu_dict.items():
    print(items+". "+ values.capitalize())

def main():
  menu_dict = display_menu()
  print(list(menu_dict.items()))
  print(list(menu_dict))
  print(list(menu_dict.values()))
