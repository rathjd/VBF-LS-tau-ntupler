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
    'edmTriggerResultsHelper'
    ),
               #edmTriggerResults =
               edmTriggerResultsHelper =
               cms.untracked.
               vstring(
#    'edmTriggerResults               TriggerResults                    1',
    'edmTriggerResultsHelper          TriggerResults::HLT                    1',
    #---------------------------------------------------------------------
    'int value("HLT_DoubleMediumIsoPFTau35_Trk5_eta2p1_v6") value_HLT_DoubleMediumIsoPFTau35_Trk5_eta2p1_v6',
    'int prescale("HLT_DoubleMediumIsoPFTau35_Trk5_eta2p1_v6") prescale_HLT_DoubleMediumIsoPFTau35_Trk5_eta2p1_v6',


#    'unsigned int  size()',
#    'bool  wasrun()',
#    'bool  accept()',
#    'bool  error()',
#    'bool  wasrun(find_HLT_DoubleMediumIsoPFTau35_Trk5_eta2p1_Prong1_v2)',
#    'bool  accept(find_HLT_DoubleMediumIsoPFTau35_Trk5_eta2p1_Prong1_v2)',
#    'bool  error(find_HLT_DoubleMediumIsoPFTau35_Trk5_eta2p1_Prong1_v2)',
#    'unsigned int  index(find_HLT_DoubleMediumIsoPFTau35_Trk5_eta2p1_Prong1_v2)'
    )
               )
