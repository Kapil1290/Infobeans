class MusicLibrary:
    def __init__(self):
        self.__library = []
    
    def add_music(self, title, singer):
        music = { "title": title, "singer": singer }
        self.__library.append(music)
        print("Music added.....")  
    
    def play_random(self):
        for i in range(0, len(self.__library)):
            print(f"Playing: {self.__library[0]["title"]}.....")
            break
        return

m1 = MusicLibrary()
# m1.add_music("teri kasam ho....", "Aham")
# m1.add_music("sitaram sitaram", "gopinath")
# m1.play_random()