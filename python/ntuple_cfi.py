#-------------------------------------------------------------------------
# Created: Mon Mar 25 16:11:24 2013 by /afs/naf.desy.de/user/m/marconi/scratch/SingleTau/ntupleProducer/CMSSW_5_3_7_patch4/src/VBFntupleProducer/VBFntupleProducer/python/test_Trigger_cfi.py
#-------------------------------------------------------------------------

# next round: need helper for taus?
# next round: remove genparticlehelper, only keep genparticlehelperplus
# next round: update to latest version ntuplemaker
# next round: remove redundant kinematic variables: keep pt, eta, phi, mass
# next round: add genjets if, hopefully, they are added to the pat recipe

import FWCore.ParameterSet.Config as cms
demo =\
cms.EDAnalyzer("TheNtupleMaker",
               ntupleName = cms.untracked.string("ntuple.root"),
               analyzerName = cms.untracked.string("analyzer.cc"),

               buffers =
               cms.untracked.
               vstring(
    'edmTriggerResultsHelper',
    'recoVertex',
    'PileupSummaryInfo',
    'edmEventHelper',
    'GenRunInfoProduct',
    'recoGenParticleHelper',
    'recoGenParticleHelperPlus',
    #'ak5GenJets',
    'recoBeamSpot',
    'patJet',
    'patElectron',
    'recoGsfElectron',
    'patMuon',
    'patTau',
    'patMET',
    'patMET2',
    'recoPFMET',
    'recoPFMET1',
    ),


               #edmTriggerResults =
               edmTriggerResultsHelper =
               cms.untracked.
               vstring(
# 'edmTriggerResults TriggerResults 1',
    'edmTriggerResultsHelper TriggerResults::HLT 1',
    #---------------------------------------------------------------------
    'int value("HLT_PFHT350_PFMET100_v1..3") value_HLT_PFHT350_PFMET100_v',
    'int value("HLT_PFNoPUHT350_PFMET100_v1..5") value_HLT_PFNoPUHT350_PFMET100_v',
    'int prescale("HLT_PFHT350_PFMET100_v1..3") prescale_HLT_PFHT350_PFMET100_v',
    'int prescale("HLT_PFNoPUHT350_PFMET100_v1..5") prescale_HLT_PFNoPUHT350_PFMET100_v',
    'int prescale("HLT_IsoMu24_eta2p1_v1..16") prescale_HLT_IsoMu24_eta2p1_v',
    'int prescale("HLT_IsoMu30_eta2p1_v1..16") prescale_HLT_IsoMu30_eta2p1_v',
    'int prescale("HLT_IsoMu34_eta2p1_v1..14") prescale_HLT_IsoMu34_eta2p1_v',
    'int prescale("HLT_IsoMu40_eta2p1_v1..11") prescale_HLT_IsoMu40_eta2p1_v',
    ),

                    recoVertex =
                    cms.untracked.
                    vstring(
   'recoVertex offlinePrimaryVertices 200',
    #---------------------------------------------------------------------
   'bool isFake()',
   'double ndof()',
   'double x()',
   'double y()',
   'double z()'
   ),

                     PileupSummaryInfo =
                     cms.untracked.
                     vstring(
   'PileupSummaryInfo addPileupInfo 10',
   #---------------------------------------------------------------------
   ' int getBunchCrossing()',
   ' int getPU_NumInteractions()',
   ' float getTrueNumInteractions()'
   ),

                     edmEventHelper =
                     cms.untracked.
                     vstring(
   'edmEventHelper info 1',
   #---------------------------------------------------------------------
   ' bool isRealData()',
   ' int run()',
   ' int event()',
   ' int luminosityBlock()',
   ' int bunchCrossing()',
   ' int orbitNumber()'
   ),

                     GenRunInfoProduct =
                     cms.untracked.
                     vstring(
   'GenRunInfoProduct generator 1',
   #---------------------------------------------------------------------
   'double filterEfficiency()',
   'double crossSection()',
   'double internalXSec().value()'
   ),

                     recoGenParticleHelper =
                     cms.untracked.
                     vstring(
    'recoGenParticleHelper genParticles 100',
   #---------------------------------------------------------------------
    ' int firstMother()',
    ' int lastMother()',
    ' int firstDaughter()',
    ' int lastDaughter()',
    ' int charge()',
    ' int pdgId()',
    ' int status()',
    ' double pt()',
    ' double eta()',
    ' double phi()',
    ' double mass()'
    ),
                     recoGenParticleHelperPlus =
                     cms.untracked.
                     vstring(
    'recoGenParticleHelperPlus genParticles 100',
   #---------------------------------------------------------------------
    ' int firstMother()',
    ' int lastMother()',
    ' int firstDaughter()',
    ' int lastDaughter()',
    ' int charge()',
    ' int pdgId()',
    ' int status()',
    ' double pt()',
    ' double eta()',
    ' double phi()',
    ' double mass()'
    ),

                     ak5GenJets =
                     cms.untracked.
                     vstring(
    'recoGenJet ak5GenJets 100',
   #---------------------------------------------------------------------
    ' int charge()',
    ' double pt()',
    ' double eta()',
    ' double phi()',
    ' double mass()'
    ),

                     recoBeamSpot =
                     cms.untracked.
                     vstring(
   'recoBeamSpot offlineBeamSpot 1',
   #---------------------------------------------------------------------
   'double x0()',
   'double y0()',
   'double z0()'
   ),

               patJet =
               cms.untracked.
               vstring(
    'patJet selectedPatJets 200',
    #---------------------------------------------------------------------
    'int charge()',
    'double p()',
    'double energy()',
    'double et()',
    'double px()',
    'double py()',
    'double pz()',
    'double pt()',
    'double phi()',
    'double eta()',
    'float neutralHadronEnergy()',
    'float chargedHadronEnergyFraction()',
    'float neutralHadronEnergyFraction()',
    'float chargedEmEnergyFraction()',
    'float neutralEmEnergyFraction()',
    'float photonEnergy()',
    'float photonEnergyFraction()',
    'float electronEnergy()',
    'float electronEnergyFraction()',
    'float muonEnergy()',
    'float muonEnergyFraction()',
    'float HFHadronEnergy()',
    'float HFHadronEnergyFraction()',
    'float HFEMEnergy()',
    'float HFEMEnergyFraction()',
    'int chargedHadronMultiplicity()',
    'int chargedMultiplicity()',
    'int neutralHadronMultiplicity()',
    'int photonMultiplicity()',
    'int electronMultiplicity()',
    'int HFHadronMultiplicity()',
    'int HFEMMultiplicity()',
    'size_t numberOfDaughters()',
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
    ),

               patElectron =
               cms.untracked.
               vstring(
    'patElectron patElectrons 200',
    #---------------------------------------------------------------------
    'double p()',
    'double energy()',
    'double et()',
    'double px()',
    'double py()',
    'double pz()',
    'double pt()',
    'double phi()',
    'double eta()',
    'float eSuperClusterOverP()',
    'float deltaEtaSuperClusterTrackAtVtx()',
    'float deltaPhiSuperClusterTrackAtVtx()',
    'float sigmaIetaIeta()',
    'float scE1x5()',
    'float scE2x5Max()',
    'float scE5x5()',
    'float hadronicOverEm()',
    'float dr04TkSumPt()',
    'float dr04EcalRecHitSumEt()',
    'double gsfTrack()->dxy()',
    'double gsfTrack()->d0()',
    'double gsfTrack()->dz()'
    ),
               recoGsfElectron =
               cms.untracked.
               vstring(
    'recoGsfElectron gsfElectrons 200',
    #---------------------------------------------------------------------
    'double p()',
    'double energy()',
    'double et()',
    'double px()',
    'double py()',
    'double pz()',
    'double pt()',
    'double phi()',
    'double eta()',
    'float eSuperClusterOverP()',
    'float deltaEtaSuperClusterTrackAtVtx()',
    'float deltaPhiSuperClusterTrackAtVtx()',
    'float sigmaIetaIeta()',
    'float scE1x5()',
    'float scE2x5Max()',
    'float scE5x5()',
    'float hadronicOverEm()',
    'float dr04TkSumPt()',
    'float dr04EcalRecHitSumEt()',
    'double gsfTrack()->dxy()',
    'double gsfTrack()->d0()',
    'double gsfTrack()->dz()'
    
    ),

               patMuon =
               cms.untracked.
               vstring(
    'patMuon patMuons 200',
    #---------------------------------------------------------------------
    'double p()',
    'double energy()',
    'double et()',
    'double px()',
    'double py()',
    'double pz()',
    'double pt()',
    'double phi()',
    'double eta()',
    'bool isGlobalMuon()',
    'bool isTrackerMuon()',
    'bool isPFMuon()',
    'float pfIsolationR03()->sumChargedHadronPt',
    'float pfIsolationR03()->sumChargedParticlePt',
    'float pfIsolationR03()->sumNeutralHadronEt',
    'float pfIsolationR03()->sumNeutralHadronEtHighThreshold',
    'float pfIsolationR03()->sumPhotonEt',
    'float pfIsolationR03()->sumPhotonEtHighThreshold',
    'float pfIsolationR03()->sumPUPt',
    'float pfIsolationR04()->sumChargedHadronPt',
    'float pfIsolationR04()->sumChargedParticlePt',
    'float pfIsolationR04()->sumNeutralHadronEt',
    'float pfIsolationR04()->sumNeutralHadronEtHighThreshold',
    'float pfIsolationR04()->sumPhotonEt',
    'float pfIsolationR04()->sumPhotonEtHighThreshold',
    'float pfIsolationR04()->sumPUPt',
    'int numberOfMatchedStations()',
    'double innerTrack()->normalizedChi2()',
    'double innerTrack()->dxy()',
    'double innerTrack()->dz()',
    'int innerTrack()->hitPattern().numberOfValidPixelHits()',
    'int innerTrack()->hitPattern().pixelLayersWithMeasurement()',
    'double globalTrack()->normalizedChi2()',
    'int globalTrack()->hitPattern().numberOfValidMuonHits()',
    'double muonBestTrack()->dxy()',
    'double muonBestTrack()->dz()'
    ),

               patTau =
               cms.untracked.
               vstring(
    'patTauHelper patTaus 200',
    #---------------------------------------------------------------------
    'int charge()',
    'double p()',
    'double energy()',
    'double et()',
    'double px()',
    'double py()',
    'double pz()',
    'double pt()',
    'double phi()',
    'double eta()',
    'double vx()',
    'double vy()',
    'double vz()',
    'float tauID("againstElectronDeadECAL") tauID_againstElectronDeadECAL',
    'float tauID("againstElectronLoose") tauID_againstElectronLoose',
    'float tauID("againstElectronLooseMVA5") tauID_againstElectronLooseMVA5',
    'float tauID("againstElectronMVA5category") tauID_againstElectronMVA5category',
    'float tauID("againstElectronMVA5raw") tauID_againstElectronMVA5raw',
    'float tauID("againstElectronMedium") tauID_againstElectronMedium',
    'float tauID("againstElectronMediumMVA5") tauID_againstElectronMediumMVA5',
    'float tauID("againstElectronTight") tauID_againstElectronTight',
    'float tauID("againstElectronTightMVA5") tauID_againstElectronTightMVA5',
    'float tauID("againstElectronVLooseMVA5") tauID_againstElectronVLooseMVA5',
    'float tauID("againstElectronVTightMVA5") tauID_againstElectronVTightMVA5', 
    'float tauID("againstMuonLoose") tauID_againstMuonLoose',
    'float tauID("againstMuonLoose2") tauID_againstMuonLoose2', 
    'float tauID("againstMuonLoose3") tauID_againstMuonLoose3',
    'float tauID("againstMuonLooseMVA") tauID_againstMuonLooseMVA',
    'float tauID("againstMuonMVAraw") tauID_againstMuonMVAraw',
    'float tauID("againstMuonMedium") tauID_againstMuonMedium',
    'float tauID("againstMuonMedium2") tauID_againstMuonMedium2',
    'float tauID("againstMuonMediumMVA") tauID_againstMuonMediumMVA',
    'float tauID("againstMuonTight") tauID_againstMuonTight',
    'float tauID("againstMuonTight2") tauID_againstMuonTight2',
    'float tauID("againstMuonTight3") tauID_againstMuonTight3',
    'float tauID("againstMuonTightMVA") tauID_againstMuonTightMVA',
    'float tauID("byCombinedIsolationDeltaBetaCorrRaw") tauID_byCombinedIsolationDeltaBetaCorrRaw',
    'float tauID("byCombinedIsolationDeltaBetaCorrRaw3Hits") tauID_byCombinedIsolationDeltaBetaCorrRaw3Hits',
    'float tauID("byIsolationMVA3newDMwLTraw") tauID_byIsolationMVA3newDMwLTraw',
    'float tauID("byIsolationMVA3newDMwoLTraw") tauID_byIsolationMVA3newDMwoLTraw',
    'float tauID("byIsolationMVA3oldDMwLTraw") tauID_byIsolationMVA3oldDMwLTraw',
    'float tauID("byIsolationMVA3oldDMwoLTraw") tauID_byIsolationMVA3oldDMwoLTraw',
    'float tauID("byLooseCombinedIsolationDeltaBetaCorr") tauID_byLooseCombinedIsolationDeltaBetaCorr',
    'float tauID("byLooseCombinedIsolationDeltaBetaCorr3Hits") tauID_byLooseCombinedIsolationDeltaBetaCorr3Hits',
    'float tauID("byLooseIsolation") tauID_byLooseIsolation',
    'float tauID("byLooseIsolationMVA3newDMwLT") tauID_byLooseIsolationMVA3newDMwLT',
    'float tauID("byLooseIsolationMVA3newDMwoLT") tauID_byLooseIsolationMVA3newDMwoLT',
    'float tauID("byLooseIsolationMVA3oldDMwLT") tauID_byLooseIsolationMVA3oldDMwLT',
    'float tauID("byLooseIsolationMVA3oldDMwoLT") tauID_byLooseIsolationMVA3oldDMwoLT',
    'float tauID("byMediumCombinedIsolationDeltaBetaCorr") tauID_byMediumCombinedIsolationDeltaBetaCorr',
    'float tauID("byMediumCombinedIsolationDeltaBetaCorr3Hits") tauID_byMediumCombinedIsolationDeltaBetaCorr3Hits',
    'float tauID("byMediumIsolationMVA3newDMwLT") tauID_byMediumIsolationMVA3newDMwLT',
    'float tauID("byMediumIsolationMVA3newDMwoLT") tauID_byMediumIsolationMVA3newDMwoLT',
    'float tauID("byMediumIsolationMVA3oldDMwLT") tauID_byMediumIsolationMVA3oldDMwLT',
    'float tauID("byMediumIsolationMVA3oldDMwoLT") tauID_byMediumIsolationMVA3oldDMwoLT',
    'float tauID("byTightCombinedIsolationDeltaBetaCorr") tauID_byTightCombinedIsolationDeltaBetaCorr',
    'float tauID("byTightCombinedIsolationDeltaBetaCorr3Hits") tauID_byTightCombinedIsolationDeltaBetaCorr3Hits',
    'float tauID("byTightIsolationMVA3newDMwLT") tauID_byTightIsolationMVA3newDMwLT',
    'float tauID("byTightIsolationMVA3newDMwoLT") tauID_byTightIsolationMVA3newDMwoLT',
    'float tauID("byTightIsolationMVA3oldDMwLT") tauID_byTightIsolationMVA3oldDMwLT',
    'float tauID("byTightIsolationMVA3oldDMwoLT") tauID_byTightIsolationMVA3oldDMwoLT',
    'float tauID("byVLooseCombinedIsolationDeltaBetaCorr") tauID_byVLooseCombinedIsolationDeltaBetaCorr',
    'float tauID("byVLooseIsolationMVA3newDMwLT") tauID_byVLooseIsolationMVA3newDMwLT',
    'float tauID("byVLooseIsolationMVA3newDMwoLT") tauID_byVLooseIsolationMVA3newDMwoLT',
    'float tauID("byVLooseIsolationMVA3oldDMwLT") tauID_byVLooseIsolationMVA3oldDMwLT',
    'float tauID("byVLooseIsolationMVA3oldDMwoLT") tauID_byVLooseIsolationMVA3oldDMwoLT',
    'float tauID("byVTightIsolationMVA3newDMwLT") tauID_byVTightIsolationMVA3newDMwLT',
    'float tauID("byVTightIsolationMVA3newDMwoLT") tauID_byVTightIsolationMVA3newDMwoLT',
    'float tauID("byVTightIsolationMVA3oldDMwLT") tauID_byVTightIsolationMVA3oldDMwLT',
    'float tauID("byVTightIsolationMVA3oldDMwoLT") tauID_byVTightIsolationMVA3oldDMwoLT',
    'float tauID("byVVTightIsolationMVA3newDMwLT") tauID_byVVTightIsolationMVA3newDMwLT',
    'float tauID("byVVTightIsolationMVA3newDMwoLT") tauID_byVVTightIsolationMVA3newDMwoLT',
    'float tauID("byVVTightIsolationMVA3oldDMwLT") tauID_byVVTightIsolationMVA3oldDMwLT',
    'float tauID("byVVTightIsolationMVA3oldDMwoLT") tauID_byVVTightIsolationMVA3oldDMwoLT',
    'float tauID("chargedIsoPtSum") tauID_chargedIsoPtSum',
    'float tauID("decayModeFinding") tauID_decayModeFinding',
    'float tauID("decayModeFindingNewDMs") tauID_decayModeFindingNewDMs',
    'float tauID("decayModeFindingOldDMs") tauID_decayModeFindingOldDMs',
    'float tauID("neutralIsoPtSum") tauID_neutralIsoPtSum',
    'float tauID("puCorrPtSum") tauID_puCorrPtSum',
    'double leadPFChargedHadrCand()->p()',
    'double leadPFChargedHadrCand()->energy()',
    'double leadPFChargedHadrCand()->et()',
    'double leadPFChargedHadrCand()->mass()',
    'double leadPFChargedHadrCand()->massSqr()',
    'double leadPFChargedHadrCand()->mt()',
    'double leadPFChargedHadrCand()->mtSqr()',
    'double leadPFChargedHadrCand()->px()',
    'double leadPFChargedHadrCand()->py()',
    'double leadPFChargedHadrCand()->pz()',
    'double leadPFChargedHadrCand()->pt()',
    'double leadPFChargedHadrCand()->phi()',
    'double leadPFChargedHadrCand()->theta()',
    'double leadPFChargedHadrCand()->eta()',
    'double leadPFChargedHadrCand()->rapidity()',
    'double leadPFChargedHadrCand()->y()',
    'size_t signalPFChargedHadrCands_size()'
    ),

               patMET =
               cms.untracked.
               vstring(
    'patMET patMETs 200',
    #---------------------------------------------------------------------
    'double p()',
    'double energy()',
    'double et()',
    'double px()',
    'double py()',
    'double pz()',
    'double pt()',
    'double phi()',
    'double eta()'
    ),

               patMET2 =
               cms.untracked.
               vstring(
    'patMET patPfMetT0pcT1Txy 200',
    #---------------------------------------------------------------------
    'double p()',
    'double energy()',
    'double et()',
    'double px()',
    'double py()',
    'double pz()',
    'double pt()',
    'double phi()',
    'double eta()'
    ),

               recoPFMET =
               cms.untracked.
               vstring(
    'recoPFMET pfType1CorrectedMet 200',
    #---------------------------------------------------------------------
    'double p()',
    'double energy()',
    'double et()',
    'double px()',
    'double py()',
    'double pz()',
    'double pt()',
    'double phi()',
    'double eta()'
    ),
               recoPFMET1 =
               cms.untracked.
               vstring(
    'recoPFMET pfType1p2CorrectedMet 200',
    #---------------------------------------------------------------------
    'double p()',
    'double energy()',
    'double et()',
    'double px()',
    'double py()',
    'double pz()',
    'double pt()',
    'double phi()',
    'double eta()'
    ),
               )
