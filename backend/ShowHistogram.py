# ShowHistogram.py
# contains some back-end functionality for writing and displaying histograms to the user
import ROOT as r

def histogram(t, weighting, variable, hist_id, n_bins, xmin, xmax, cuts="1", title=None, x_label = None, y_label = "Number of entries/bin",color = r.kBlack):
    
    #DRAW HISTOGRAM using C-style string
    t.Draw(variable+" >>"+hist_id +"("+str(n_bins)+","+str(xmin)+","+str(xmax)+")", weighting+"*("+cuts+")")
    hist = r.gDirectory.Get(hist_id)

    if title == None:
        title = variable+":"+cuts   # Set default title to "Variable:cuts"
    
    if x_label == None:
        x_label = variable   # Set default x-axis label to "Variable"
    
    # Configure histogram before writing
    hist = configureHistogram(hist, title=title, x_label = x_label, y_label = y_label,color = color)
    
    hist.Write() # Writes histograms to the output file.
    # Histograms are automatically plotted in RunAnalysis.py

def configureHistogram(hist,title=None, x_label = None, y_label = None,color = None):
    '''
    For more information on histogram styling see: https://root.cern.ch/root/htmldoc/guides/users-guide/Histograms.html
    '''
    # Set style of histogram.
    if title != None:
        hist.SetTitle(title) # Set histogram title
    if x_label != None:
        hist.GetXaxis().SetTitle(x_label) # Label x axis
    if y_label != None:
        hist.GetYaxis().SetTitle(y_label) # Label y axis
    if color != None:
        hist.SetLineColor(color) # Set the line colour
    
    return hist
    
def plotHistogram(hist, title=None, x_label = None, y_label = None,color = None,log_y=False):
    
    # configure histogram before plotting
    hist = configureHistogram(hist, title=title, x_label = x_label, y_label = y_label,color = color)
    
    # Make canvas with unique name
    canvas = r.TCanvas("canvas_"+hist.GetName())
    canvas.SetCanvasSize(1920, 1080)
    
    # Make y-axis logarithmic
    if log_y:
        canvas.SetLogy()
    
    # Change the histogram directories so that they do not disappear once the root file has been closed
    hist.SetDirectory(0)
    
    # Show 'integral' value in statistics box of all histograms
    # Hide 'name' value in statistics box of all histograms
    r.gStyle.SetOptStat("emruoi") 

    hist.Draw() # Draw histogram

    canvas.Draw() # Show histogram by displaying the canvas
    
    return canvas


def histogramsFromFile(histFile):
    
    # Get list of keys
    hist_keys = histFile.GetListOfKeys()
    
    # Get dictionary of all histograms
    histograms = {}
    printString = ""  #Reminder of IDs
    for key in hist_keys:
        hist = histFile.Get(key.GetName()) # Get histograms
        if hist.InheritsFrom("TH1"): # Check histograms
            histograms[key.GetName()] = hist # Add histograms to array
            printString = printString+'histograms["'+key.GetName()+'"], title: '+hist.GetTitle()+", x-axis: "+hist.GetXaxis().GetTitle()+"\n"
    
    # Reminder of histogram numbers

    # Return histograms from file
    return histograms,printString
