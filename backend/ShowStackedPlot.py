# ShowHistogram.py
# contains some back-end functionality for writing and displaying histograms to the user
import ROOT as r
from ShowHistogram import histogramsFromFile

def plotStackedHist(dataName, MCNames, hist_id, x_min = 0, x_max = 140e3,
                    y_min = None, y_max = None,title="",x_label="",y_label="Number of entries/bin",
                    nameArray = None, showLegend=True, colourArray=None, 
                    legend_text_size=None,log_y = False):
    
    try:
        # Get DATA histogram
        dataString=dataName.replace("out/","").replace(".root","")
        dataFile = r.TFile.Open("out/"+dataString+".root","READ")
        dataHist = histogramsFromFile(dataFile)[0][hist_id]
        dataHist.SetDirectory(0)
        dataFile.Close()
    
    #Handles Errors
    except ReferenceError: # Occurs when dataName is not correct
        print("File out/"+dataString+".root could not be openned. Check it exists.")
        return None,None
    
    except IndexError: # Occurs when hist_n is too large
        print("hist_n out of range for file: out/"+dataString+".root")
        return None,None
        
     
    # Make a canvas and stacked histogram
    canvasstack = r.TCanvas("canvas" + hist_id)
    hs = r.THStack("hs" + hist_id,"Stacked plot" + hist_id)
    canvasstack.SetCanvasSize(1920, 1080)
    
    
    # Configure and plot the 2lep data
    dataHist.SetTitle(title)
    dataHist.GetXaxis().SetTitle(x_label)
    dataHist.GetYaxis().SetTitle(y_label)
    dataHist.SetStats(0)
    dataHist.SetLineColor(r.kBlack)
    dataHist.SetLineWidth(1)
    dataHist.SetMarkerColor(r.kBlack)
    dataHist.SetMarkerStyle(21)
    dataHist.SetMarkerSize(0.5)
    dataHist.Draw("e")

    # Create a legend
    legend = r.TLegend(0.7,0.60,0.9,0.85)
    
    if colourArray == None:
        colourArray = [r.kBlue,r.kRed,r.kGreen,r.kOrange,r.kTeal,r.kMagenta,r.kGray]
    
    #Loops around each provided MC and stacks onto hs
    for i in range(len(MCNames)):    
        try:
            # Get MC histograms
            MCString=MCNames[i].replace("out/","").replace(".root","")
            file = r.TFile.Open("out/"+MCString+".root","READ")
            mcHist = histogramsFromFile(file)[0][hist_id]
            mcHist.SetDirectory(0)
            file.Close()
        
        # Handles Errors
        except ReferenceError: # Occurs when MCNames[i] is not correct
            print("File out/"+MCString+".root could not be openned. Check it exists.")
            return None,None
    
        except IndexError: # Occurs when hist_id does not exist
            print("hist_id does not exist for file: out/"+MCString+".root")
            return None,None

        # Add MC contributions to the stacked histogram
        mcHist.SetLineColor(colourArray[i%len(colourArray)])
        mcHist.SetFillColor(colourArray[i%len(colourArray)])
        hs.Add(mcHist,"h")
       
        #Add MC histogram to legend
        if nameArray == None:
            legend.AddEntry(mcHist,MCString)
        else:
            legend.AddEntry(mcHist,nameArray[i+1])
        
    # Draw the stacked plot onto the canvas
    hs.Draw("same,hist")
    dataHist.Draw("e,same")
    
    # Edit the x axis range of both stacked plot and data
    hs.GetXaxis().SetRangeUser(x_min,x_max)
    dataHist.GetXaxis().SetRangeUser(x_min,x_max)
    if y_min != None and y_max != None:
        hs.GetYaxis().SetRangeUser(y_min,y_max)
        dataHist.GetYaxis().SetRangeUser(y_min,y_max)
    
    #Add Data histogram to legend
    if nameArray == None:
        legend.AddEntry(dataHist,dataString)
    else:
        legend.AddEntry(dataHist,nameArray[0])
    legend.SetLineWidth(0)
    if legend_text_size != None:
        legend.SetTextSize(legend_text_size)
    legend.Draw("same")
    
    if log_y:
        canvasstack.SetLogy()
    
    # Plot the canvas
    canvasstack.Draw()
    
    #Shows the legend if showLegend == True
    if showLegend:
        return canvasstack,(hs,legend)
    else: # Legend not plotted if not returned
        return canvasstack,hs