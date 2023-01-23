class FootballPlayer:
    uniform_color = "Blue"

    def run(self):
        raise NotImplementedError
    
    def throw(self):
        print("The ball is being thrown")
    
    def tackle(self, football_player="Visiting player"):
        print("The football player is tackling", football_player)

class NewPlayer(FootballPlayer):
    def run(self):
        print("The New Player is running")
    
    def throw(self):
        print("The New Player is throwing")

    def tackle(self, football_player):
        super().tackle(football_player)
        print(football_player, "was tackled by the new player")

new_player = NewPlayer()
new_player.tackle("another player")