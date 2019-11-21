from ROOT import *
from array import array
import os
from tdrStyle import *
setTDRStyle()

from paraConfigurations import *

import argparse
def ParseOption():

    parser = argparse.ArgumentParser(description='submit all')
    parser.add_argument('-t', dest='tag', type=str, help='for each plot')

    args = parser.parse_args()
    return args

args=ParseOption()

tag = args.tag
paraConfig = paraConfigs[tag]

rootPath1 = paraConfig['rootPath1']
rootPath2 = paraConfig['rootPath2']
rootfile1 = paraConfig['rootfile1']
rootfile2 = paraConfig['rootfile2']
tree1 = paraConfig['tree1']
tree2 = paraConfig['tree2']
binInfo = paraConfig['binInfo']
vars1 = paraConfig['vars1']
vars2 = paraConfig['vars2']
cuts1 = paraConfig['cuts1']
cuts2 = paraConfig['cuts2']
weight1 = paraConfig['weight1']
weight2 = paraConfig['weight2']
xTitle = paraConfig['xTitle']
yTitle = paraConfig['yTitle']
legend1 = paraConfig['legend1']
legend2 = paraConfig['legend2']
savePath = paraConfig['savePath']
saveName = paraConfig['saveName']
latexNote1 = paraConfig['latexNote1']
latexNote2 = paraConfig['latexNote2']
doFit = paraConfig['doFit']
pdfName = paraConfig['pdfName']
#color1 = paraConfig['color1']
#gauss.paramOn(xframe, RooFit.Layout(0.17, 0.3, 0.9), RooFit.Format("NE", RooFit.FixedPrecision(2)))
f1 = TFile(rootPath1 + rootfile1, 'READ')
f2 = TFile(rootPath2 + rootfile2, 'READ')

t1 = f1.Get(tree1)
t2 = f2.Get(tree2)

hists1 = [ TH1F('hist1_'+str(i),'', binInfo[0], binInfo[1], binInfo[2]) for i in range(len(vars1)) ]
hists2 = [ TH1F('hist2_'+str(i),'', binInfo[0], binInfo[1], binInfo[2]) for i in range(len(vars2)) ]

HIST1 = TH1F('HIST1', '', binInfo[0], binInfo[1], binInfo[2])
HIST2 = TH1F('HIST2', '', binInfo[0], binInfo[1], binInfo[2])
hs = THStack("hs","")
hs2 = THStack("hs2","")
for i in range(len(vars1)):
    t1.Project(hists1[i].GetName(), vars1[i], weight1[i]+"*"+cuts1[i])
    if i == 0:
       HIST1 = hists1[0].Clone()
    else:
       HIST1.Add(hists1[i])
for i in range(len(vars2)):
    t2.Project(hists2[i].GetName(), vars2[i], weight2[i]+"*"+cuts2[i])
    if i == 0:
       HIST2 = hists2[0].Clone()
    else:
       HIST2.Add(hists2[i])

w = RooWorkspace('w')

xmin = binInfo[1]
xmax = binInfo[2]

w.factory('Gaussian::gauss(x[' + str(xmin) + ',' + str(xmax) + '],meanGauss[0,-1,1],sigmaGauss[0.01,0,0.1])')
w.factory('BreitWigner::bw(x[' + str(xmin) + ',' + str(xmax) + '],meanBW[91.2, 90, 92],sigmaBW[2.5,2,3])')
#w.factory('BreitWigner::bw(x[' + str(xmin) + ',' + str(xmax) + '],meanBW[91.2],sigmaBW[2.406])')
w.factory('DoubleCB::doubleCB(x[' + str(xmin) + ',' + str(xmax) + '], \
                              meanDCB[125,124,126], sigmaDCB[1.75,0,10], \
                              alphaDCB[1,0,5], nDCB[1,0,20], alpha2[1,0,5], n2[1,0,20])')
w.factory('CBShape::singleCB(x[' + str(xmin) + ',' + str(xmax) + '], \
                            meanCB[0,-1.5,1.5], sigmaCB[0.1,0,10], alphaCB[1,0,50], nCB[1,0,50])')
w.factory("Exponential::bkg(x, tau[0.1,-1,1])")

