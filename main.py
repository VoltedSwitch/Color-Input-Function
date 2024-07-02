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
     
    
    










  
  
  
# Outcome of function and usage:  
# name = incolor("Enter your name: ")
