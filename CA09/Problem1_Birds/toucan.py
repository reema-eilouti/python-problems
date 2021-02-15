from bird import Bird
import termcolor

# Toucan class (child)

class Toucan(Bird):
    def __init__(self, name, age):

        super().__init__(name, age)
        self.beak_color = None
        self.beak_length = None
        self.number_eggs = None
    
    def __str__(self):
        return termcolor.colored("""  _.--.__                                             _.--.
    ./'       `--.__                                   ..-'   ,'
  ,/               |`-.__                            .'     ./
 :,                 :    `--_    __                .'   ,./'_.....
 :                  :   /    `-:' _\.            .'   ./..-'   _.'
 :                  ' ,'       : / \ :         .'    `-'__...-'
 `.               .'  .        : \@/ :       .'       '------.,
    ._....____  ./    :     .. `     :    .-'      _____.----'
              `------------' : |     `..-'        `---.
                         .---'  :    ./      _._-----'
.---------._____________ `-.__/ : /`      ./_-----/':
`---...--.              `-_|    `.`-._______-'  /  / ,-----.__----.
   ,----' ,__.  .          |   /  `\.________./  ====__....._____.'
   `-___--.-' ./. .-._-'----\.                  ./.---..____.--.
         :_.-' '-'            `..            .-'===.__________.'
                                 `--...__.--'""", color = "yellow")


    def wood_pecking(self):
        if self.age < 2:
            print(f"sorry,{self.name} are too tiny to pecking")
        else:
            print(f"{self.name} can peck a tree now!")
    
    def toucan_info(self):
        print(f"the toucan {self.name} is {self.age} and have a {self.beak_length} long also {self.beak_color} color")





    