w.var('x').setBins(1000, 'fft')
w.factory('FCONV::BWxCB(x,bw,singleCB)')
w.factory('FCONV::BWxDCB(x,bw,doubleCB)')
w.factory('SUM:model(fsig[0.9,0.7,1]*BWxCB, bkg)')

HIST2.Scale(1/HIST2.Integral()*HIST1.Integral())

dataHist1 = RooDataHist('dataHist1', 'dataHist1', RooArgList(w.var('x')), HIST1, 1)
dataHist2 = RooDataHist('dataHist2', 'dataHist2', RooArgList(w.var('x')), HIST2, 1)

meanReco = ''
meanRefit = ''
sigmaReco = ''
sigmaRefit = ''

if doFit:


   pdf = w.pdf(pdfName)
   fFit = pdf.fitTo(dataHist1)

   meanReco += str('{:.2f}'.format(round(w.var('meanDCB').getVal(),2))) + ' #pm ' + str(round(w.var('meanDCB').getError(),2))
   sigmaReco += str('{:.2f}'.format(round(w.var('sigmaDCB').getVal(),2)))# + ' #pm ' + str(round(w.var('sigmaDCB').getError(),2))

   xframe = w.var('x').frame(RooFit.Title(xTitle))

   dataHist1.plotOn(xframe, RooFit.MarkerStyle(20), RooFit.MarkerColor(1), RooFit.MarkerSize(1), RooFit.Name("data1"),RooFit.LineWidth(1))
   pdf.plotOn(xframe, RooFit.LineColor(1), RooFit.LineWidth(3), RooFit.Name("pdf1") , RooFit.LineStyle(1))
   if pdfName == 'model':
      pdf.plotOn(xframe, RooFit.LineColor(1), RooFit.LineWidth(2), RooFit.Components("bkg"), RooFit.LineStyle(kDashed), RooFit.Name("pdf1"))
#   pdf.paramOn(xframe, RooFit.Layout(0.15, 0.42, 0.7), RooFit.Format("NE", RooFit.FixedPrecision(4)))


   fFit = pdf.fitTo(dataHist2)

   meanRefit += str('{:.2f}'.format(round(w.var('meanDCB').getVal(),2))) + ' #pm ' + str(round(w.var('meanDCB').getError(),2))
   sigmaRefit += str('{:.2f}'.format(round(w.var('sigmaDCB').getVal(),2)))# + ' #pm ' + str(round(w.var('sigmaDCB').getError(),2))

   dataHist2.plotOn(xframe, RooFit.MarkerStyle(20), RooFit.MarkerColor(TColor.GetColor(color1)), RooFit.MarkerSize(1), RooFit.Name("data2"), RooFit.LineColor(TColor.GetColor(color1)), RooFit.LineWidth(1))
   pdf.plotOn(xframe, RooFit.LineColor(TColor.GetColor(color1)), RooFit.LineWidth(3),  RooFit.Name("pdf2") )
   if pdfName == 'model':
      pdf.plotOn(xframe, RooFit.LineColor(2), RooFit.LineWidth(2), RooFit.Components("bkg"), RooFit.LineStyle(kDashed), RooFit.Name("pdf2"))
#   pdf.paramOn(xframe, RooFit.Layout(0.65, 0.92, 0.7), RooFit.Format("NE", RooFit.FixedPrecision(4)))

   yMax_doFit = max(HIST1.GetMaximum()*1.2,HIST2.GetMaximum()*1.2)
   
HIST1.Sumw2()
HIST2.Sumw2()
HIST1.Scale(1/HIST1.Integral())
HIST2.Scale(1/HIST2.Integral())
###
for i in range(len(vars1)):
   hists1[i].Sumw2()
   hists1[i].Scale(1/hists1[i].Integral())
   hists1[i].SetLineColor(1)
for i in range(len(vars1)):
   hists2[i].Sumw2()
   hists2[i].Scale(1/hists2[i].Integral())
   hists2[i].SetLineColor(2)
