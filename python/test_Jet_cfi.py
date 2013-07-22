#-------------------------------------------------------------------------
# Created: Mon Mar 25 11:48:48 2013 by /afs/naf.desy.de/user/m/marconi/scratch/SingleTau/ntupleProducer/CMSSW_5_3_7_patch4/src/VBFntupleProducer/VBFntupleProducer/python/test_Jet_cfi.py
#-------------------------------------------------------------------------
import FWCore.ParameterSet.Config as cms
demo =\
cms.EDAnalyzer("TheNtupleMaker",
               ntupleName = cms.untracked.string("ntuple.root"),
               analyzerName = cms.untracked.string("analyzer.cc"),

               buffers =
               cms.untracked.
               vstring(
    'patJet'
    ),
               patJet =
               cms.untracked.
               vstring(
    'patJet                          selectedPatJets                 200',
    #---------------------------------------------------------------------
    'int  charge()',
    'double  p()',
    'double  energy()',
    'double  et()',
    'double  px()',
    'double  py()',
    'double  pz()',
    'double  pt()',
    'double  phi()',
    'double  eta()',
    'float  neutralHadronEnergy()',
    'float  chargedHadronEnergyFraction()',
    'float  neutralHadronEnergyFraction()',
    'float  chargedEmEnergyFraction()',
    'float  neutralEmEnergyFraction()',
    'float  photonEnergy()',
    'float  photonEnergyFraction()',
    'float  electronEnergy()',
    'float  electronEnergyFraction()',
    'float  muonEnergy()',
    'float  muonEnergyFraction()',
    'float  HFHadronEnergy()',
    'float  HFHadronEnergyFraction()',
    'float  HFEMEnergy()',
    'float  HFEMEnergyFraction()',
    'int  chargedHadronMultiplicity()',
    'int  neutralHadronMultiplicity()',
    'int  photonMultiplicity()',
    'int  electronMultiplicity()',
    'int  HFHadronMultiplicity()',
    'int  HFEMMultiplicity()',
    'size_t  numberOfDaughters()',
    'float bDiscriminator("impactParameterTagInfos") bDiscriminator_impactParameterTagInfos ',
    'float bDiscriminator("secondaryVertexTagInfos") bDiscriminator_secondaryVertexTagInfos ',
    'float bDiscriminator("softMuonTagInfos") bDiscriminator_softMuonTagInfos ',
    'float bDiscriminator("secondaryVertexNegativeTagInfos") bDiscriminator_secondaryVertexNegativeTagInfos ', 
    'float bDiscriminator("inclusiveSecondaryVertexFinderTagInfos") bDiscriminator_inclusiveSecondaryVertexFinderTagInfos ',
    'float bDiscriminator("softElectronTagInfos") bDiscriminator_softElectronTagInfos ',
    'float bDiscriminator("jetBProbabilityBJetTags") bDiscriminator_jetBProbabilityBJetTags ',
    'float bDiscriminator("jetProbabilityBJetTags") bDiscriminator_jetProbabilityBJetTags ',
    'float bDiscriminator("trackCountingHighPurBJetTags") bDiscriminator_trackCountingHighPurBJetTags ',
    'float bDiscriminator("trackCountingHighEffBJetTags") bDiscriminator_trackCountingHighEffBJetTags ',
    'float bDiscriminator("simpleSecondaryVertexHighEffBJetTags") bDiscriminator_simpleSecondaryVertexHighEffBJetTags ',
    'float bDiscriminator("simpleSecondaryVertexHighPurBJetTags") bDiscriminator_simpleSecondaryVertexHighPurBJetTags ',
    'float bDiscriminator("combinedSecondaryVertexBJetTags") bDiscriminator_combinedSecondaryVertexBJetTags ',
    'float bDiscriminator("combinedSecondaryVertexMVABJetTags") bDiscriminator_combinedSecondaryVertexMVABJetTags ',
    'float bDiscriminator("softMuonBJetTags") bDiscriminator_softMuonBJetTags ',
    'float bDiscriminator("softMuonByPtBJetTags") bDiscriminator_softMuonByPtBJetTags ',
    'float bDiscriminator("softMuonByIP3dBJetTags") bDiscriminator_softMuonByIP3dBJetTags ',
    'float bDiscriminator("simpleSecondaryVertexNegativeHighEffBJetTags") bDiscriminator_simpleSecondaryVertexNegativeHighEffBJetTags ',
    'float bDiscriminator("simpleSecondaryVertexNegativeHighPurBJetTags") bDiscriminator_simpleSecondaryVertexNegativeHighPurBJetTags ',
    'float bDiscriminator("negativeTrackCountingHighEffJetTags") bDiscriminator_negativeTrackCountingHighEffJetTags ',
    'float bDiscriminator("negativeTrackCountingHighPurJetTags") bDiscriminator_negativeTrackCountingHighPurJetTags ',
    'float bDiscriminator("combinedInclusiveSecondaryVertexBJetTags") bDiscriminator_combinedInclusiveSecondaryVertexBJetTags ',
    'float bDiscriminator("combinedMVABJetTags") bDiscriminator_combinedMVABJetTags '
    )
               )
