#-------------------------------------------------------------------------
# Created: Mon Mar 25 16:11:24 2013 by /afs/naf.desy.de/user/m/marconi/scratch/SingleTau/ntupleProducer/CMSSW_5_3_7_patch4/src/VBFntupleProducer/VBFntupleProducer/python/test_Trigger_cfi.py
#-------------------------------------------------------------------------
import FWCore.ParameterSet.Config as cms
demo =\
cms.EDAnalyzer("TheNtupleMaker",
               ntupleName = cms.untracked.string("ntuple.root"),
               analyzerName = cms.untracked.string("analyzer.cc"),

               buffers =
               cms.untracked.
               vstring(
    'recoGenParticleHelper',
    'recoGenParticle'
    ),



               recoGenParticleHelper = 
               cms.untracked.
               vstring(
    'recoGenParticleHelperPlus           genParticles                     2000',
    #---------------------------------------------------------------------                                                                                                                                  
    '    int   firstMother()',
    '    int   lastMother()',
    '    int   firstDaughter()',
    '    int   lastDaughter()',
    '    int   charge()',
    '    int   pdgId()',
    '    int   status()',
    ' double   pt()',
    ' double   eta()',
    ' double   phi()',
    ' double   mass()'
    ),


               recoGenParticle =
               cms.untracked.
               vstring(
    'recoGenParticle                 genParticles                    2000',
    #---------------------------------------------------------------------
    'int  charge()',
    'double  pt()',
    'double  phi()',
    'double  eta()',
    ' double   mass()',
    'int  pdgId()',
    'int  status()'
    )
               )
