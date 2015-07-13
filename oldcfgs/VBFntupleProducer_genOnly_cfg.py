#$Revision: 1.2 $
import FWCore.ParameterSet.Config as cms

process = cms.Process("TheNtupleMaker")

process.load("FWCore.MessageService.MessageLogger_cfi")

process.load("L1TriggerConfig.L1GtConfigProducers.L1GtConfig_cff")

process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(10) )

process.source = cms.Source("PoolSource",
                            fileNames =
                            cms.untracked.vstring(
    "file:/scratch/hh/dust/naf/cms/user/lveldere/staustuff/Ztautau.root" 
    )
							)
process.load("ntuples.VBF-LS-tau-ntupler.test_ntuple_genonly_cfi")

process.p = cms.Path(process.demo)
