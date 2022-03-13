'''
# Analysis.py
# Skeleton code in python provided for you
# In place of this comment you should write [YOUR NAME] -- [THE DATE] and update it as you go!
# Make sure to make backups and comment as you go along :-)
####################################################################################################
Draw Histograms using format:
     -    histogram(t, weighting, variable, hist_id, n_bins, xmin, xmax, cuts="1", title=None, x_label = None, y_label = "Number of entries/bin",color = r.kBlack)
        
Define Selection cuts as Boolean String ["&&" = AND, "||" = OR] e.g.:
     -   selection_cut = "("+"sel_cut1"+"&&"+"("+"sel_cut2"+"||"+"sel_cut3"+")"+")"
    is (sel_cut1 AND (sel_cut2 OR sel_cut3))
    
Define new variable to plot using:
     -   SetAlias("name","formula")
     
####################################################################################################
THIS SCRIPT IS RUN BY RunAnalysis.py SO CODE ADJUSTMENTS SHOULD BE MADE HERE.
FOR MORE PLOTTING EXAMPLES SEE ExampleAnalysis.py 
'''
#Allow python to use ROOT
import ROOT as r
from ShowHistogram import histogram

def Analyse(t,weighting):
    
    t.SetAlias("Mll","sqrt(2 * lep_pt[0] * lep_pt[1] * (cosh(lep_eta[0]-lep_eta[1]) - cos(lep_phi[0]-lep_phi[1])) )")
    t.SetAlias("Pt_tot","(lep_pt[0] * lep_pt[0] + lep_pt[1] * lep_pt[1] + 2 *cos(lep_phi[0]-lep_phi[1]) *lep_pt[0] *lep_pt[1]) ^ 0.5")
    
    lepcuts = "lep_n == 2 && lep_charge[0]*lep_charge[1] == -1 && lep_type[0] == 13 && lep_type[1] == 13"
    etacuts = "lep_eta[0] >=-2.4 && lep_eta[0] <=2.4 && lep_eta[1] >=-2.4 && lep_eta[1] <=2.4"
    ptcuts = "lep_pt[0] >= 30e3 && lep_pt[1] >= 30e3" #&& lep_pt[0] <= 76e3 && lep_pt[1] <= 76e3
    pttotcuts = "Pt_tot < 200e3"
    masscuts = "Mll >= 66e3 " #&& Mll < 119e3
    conecuts = "lep_ptcone30[0] < 4000 && lep_ptcone30[1] < 4000 && lep_etcone20[0] < 5000 && lep_etcone20[1] < 5000"
    
    multicuts = "(" + lepcuts + "&&" + etacuts +"&&" + ptcuts  +"&&" + masscuts +"&&" + conecuts +"&&" + pttotcuts +")"
    #multicuts = "(" + lepcuts + "&&" + etacuts + ")"
    inversecuts_pt = "(" + lepcuts + "&&" + etacuts + "&& (lep_pt[0] < 20e3 || lep_pt[1] < 20e3)" + ")"
    inversecuts_pttot = "(" + lepcuts + "&&" + etacuts + "&& (Pt_tot > 200e3)" + ")"
    inversecuts_ptcone = "(" + lepcuts + "&&" + etacuts + "&& (lep_ptcone30[0] > 4000 || lep_ptcone30[1] > 4000)" + ")"
    inversecuts_etcone = "(" + lepcuts + "&&" + etacuts + "&& (lep_etcone20[0] > 5000 || lep_etcone20[1] > 5000)" + ")"
    
    
    #EXAMPLE 1: histogram of number of leptons per event
    histogram(t=t, weighting = weighting,
              variable = "lep_n", hist_id = "h_lep_n",
              n_bins=10, xmin=-0.5, xmax=9.5,
              cuts="1",
              title = "lep_n:1", x_label = "lep_n", y_label = "lep_n",
              color = r.kBlack)
        # Plots histogram of number of leptons between range -0.5 to 9.5 with 10 bins
        # No selection cuts are used ("1")
        # Arguments 'cuts','title','x_label','y_label' and 'color' are OPTIONAL arguments
    
    #-------------------------------------------------------------------------------
        
    #EXAMPLE 2: Using Selection Cuts
        # Selection cuts can be used to plot only event that pass certain conditions.
        # Use 'cuts' argument in histogram(...)

    #histogram(t=t, weighting = weighting,
    #          variable = "lep_pt[0]",  hist_id = "h_lep_pt0",
    #          n_bins=200, xmin=0, xmax=140e3,
    #          cuts= lepcuts)
    #histogram(t=t, weighting = weighting,
    #          variable = "lep_pt[1]",  hist_id = "h_lep_pt1",
    #          n_bins=200, xmin=0, xmax=140e3,
    #          cuts= lepcuts)
    
    histogram(t=t, weighting = weighting,
              variable = "lep_pt",  hist_id = "h_lep_pt",
              n_bins=200, xmin=0, xmax=150e3,
              cuts= multicuts)
    
    histogram(t=t, weighting = weighting,
              variable = "Mll",  hist_id = "h_lep_m",
              n_bins=200, xmin=60e3, xmax=140e3,
              cuts= multicuts,
              title="Invariant Mass of System")
    
    #histogram(t=t, weighting = weighting,
    #          variable = "lep_eta",  hist_id = "h_lep_eta",
    #          n_bins=200, xmin=-2.5, xmax=2.5,
    #          cuts= multicuts,
    #          title="pseudo-rapidity lep_eta")
    
    #histogram(t=t, weighting = weighting,
    #          variable = "lep_ptcone30",  hist_id = "h_lep_ptcone",
    #          n_bins=200, xmin=0, xmax=6e3,
    #          cuts= multicuts, title="ptcone30")
    
    #histogram(t=t, weighting = weighting,
    #          variable = "lep_etcone20",  hist_id = "h_lep_etcone",
    #          n_bins=200, xmin=-3e3, xmax=10e3,
    #          cuts= multicuts, title="etcone20")
    
    histogram(t=t, weighting = weighting,
              variable = "Pt_tot",  hist_id = "h_lep_pt_tot",
              n_bins=250, xmin=-3e3, xmax=180e3,
              cuts= multicuts, title="lep_Pt_tot")
    
    #inverse cuts
    
    histogram(t=t, weighting = weighting,
              variable = "Mll",  hist_id = "h_lep_mll_cutpt",
              n_bins=250, xmin=0, xmax=140e3,
              cuts= inversecuts_pt, title="lep_mll_cutpt")
    histogram(t=t, weighting = weighting,
              variable = "Mll",  hist_id = "h_lep_mll_cutpttot",
              n_bins=250, xmin=0, xmax=220e3,
              cuts= inversecuts_pttot, title="lep_mll_cutpttot")
    histogram(t=t, weighting = weighting,
              variable = "Mll",  hist_id = "h_lep_mll_cutptcone",
              n_bins=250, xmin=0, xmax=140e3,
              cuts= inversecuts_ptcone, title="lep_mll_cutptcone")
    histogram(t=t, weighting = weighting,
              variable = "Mll",  hist_id = "h_lep_mll_cutetcone",
              n_bins=250, xmin=0, xmax=140e3,
              cuts= inversecuts_etcone, title="lep_mll_cutetcone")
    
    

# For a list of predefined variable names see: http://opendata.atlas.cern/release/2020/documentation/datasets/dataset13.html
