from Game import Game

class Sim:
    def __init__(self, games):
        self.games = games
        self.run()
    def run(self):
        for t in ["random", 0, 1, 2, 3, 4]:
            p1_wins = 0
            p2_wins = 0
            total_turns = 0
            print("Simulating", self.games, "Games, p1 starts with", t, "aces")
            for x in range(self.games):
                
                if(t=="random"):
                    g = Game()
                else:
                    g = Game(t)
                data = g.playAll()
                if(data[0]=="p1"):
                    p1_wins += 1
                elif(data[0]=="p2"):
                    p2_wins += 1
                else:
                    raise Exception("Nobody won?")
                total_turns += data[1]
            p1_winrate = p1_wins / (p1_wins+p2_wins)
            avg_turns = total_turns / self.games
            print("P1 Winrate: ", p1_winrate)
            print("Average Turns per Game: ", avg_turns)
           