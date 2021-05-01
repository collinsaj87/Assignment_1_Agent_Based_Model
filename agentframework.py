"""
Agent Based Model Package - agentframework.py
------------------------------
This creates the agents and their associated behaviours that are to
be run in the model.py.
"""


import random

class Agent():
    """
    This class is used to create the agent that will move within the environment, 
    consume it, and interact with any in proximity. 
    
    ...
    
    Methods
    ----------
    move()
        Moves in the agent one step on the x and y axis. 
        
    eat()
        Consumes ten units of the environment if available and adds to agent
        
    share_with_neighbours(neighbourhood)
        Evaluate distance between agents and share resources
    """
    
    def __init__(self, environment, agents, td_y, td_x):
        """
        Gives agents the labels x and y, sets the start location and
        determines intial position of y and x using web scrape to initialise.
        Environment data is imported from a csv file as the values that can be
        consumed by agents. 
        
        Parameters
        -----------
        environment : list
            empty list to receive integer raster data values of the environment
            from in.csv
            
        agents : list
            an empty list to receive integer data for the position of the 
            agents for the number of agents specified in num__of_agents in
            model.py
            
        td_y : int
            an integer denoting the y axis position of the agent, derived from 
            bs4 html parsing
            
        td_x : int
            an integer denoting the x axis position of the agent, derived from 
            bs4 html parsing
        """
        if (td_y == None):
            # accounts for the possibility of empty cells in imported data
            # if data cell is empty than random integer applied for the position
            self._y = random.randint(0, 100)
        else:
            self._y = td_y
        if (td_x == None):
            self._x = random.randint(0, 100)
        else:
            self._x = td_x
        self.environment = environment     
        self.agents = agents
        self.store = 0
        
            
    #Property get and set to protect variables
    def gety(self):
        return self._y
        
    def sety(self, value):
        self._y = value 
            
    def dely(self):
        del self._y
            
    y = property(gety, sety, dely, "I'm the 'y' property.")
        
    def getx(self):
        return self._x
        
    def setx(self, value):
        self._x = value 
            
    def delx(self):
        del self._x
            
    x = property(getx, setx, delx, "I'm the 'x' property.")
    
    def move(self):
        """
        Moves the x and y position of agents based on the result of a randomly
        generated float and corrected for torus environment.
        """
        if random.random() < 0.5:
            self._y = (self._y + 1) % 100 
        else:
            self._y = (self._y - 1) % 100
            
        if random.random() < 0.5:
            self._x = (self._x + 1) % 100 
        else:
            self._x = (self._x - 1) % 100
            
    
    def eat(self):                                 
        """
        Creates a method to eat 10 units of the environment if the amount of
        environment data is greater than 10
        """ 
        if self.environment[self.y][self.x] > 10:
            self.environment[self.y][self.x] -= 10
            self.store += 10
            
            
    def share_with_neighbours(self, neighbourhood):
        """
        Method to share information with each agent and share resources
        using neighbourhood data to evaluate an agent as nearby. 
        
        Parameters
        ----------
        neighbourhood : int
            a hardwired integer in model.py that sets the parameters for another
            agent being considered a neighbour.
        """
        self.neighbourhood = neighbourhood
        for agent in self.agents:                   
        # Loops through created agents list
            distance = self.distance_between(agent)
            if distance <= self.neighbourhood:      
            # Evaluates the distance compared to neighbourhood variable
                sum = self.store + agent.store
                average = sum / 2
                self.store = average
                agent.store = average
               # print("sharing " + str(distance) + " " + str(average))
            
    def distance_between(self, agents):
        """
        Calculates the pythagorean distance between two agents in the model.
        
        Parameters
        ----------
        agents : list
            a list that now contains the x and y coordinates of the specified 
            number of agents from num_of_agents in model.py
            
        Returns
        ----------
        float
            a float of the distance between agents.
        """
        return (((self._x - agents._x)**2) +((self._y - agents._y)**2))**0.5
        
        
       
        

            
            
    
        
            
       
            
            
        
        
        