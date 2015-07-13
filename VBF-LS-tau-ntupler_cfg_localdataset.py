#$Revision: 1.1 $
import FWCore.ParameterSet.Config as cms
from FWCore.ParameterSet.VarParsing import VarParsing
options = VarParsing ('python')

options.register ('filepath',
		False,
		VarParsing.multiplicity.singleton,
		VarParsing.varType.string,
		"produces pdf weights for uncertainties study")
options.parseArguments()
filepath = options.filepath

process = cms.Process("TheNtupleMaker")

process.load("FWCore.MessageService.MessageLogger_cfi")
# See TheNtupleMaker twiki for a brief explanation
#process.MessageLogger.destinations = cms.untracked.vstring("cerr")
#process.MessageLogger.cerr.FwkReport.reportEvery = 10
#process.MessageLogger.cerr.default.limit = 5

# This is required in order to configure HLTConfigProducer
process.load("L1TriggerConfig.L1GtConfigProducers.L1GtConfig_cff")

process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )

process.source = cms.Source("PoolSource",
							fileNames =
							cms.untracked.vstring( 
								#'file:'+filepath,
								#filepath,
								#"file:VBFC1pmN2_C1ToTau_N2ToTauTau_LSP050_Stau195_Chargino200_qcd0_qed4_unwgt_MINIAODSIM_4.root"
												  )
							)
FILE = open(filepath)
lines = FILE.readlines()
FILE.close()
filelist = []
for line in lines:
	line = line.strip()
	if len(line) == 0:
		continue
	filelist.append("file:" + line)
process.source.fileNames = filelist

process.load("ntuples.VBF-LS-tau-ntupler.ntuple_cfi")

process.p = cms.Path(process.demo)
