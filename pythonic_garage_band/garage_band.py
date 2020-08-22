from abc import abstractmethod, ABC

class Band(ABC):

    all_bands=[]
    def __init__(self,name,members,song):
        self.name = name
        self.members = members
        self.song = song
        Band.all_bands.append(self)

    def play_solos(self):
        """
        Asks each member musician to play a solo, in the order they were added to band.
        """
        solo=[]
        for i in self.members :
            solo.append(i.play_solo())
        return solo

    def play_song(self):
        return self.song
    
    def __str__(self):
        members = ','.join(str(v) for v in self.members)
        return '{} band, the members are {}. Check out thier song: {}!'.format(self.name,members,self.song)

    def __repr__(self):
        
        return f'{self.name} band, the members are {self.members}. Check out thier song: {self.song}'

    @classmethod
    def to_list(cls):
        """
        Returns a list of previously created Band instances
        """
        return cls.all_bands

    @staticmethod
    def create_from_data(data):
          
        data.seek(0)
        to_formate = data.readlines()
        print(to_formate[0])
        name = input("{}".format(to_formate[1]))
        print(to_formate[2])

        guitar = Guitarist(input("{}".format(to_formate[3])))

        bass_name = input("{}".format(to_formate[4]))
        bass_instrument = input("{}".format(to_formate[5]))
        bass = Bassist(bass_name, bass_instrument)

        drummer = Drummer(input("{}".format(to_formate[6])))

        song = input("{}".format(to_formate[7]))

        new_band = Band(name,[guitar,bass,drummer],song)
        return new_band

class Musician(ABC):

    def __init__(self,name):
        self.name = name

    def __str__(self):
        return self.name
    def __repr__(self):
        return self.name

    @staticmethod
    def play_solo():
        """
         Returns the solo play for the member.
        """
        pass
    
    @staticmethod
    def get_instrument():
        """
         Returns the instrument for the band member.
        """
        pass
    
   

class Guitarist(Musician):

    def play_solo(self):
        return "wawawawawwawawa"
    
    def get_instrument(self):
        return "Guitar"

class Bassist(Musician):

    def __init__(self,name,instrument):
        self.instrument = instrument
        super().__init__(name)

    def play_solo(self):
        return "tantantantan"
    
    def get_instrument(self):
        return self.instrument

class Drummer(Musician):

    def play_solo(self):
        return "dum dum dum dum"
    def get_instrument(self):
        return "Drum"

if __name__ == "__main__" :
    # guitarist = Guitarist("guitarist")
    # drummer = Drummer("drummer")
    # bassist = Bassist("bassist","Bass guitar")
    # tbep = Band("The Black Eyed Peas", [guitarist,drummer],"I gotta a feeling")
    # print(bassist.get_instrument())
    
    file1 = open("assets/data.txt","r+")  
    new_band = Band.create_from_data(file1)
    file = open('assets/ready.txt','w')
    file.write(new_band.__str__())
 

    # userBand = Band(input("Enter the band name:"),[Guitarist(input("enter a guitarist member:")), Drummer(input("Enter a drummer member:")), Bassist(input("Enter a bassist member:"),input("Enter the bass instrument:"))], input("Enter your favourite song from the band:"))
    # print(type(tbep.members[0]))

    # print(*(tbep.play_solos()), sep= "\n")
    # print(tbep.play_song())
    # print(*(Band.to_list()), sep= "\n")
    # Band.to_list()

    

  

    

