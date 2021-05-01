Assignment 1: Agent Based Model
================================

The Agent Based Model
----------------------

This model creates a representation of agents moving in a torus environment and consuming units of the environment until they are 'full'. 
On running the model the user is presented with an interface and a menu in which they may select to run the model. On running the model 
the agents will initialise based on data gained from web scraping and move and eat until they have consumed a predetermined amount of the environment
or until the iterations are completed. This model may be run continuously with the agents restarting the next run from their final positions 
the last time the model was run. 


<p>The model consists of two files:</p>
  <li>model.py</li>
  <li>agentframework.py</li>
  
  

Model.py
--------

This contains the elements that run the model and draw in the required data. Contained within this is the code to initiate lists of
variables that will alter after the execution of movements and consumption within the environments. This also contains the code to establish
the graphical user interface which allows a user to run the model. 


Agentframework.py
-----------------

This contains the code for the Agent class, initialising the agents and giving them their behaviour with regards to movement, consuming the 
environment and communicating with other agents. 