## 
c1 = TCanvas("c1", "c1", 800, 800)
c1.SetLeftMargin(0.15)
#c1.SetLogy()
#pad1 = TPad("pad1", "pad1", 0, 0.3, 1, 1.0)
#pad1.SetBottomMargin(0)
#pad1.SetGridx()
#pad1.Draw()
#pad1.cd()
#pad1.SetLogy()

dummy = TH1D("dummy","dummy",1,binInfo[1],binInfo[2])
dummy.SetMinimum(0)
yMax1 = HIST1.GetMaximum()*1.2
yMax2 = HIST2.GetMaximum()*1.2
yMax = max(yMax1,yMax2)
if not doFit:
   dummy.SetMaximum(yMax)
else:
   dummy.SetMaximum(yMax_doFit)
dummy.SetLineColor(0)
dummy.SetMarkerColor(0)
dummy.SetLineWidth(0)
dummy.SetMarkerSize(0)
dummy.GetYaxis().SetTitle(yTitle)
dummy.GetYaxis().SetTitleOffset(1.4)
dummy.GetXaxis().SetTitle(xTitle)
#dummy.GetXaxis().SetLableOffset(1.2)
dummy.Draw()

if not doFit:
   #HIST1.Draw('hist same')
   #HIST2.Draw('hist same')
   for i in range(len(vars1)):
      hists1[i].SetLineColor(1)
      hs.Add(hists1[i])
   for i in range(len(vars2)):
      hists2[i].SetLineColor(2)
      hs2.Add(hists2[i])
   #hs.Draw()
   hs2.Draw()
   hs2.GetYaxis().SetTitle(yTitle)
   hs2.GetYaxis().SetTitleOffset(1.4)
   hs2.GetXaxis().SetTitle(xTitle)
   c1.Modified()
else:
   xframe.Draw('same')

HIST1.SetLineColor(1)
HIST2.SetLineColor(2)
HIST1.SetLineWidth(1)
HIST2.SetLineWidth(1)

legend = TLegend(0.5,0.8,0.85,0.9)
legend.AddEntry(HIST1, legend1, 'l')
legend.AddEntry(HIST2, legend2, 'l')
#legend.SetHeader("No m_{Z_{1}} constraint:")

#l1 = legend.AddEntry(xframe.findObject("data1"), "Simulation", 'pe1')
#l2 = legend.AddEntry(xframe.findObject("pdf1"), "Parametric Model", 'l')

#l3 = legend.AddEntry(xframe.findObject("data2"), "Simulation (with m_{Z1} constraint)", 'pe1')
#l4 = legend.AddEntry(xframe.findObject("pdf2"), "Parametric Model (#sigma_{dCB}^{m\'_{4#mu}} = " + sigmaRefit + " GeV)", 'l')
#l3.SetTextColor(TColor.GetColor(color1))
#l4.SetTextColor(TColor.GetColor(color1))
legend.SetTextSize(0.04)
legend.SetLineWidth(2)
legend.SetFillColor(0)
legend.SetBorderSize(0)
legend.Draw('SAME')

#legend2 = TLegend(0.2,0.4,0.42,0.55)
#legend.AddEntry(HIST1, legend1, 'l')
#legend.AddEntry(HIST2, legend2, 'l')
#l1 = legend.AddEntry(xframe.findObject("data1"), "Simulation (no m_{Z1} constraint)", 'pe1')
#l2 = legend.AddEntry(xframe.findObject("pdf1"), "Parametric Model (#sigma_{dCB}^{m_{4#mu}} = " + sigmaReco + " GeV)", 'l')
#legend2.SetHeader("No m_{Z_{1}} constraint")
#l3 = legend2.AddEntry(xframe.findObject("data2"), "Simulation", 'pe1')
#l4 = legend2.AddEntry(xframe.findObject("pdf2"), "Parametric Model", 'l')
#l3.SetTextColor(TColor.GetColor(color1))
#l4.SetTextColor(TColor.GetColor(color1))
#legend2.SetTextSize(0.03)
#legend2.SetLineWidth(2)
#legend2.SetFillColor(0)
#legend2.SetBorderSize(0)
#legend2.Draw('SAME')

