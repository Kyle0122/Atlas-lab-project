import ROOT as r
from ShowHistogram import histogram

def Analyse(t,weighting):
    
    t.SetAlias("M01","(2 * lep_pt[0] * lep_pt[1] * (cosh(lep_eta[0]-lep_eta[1]) - cos(lep_phi[0]-lep_phi[1])) )")
    t.SetAlias("M02","(2 * lep_pt[0] * lep_pt[2] * (cosh(lep_eta[0]-lep_eta[2]) - cos(lep_phi[0]-lep_phi[2])) )")
    t.SetAlias("M03","(2 * lep_pt[0] * lep_pt[3] * (cosh(lep_eta[0]-lep_eta[3]) - cos(lep_phi[0]-lep_phi[3])) )")
    t.SetAlias("M12","(2 * lep_pt[1] * lep_pt[2] * (cosh(lep_eta[1]-lep_eta[2]) - cos(lep_phi[1]-lep_phi[2])) )")
    t.SetAlias("M13","(2 * lep_pt[1] * lep_pt[3] * (cosh(lep_eta[1]-lep_eta[3]) - cos(lep_phi[1]-lep_phi[3])) )")
    t.SetAlias("M23","(2 * lep_pt[2] * lep_pt[3] * (cosh(lep_eta[2]-lep_eta[3]) - cos(lep_phi[2]-lep_phi[3])) )")
    t.SetAlias("Mllll", "sqrt(M01 + M02 + M03 + M12 + M13 + M23)")
    t.SetAlias("Pt_tot","(lep_pt[0] * lep_pt[0] + lep_pt[1] * lep_pt[1] + 2 *cos(lep_phi[0]-lep_phi[1]) *lep_pt[0] *lep_pt[1]) ^ 0.5")
    
    lepcuts = "lep_n == 4" #&& lep_type[0]==13 && lep_type[1]==13
    #chargecuts = "((lep_charge[0]+lep_charge[1]==0 && lep_charge[2]+lep_charge[3]==0) || (lep_charge[0]+lep_charge[2]==0 && lep_charge[1]+lep_charge[3]==0) || (lep_charge[0]+lep_charge[3]==0 && lep_charge[1]+lep_charge[2]==0))"
    chargecuts = "lep_charge[0] + lep_charge[1] + lep_charge[2] + lep_charge[3] ==0"
    etacuts = "lep_eta[0] >=-2.4 && lep_eta[0] <=2.4 && lep_eta[1] >=-2.4 && lep_eta[1] <=2.4 && lep_eta[2] >=-2.4 && lep_eta[2] <=2.4 && lep_eta[3] >=-2.4 && lep_eta[3] <=2.4"
    ptcuts = "lep_pt[1] <= 40e3 && lep_pt[2] <= 40e3 && lep_pt[3] <= 40e3"#lep_pt[0] <= 20e3  && 
    masscuts = "Mllll >= 100e3 && Mllll <= 150e3"
    ptconecuts = "lep_ptcone30[0] < 1000 && lep_ptcone30[1] < 1000 && lep_ptcone30[2] < 1000 && lep_ptcone30[3] < 1000"
    etconecuts = "lep_etcone20[0] < 2500 && lep_etcone20[1] < 2500 && lep_etcone20[2] < 2500 && lep_etcone20[3] < 2500"
    
    #multicuts = "(" + lepcuts +"&&" + chargecuts +"&&" + etacuts + ")" #+"&&" + conecuts +"&&" + masscuts +"&&"+ ptcuts
    multicuts = "(" + lepcuts +"&&" + chargecuts +"&&" + etacuts +"&&" + masscuts +"&&"+ ptcuts +")"
    
    #-------------------------------------------------------------------------------
    
    histogram(t=t, weighting = weighting,
              variable = "Mllll",  hist_id = "h_lep_m",
              n_bins=100, xmin=100e3, xmax=150e3,
              cuts= multicuts,
              title="Invariant Mass of System - delta mass")
    
    histogram(t=t, weighting = weighting,
              variable = "lep_pt[0]",  hist_id = "h_lep_pt0",
              n_bins=200, xmin=0, xmax=180e3,
              cuts= lepcuts + "&&" + chargecuts +"&& !lep_trigMatched")
    histogram(t=t, weighting = weighting,
              variable = "lep_pt[1]",  hist_id = "h_lep_pt1",
              n_bins=200, xmin=0, xmax=180e3,
              cuts= lepcuts + "&&" + chargecuts +"&& !lep_trigMatched")
    histogram(t=t, weighting = weighting,
              variable = "lep_pt[2]",  hist_id = "h_lep_pt2",
              n_bins=200, xmin=0, xmax=180e3,
              cuts= lepcuts + "&&" + chargecuts +"&& !lep_trigMatched")
    histogram(t=t, weighting = weighting,
              variable = "lep_pt[3]",  hist_id = "h_lep_pt3",
              n_bins=200, xmin=0, xmax=180e3,
              cuts= lepcuts + "&&" + chargecuts +"&& !lep_trigMatched")
    
    
    

# For a list of predefined variable names see: http://opendata.atlas.cern/release/2020/documentation/datasets/dataset13.html
