formula = {}
paraConfigs = { }

savePath = '/home/muahmad/public_html/2019/BPH_FourMu/Upsilon-pT_Fit/'


saveName = 'Upsilon_pT_Fit_inclusive'
paraConfigs[saveName] = \
{\
'rootPath1': '/raid/raid9/ahmad/Ymumu/make1Dplot_Ymumu/',
'rootfile1': 'fourMuMass.root',
'tree1': 'fourmu_tree',
'binInfo': [50,0,50],
'vars1': ['pt_upsilon'],
'cuts1': ['1'],
'weight1': ['1'],
'xTitle': 'p_{T}(#Upsilon)',
'yTitle': '',
'savePath': savePath,
'saveName': saveName, #
'latexNote1': '', #
'latexNote2': '',
'doFit': True,
'pdfName': 'LikeSignPdf'
}

saveName = 'Upsilon_pT_Fit_etabin1'
paraConfigs[saveName] = \
{\
'rootPath1': '/raid/raid9/ahmad/Ymumu/make1Dplot_Ymumu/',
'rootfile1': 'fourMuMass.root',
'tree1': 'fourmu_tree',
'binInfo': [50,0,50],
'vars1': ['pt_upsilon'],
'cuts1': ['abs(eta_upsilon)>0.0&&abs(eta_upsilon)<0.7'],
'weight1': ['1'],
'xTitle': 'p_{T}(#Upsilon)',
'yTitle': '',
'savePath': savePath,
'saveName': saveName, #
'latexNote1': '', #
'latexNote2': '',
'doFit': True,
'pdfName': 'LikeSignPdf'
}
saveName = 'Upsilon_pT_Fit_etabin2'
paraConfigs[saveName] = \
{\
'rootPath1': '/raid/raid9/ahmad/Ymumu/make1Dplot_Ymumu/',
'rootfile1': 'fourMuMass.root',
'tree1': 'fourmu_tree',
'binInfo': [50,0,50],
'vars1': ['pt_upsilon'],
'cuts1': ['abs(eta_upsilon)>0.7&&abs(eta_upsilon)<1.2'],
'weight1': ['1'],
'xTitle': 'p_{T}(#Upsilon)',
'yTitle': '',
'savePath': savePath,
'saveName': saveName, #
'latexNote1': '', #
'latexNote2': '',
'doFit': True,
'pdfName': 'LikeSignPdf'
}

saveName = 'Upsilon_pT_Fit_etabin3'
paraConfigs[saveName] = \
{\
'rootPath1': '/raid/raid9/ahmad/Ymumu/make1Dplot_Ymumu/',
'rootfile1': 'fourMuMass.root',
'tree1': 'fourmu_tree',
'binInfo': [50,0,50],
'vars1': ['pt_upsilon'],
'cuts1': ['abs(eta_upsilon)>1.2&&abs(eta_upsilon)<1.6'],
'weight1': ['1'],
'xTitle': 'p_{T}(#Upsilon)',
'yTitle': '',
'savePath': savePath,
'saveName': saveName, #
'latexNote1': '', #
'latexNote2': '',
'doFit': True,
'pdfName': 'LikeSignPdf'
}
saveName = 'Upsilon_pT_Fit_etabin4'
paraConfigs[saveName] = \
{\
'rootPath1': '/raid/raid9/ahmad/Ymumu/make1Dplot_Ymumu/',
'rootfile1': 'fourMuMass.root',
'tree1': 'fourmu_tree',
'binInfo': [50,0,50],
'vars1': ['pt_upsilon'],
'cuts1': ['abs(eta_upsilon)>1.6&&abs(eta_upsilon)<1.9'],
'weight1': ['1'],
'xTitle': 'p_{T}(#Upsilon)',
'yTitle': '',
'savePath': savePath,
'saveName': saveName, #
'latexNote1': '', #
'latexNote2': '',
'doFit': True,
'pdfName': 'LikeSignPdf'
}
saveName = 'Upsilon_pT_Fit_etabin5'
paraConfigs[saveName] = \
{\
'rootPath1': '/raid/raid9/ahmad/Ymumu/make1Dplot_Ymumu/',
'rootfile1': 'fourMuMass.root',
'tree1': 'fourmu_tree',
'binInfo': [40,0,40],
'vars1': ['pt_upsilon'],
'cuts1': ['abs(eta_upsilon)>1.9&&abs(eta_upsilon)<2.2'],
'weight1': ['1'],
'xTitle': 'p_{T}(#Upsilon)',
'yTitle': '',
'savePath': savePath,
'saveName': saveName, #
'latexNote1': '', #
'latexNote2': '',
'doFit': True,
'pdfName': 'LikeSignPdf'
}
saveName = 'Upsilon_pT_Fit_etabin6'
paraConfigs[saveName] = \
{\
'rootPath1': '/raid/raid9/ahmad/Ymumu/make1Dplot_Ymumu/',
'rootfile1': 'fourMuMass.root',
'tree1': 'fourmu_tree',
'binInfo': [40,0,25],
'vars1': ['pt_upsilon'],
'cuts1': ['abs(eta_upsilon)>2.2&&abs(eta_upsilon)<2.5'],
'weight1': ['1'],
'xTitle': 'p_{T}(#Upsilon)',
'yTitle': '',
'savePath': savePath,
'saveName': saveName, #
'latexNote1': '', #
'latexNote2': '',
'doFit': True,
'pdfName': 'LikeSignPdf'
}

saveName = 'Upsilon_pT_Fit_etabin7'
paraConfigs[saveName] = \
{\
'rootPath1': '/raid/raid9/ahmad/Ymumu/make1Dplot_Ymumu/',
'rootfile1': 'fourMuMass.root',
'tree1': 'fourmu_tree',
'binInfo': [30,0,15],
'vars1': ['pt_upsilon'],
'cuts1': ['abs(eta_upsilon)>2.5&&abs(eta_upsilon)<2.9'],
'weight1': ['1'],
'xTitle': 'p_{T}(#Upsilon)',
'yTitle': '',
'savePath': savePath,
'saveName': saveName, #
'latexNote1': '', #
'latexNote2': '',
'doFit': True,
'pdfName': 'LikeSignPdf'
}

saveName = 'Upsilon_pT_Fit_etabin8'
paraConfigs[saveName] = \
{\
'rootPath1': '/raid/raid9/ahmad/Ymumu/make1Dplot_Ymumu/',
'rootfile1': 'fourMuMass.root',
'tree1': 'fourmu_tree',
'binInfo': [30,0,10],
'vars1': ['pt_upsilon'],
'cuts1': ['abs(eta_upsilon)>2.9'],
'weight1': ['1'],
'xTitle': 'p_{T}(#Upsilon)',
'yTitle': '',
'savePath': savePath,
'saveName': saveName, #
'latexNote1': '', #
'latexNote2': '',
'doFit': True,
'pdfName': 'LikeSignPdf'
}
