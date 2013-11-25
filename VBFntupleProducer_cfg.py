#$Revision: 1.2 $
import FWCore.ParameterSet.Config as cms

process = cms.Process("TheNtupleMaker")

process.load("FWCore.MessageService.MessageLogger_cfi")
# See TheNtupleMaker twiki for a brief explanation
#process.MessageLogger.destinations = cms.untracked.vstring("cerr")
#process.MessageLogger.cerr.FwkReport.reportEvery = 10
#process.MessageLogger.cerr.default.limit = 5

# This is required in order to configure HLTConfigProducer
process.load("L1TriggerConfig.L1GtConfigProducers.L1GtConfig_cff")

process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(10) )

process.source = cms.Source("PoolSource",
							fileNames =
							cms.untracked.vstring(
                                                                          #"file:reco.root"
    #"/store/user/lveldere/VBFSUSY_C1pmC1pm_8TeV_Madgraph/VBFinclusive20130313_V3/4a34f2a69e63f3fe574e5dc5e8d98c50/skimPat_100_1_8aW.root"
    "file:skimPat.root"
    )
							)
#process.load("VBFntupleProducer.VBFntupleProducer.ntuple_cfi")
#process.load("VBFntupleProducer.VBFntupleProducer.test_Tau_cfi")
#process.load("VBFntupleProducer.VBFntupleProducer.test_Vertex_cfi")
#process.load("VBFntupleProducer.VBFntupleProducer.test_Muon_cfi")
#process.load("VBFntupleProducer.VBFntupleProducer.test_Electron_cfi")
#process.load("VBFntupleProducer.VBFntupleProducer.test_PFMET_cfi")
#process.load("VBFntupleProducer.VBFntupleProducer.test_Trigger_cfi")
#process.load("VBFntupleProducer.VBFntupleProducer.test_Jet_cfi")
process.load("ntuples.VBF-LS-tau-ntupler.ntuple_cfi")

process.p = cms.Path(process.demo)
