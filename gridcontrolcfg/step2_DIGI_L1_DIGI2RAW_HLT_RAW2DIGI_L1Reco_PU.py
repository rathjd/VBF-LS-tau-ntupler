# Auto generated configuration file
# using: 
# Revision: 1.19 
# Source: /local/reps/CMSSW/CMSSW/Configuration/Applications/python/ConfigBuilder.py,v 
# with command line options: step2 --conditions auto:run2_mc --filein=file:ZEE_13TeV_GEN-SIM.root --fileout file:ZEE_13TeV_GEN-SIM-RAW.root --pileup_input das:/RelValMinBias_13/CMSSW_7_2_0_pre7-PRE_LS172_V11-v1/GEN-SIM -n 100 --eventcontent RAWSIM -s DIGI,L1,DIGI2RAW,HLT:@relval,RAW2DIGI,L1Reco --datatier GEN-SIM-DIGI-RAW-HLTDEBUG --pileup AVE_10_BX_25ns_m8 --customise SLHCUpgradeSimulations/Configuration/postLS1Customs.customisePostLS1 --magField 38T_PostLS1
import FWCore.ParameterSet.Config as cms

process = cms.Process('HLT')

# import of standard configurations
process.load('Configuration.StandardSequences.Services_cff')
process.load('SimGeneral.HepPDTESSource.pythiapdt_cfi')
process.load('FWCore.MessageService.MessageLogger_cfi')
process.load('Configuration.EventContent.EventContent_cff')
process.load('SimGeneral.MixingModule.mix_POISSON_average_cfi')
process.load('Configuration.StandardSequences.GeometryRecoDB_cff')
process.load('Configuration.StandardSequences.MagneticField_38T_PostLS1_cff')
process.load('Configuration.StandardSequences.Digi_cff')
process.load('Configuration.StandardSequences.SimL1Emulator_cff')
process.load('Configuration.StandardSequences.DigiToRaw_cff')
process.load('HLTrigger.Configuration.HLT_GRun_cff')
process.load('Configuration.StandardSequences.RawToDigi_cff')
process.load('Configuration.StandardSequences.L1Reco_cff')
process.load('Configuration.StandardSequences.EndOfProcess_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_condDBv2_cff')

process.maxEvents = cms.untracked.PSet(
    #input = cms.untracked.int32(100)
    input = cms.untracked.int32(-1)
)

# Input source
process.source = cms.Source("PoolSource",
    secondaryFileNames = cms.untracked.vstring(),
    fileNames = cms.untracked.vstring('file:ZEE_13TeV_GEN-SIM.root')
)

process.options = cms.untracked.PSet(

)

# Production Info
process.configurationMetadata = cms.untracked.PSet(
    version = cms.untracked.string('$Revision: 1.19 $'),
    annotation = cms.untracked.string('step2 nevts:100'),
    name = cms.untracked.string('Applications')
)

# Output definition

process.RAWSIMoutput = cms.OutputModule("PoolOutputModule",
    splitLevel = cms.untracked.int32(0),
    eventAutoFlushCompressedSize = cms.untracked.int32(5242880),
    outputCommands = process.RAWSIMEventContent.outputCommands,
    fileName = cms.untracked.string('file:ZEE_13TeV_GEN-SIM-RAW.root'),
    dataset = cms.untracked.PSet(
        filterName = cms.untracked.string(''),
        dataTier = cms.untracked.string('GEN-SIM-DIGI-RAW-HLTDEBUG')
    )
)

# Additional output definition

# Other statements
process.mix.input.nbPileupEvents.averageNumber = cms.double(10.000000)
process.mix.bunchspace = cms.int32(25)
process.mix.minBunch = cms.int32(-8)
process.mix.maxBunch = cms.int32(3)
process.mix.input.fileNames = cms.untracked.vstring(['/store/relval/CMSSW_7_2_0_pre7/RelValMinBias_13/GEN-SIM/PRE_LS172_V11-v1/00000/08596E6D-824B-E411-BD16-003048FFCB9E.root', '/store/relval/CMSSW_7_2_0_pre7/RelValMinBias_13/GEN-SIM/PRE_LS172_V11-v1/00000/0CC19732-874B-E411-8077-002618943935.root', '/store/relval/CMSSW_7_2_0_pre7/RelValMinBias_13/GEN-SIM/PRE_LS172_V11-v1/00000/40E48F8A-804B-E411-B002-002354EF3BE3.root', '/store/relval/CMSSW_7_2_0_pre7/RelValMinBias_13/GEN-SIM/PRE_LS172_V11-v1/00000/7A1F2BC2-7E4B-E411-8C0C-0025905938AA.root', '/store/relval/CMSSW_7_2_0_pre7/RelValMinBias_13/GEN-SIM/PRE_LS172_V11-v1/00000/82233874-814B-E411-92DA-0025905A6060.root', '/store/relval/CMSSW_7_2_0_pre7/RelValMinBias_13/GEN-SIM/PRE_LS172_V11-v1/00000/B08A0836-874B-E411-836C-0025905A48D6.root', '/store/relval/CMSSW_7_2_0_pre7/RelValMinBias_13/GEN-SIM/PRE_LS172_V11-v1/00000/F2284CC0-7E4B-E411-8075-002618943875.root', '/store/relval/CMSSW_7_2_0_pre7/RelValMinBias_13/GEN-SIM/PRE_LS172_V11-v1/00000/FEED411E-824B-E411-9455-0025905A48F0.root'])
from Configuration.AlCa.GlobalTag_condDBv2 import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, 'auto:run2_mc', '')

# Path and EndPath definitions
process.digitisation_step = cms.Path(process.pdigi)
process.L1simulation_step = cms.Path(process.SimL1Emulator)
process.digi2raw_step = cms.Path(process.DigiToRaw)
process.raw2digi_step = cms.Path(process.RawToDigi)
process.L1Reco_step = cms.Path(process.L1Reco)
process.endjob_step = cms.EndPath(process.endOfProcess)
process.RAWSIMoutput_step = cms.EndPath(process.RAWSIMoutput)

# Schedule definition
process.schedule = cms.Schedule(process.digitisation_step,process.L1simulation_step,process.digi2raw_step)
process.schedule.extend(process.HLTSchedule)
process.schedule.extend([process.raw2digi_step,process.L1Reco_step,process.endjob_step,process.RAWSIMoutput_step])

# customisation of the process.

# Automatic addition of the customisation function from HLTrigger.Configuration.customizeHLTforMC
from HLTrigger.Configuration.customizeHLTforMC import customizeHLTforMC 

#call to customisation function customizeHLTforMC imported from HLTrigger.Configuration.customizeHLTforMC
process = customizeHLTforMC(process)

# Automatic addition of the customisation function from SLHCUpgradeSimulations.Configuration.postLS1Customs
from SLHCUpgradeSimulations.Configuration.postLS1Customs import customisePostLS1 

#call to customisation function customisePostLS1 imported from SLHCUpgradeSimulations.Configuration.postLS1Customs
process = customisePostLS1(process)

# End of customisation functions

