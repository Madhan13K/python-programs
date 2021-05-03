class song:
    def __init__(self,title,artist,duration):
        self.title=title
        self.artist=artist
        self.duration=duration
# print(song.__dict__)
class album:
    def __init__(self,name,year,artist=None):
        self.name=name
        self.year=year
        if artist is None:
            self.artist=Artist("various artist")
        else:
            self.artist=artist
        self.tracks=[]
    def add_song(self,song,position=None):
        if position is None:
            self.tracks.append(song)
        else:
            self.tracks.insert(song,position)

class artist:
    def __init__(self,name):
        self.name=name
        self.album=[]
    def add_album(self,album):
        self.album.append(album)
#         self.__init__.__doc__="""andbhvgdhuhxdhch"""
# print(artist.__init__.__doc__)


def load_data():
    new_artist=None
    new_album=None
    artist_list=[]
    with open("albums.txt","r") as album:
        for line in album:
            artist_feild,album_feild,year_feild,song_feild=tuple(line.strip("\n").split("\t"))
            year_feild=int(year_feild)
            print("{}:{}:{}:{}".format(artist_feild,album_feild,year_feild,song_feild))
            if new_artist==None:
                new_artist=Artist(artist_feild)
            elif new_artist.name!=artist_feild:
                new_artist.add_album(new_album)
                artist_list.append(new_artist)
                new_artist=artist(artist_feild)
                new_album=None
            if new_album==None:
                new_album=Album(album_feild,year_feild,new_artist)

if __name__=="__main__":
    load_data()


