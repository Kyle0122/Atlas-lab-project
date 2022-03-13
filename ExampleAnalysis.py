'''
# ExampleAnalysis.py
# Skeleton code in python provided for you
####################################################################################################
Draw Histograms using format:
     -    histogram(t, weighting, variable, hist_id, n_bins, xmin, xmax, cuts="1", title=None, x_label = None, y_label = "Number of entries/bin",color = r.kBlack)
        
Define Selection cuts as Boolean String ["&&" = AND, "||" = OR] e.g.:
     -   selection_cut = "("+"sel_cut1"+"&&"+"("+"sel_cut2"+"||"+"sel_cut3"+")"+")"
    is (sel_cut1 AND (sel_cut2 OR sel_cut3))
    
Define new variable to plot using:
     -   SetAlias("name","formula")
     
####################################################################################################
THIS FILE CONTAINS MORE EXAMPLES THAN IN Analysis.py, BUT IS NOT RUN BY RunAnalysis.py.
TO USE THE CODE IT NEEDS TO BE COPIED INTO Analysis.py
'''
# allow python to use ROOT
import ROOT as r
from ShowHistogram import histogram

def Analyse(t,weighting):

    #EXAMPLE 1: histogram of number of leptons per event
    histogram(t=t, weighting = weighting,
              variable = "lep_n",hist_id = "h_lep_n",
              n_bins=10, xmin=-0.5, xmax=9.5,
              cuts="1",
              title = "lep_n:1", x_label = "lep_n", y_label = "lep_n",
              color = r.kBlack)
        # Plots histogram of number of leptons between range -0.5 to 9.5 with 10 bins
        # No selection cuts are used ("1")
        # Arguments 'cuts','title','x_label','y_label' and 'color' are OPTIONAL arguments
    
    #-------------------------------------------------------------------------------
    
    #EXAMPLE 2: histogram of the "lepton type" of every lepton in every event
    histogram(t=t, weighting = weighting,
              variable = "lep_type",hist_id = "h_lep_type",
              n_bins=10, xmin=7.5, xmax=17.5,
              title = "Lepton Type", x_label = "Lepton Type")
        # Note: lepton type takes the value 11 for electrons and 13 for muons
    
    #-------------------------------------------------------------------------------

    #EXAMPLE 3: Using Selection Cuts
        # Selection cuts can be used to plot only events that pass certain conditions.
        # Use 'cuts' argument in histogram(...)

        #e.g. Transverse momentum of ALL leptons for events with 3 leptons:
    histogram(t=t, weighting = weighting,
              variable = "lep_pt", hist_id = "h_lep_pt",
              n_bins=200, xmin=0, xmax=140e3,
              cuts= "(lep_n ==3)")
    
        #e.g. Transverse momentum of a SINGLE lepton (lepton [0]) for events with 3 leptons:
    histogram(t=t, weighting = weighting,
              variable = "lep_pt[0]",  hist_id = "h_lep_pt_0",
              n_bins=200, xmin=0, xmax=140e3,
              cuts= "(lep_n ==3)")
        #Note: lep_n ==3 so lep_pt[3],lep_pt[4]...etc will create empty histograms

    #-------------------------------------------------------------------------------

    #EXAMPLE 4: Defining variables to plot
        # It is also possible to plot calculated quantities
        #Intermediate calculations can be performed using the function: SetAlias("name","formula") 
        # Use standard Python variable naming rules for "name" i.e. alphanumeric characters and '_' only
        
        # e.g. the average transverse momenta of leptons in each event:
    t.SetAlias("meanPt","Sum$(lep_pt)/Length$(lep_pt)") # define meanPt
    histogram(t=t, weighting = weighting,
              variable = "meanPt",hist_id = "h_meanPt",
              n_bins=200, xmin=0, xmax=140e3,
              title = "Mean Pt")
# For more information see https://root.cern.ch/doc/master/classTTree.html#a73450649dc6e54b5b94516c468523e45
# and https://root.cern.ch/doc/master/classTTree.html#a7c505db0d8ed56b5581e683375eb78e1

    #-------------------------------------------------------------------------------

    #EXAMPLE 5: More complicated selection cuts and dummy arguments
        # It can be useful to define selection cuts that can take input arguments - here is an example
    
        # Define selection cuts for each lepton
    lepCut = "lep_pt[{0}] > 20e3  && lep_type[{0}]=={1}"
        # Note: "{0}" and "{1}" are dummy arguments. Their values are specified on use using lepCut.format(...) 
    numCut = "(lep_n=={0})"
        # Require 2 leptons [0] and [1], each satisfy the specified selection cuts 
    selCutsE = "(" + lepCut.format(0,11) + "&&" + lepCut.format(1,11) + "&&" + numCut.format(2)+ ")"
    
        # e.g. Average of the pseudorapidity of electrons in two electron events
    histogram(t=t, weighting = weighting,
              variable = "(lep_eta[0]+lep_eta[1])/2.0",hist_id = "h_meanEta",
              n_bins=100, xmin=-3.0, xmax=3.0,
              cuts= selCutsE,
              title = "Mean Pseudorapidity")
        #Note: lep_eta is an array of pseudorapidities. lep_eta[0] and lep_eta[1] are the pseudorapidities for the two electrons
        
    #-------------------------------------------------------------------------------
    
    #EXAMPLE 6: Using TMath functions
        #For more complicated functions (e.g. trig functions). Use TMATH:: syntax.
    histogram(t=t, weighting = weighting,
              variable = "TMath::ACosH(lep_phi[0])",hist_id = "h_TMath",
              n_bins=100, xmin=0.0, xmax=2.5,
              cuts= selCutsE,
              title = "test")       
        #For more TMath functions see: https://root.cern.ch/root/html524/TMath.html#TMath:ACosH
    #-------------------------------------------------------------------------------

