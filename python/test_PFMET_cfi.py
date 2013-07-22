#-------------------------------------------------------------------------
# Created: Thu Mar 28 14:49:37 2013 by /afs/naf.desy.de/user/m/marconi/scratch/SingleTau/ntupleProducer/CMSSW_5_3_7_patch4/src/VBFntupleProducer/VBFntupleProducer/python/test_PFMET_cfi.py
#-------------------------------------------------------------------------
import FWCore.ParameterSet.Config as cms
demo =\
cms.EDAnalyzer("TheNtupleMaker",
               ntupleName = cms.untracked.string("ntuple.root"),
               analyzerName = cms.untracked.string("analyzer.cc"),

               buffers =
               cms.untracked.
               vstring(
    'recoPFMET',
    'recoPFMET1'
    ),
               recoPFMET =
               cms.untracked.
               vstring(
    'recoPFMET                       pfType1CorrectedMet             200',
    #---------------------------------------------------------------------
    'double  p()',
    'double  energy()',
    'double  et()',
    'double  px()',
    'double  py()',
    'double  pz()',
    'double  pt()',
    'double  phi()',
    'double  eta()'
    ),
               recoPFMET1 =
               cms.untracked.
               vstring(
    'recoPFMET                       pfType1p2CorrectedMet           200',
    #---------------------------------------------------------------------
    'double  p()',
    'double  energy()',
    'double  et()',
    'double  px()',
    'double  py()',
    'double  pz()',
    'double  pt()',
    'double  phi()',
    'double  eta()'
    )
               )