'''
latex = TLatex()
latex.SetNDC()
latex.SetTextSize(0.6*c1.GetTopMargin())
latex.SetTextFont(42)
latex.SetTextAlign(11)

latex.SetTextColor(1)
#latex.DrawLatex(0.15, 0.85, 'mean_{DCB} = ' + meanReco + ', sigma_{DCB} = ' + sigmaReco + ' (Reco)')
latex.DrawLatex(0.64, 0.85, '#sigma_{dCB}^{m_{4#mu}} = ' + sigmaReco + ' GeV')
latex.DrawLatex(0.2, 0.85, 'H #rightarrow ZZ #rightarrow 4#mu')
latex.DrawLatex(0.2, 0.78, 'm_{H} = 125 GeV')
#latex.SetTextColor(TColor.GetColor(color1))
#latex.DrawLatex(0.15, 0.78, 'mean_{DCB} = ' + meanRefit + ', sigma_{DCB} = ' + sigmaRefit + ' (Refit)')
latex.DrawLatex(0.64, 0.78, '#sigma_{dCB}^{m\'_{4#mu}} = ' + sigmaRefit + ' GeV')

latex.DrawLatex(0.45, 0.85, latexNote1)
if len(latexNote2) > 0:
   latex.DrawLatex(0.45, 0.75, latexNote2)

c1.cd()
pad2 = TPad("pad2", "pad2", 0, 0.05, 1, 0.3)
pad2.SetTopMargin(0)
pad2.SetBottomMargin(0.2)
pad2.SetGrid()
pad2.Draw()
pad2.cd()
#make ratio plot
ratio = HIST1.Clone("ratio")
ratio.SetMinimum(0.6)
ratio.SetMaximum(1.4)
#ratio.Sumw2()
ratio.SetStats(0)
ratio.Divide(HIST2)
ratio.SetMarkerStyle(20)
ratio.Draw('e1p')
ratio.SetTitle("")
ratio.GetYaxis().SetTitle("black/red ratio")
ratio.GetXaxis().SetTitle(xTitle)
ratio.GetYaxis().SetTitleSize(30)
ratio.GetYaxis().SetTitleFont(43)
ratio.GetYaxis().SetTitleOffset(1.75)
ratio.GetYaxis().SetLabelFont(43)
ratio.GetYaxis().SetLabelSize(25)
ratio.GetXaxis().SetTitleSize(30)
ratio.GetXaxis().SetTitleFont(43)
ratio.GetXaxis().SetTitleOffset(4.)
ratio.GetXaxis().SetLabelFont(43)
ratio.GetXaxis().SetLabelSize(25)
'''

latex2 = TLatex()
latex2.SetNDC()
latex2.SetTextSize(0.5*c1.GetTopMargin())
latex2.SetTextFont(42)
latex2.SetTextAlign(31) # align right                                                                     
latex2.DrawLatex(0.90, 0.95,"#sqrt{s} = 13 TeV")
latex2.SetTextSize(0.8*c1.GetTopMargin())
latex2.SetTextFont(62)
latex2.SetTextAlign(11) # align right                                                                     
latex2.DrawLatex(0.15, 0.95, "CMS")
latex2.SetTextSize(0.6*c1.GetTopMargin())
latex2.SetTextFont(52)
latex2.SetTextAlign(11)
latex2.DrawLatex(0.28, 0.95, "Simulation")
latex2.DrawLatex(0.465, 0.95, "Preliminary")
latex2.SetTextFont(42)
latex2.SetTextSize(0.45*c1.GetTopMargin())

c1.SaveAs(savePath+saveName+'.png')
c1.SaveAs(savePath+saveName+'.pdf')

with open(savePath + saveName + ".txt", "w") as myfile:
   myfile.write('rootPath1: ' + rootPath1 + '\n')
   myfile.write('rootfile1: ' + rootfile1 + '\n')
   for i in range(len(vars1)):
       myfile.write('var1: ' + vars1[i] + '\n')
       myfile.write('cut1: ' + cuts1[i] + '\n\n')

   myfile.write('rootPath2: ' + rootPath2 + '\n')
   myfile.write('rootfile2: ' + rootfile2 + '\n')
   for i in range(len(vars2)):
       myfile.write('var2: ' + vars2[i] + '\n')
       myfile.write('cut2: ' + cuts2[i] + '\n\n')


   
myfile.close()

