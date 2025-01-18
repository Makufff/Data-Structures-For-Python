class Song : 
    def __init__(name : int , genre : str , duration : int) -> None:
        self.name = name
        self.genre = genre
        self.duration = duration

    def showinfo(self) -> str:
        return f"{self.name} <|> {self.genre} <|> {self.duration//60}:{self.duration%60}"
    
Rickroll = Song(input(), input(), int(input()))
print(Rickroll.showinfo())