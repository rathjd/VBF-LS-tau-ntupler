#-------------------------------------------------------------------------
# Created: Thu Apr  4 16:14:54 2013 by /afs/naf.desy.de/user/m/marconi/scratch/SingleTau/ntupleProducer/CMSSW_5_3_7_patch4/src/VBFntupleProducer/VBFntupleProducer/python/test_Muon_cfi.py
#-------------------------------------------------------------------------
import FWCore.ParameterSet.Config as cms
demo =\
cms.EDAnalyzer("TheNtupleMaker",
               ntupleName = cms.untracked.string("ntuple.root"),
               analyzerName = cms.untracked.string("analyzer.cc"),

               buffers =
               cms.untracked.
               vstring(
    'recoVertex',
    'PileupSummaryInfo',
    'edmEventHelper',
    'GenRunInfoProduct',
    'recoGenParticleHelper',
    'recoBeamSpot'
    ),


                    recoVertex = 
                    cms.untracked.
                    vstring(
   'recoVertex                      offlinePrimaryVertices          200',
    #---------------------------------------------------------------------                                                                                                                                  
   'bool  isFake()',
   'double  ndof()',
   'double  x()',
   'double  y()',
   'double  z()'
   ),

                     PileupSummaryInfo =
                     cms.untracked.
                     vstring(
   'PileupSummaryInfo                addPileupInfo                     10',
   #---------------------------------------------------------------------                                                                                                                                  
   '   int getBunchCrossing()',
   '   int getPU_NumInteractions()'
   ),

                     edmEventHelper = 
                     cms.untracked.
                     vstring(
   'edmEventHelper                  info                              1',
   #---------------------------------------------------------------------                                                                                                                                  
   '   bool  isRealData()',
   '   int   run()',
   '   int   event()',
   '   int   luminosityBlock()',
   '   int   bunchCrossing()',
   '   int   orbitNumber()'
   ),

                     GenRunInfoProduct = 
                     cms.untracked.
                     vstring(
   'GenRunInfoProduct               generator                         1',
   #---------------------------------------------------------------------                                                                                                                                  
   'double  filterEfficiency()',
   'double  crossSection()',
   'double internalXSec().value()'
   ),

                     recoGenParticleHelper = 
                     cms.untracked.
                     vstring(
    'recoGenParticleHelper           genParticles                     500',
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

                     recoBeamSpot = 
                     cms.untracked.
                     vstring(
   'recoBeamSpot                    offlineBeamSpot                   1',
   #---------------------------------------------------------------------                                                                                                                                  
   'double  x0()',
   'double  y0()',
   'double  z0()'
   )

)
