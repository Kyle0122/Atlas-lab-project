# Atlas-lab-project
Using ROOT and python to analyze data from Atlas

In this Lab, students on need to edit Analysis.py and LabNotebook.ipynb

The rest of the code is run from these files or behind the scenes.

For those who are curious about the details of the other files, please see below.

######################################################################################    

Analysis.py - Defines histograms to be plotted when RunAnalysis.py is called in the LabNotebook.ipynb

LabNotebook.ipynb - Runs all the other scripts. This is where histograms will be viewed.

RunAnalysis.py - Runs the Analysis.py file creating the histograms and '.root' files in the '/out' folder

ExampleAnalysis.py - Contains useful examples that can be modified and copied to the Analysis.py file.
                   - This script is never actually run, but should be useful as a guide to making more sophisticated plots.

TotExpected.py - This file prints the total number of expected events for MC simulations
               - It can be run using the command "import TotExpected" when you are running the LabNotebook.ipynb
    
######################################################################################  

BACKEND FILES:

dataSets.py - Defines string codes which can be used to run different MC simulations

Draw.py - Called by RunAnalysis.py. Creates output '.root' file and gets the TTree object to send to Analysis.py.

getInput.py - Called by RunAnalysis.py
            - Gets the users input for which string codes to run and validates them
            - Gets the user input to determine whether the 1% or the full data set should be run

infofile.py - Contains information about the defined MC simulations

ShowHistogram.py - Contains backend code to plot, edit and retrieve histograms
                 - Also used when defining histograms in Analysis.py
                 
ShowStackedPlot.py - Contains backend code to plot and configure stacked histograms

