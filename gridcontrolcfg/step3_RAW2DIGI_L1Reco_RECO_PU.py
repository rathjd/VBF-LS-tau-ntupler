# Auto generated configuration file
# using: 
# Revision: 1.19 
# Source: /local/reps/CMSSW/CMSSW/Configuration/Applications/python/ConfigBuilder.py,v 
# with command line options: step3 --conditions auto:run2_mc --filein=file:ZEE_13TeV_GEN-SIM-RAW.root --fileout file:ZEE_13TeV_AODSIM.root --pileup_input das:/RelValMinBias_13/CMSSW_7_1_0_pre8-PRE_LS171_V9-v1/GEN-SIM -n 100 --eventcontent AODSIM -s RAW2DIGI,L1Reco,RECO --datatier AODSIM --pileup AVE_35_BX_25ns --customise SLHCUpgradeSimulations/Configuration/postLS1Customs.customisePostLS1 --magField 38T_PostLS1
import FWCore.ParameterSet.Config as cms

process = cms.Process('RECO')

# import of standard configurations
process.load('Configuration.StandardSequences.Services_cff')
process.load('SimGeneral.HepPDTESSource.pythiapdt_cfi')
process.load('FWCore.MessageService.MessageLogger_cfi')
process.load('Configuration.EventContent.EventContent_cff')
process.load('SimGeneral.MixingModule.mix_POISSON_average_cfi')
process.load('Configuration.StandardSequences.GeometryRecoDB_cff')
process.load('Configuration.StandardSequences.MagneticField_38T_PostLS1_cff')
process.load('Configuration.StandardSequences.RawToDigi_cff')
process.load('Configuration.StandardSequences.L1Reco_cff')
process.load('Configuration.StandardSequences.Reconstruction_cff')
process.load('Configuration.StandardSequences.EndOfProcess_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(100)
)

# Input source
process.source = cms.Source("PoolSource",
    secondaryFileNames = cms.untracked.vstring(),
    fileNames = cms.untracked.vstring('file:ZEE_13TeV_GEN-SIM-RAW.root')
)

process.options = cms.untracked.PSet(

)

# Production Info
process.configurationMetadata = cms.untracked.PSet(
    version = cms.untracked.string('$Revision: 1.19 $'),
    annotation = cms.untracked.string('step3 nevts:100'),
    name = cms.untracked.string('Applications')
)

# Output definition

process.AODSIMoutput = cms.OutputModule("PoolOutputModule",
    compressionLevel = cms.untracked.int32(4),
    compressionAlgorithm = cms.untracked.string('LZMA'),
    eventAutoFlushCompressedSize = cms.untracked.int32(15728640),
    outputCommands = process.AODSIMEventContent.outputCommands,
    fileName = cms.untracked.string('file:ZEE_13TeV_AODSIM.root'),
    dataset = cms.untracked.PSet(
        filterName = cms.untracked.string(''),
        dataTier = cms.untracked.string('AODSIM')
    )
)

# Additional output definition

# Other statements
process.mix.input.nbPileupEvents.averageNumber = cms.double(35.000000)
process.mix.bunchspace = cms.int32(25)
process.mix.minBunch = cms.int32(-12)
process.mix.maxBunch = cms.int32(3)
process.mix.input.fileNames = cms.untracked.vstring(['/store/relval/CMSSW_7_1_0_pre8/RelValMinBias_13/GEN-SIM/PRE_LS171_V9-v1/00000/066245C6-BAE1-E311-92BA-0026189438C2.root', '/store/relval/CMSSW_7_1_0_pre8/RelValMinBias_13/GEN-SIM/PRE_LS171_V9-v1/00000/08AF831E-BCE1-E311-97A1-0025905A60BE.root', '/store/relval/CMSSW_7_1_0_pre8/RelValMinBias_13/GEN-SIM/PRE_LS171_V9-v1/00000/0C27A4A8-BDE1-E311-95BF-0025905A60B2.root', '/store/relval/CMSSW_7_1_0_pre8/RelValMinBias_13/GEN-SIM/PRE_LS171_V9-v1/00000/4CD664D1-BCE1-E311-A787-0025905A48B2.root', '/store/relval/CMSSW_7_1_0_pre8/RelValMinBias_13/GEN-SIM/PRE_LS171_V9-v1/00000/94E3C597-C2E1-E311-8C80-002590596490.root', '/store/relval/CMSSW_7_1_0_pre8/RelValMinBias_13/GEN-SIM/PRE_LS171_V9-v1/00000/D24ECE88-BBE1-E311-B84A-0026189438C1.root', '/store/relval/CMSSW_7_1_0_pre8/RelValMinBias_13/GEN-SIM/PRE_LS171_V9-v1/00000/ECF1D296-BEE1-E311-916D-0025905A60BC.root'])
from Configuration.AlCa.GlobalTag import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, 'auto:run2_mc', '')

# Path and EndPath definitions
process.raw2digi_step = cms.Path(process.RawToDigi)
process.L1Reco_step = cms.Path(process.L1Reco)
process.reconstruction_step = cms.Path(process.reconstruction)
process.endjob_step = cms.EndPath(process.endOfProcess)
process.AODSIMoutput_step = cms.EndPath(process.AODSIMoutput)

# Schedule definition
process.schedule = cms.Schedule(process.raw2digi_step,process.L1Reco_step,process.reconstruction_step,process.endjob_step,process.AODSIMoutput_step)

# customisation of the process.

# Automatic addition of the customisation function from SLHCUpgradeSimulations.Configuration.postLS1Customs
from SLHCUpgradeSimulations.Configuration.postLS1Customs import customisePostLS1 

#call to customisation function customisePostLS1 imported from SLHCUpgradeSimulations.Configuration.postLS1Customs
process = customisePostLS1(process)

# End of customisation functions
