
#*TO DO APPLICATION

#we need to import prettytable module for creating beautiful ascii table for app.
from prettytable import PrettyTable

print("\nMy TO-DO List.")

instructions = "\n1: Enter A or a to add new TO-DO.\n2: Enter D or d to delete TO-DO.\n3: Enter U or u to update TO-DO.\n4: Enter E or e to exit the program.\n5: Enter L or l to check your TO-DO List. "
print(instructions)

# we need to add all the information in our todo list. 
my_todo_list = []

x = PrettyTable()
#need to make a seperate function for updating our list becouse we will need it in
# many points to reuse it.

def my_list():
  x.field_names = ["Item Names"]
  for i in my_todo_list:
    #this will add new row to our prettytable on every interation.
    x.add_row([i])
  #this will give us a title
  print(x.get_string(title="TO DO List"))
  #Every time this table loads, it will clear all the previous values in it and
  #update ouf list with new information.
  x.clear_row()

#Now we are done with our metthod.

runing = True
while runing:
  #get user input
  user_input = input("\nWhat do you want to do? (A, D, U, E, L) : ").lower()
  if user_input == "a":
    new_todo = input("\nPlease enter your new TODO: ").lower()
    print(f"\nYour current TODO is {new_todo}.")
    #append the new todo to our list
    my_todo_list.append(new_todo)
    #Now Let's code the "d" part.
  elif user_input == "d":
    #first we need ather while loop, we will loop until a user a valid value.
    while True:
      #ask a user to enter the item name.
      item_name = input("\nPlease enter a name of an item you want to delete.").lower()
      #here we will use try catch to avoid any exception.
      try:
        #first check if the item is present in to do list.
        if item_name in my_todo_list:
          #now ask user for confirmation.
          choice = input(f"Are you sure to delete {item_name} from your TODO list? (Y/N): ").lower()
          if choice == "y":
            #remove the item from a todo list
            my_todo_list.remove(item_name)
            print("Your updated TO-DO List.")
            #now call the my_list function
            my_list()
            #break the loop here
            break
        else:
          print("Item not found.")
      #except block here
      except Exception:
        print("Something went wrong.")
  #now let's code for update part
  elif user_input == "u":
    #same code like delete but a few changes
    #first while loop
    while True:
      item_name = input("\nPlease enter a name of an item you want to update.").lower()
      try:
        #check if the item is in the list
        if item_name in my_todo_list:
          #ask user for confirmation
          choice = input(f"Are you sure to update {item_name} from your TO-DO List? (Y/N): ").lower()
          if choice == "y":
            update_item = input(f"Please enter a name you want to update {item_name} with. ").lower()
            #get the index of an item you want to update
            index = my_todo_list.index(item_name)
            #replace the item with your updated item
            my_todo_list[index] = update_item
            print("Your updated TO-DO List.")
            my_list()
            #terminated the loop
            break
        else:
          print("Item not found.")
          
      except Exception:
        print("Something went wrong.")
  #now let's code the e part
  elif user_input == "e":
    ask_user = input("\nAre you sure to exit? (Y/N): ").lower()
    if ask_user =="y":
      runing = False
  elif user_input == "l":
    my_list()
  elif user_input == "" or user_input == " ":
    print("Please enter something.")
  else:
    print("Please enter a valid value.")

#now let's check all the functionality af program.
