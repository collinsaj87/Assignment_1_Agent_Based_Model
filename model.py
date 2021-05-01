"""
Agent Based Model Package - model.py
------------------------------
This is an agent based model which displays agents moving in an environment and consuming it.
The data is based on using input from a HTML source and from 'in.csv', both containing
coordinate data. 
"""

import tkinter                  # for displaying GUI
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot
import agentframework           # See agentframework.py
import csv                      # For reading in csv file
import matplotlib.animation     # generates animation with x and y axis
import requests                 # allows for import of html data
import bs4                      # allows html data to be parsed into the model

# The below draws in html data for the model. Print is to test it is reading data
r = requests.get('http://www.geog.leeds.ac.uk/courses/computing/practicals/python/agent-framework/part9/data.html')
content = r.text
soup = bs4.BeautifulSoup(content, 'html.parser')
td_y = soup.find_all(attrs={"class" : "y"})
td_x = soup.find_all(attrs={"class" : "x"})
print(td_y)
print(td_x)


num_of_agents = 10              # Dictates the number of agents in the environment
num_of_iterations = 100         # Determines the number of times agent moves position
agents = []                     # Empty list for storing agents
environment = []                # Empty list for the environment data to be read in to
neighbourhood = 20


# Set parameters
fig = matplotlib.pyplot.figure(figsize=(7, 7))
ax = fig.add_axes([0, 0, 1, 1])



# Imports the csv data as the environment and compiles list
with open('in.csv', newline='') as f:
    environment = [] # Establishes a list containing the file data
    # Reads in the csv data and appends to the created lists
    reader = csv.reader(f, quoting=csv.QUOTE_NONNUMERIC)
    for row in reader:
        rowlist = []
        environment.append(rowlist)
        for value in row:
            rowlist.append(value)
            
f.close()

# Make the agents.
for i in range(num_of_agents):
    y = int(td_y[i].text)
    x = int(td_x[i].text)
    agents.append(agentframework.Agent(environment, agents, y, x))

carry_on = True
       

def update(frame_number):
    # Updates the animation through each iteration.
    fig.clear()                         
    global carry_on
    
    # Move the agents, consume from environment and share with neighbours 
    for i in range(num_of_agents):   
           agents[i].move()
           agents[i].eat()
           agents[i].share_with_neighbours(neighbourhood)
           print(type(agents[i].x))       # Test to check storage in agents
      
    # Set a stopping condition for the model to cease when each agent has eaten the input number.
    if agents[i].store >= 1000:
          carry_on = False
          print("Stopping condition")
 
    # Plot the agents on a scatter graph with environment shown.   
    for i in range(num_of_agents):
           matplotlib.pyplot.xlim(0, 99)
           matplotlib.pyplot.ylim(0, 99)
           matplotlib.pyplot.imshow(environment)
           matplotlib.pyplot.scatter(agents[i].x,agents[i].y)   
           # Creates the update function running in the animation variable
           
          
def gen_function(b = [0]):
    # a function to determine the number of iterations in the model
    a = 0
    global carry_on
    while (a < 10) & (carry_on) :
        yield a			# Returns control and waits next call.
        a = a + 1           
           
        
def run():
    # define the action for runnng the model in GUI. 
    animation = matplotlib.animation.FuncAnimation(fig, update, frames=gen_function, 
                                                   repeat=False)
    canvas.draw()

# develop the windows for the GUI
root = tkinter.Tk()
root.wm_title("Model")
canvas = matplotlib.backends.backend_tkagg.FigureCanvasTkAgg(fig, master=root)
canvas._tkcanvas.pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)

# develop the menu to run the model in GUI
menu = tkinter.Menu(root)
root.config(menu=menu)
model_menu = tkinter.Menu(menu)
menu.add_cascade(label="Model", menu=model_menu)
model_menu.add_command(label="Run model", command=run)

tkinter.mainloop()



