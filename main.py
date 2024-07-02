def incolor(string):
    import random
    user_input = input(string)
    colors = ["\033[38;5;196m", "\033[38;5;208m", "\033[38;5;226m", "\033[38;5;46m", 
              "\033[38;5;21m", "\033[1;36m", "\033[1;35m"] 
    reset_color = "\033[0m"
    random_color = random.choice(colors)
    user_input_colored = f"{random_color}{user_input}{reset_color}"
    return user_input_colored

name = incolor("Your name: ")
print(name)
     
    
    
# Important Points To Consider When using the incolor function:
# > Don't use type conversion functions around the incolor function:
# such as for example: int(incolor("Enter a number: ") which can 
# cause your program to crash. Intead if you want to intake numerical 
# input from the user for example you can simply type incolor("Enter a number: ")
# and you will get your numerical input returned whilst being colored.











  
  
  
# Outcome of function and usage:  
# name = incolor("Enter your name: ")
