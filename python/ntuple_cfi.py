#-------------------------------------------------------------------------
# Created: Tue Apr  7 18:04:55 2015 by mkntuplecfi.py
#-------------------------------------------------------------------------
import FWCore.ParameterSet.Config as cms
demo =\
cms.EDAnalyzer("TheNtupleMaker",
               ntupleName = cms.untracked.string("ntuple.root"),
               analyzerName = cms.untracked.string("analyzer.cc"),


# NOTE: the names listed below will be the prefixes for
#       the associated C++ variables created by mkanalyzer.py
#       and the asscociated C++ structs.

               buffers =
               cms.untracked.
               vstring(
    'BeamSpot',
    'Electron',
    'Jet',
    'MET',
    'Muon',
    'Tau',
    'GenParticleHelper',
    'Vertex'
    ),

               BeamSpot =
               cms.untracked.
               vstring(
    'recoBeamSpot                    offlineBeamSpot                   1',
    #---------------------------------------------------------------------
    'double  x0()',
    'double  y0()',
    'double  z0()'
    ),
               Electron =
               cms.untracked.
               vstring(
    'patElectron                     slimmedElectrons                200',
    #---------------------------------------------------------------------
    'int  charge()',
    'double  p()',
    'double  energy()',
    'double  et()',
    'double  px()',
    'double  py()',
    'double  pz()',
    'float  pt()',
    'float  phi()',
    'float  eta()',
    'float  trackIso()',
    'float  ecalIso()',
    'float  hcalIso()',
    'float  caloIso()',
    'bool  isPF()',
    'float  eSuperClusterOverP()',
    'float  deltaEtaSuperClusterTrackAtVtx()',
    'float  deltaPhiSuperClusterTrackAtVtx()',
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
               Jet =
               cms.untracked.
               vstring(
    'patJet                          slimmedJets                     200',
    #---------------------------------------------------------------------
    'int  charge()',
    'double  p()',
    'double  energy()',
    'double  et()',
    'double  px()',
    'double  py()',
    'double  pz()',
    'float  pt()',
    'float  phi()',
    'float  eta()',
    'int  partonFlavour()',
    'int  hadronFlavour()',
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
    'float  chargedMuEnergy()',
    'float  chargedMuEnergyFraction()',
    'int  neutralMultiplicity()',
    'size_t  numberOfDaughters()',
    #'float bDiscriminator("simpleSecondaryVertexBJetTags") bDiscriminator_simpleSecondaryVertexBJetTags ',
    #'float bDiscriminator("combinedSecondaryVertexMVABJetTags") bDiscriminator_combinedSecondaryVertexMVABJetTags ',
    #'float bDiscriminator("combinedSecondaryVertexBJetTags") bDiscriminator_combinedSecondaryVertexBJetTags '
    ),
	       MET =
	       cms.untracked.
	       vstring(
			       'patMET                          slimmedMETs                     200',
			       #---------------------------------------------------------------------
			       'double  p()',
			       'double  energy()',
			       'double  et()',
			       'double  px()',
			       'double  py()',
			       'double  pz()',
			       'float  pt()',
			       'float  phi()',
			       'float  eta()'
			       ),
	       Muon =
	       cms.untracked.
	       vstring(
			       'patMuon                         slimmedMuons                    200',
			       #---------------------------------------------------------------------
			       'int  charge()',
			       'double  p()',
			       'double  energy()',
			       'double  et()',
			       'double  px()',
			       'double  py()',
			       'double  pz()',
			       'float  pt()',
			       'float  phi()',
			       'float  eta()',
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
	       Tau =
	       cms.untracked.
	       vstring(
			       'patTauHelper                          slimmedTaus                     200',
			       #    'patTau                          slimmedTaus                     200',
			       #---------------------------------------------------------------------
			       'int  charge()',
			       'double  p()',
			       'double  energy()',
			       'double  et()',
			       'double  px()',
			       'double  py()',
			       'double  pz()',
			       'float  pt()',
			       'float  phi()',
			       'float  eta()',
			       'float  mass()',
			       'double  leadChargedHadrCand()->p()',
			       'double  leadChargedHadrCand()->energy()',
			       'double  leadChargedHadrCand()->et()',
			       'float  leadChargedHadrCand()->mass()',
			       'float  leadChargedHadrCand()->massSqr()',
			       'double  leadChargedHadrCand()->mt()',
			       'double  leadChargedHadrCand()->mtSqr()',
			       'double  leadChargedHadrCand()->px()',
			       'double  leadChargedHadrCand()->py()',
			       'double  leadChargedHadrCand()->pz()',
			       'float  leadChargedHadrCand()->pt()',
			       'float  leadChargedHadrCand()->phi()',
			       'double  leadChargedHadrCand()->theta()',
			       'float  leadChargedHadrCand()->eta()',
			       'double  leadChargedHadrCand()->rapidity()',
			       'double  leadChargedHadrCand()->y()',
			       'size_t signalChargedHadrCands_size()',
			       #    'double  electronPreIDTrack()->outerY()',
			       #    'double  electronPreIDTrack()->outerP()',
			       #    'double  electronPreIDTrack()->outerRadius()',
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
    'float tauID("byCombinedIsolationDeltaBetaCorrRaw3Hits") tauID_byCombinedIsolationDeltaBetaCorrRaw3Hits',
    'float tauID("byIsolationMVA3newDMwLTraw") tauID_byIsolationMVA3newDMwLTraw',
    'float tauID("byIsolationMVA3newDMwoLTraw") tauID_byIsolationMVA3newDMwoLTraw',
    'float tauID("byIsolationMVA3oldDMwLTraw") tauID_byIsolationMVA3oldDMwLTraw',
    'float tauID("byIsolationMVA3oldDMwoLTraw") tauID_byIsolationMVA3oldDMwoLTraw',
    'float tauID("byLooseCombinedIsolationDeltaBetaCorr3Hits") tauID_byLooseCombinedIsolationDeltaBetaCorr3Hits',
    'float tauID("byLooseIsolationMVA3newDMwLT") tauID_byLooseIsolationMVA3newDMwLT',
    'float tauID("byLooseIsolationMVA3newDMwoLT") tauID_byLooseIsolationMVA3newDMwoLT',
    'float tauID("byLooseIsolationMVA3oldDMwLT") tauID_byLooseIsolationMVA3oldDMwLT',
    'float tauID("byLooseIsolationMVA3oldDMwoLT") tauID_byLooseIsolationMVA3oldDMwoLT',
    'float tauID("byMediumCombinedIsolationDeltaBetaCorr3Hits") tauID_byMediumCombinedIsolationDeltaBetaCorr3Hits',
    'float tauID("byMediumIsolationMVA3newDMwLT") tauID_byMediumIsolationMVA3newDMwLT',
    'float tauID("byMediumIsolationMVA3newDMwoLT") tauID_byMediumIsolationMVA3newDMwoLT',
    'float tauID("byMediumIsolationMVA3oldDMwLT") tauID_byMediumIsolationMVA3oldDMwLT',
    'float tauID("byMediumIsolationMVA3oldDMwoLT") tauID_byMediumIsolationMVA3oldDMwoLT',
    'float tauID("byTightCombinedIsolationDeltaBetaCorr3Hits") tauID_byTightCombinedIsolationDeltaBetaCorr3Hits',
    'float tauID("byTightIsolationMVA3newDMwLT") tauID_byTightIsolationMVA3newDMwLT',
    'float tauID("byTightIsolationMVA3newDMwoLT") tauID_byTightIsolationMVA3newDMwoLT',
    'float tauID("byTightIsolationMVA3oldDMwLT") tauID_byTightIsolationMVA3oldDMwLT',
    'float tauID("byTightIsolationMVA3oldDMwoLT") tauID_byTightIsolationMVA3oldDMwoLT',
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
    'float tauID("neutralIsoPtSum") tauID_neutralIsoPtSum',
    'float tauID("puCorrPtSum") tauID_puCorrPtSum'
    ),
	       GenParticleHelper =
	       cms.untracked.
	       vstring(
			       'recoGenParticleHelper2                 prunedGenParticles              200',
			       #---------------------------------------------------------------------
			       'int  charge()',
			       'int pdgId()',
			       'int status()',
			       'double  energy()',
			       'float  pt()',
			       'float  phi()',
			       'float  eta()',
			       'float  mass()',
			       'int firstMother()',
			       'int lastMother()',
			       'int firstDaughter()',
			       'int lastDaughter()'
			       ),
	       Vertex =
	       cms.untracked.
	       vstring(
			       'recoVertex                      offlineSlimmedPrimaryVertices   200',
			       #---------------------------------------------------------------------
			       'bool  isValid()',
			       'bool  isFake()',
			       'double  chi2()',
			       'double  ndof()',
			       'double  x()',
			       'double  y()',
			       'double  z()'
			       )
	       )
