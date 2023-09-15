'''Implement a class called player that represents a cricket player.the player class should have a
method called play() which prints"the player is playing cricket  dervive two classes,batsman and
bowler,from the player class.override the play() method in each derived class to print "the batsman 
is batting" and "the bowler is bowling ",respectively.write a program to create objects of the both the
batsman and bowler classes and call the play() method for each object.'''

 
# Define the base class player
class player:
    def play(self):
        print("The player is playing cricket.")

# Define the derived class Batsman 
class Batsman(player):
  def play(self):
    print(" The batsman is batting.")

# Define the derived class Bowler 
class Bowler(player):
   def play (self):
     print("The bowler is bowling.")

# Create  objects  of  Batsman and Bowler classes 
batsman = Batsman()
bowler  = Bowler()
# Call the play () method for each object 
batsman.play()
bowler.play()