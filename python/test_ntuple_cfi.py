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
    'edmTriggerResultsHelper',
    'recoVertex',
    'PileupSummaryInfo',
    'edmEventHelper',
    'GenRunInfoProduct',
    'recoGenParticleHelper',
    'recoBeamSpot',
    'patJet',
    'patElectron',
    'recoGsfElectron',
    'patMuon',
    'patTau',
    'patMET',
    'recoPFMET',
    'recoPFMET1'
    ),


               #edmTriggerResults =
               edmTriggerResultsHelper =
               cms.untracked.
               vstring(
#    'edmTriggerResults               TriggerResults                    1',
    'edmTriggerResultsHelper          TriggerResults::HLT                    1',
    #---------------------------------------------------------------------
    'int value("HLT_DoubleMediumIsoPFTau35_Trk5_eta2p1_Prong1_v2") value_HLT_DoubleMediumIsoPFTau35_Trk5_eta2p1_Prong1_v2',
    'int prescale("HLT_DoubleMediumIsoPFTau35_Trk5_eta2p1_Prong1_v2") prescale_HLT_DoubleMediumIsoPFTau35_Trk5_eta2p1_Prong1_v2',
    'int value("HLT_DoubleMediumIsoPFTau35_Trk5_eta2p1_Prong1_v3") value_HLT_DoubleMediumIsoPFTau35_Trk5_eta2p1_Prong1_v3',
    'int prescale("HLT_DoubleMediumIsoPFTau35_Trk5_eta2p1_Prong1_v3") prescale_HLT_DoubleMediumIsoPFTau35_Trk5_eta2p1_Prong1_v3',
    'int value("HLT_DoubleMediumIsoPFTau35_Trk5_eta2p1_Prong1_v4") value_HLT_DoubleMediumIsoPFTau35_Trk5_eta2p1_Prong1_v4',
    'int prescale("HLT_DoubleMediumIsoPFTau35_Trk5_eta2p1_Prong1_v4") prescale_HLT_DoubleMediumIsoPFTau35_Trk5_eta2p1_Prong1_v4',
    'int value("HLT_DoubleMediumIsoPFTau35_Trk5_eta2p1_Prong1_v6") value_HLT_DoubleMediumIsoPFTau35_Trk5_eta2p1_Prong1_v6',
    'int prescale("HLT_DoubleMediumIsoPFTau35_Trk5_eta2p1_Prong1_v6") prescale_HLT_DoubleMediumIsoPFTau35_Trk5_eta2p1_Prong1_v6',
    'int value("HLT_DoubleMediumIsoPFTau35_Trk1_eta2p1_Prong1_v3") value_HLT_DoubleMediumIsoPFTau35_Trk1_eta2p1_Prong1_v3',
    'int prescale("HLT_DoubleMediumIsoPFTau35_Trk1_eta2p1_Prong1_v3") prescale_HLT_DoubleMediumIsoPFTau35_Trk1_eta2p1_Prong1_v3',
    'int value("HLT_DoubleMediumIsoPFTau35_Trk1_eta2p1_Prong1_v4") value_HLT_DoubleMediumIsoPFTau35_Trk1_eta2p1_Prong1_v4',
    'int prescale("HLT_DoubleMediumIsoPFTau35_Trk1_eta2p1_Prong1_v4") prescale_HLT_DoubleMediumIsoPFTau35_Trk1_eta2p1_Prong1_v4'
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
    ),

               patElectron =
               cms.untracked.
               vstring(
    'patElectron                     patElectrons                    200',
    #---------------------------------------------------------------------
    'double  p()',
    'double  energy()',
    'double  et()',
    'double  px()',
    'double  py()',
    'double  pz()',
    'double  pt()',
    'double  phi()',
    'double  eta()',
    'float  eSuperClusterOverP()',
    'float  deltaEtaSuperClusterTrackAtVtx()',
    'float  deltaPhiSuperClusterTrackAtVtx()',
    'float  sigmaIetaIeta()',
    'float  scE1x5()',
    'float  scE2x5Max()',
    'float  scE5x5()',
    'float  hadronicOverEm()',
    'float  dr04TkSumPt()',
    'float  dr04EcalRecHitSumEt()',
    'double  gsfTrack()->dxy()',
    'double  gsfTrack()->d0()',
    'double  gsfTrack()->dz()'
    ),
               recoGsfElectron =
               cms.untracked.
               vstring(
    'recoGsfElectron                 gsfElectrons                    200',
    #---------------------------------------------------------------------
    'double  p()',
    'double  energy()',
    'double  et()',
    'double  px()',
    'double  py()',
    'double  pz()',
    'double  pt()',
    'double  phi()',
    'double  eta()',
    'float  eSuperClusterOverP()',
    'float  deltaEtaSuperClusterTrackAtVtx()',
    'float  deltaPhiSuperClusterTrackAtVtx()',
    'float  sigmaIetaIeta()',
    'float  scE1x5()',
    'float  scE2x5Max()',
    'float  scE5x5()',
    'float  hadronicOverEm()',
    'float  dr04TkSumPt()',
    'float  dr04EcalRecHitSumEt()',
    'double  gsfTrack()->dxy()',
    'double  gsfTrack()->d0()',
    'double  gsfTrack()->dz()'
    
    ),

               patMuon =
               cms.untracked.
               vstring(
    'patMuon                         patMuons                        200',
    #---------------------------------------------------------------------
    'double  p()',
    'double  energy()',
    'double  et()',
    'double  px()',
    'double  py()',
    'double  pz()',
    'double  pt()',
    'double  phi()',
    'double  eta()',
    'bool  isGlobalMuon()',
    'bool  isTrackerMuon()',
    'bool  isPFMuon()',
    'float  pfIsolationR03()->sumChargedHadronPt',
    'float  pfIsolationR03()->sumChargedParticlePt',
    'float  pfIsolationR03()->sumNeutralHadronEt',
    'float  pfIsolationR03()->sumNeutralHadronEtHighThreshold',
    'float  pfIsolationR03()->sumPhotonEt',
    'float  pfIsolationR03()->sumPhotonEtHighThreshold',
    'float  pfIsolationR03()->sumPUPt',
    'float  pfIsolationR04()->sumChargedHadronPt',
    'float  pfIsolationR04()->sumChargedParticlePt',
    'float  pfIsolationR04()->sumNeutralHadronEt',
    'float  pfIsolationR04()->sumNeutralHadronEtHighThreshold',
    'float  pfIsolationR04()->sumPhotonEt',
    'float  pfIsolationR04()->sumPhotonEtHighThreshold',
    'float  pfIsolationR04()->sumPUPt',
    'int  numberOfMatchedStations()',
    'double  innerTrack()->normalizedChi2()',
    'double  innerTrack()->dxy()',
    'double  innerTrack()->dz()',
    'int  innerTrack()->hitPattern().numberOfValidPixelHits()',
    'int  innerTrack()->hitPattern().pixelLayersWithMeasurement()',
    'double  globalTrack()->normalizedChi2()',
    'int  globalTrack()->hitPattern().numberOfValidMuonHits()',
    'double  muonBestTrack()->dxy()',
    'double  muonBestTrack()->dz()'
    ),

               patTau =
               cms.untracked.
               vstring(
    'patTauHelper                          patTaus                         200',
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
    'float  tauID("byIsolationMVAraw") tauID_byIsolationMVAraw',
    'float  tauID("byMediumCombinedIsolationDeltaBetaCorr") tauID_byMediumCombinedIsolationDeltaBetaCorr',
    'float  tauID("byCombinedIsolationDeltaBetaCorrRaw3Hits") tauID_byCombinedIsolationDeltaBetaCorrRaw3Hits',
    'float  tauID("againstMuonMedium") tauID_againstMuonMedium',
    'float  tauID("againstElectronTightMVA3") tauID_againstElectronTightMVA3',
    'float  tauID("againstElectronTightMVA2") tauID_againstElectronTightMVA2',
    'float  tauID("byLooseIsolationMVA2") tauID_byLooseIsolationMVA2',
    'float  tauID("againstMuonTight") tauID_againstMuonTight',
    'float  tauID("againstMuonLoose2") tauID_againstMuonLoose2',
    'float  tauID("byTightIsolationMVA") tauID_byTightIsolationMVA',
    'float  tauID("byLooseIsolation") tauID_byLooseIsolation',
    'float  tauID("byLooseCombinedIsolationDeltaBetaCorr") tauID_byLooseCombinedIsolationDeltaBetaCorr',
    'float  tauID("againstElectronLooseMVA3") tauID_againstElectronLooseMVA3',
    'float  tauID("againstElectronLooseMVA2") tauID_againstElectronLooseMVA2',
    'float  tauID("againstElectronTight") tauID_againstElectronTight',
    'float  tauID("byVLooseCombinedIsolationDeltaBetaCorr") tauID_byVLooseCombinedIsolationDeltaBetaCorr',
    'float  tauID("againstElectronVTightMVA3") tauID_againstElectronVTightMVA3',
    'float  tauID("againstElectronMediumMVA3") tauID_againstElectronMediumMVA3',
    'float  tauID("againstElectronMediumMVA2") tauID_againstElectronMediumMVA2',
    'float  tauID("againstElectronMVA") tauID_againstElectronMVA',
    'float  tauID("againstMuonLoose") tauID_againstMuonLoose',
    'float  tauID("againstMuonTight2") tauID_againstMuonTight2',
    'float  tauID("againstElectronMedium") tauID_againstElectronMedium',
    'float  tauID("againstElectronVLooseMVA2") tauID_againstElectronVLooseMVA2',
    'float  tauID("againstMuonMedium2") tauID_againstMuonMedium2',
    'float  tauID("byMediumIsolationMVA") tauID_byMediumIsolationMVA',
    'float  tauID("byMediumCombinedIsolationDeltaBetaCorr3Hits") tauID_byMediumCombinedIsolationDeltaBetaCorr3Hits',
    'float  tauID("byLooseIsolationDeltaBetaCorr") tauID_byLooseIsolationDeltaBetaCorr',
    'float  tauID("byIsolationMVA2raw") tauID_byIsolationMVA2raw',
    'float  tauID("byTightIsolationMVA2") tauID_byTightIsolationMVA2',
    'float  tauID("againstElectronMVA2category") tauID_againstElectronMVA2category',
    'float  tauID("byTightIsolationDeltaBetaCorr") tauID_byTightIsolationDeltaBetaCorr',
    'float  tauID("againstElectronDeadECAL") tauID_againstElectronDeadECAL',
    'float  tauID("againstElectronMVA3category") tauID_againstElectronMVA3category',
    'float  tauID("byVLooseIsolationDeltaBetaCorr") tauID_byVLooseIsolationDeltaBetaCorr',
    'float  tauID("againstElectronMVA2raw") tauID_againstElectronMVA2raw',
    'float  tauID("byTightCombinedIsolationDeltaBetaCorr") tauID_byTightCombinedIsolationDeltaBetaCorr',
    'float  tauID("againstElectronMVA3raw") tauID_againstElectronMVA3raw',
    'float  tauID("byLooseCombinedIsolationDeltaBetaCorr3Hits") tauID_byLooseCombinedIsolationDeltaBetaCorr3Hits',
    'float  tauID("byMediumIsolationMVA2") tauID_byMediumIsolationMVA2',
    'float  tauID("byMediumIsolationDeltaBetaCorr") tauID_byMediumIsolationDeltaBetaCorr',
    'float  tauID("againstElectronLoose") tauID_againstElectronLoose',
    'float  tauID("byTightIsolation") tauID_byTightIsolation',
    'float  tauID("byVLooseIsolation") tauID_byVLooseIsolation',
    'float  tauID("byLooseIsolationMVA") tauID_byLooseIsolationMVA',
    'float  tauID("byCombinedIsolationDeltaBetaCorrRaw") tauID_byCombinedIsolationDeltaBetaCorrRaw',
    'float  tauID("byTightCombinedIsolationDeltaBetaCorr3Hits") tauID_byTightCombinedIsolationDeltaBetaCorr3Hits',
    'float  tauID("decayModeFinding") tauID_decayModeFinding',
    'float  tauID("byMediumIsolation") tauID_byMediumIsolation',
    'double  leadPFChargedHadrCand()->p()',
    'double  leadPFChargedHadrCand()->energy()',
    'double  leadPFChargedHadrCand()->et()',
    'double  leadPFChargedHadrCand()->mass()',
    'double  leadPFChargedHadrCand()->massSqr()',
    'double  leadPFChargedHadrCand()->mt()',
    'double  leadPFChargedHadrCand()->mtSqr()',
    'double  leadPFChargedHadrCand()->px()',
    'double  leadPFChargedHadrCand()->py()',
    'double  leadPFChargedHadrCand()->pz()',
    'double  leadPFChargedHadrCand()->pt()',
    'double  leadPFChargedHadrCand()->phi()',
    'double  leadPFChargedHadrCand()->theta()',
    'double  leadPFChargedHadrCand()->eta()',
    'double  leadPFChargedHadrCand()->rapidity()',
    'double  leadPFChargedHadrCand()->y()',
    'size_t  signalPFChargedHadrCands_size()'
    ),

               patMET =
               cms.untracked.
               vstring(
    'patMET                          patMETs                         200',
    #---------------------------------------------------------------------
    'double  p()',
    'double  energy()',
    'double  et()',
    'double  px()',
    'double  py()',
    'double  pz()',
    'double  pt()',
    'double  phi()',
    'double  eta()'
    ),

               recoPFMET =
               cms.untracked.
               vstring(
    'recoPFMET                       pfType1CorrectedMet             200',
    #---------------------------------------------------------------------
    'double  p()',
    'double  energy()',
    'double  et()',
    'double  px()',
    'double  py()',
    'double  pz()',
    'double  pt()',
    'double  phi()',
    'double  eta()'
    ),
               recoPFMET1 =
               cms.untracked.
               vstring(
    'recoPFMET                       pfType1p2CorrectedMet           200',
    #---------------------------------------------------------------------
    'double  p()',
    'double  energy()',
    'double  et()',
    'double  px()',
    'double  py()',
    'double  pz()',
    'double  pt()',
    'double  phi()',
    'double  eta()'
    )



               )
