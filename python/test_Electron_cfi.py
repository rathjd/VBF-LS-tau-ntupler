#-------------------------------------------------------------------------
# Created: Thu Apr  4 17:20:13 2013 by /afs/naf.desy.de/user/m/marconi/scratch/SingleTau/ntupleProducer/CMSSW_5_3_7_patch4/src/VBFntupleProducer/VBFntupleProducer/python/test_Electron_cfi.py
#-------------------------------------------------------------------------
import FWCore.ParameterSet.Config as cms
demo =\
cms.EDAnalyzer("TheNtupleMaker",
               ntupleName = cms.untracked.string("ntuple.root"),
               analyzerName = cms.untracked.string("analyzer.cc"),

               buffers =
               cms.untracked.
               vstring(
    'patElectron',
    'recoGsfElectron'
    ),
               patElectron =
               cms.untracked.
               vstring(
    'patElectron                     patElectrons                    200',
    #---------------------------------------------------------------------
    'double  p()',
    'double  energy()',
    'double  et()',
    'double  px()',
    'double  py()',
    'double  pz()',
    'double  pt()',
    'double  phi()',
    'double  eta()',
    'float  eSuperClusterOverP()',
    'float  deltaEtaSuperClusterTrackAtVtx()',
    'float  deltaPhiSuperClusterTrackAtVtx()',
    'float  sigmaIetaIeta()',
    'float  scE1x5()',
    'float  scE2x5Max()',
    'float  scE5x5()',
    'float  hadronicOverEm()',
    'float  dr04TkSumPt()',
    'float  dr04EcalRecHitSumEt()',
    'double  gsfTrack()->dxy()',
    'double  gsfTrack()->d0()',
    'double  gsfTrack()->dz()'
    ),
               recoGsfElectron =
               cms.untracked.
               vstring(
    'recoGsfElectron                 gsfElectrons                    200',
    #---------------------------------------------------------------------
    'double  p()',
    'double  energy()',
    'double  et()',
    'double  px()',
    'double  py()',
    'double  pz()',
    'double  pt()',
    'double  phi()',
    'double  eta()',
    'float  eSuperClusterOverP()',
    'float  deltaEtaSuperClusterTrackAtVtx()',
    'float  deltaPhiSuperClusterTrackAtVtx()',
    'float  sigmaIetaIeta()',
    'float  scE1x5()',
    'float  scE2x5Max()',
    'float  scE5x5()',
    'float  hadronicOverEm()',
    'float  dr04TkSumPt()',
    'float  dr04EcalRecHitSumEt()',
    'double  gsfTrack()->dxy()',
    'double  gsfTrack()->d0()',
    'double  gsfTrack()->dz()'
    
    )
               )
