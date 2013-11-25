#ifndef PATTAUHELPER_H
#define PATTAUHELPER_H
//-----------------------------------------------------------------------------
// Subsystem:   ntuples
// Package:     VBF-LS-tau-ntupler
// Description: TheNtupleMaker helper class for pat::Tau
// Created:     Mon Nov 18 14:23:58 2013
// Author:      Daniele Marconi      
//-----------------------------------------------------------------------------
#include <algorithm>
#include <iostream>
#include <vector>
#include <map>
#include "PhysicsTools/TheNtupleMaker/interface/HelperFor.h"
#include "DataFormats/PatCandidates/interface/Tau.h"
//-----------------------------------------------------------------------------
// Definitions:
//   helper:        object of class TauHelper
//   helped object: object of class pat::Tau
//
//
// The following variables are automatically defined and available to
//       all methods:
//
//         blockname          name of config. buffer object (config block) 
//         buffername         name of buffer in config block
//         labelname          name of label in config block (for getByLabel)
//         parameter          parameter (as key, value pairs)
//                            accessed as in the following example:
//
//                            string param = parameter("label");
//
//         0. hltconfig       pointer to HLTConfigProvider
//                            Note: this will be zero if HLTConfigProvider
//                                  has not been properly initialized
//
//         1. config          pointer to global ParameterSet object
//         2. event           pointer to the current event
//         3. object          pointer to the current helped object
//         4. oindex          index of current helped object
//
//         5. index           index of item(s) returned by helper.
//                            Note 1: an item is associated with all
//                                    helper methods (think of it as an
//                                    extension of the helped object)
//                                  
//                            Note 2: index may differ from oindex if,
//                                    for a given helped object, the count
//                                    variable (see below) differs from 1.
//
//         6. count           number of items per helped object (default=1)
//                            Note:
//                                  count = 0  ==> current helped object is
//                                                 to be skipped
//
//                                  count = 1  ==> current helped object is
//                                                 to be kept
//
//                                  count > 1  ==> current helped object is
//                                                 associated with "count"
//                                                 items, where each item
//                                                 is associated with all the
//                                                 helper methods
//
//       variables 0-6 are initialized by TheNtupleMaker.
//       variables 0-5 should not be changed.
//       variable    6 can be changed by the helper to control whether a
//                     helped object should be kept or generates more items
//-----------------------------------------------------------------------------

namespace pat
{
  /// A helper class for pat::Tau.
  class TauHelper : public HelperFor<pat::Tau>
  {
  public:
	///
	TauHelper();

	virtual ~TauHelper();

	// Uncomment if this class does some event-level analysis
	// virtual void analyzeEvent();
	 
	// Uncomment if this class does some object-level analysis
	// virtual void analyzeObject();

	// ---------------------------------------------------------
	// -- User access methods go here
	// ---------------------------------------------------------

        size_t signalPFChargedHadrCands_size() const
        {return object->signalPFChargedHadrCands().size();}
	
  private:
    // -- User internals


  public:
    // ---------------------------------------------------------
    // -- Access Methods
    // ---------------------------------------------------------

	// WARNING: some methods may fail to compile because of coding
	//          problems in one of the CMSSW base classes. If so,
	//          just comment out the offending method and try again.
  


    // from reco::BaseTau
    math::XYZTLorentzVector alternatLorentzVect() const
    { return object->alternatLorentzVect(); }

    // from pat::Tau
    const std::vector<std::string> availableJECLevels(int set=0) const
    { return object->availableJECLevels(set); }

    // from pat::Tau
    const std::vector<std::string> availableJECLevels(std::string set) const
    { return object->availableJECLevels(set); }

    // from pat::Tau
    const std::vector<std::string> availableJECSets() const
    { return object->availableJECSets(); }

    // from reco::RecoCandidate
    reco::Track* bestTrack() const
    { return (reco::Track*)object->bestTrack(); }

    // from reco::RecoCandidate
    reco::TrackBaseRef bestTrackRef() const { return object->bestTrackRef(); }

    // from reco::RecoCandidate
    reco::RecoCandidate::TrackType bestTrackType() const
    { return object->bestTrackType(); }

    // from reco::LeafCandidate
    math::XYZVector boostToCM() const { return object->boostToCM(); }

    // from pat::Tau
    float bremsRecoveryEOverPLead() const
    { return object->bremsRecoveryEOverPLead(); }

    // from pat::Tau
    float caloComp() const { return object->caloComp(); }

    // from pat::Lepton<reco::BaseTau>
    float caloIso() const { return object->caloIso(); }

    // from pat::Tau
    const pat::tau::TauCaloSpecific caloSpecific() const
    { return object->caloSpecific(); }

    // from pat::Tau
    reco::CaloTauTagInfoRef caloTauTagInfoRef() const
    { return object->caloTauTagInfoRef(); }

    // from reco::RecoCandidate
    CaloTowerRef caloTower() const { return object->caloTower(); }

    // from reco::LeafCandidate
    int charge() const { return object->charge(); }

    // from pat::Lepton<reco::BaseTau>
    float chargedHadronIso() const { return object->chargedHadronIso(); }

    // from reco::RecoCandidate
    reco::TrackRef combinedMuon() const { return object->combinedMuon(); }

    // from pat::Tau
    const math::XYZTLorentzVector
    correctedP4(std::string level, std::string set="") const
    { return object->correctedP4(level, set); }

    // from pat::Tau
    const math::XYZTLorentzVector
    correctedP4(unsigned int level, unsigned int set=0) const
    { return object->correctedP4(level, set); }

    // from pat::Tau
    pat::Tau correctedTauJet(std::string level, std::string set="") const
    { return object->correctedTauJet(level, set); }

    // from pat::Tau
    pat::Tau correctedTauJet(unsigned int level, unsigned int set=0) const
    { return object->correctedTauJet(level, set); }

    // from pat::Tau
    std::string currentJECLevel() const { return object->currentJECLevel(); }

    // from pat::Tau
    std::string currentJECSet() const { return object->currentJECSet(); }

    // from reco::LeafCandidate
    reco::Candidate* daughter(size_t x0) const
    { return (reco::Candidate*)object->daughter(x0); }

    // from reco::LeafCandidate
    reco::Candidate* daughter(std::string s) const
    { return (reco::Candidate*)object->daughter(s); }

    // from pat::Tau
    int decayMode() const { return object->decayMode(); }

    // from pat::Tau
    double dxy() const { return object->dxy(); }

    // from pat::Tau
    double dxy_error() const { return object->dxy_error(); }

    // from pat::Tau
    const math::XYZPoint dxy_PCA() const { return object->dxy_PCA(); }

    // from pat::Tau
    double dxy_Sig() const { return object->dxy_Sig(); }

    // from pat::Lepton<reco::BaseTau>
    float ecalIso() const { return object->ecalIso(); }

    // from pat::Lepton<reco::BaseTau>
    pat::IsoDeposit* ecalIsoDeposit() const
    { return (pat::IsoDeposit*)object->ecalIsoDeposit(); }

    // from pat::Tau
    float ecalStripSumEOverPLead() const
    { return object->ecalStripSumEOverPLead(); }

    // from pat::PATObject<reco::BaseTau>
    std::vector<std::pair<std::string,pat::LookupTableRecord> >
    efficiencies() const
    { return object->efficiencies(); }

    // from pat::PATObject<reco::BaseTau>
    const pat::LookupTableRecord efficiency(std::string name) const
    { return object->efficiency(name); }

    // from pat::PATObject<reco::BaseTau>
    const std::vector<std::string> efficiencyNames() const
    { return object->efficiencyNames(); }

    // from pat::PATObject<reco::BaseTau>
    const std::vector<pat::LookupTableRecord> efficiencyValues() const
    { return object->efficiencyValues(); }

    // from pat::Tau
    bool electronPreIDDecision() const
    { return object->electronPreIDDecision(); }

    // from pat::Tau
    float electronPreIDOutput() const { return object->electronPreIDOutput(); }

    // from pat::Tau
    const reco::TrackRef electronPreIDTrack() const
    { return object->electronPreIDTrack(); }

    // from pat::Tau
    float emFraction() const { return object->emFraction(); }

    // from reco::LeafCandidate
    double energy() const { return object->energy(); }

    // from reco::LeafCandidate
    double et() const { return object->et(); }

    // from reco::LeafCandidate
    double eta() const { return object->eta(); }

    // from pat::Tau
    float etaetaMoment() const { return object->etaetaMoment(); }

    // from pat::Tau
    float etaphiMoment() const { return object->etaphiMoment(); }

    // from pat::Tau
    const math::XYZVector flightLength() const
    { return object->flightLength(); }

    // from pat::Tau
    ROOT::Math::SMatrix<double,3,3,ROOT::Math::MatRepSym<double,3> >
    flightLengthCov() const
    { return object->flightLengthCov(); }

    // from pat::Tau
    double flightLengthSig() const { return object->flightLengthSig(); }

    // from pat::Tau
    reco::GenJet* genJet() const { return (reco::GenJet*)object->genJet(); }

    // from pat::Lepton<reco::BaseTau>
    reco::GenParticle* genLepton() const
    { return (reco::GenParticle*)object->genLepton(); }

    // from pat::PATObject<reco::BaseTau>
    reco::GenParticle* genParticle(size_t idx=0) const
    { return (reco::GenParticle*)object->genParticle(idx); }

    // from pat::PATObject<reco::BaseTau>
    /**
    reco::GenParticleRef
    genParticleById(int pdgId, int status, uint8_t autoCharge=0) const
    { return object->genParticleById(pdgId, status, autoCharge); }
    */

    // from pat::PATObject<reco::BaseTau>
    reco::GenParticleRef genParticleRef(size_t idx=0) const
    { return object->genParticleRef(idx); }

    // from pat::PATObject<reco::BaseTau>
    std::vector<reco::GenParticleRef> genParticleRefs() const
    { return object->genParticleRefs(); }

    // from pat::PATObject<reco::BaseTau>
    size_t genParticlesSize() const { return object->genParticlesSize(); }

    // from pat::PATObject<reco::BaseTau>
    const pat::CandKinResolution getKinResolution(std::string label="") const
    { return object->getKinResolution(label); }

    // from reco::RecoCandidate
    reco::GsfTrackRef gsfTrack() const { return object->gsfTrack(); }

    // from pat::PATObject<reco::BaseTau>
    bool hasKinResolution(std::string label="") const
    { return object->hasKinResolution(label); }

    // from pat::PATObject<reco::BaseTau>
    bool hasOverlaps(std::string label) const
    { return object->hasOverlaps(label); }

    // from pat::Tau
    bool hasSecondaryVertex() const { return object->hasSecondaryVertex(); }

    // from pat::PATObject<reco::BaseTau>
    bool hasUserCand(std::string key) const
    { return object->hasUserCand(key); }

    // from pat::PATObject<reco::BaseTau>
    bool hasUserData(std::string key) const
    { return object->hasUserData(key); }

    // from pat::PATObject<reco::BaseTau>
    bool hasUserFloat(char* key) const { return object->hasUserFloat(key); }

    // from pat::PATObject<reco::BaseTau>
    bool hasUserFloat(std::string key) const
    { return object->hasUserFloat(key); }

    // from pat::PATObject<reco::BaseTau>
    bool hasUserInt(std::string key) const { return object->hasUserInt(key); }

    // from pat::Tau
    float hcal3x3OverPLead() const { return object->hcal3x3OverPLead(); }

    // from pat::Lepton<reco::BaseTau>
    float hcalIso() const { return object->hcalIso(); }

    // from pat::Lepton<reco::BaseTau>
    pat::IsoDeposit* hcalIsoDeposit() const
    { return (pat::IsoDeposit*)object->hcalIsoDeposit(); }

    // from pat::Tau
    float hcalMaxOverPLead() const { return object->hcalMaxOverPLead(); }

    // from pat::Tau
    float hcalTotOverPLead() const { return object->hcalTotOverPLead(); }

    // from reco::LeafCandidate
    bool isCaloMuon() const { return object->isCaloMuon(); }

    // from pat::Tau
    bool isCaloTau() const { return object->isCaloTau(); }

    // from reco::LeafCandidate
    bool isConvertedPhoton() const { return object->isConvertedPhoton(); }

    // from reco::LeafCandidate
    bool isElectron() const { return object->isElectron(); }

    // from reco::LeafCandidate
    bool isGlobalMuon() const { return object->isGlobalMuon(); }

    // from reco::LeafCandidate
    bool isJet() const { return object->isJet(); }

    // from reco::LeafCandidate
    bool isMuon() const { return object->isMuon(); }

    // from pat::Lepton<reco::BaseTau>
    /**
    pat::IsoDeposit* isoDeposit(pat::IsolationKeys key) const
    { return (pat::IsoDeposit*)object->isoDeposit(key); }
    */

    // from pat::Tau
    float isolationECALhitsEtSum() const
    { return object->isolationECALhitsEtSum(); }

    // from pat::Tau
    const std::vector<edm::Ptr<reco::PFCandidate> > isolationPFCands() const
    { return object->isolationPFCands(); }

    // from pat::Tau
    const std::vector<edm::Ptr<reco::PFCandidate> >
    isolationPFChargedHadrCands() const
    { return object->isolationPFChargedHadrCands(); }

    // from pat::Tau
    float isolationPFChargedHadrCandsPtSum() const
    { return object->isolationPFChargedHadrCandsPtSum(); }

    // from pat::Tau
    const std::vector<edm::Ptr<reco::PFCandidate> >
    isolationPFGammaCands() const
    { return object->isolationPFGammaCands(); }

    // from pat::Tau
    float isolationPFGammaCandsEtSum() const
    { return object->isolationPFGammaCandsEtSum(); }

    // from pat::Tau
    const std::vector<edm::Ptr<reco::PFCandidate> >
    isolationPFNeutrHadrCands() const
    { return object->isolationPFNeutrHadrCands(); }

    // from pat::Tau
    const std::vector<reco::RecoTauPiZero> isolationPiZeroCandidates() const
    { return object->isolationPiZeroCandidates(); }

    // from pat::Tau
    const std::vector<reco::PFRecoTauChargedHadron>
    isolationTauChargedHadronCandidates() const
    { return object->isolationTauChargedHadronCandidates(); }

    // from pat::Tau
    const reco::TrackRefVector isolationTracks() const
    { return object->isolationTracks(); }

    // from pat::Tau
    float isolationTracksPtSum() const
    { return object->isolationTracksPtSum(); }

    // from pat::Tau
    bool isPFTau() const { return object->isPFTau(); }

    // from reco::LeafCandidate
    bool isPhoton() const { return object->isPhoton(); }

    // from reco::LeafCandidate
    bool isStandAloneMuon() const { return object->isStandAloneMuon(); }

    // from pat::Tau
    bool isTauIDAvailable(std::string name) const
    { return object->isTauIDAvailable(name); }

    // from reco::LeafCandidate
    bool isTrackerMuon() const { return object->isTrackerMuon(); }

    // from pat::Tau
    float jecFactor(std::string level, std::string set="") const
    { return object->jecFactor(level, set); }

    // from pat::Tau
    float jecFactor(unsigned int level, unsigned int set=0) const
    { return object->jecFactor(level, set); }

    // from pat::Tau
    bool jecSetAvailable(std::string set) const
    { return object->jecSetAvailable(set); }

    // from pat::Tau
    bool jecSetAvailable(unsigned int set) const
    { return object->jecSetAvailable(set); }

    // from pat::Tau
    bool jecSetsAvailable() const { return object->jecSetsAvailable(); }

    // from pat::Tau
    const reco::PFCandidatePtr leadPFCand() const
    { return object->leadPFCand(); }

    // from pat::Tau
    const reco::PFCandidatePtr leadPFChargedHadrCand() const
    { return object->leadPFChargedHadrCand(); }

    // from pat::Tau
    float leadPFChargedHadrCandsignedSipt() const
    { return object->leadPFChargedHadrCandsignedSipt(); }

    // from pat::Tau
    const reco::PFCandidatePtr leadPFNeutralCand() const
    { return object->leadPFNeutralCand(); }

    // from pat::Tau
    reco::PFRecoTauChargedHadronRef leadTauChargedHadronCandidate() const
    { return object->leadTauChargedHadronCandidate(); }

    // from pat::Tau
    reco::TrackRef leadTrack() const { return object->leadTrack(); }

    // from pat::Tau
    float leadTrackHCAL3x3hitsEtSum() const
    { return object->leadTrackHCAL3x3hitsEtSum(); }

    // from pat::Tau
    float leadTrackHCAL3x3hottesthitDEta() const
    { return object->leadTrackHCAL3x3hottesthitDEta(); }

    // from pat::Tau
    float leadTracksignedSipt() const { return object->leadTracksignedSipt(); }

    // from reco::LeafCandidate
    bool longLived() const { return object->longLived(); }

    // from reco::LeafCandidate
    double mass() const { return object->mass(); }

    // from reco::LeafCandidate
    bool massConstraint() const { return object->massConstraint(); }

    // from reco::LeafCandidate
    double massSqr() const { return object->massSqr(); }

    // from pat::Tau
    float maximumHCALhitEt() const { return object->maximumHCALhitEt(); }

    // from pat::Tau
    float maximumHCALPFClusterEt() const
    { return object->maximumHCALPFClusterEt(); }

    // from reco::LeafCandidate
    math::XYZVector momentum() const { return object->momentum(); }

    // from reco::LeafCandidate
    reco::Candidate* mother(size_t x0) const
    { return (reco::Candidate*)object->mother(x0); }

    // from reco::LeafCandidate
    double mt() const { return object->mt(); }

    // from reco::LeafCandidate
    double mtSqr() const { return object->mtSqr(); }

    // from pat::Tau
    bool muonDecision() const { return object->muonDecision(); }

    // from pat::Lepton<reco::BaseTau>
    float neutralHadronIso() const { return object->neutralHadronIso(); }

    // from reco::LeafCandidate
    size_t numberOfDaughters() const { return object->numberOfDaughters(); }

    // from reco::LeafCandidate
    size_t numberOfMothers() const { return object->numberOfMothers(); }

    // from reco::LeafCandidate
    size_t numberOfSourceCandidatePtrs() const
    { return object->numberOfSourceCandidatePtrs(); }

    // from reco::RecoCandidate
    size_t numberOfTracks() const { return object->numberOfTracks(); }

    // from pat::PATObject<reco::BaseTau>
    reco::Candidate* originalObject() const
    { return (reco::Candidate*)object->originalObject(); }

    // from pat::PATObject<reco::BaseTau>
    const edm::Ptr<reco::Candidate> originalObjectRef() const
    { return object->originalObjectRef(); }

    // from reco::RecoCandidate
    /**
    bool overlap(reco::Candidate x0) const { return object->overlap(x0); }
    */

    // from pat::PATObject<reco::BaseTau>
    const std::vector<std::string> overlapLabels() const
    { return object->overlapLabels(); }

    // from pat::PATObject<reco::BaseTau>
    const edm::PtrVector<reco::Candidate> overlaps(std::string label) const
    { return object->overlaps(label); }

    // from reco::LeafCandidate
    double p() const { return object->p(); }

    // from reco::LeafCandidate
    const math::XYZTLorentzVector p4() const { return object->p4(); }

    // from pat::Tau
    const math::XYZTLorentzVector p4Jet() const { return object->p4Jet(); }

    // from pat::Lepton<reco::BaseTau>
    float particleIso() const { return object->particleIso(); }

    // from reco::LeafCandidate
    int pdgId() const { return object->pdgId(); }

    // from pat::Tau
    const reco::PFJetRef pfJetRef() const { return object->pfJetRef(); }

    // from pat::Tau
    const pat::tau::TauPFSpecific pfSpecific() const
    { return object->pfSpecific(); }

    // from reco::LeafCandidate
    double phi() const { return object->phi(); }

    // from pat::Tau
    float phiphiMoment() const { return object->phiphiMoment(); }

    // from pat::Lepton<reco::BaseTau>
    float photonIso() const { return object->photonIso(); }

    // from reco::LeafCandidate
    const math::PtEtaPhiMLorentzVector polarP4() const
    { return object->polarP4(); }

    // from pat::Tau
    const reco::VertexRef primaryVertex() const
    { return object->primaryVertex(); }

    // from pat::Tau
    const ROOT::Math::SMatrix<double,3,3,ROOT::Math::MatRepSym<double,3> >
    primaryVertexCov() const
    { return object->primaryVertexCov(); }

    // from pat::Tau
    const math::XYZPoint primaryVertexPos() const
    { return object->primaryVertexPos(); }

    // from reco::LeafCandidate
    double pt() const { return object->pt(); }

    // from pat::Lepton<reco::BaseTau>
    float puChargedHadronIso() const { return object->puChargedHadronIso(); }

    // from reco::LeafCandidate
    double px() const { return object->px(); }

    // from reco::LeafCandidate
    double py() const { return object->py(); }

    // from reco::LeafCandidate
    double pz() const { return object->pz(); }

    // from reco::LeafCandidate
    double rapidity() const { return object->rapidity(); }

    // from pat::PATObject<reco::BaseTau>
    double resolE(std::string label="") const { return object->resolE(label); }

    // from pat::PATObject<reco::BaseTau>
    double resolEt(std::string label="") const
    { return object->resolEt(label); }

    // from pat::PATObject<reco::BaseTau>
    double resolEta(std::string label="") const
    { return object->resolEta(label); }

    // from pat::PATObject<reco::BaseTau>
    double resolM(std::string label="") const { return object->resolM(label); }

    // from pat::PATObject<reco::BaseTau>
    double resolP(std::string label="") const { return object->resolP(label); }

    // from pat::PATObject<reco::BaseTau>
    double resolPhi(std::string label="") const
    { return object->resolPhi(label); }

    // from pat::PATObject<reco::BaseTau>
    double resolPInv(std::string label="") const
    { return object->resolPInv(label); }

    // from pat::PATObject<reco::BaseTau>
    double resolPt(std::string label="") const
    { return object->resolPt(label); }

    // from pat::PATObject<reco::BaseTau>
    double resolPx(std::string label="") const
    { return object->resolPx(label); }

    // from pat::PATObject<reco::BaseTau>
    double resolPy(std::string label="") const
    { return object->resolPy(label); }

    // from pat::PATObject<reco::BaseTau>
    double resolPz(std::string label="") const
    { return object->resolPz(label); }

    // from pat::PATObject<reco::BaseTau>
    double resolTheta(std::string label="") const
    { return object->resolTheta(label); }

    // from pat::Tau
    const reco::VertexRef secondaryVertex() const
    { return object->secondaryVertex(); }

    // from pat::Tau
    const ROOT::Math::SMatrix<double,3,3,ROOT::Math::MatRepSym<double,3> >
    secondaryVertexCov() const
    { return object->secondaryVertexCov(); }

    // from pat::Tau
    const math::XYZPoint secondaryVertexPos() const
    { return object->secondaryVertexPos(); }

    // from pat::Tau
    float segComp() const { return object->segComp(); }

    // from pat::Tau
    const std::vector<edm::Ptr<reco::PFCandidate> > signalPFCands() const
    { return object->signalPFCands(); }

    // from pat::Tau
    const std::vector<edm::Ptr<reco::PFCandidate> >
    signalPFChargedHadrCands() const
    { return object->signalPFChargedHadrCands(); }

    // from pat::Tau
    const std::vector<edm::Ptr<reco::PFCandidate> > signalPFGammaCands() const
    { return object->signalPFGammaCands(); }

    // from pat::Tau
    const std::vector<edm::Ptr<reco::PFCandidate> >
    signalPFNeutrHadrCands() const
    { return object->signalPFNeutrHadrCands(); }

    // from pat::Tau
    const std::vector<reco::RecoTauPiZero> signalPiZeroCandidates() const
    { return object->signalPiZeroCandidates(); }

    // from pat::Tau
    const std::vector<reco::PFRecoTauChargedHadron>
    signalTauChargedHadronCandidates() const
    { return object->signalTauChargedHadronCandidates(); }

    // from pat::Tau
    const reco::TrackRefVector signalTracks() const
    { return object->signalTracks(); }

    // from pat::Tau
    float signalTracksInvariantMass() const
    { return object->signalTracksInvariantMass(); }

    // from reco::LeafCandidate
    reco::CandidatePtr sourceCandidatePtr(size_t i) const
    { return object->sourceCandidatePtr(i); }

    // from reco::RecoCandidate
    reco::TrackRef standAloneMuon() const { return object->standAloneMuon(); }

    // from reco::LeafCandidate
    int status() const { return object->status(); }

    // from reco::RecoCandidate
    reco::SuperClusterRef superCluster() const
    { return object->superCluster(); }

    // from pat::Tau
    float tauID(char* name) const { return object->tauID(name); }

    // from pat::Tau
    float tauID(std::string name) const { return object->tauID(name); }

    // from pat::Tau
    const std::vector<std::pair<std::string,float> > tauIDs() const
    { return object->tauIDs(); }

    // from reco::LeafCandidate
    double theta() const { return object->theta(); }

    // from reco::LeafCandidate
    int threeCharge() const { return object->threeCharge(); }

    // from reco::RecoCandidate
    reco::TrackRef track() const { return object->track(); }

    // from reco::RecoCandidate
    reco::TrackRef track(size_t x0) const { return object->track(x0); }

    // from pat::Lepton<reco::BaseTau>
    float trackIso() const { return object->trackIso(); }

    // from pat::Lepton<reco::BaseTau>
    pat::IsoDeposit* trackIsoDeposit() const
    { return (pat::IsoDeposit*)object->trackIsoDeposit(); }

    // from pat::Tau
    float TracksInvariantMass() const { return object->TracksInvariantMass(); }

    // from pat::PATObject<reco::BaseTau>
    pat::TriggerObjectStandAlone* triggerObjectMatch(size_t idx=0) const
    { return (pat::TriggerObjectStandAlone*)object->triggerObjectMatch(idx); }

    // from pat::PATObject<reco::BaseTau>
    pat::TriggerObjectStandAlone*
    triggerObjectMatchByAlgorithm(char* nameAlgorithm, bool algoCondAccepted=true, size_t idx=0) const
    { return (pat::TriggerObjectStandAlone*)object->triggerObjectMatchByAlgorithm(nameAlgorithm, algoCondAccepted, idx); }

    // from pat::PATObject<reco::BaseTau>
    pat::TriggerObjectStandAlone*
    triggerObjectMatchByAlgorithm(char* nameAlgorithm, unsigned int algoCondAccepted, size_t idx=0) const
    { return (pat::TriggerObjectStandAlone*)object->triggerObjectMatchByAlgorithm(nameAlgorithm, algoCondAccepted, idx); }

    // from pat::PATObject<reco::BaseTau>
    pat::TriggerObjectStandAlone*
    triggerObjectMatchByAlgorithm(std::string nameAlgorithm, bool algoCondAccepted=true, size_t idx=0) const
    { return (pat::TriggerObjectStandAlone*)object->triggerObjectMatchByAlgorithm(nameAlgorithm, algoCondAccepted, idx); }

    // from pat::PATObject<reco::BaseTau>
    pat::TriggerObjectStandAlone*
    triggerObjectMatchByAlgorithm(std::string nameAlgorithm, unsigned int algoCondAccepted, size_t idx=0) const
    { return (pat::TriggerObjectStandAlone*)object->triggerObjectMatchByAlgorithm(nameAlgorithm, algoCondAccepted, idx); }

    // from pat::PATObject<reco::BaseTau>
    pat::TriggerObjectStandAlone*
    triggerObjectMatchByCollection(char* coll, size_t idx=0) const
    { return (pat::TriggerObjectStandAlone*)object->triggerObjectMatchByCollection(coll, idx); }

    // from pat::PATObject<reco::BaseTau>
    pat::TriggerObjectStandAlone*
    triggerObjectMatchByCollection(std::string coll, size_t idx=0) const
    { return (pat::TriggerObjectStandAlone*)object->triggerObjectMatchByCollection(coll, idx); }

    // from pat::PATObject<reco::BaseTau>
    pat::TriggerObjectStandAlone*
    triggerObjectMatchByCondition(char* nameCondition, size_t idx=0) const
    { return (pat::TriggerObjectStandAlone*)object->triggerObjectMatchByCondition(nameCondition, idx); }

    // from pat::PATObject<reco::BaseTau>
    pat::TriggerObjectStandAlone*
    triggerObjectMatchByCondition(std::string nameCondition, size_t idx=0) const
    { return (pat::TriggerObjectStandAlone*)object->triggerObjectMatchByCondition(nameCondition, idx); }

    // from pat::PATObject<reco::BaseTau>
    pat::TriggerObjectStandAlone*
    triggerObjectMatchByFilter(char* labelFilter, size_t idx=0) const
    { return (pat::TriggerObjectStandAlone*)object->triggerObjectMatchByFilter(labelFilter, idx); }

    // from pat::PATObject<reco::BaseTau>
    pat::TriggerObjectStandAlone*
    triggerObjectMatchByFilter(std::string labelFilter, size_t idx=0) const
    { return (pat::TriggerObjectStandAlone*)object->triggerObjectMatchByFilter(labelFilter, idx); }

    // from pat::PATObject<reco::BaseTau>
    pat::TriggerObjectStandAlone*
    triggerObjectMatchByFilterID(unsigned int triggerObjectType, size_t idx=0) const
    { return (pat::TriggerObjectStandAlone*)object->triggerObjectMatchByFilterID(triggerObjectType, idx); }

    // from pat::PATObject<reco::BaseTau>
    pat::TriggerObjectStandAlone*
    triggerObjectMatchByPath(char* namePath, bool pathLastFilterAccepted=false, bool pathL3FilterAccepted=true, size_t idx=0) const
    { return (pat::TriggerObjectStandAlone*)object->triggerObjectMatchByPath(namePath, pathLastFilterAccepted, pathL3FilterAccepted, idx); }

    // from pat::PATObject<reco::BaseTau>
    pat::TriggerObjectStandAlone*
    triggerObjectMatchByPath(char* namePath, unsigned int pathLastFilterAccepted, unsigned int pathL3FilterAccepted=1, size_t idx=0) const
    { return (pat::TriggerObjectStandAlone*)object->triggerObjectMatchByPath(namePath, pathLastFilterAccepted, pathL3FilterAccepted, idx); }

    // from pat::PATObject<reco::BaseTau>
    pat::TriggerObjectStandAlone*
    triggerObjectMatchByPath(std::string namePath, bool pathLastFilterAccepted=false, bool pathL3FilterAccepted=true, size_t idx=0) const
    { return (pat::TriggerObjectStandAlone*)object->triggerObjectMatchByPath(namePath, pathLastFilterAccepted, pathL3FilterAccepted, idx); }

    // from pat::PATObject<reco::BaseTau>
    pat::TriggerObjectStandAlone*
    triggerObjectMatchByPath(std::string namePath, unsigned int pathLastFilterAccepted, unsigned int pathL3FilterAccepted=1, size_t idx=0) const
    { return (pat::TriggerObjectStandAlone*)object->triggerObjectMatchByPath(namePath, pathLastFilterAccepted, pathL3FilterAccepted, idx); }

    // from pat::PATObject<reco::BaseTau>
    /**
    pat::TriggerObjectStandAlone*
    triggerObjectMatchByType(trigger::TriggerObjectType triggerObjectType, size_t idx=0) const
    { return (pat::TriggerObjectStandAlone*)object->triggerObjectMatchByType(triggerObjectType, idx); }
    */

    // from pat::PATObject<reco::BaseTau>
    pat::TriggerObjectStandAlone*
    triggerObjectMatchByType(unsigned int triggerObjectType, size_t idx=0) const
    { return (pat::TriggerObjectStandAlone*)object->triggerObjectMatchByType(triggerObjectType, idx); }

    // from pat::PATObject<reco::BaseTau>
    const std::vector<pat::TriggerObjectStandAlone>
    triggerObjectMatches() const
    { return object->triggerObjectMatches(); }

    // from pat::PATObject<reco::BaseTau>
    const std::vector<pat::TriggerObjectStandAlone>
    triggerObjectMatchesByAlgorithm(char* nameAlgorithm, bool algoCondAccepted=true) const
    { return object->triggerObjectMatchesByAlgorithm(nameAlgorithm, algoCondAccepted); }

    // from pat::PATObject<reco::BaseTau>
    const std::vector<pat::TriggerObjectStandAlone>
    triggerObjectMatchesByAlgorithm(char* nameAlgorithm, unsigned int algoCondAccepted) const
    { return object->triggerObjectMatchesByAlgorithm(nameAlgorithm, algoCondAccepted); }

    // from pat::PATObject<reco::BaseTau>
    const std::vector<pat::TriggerObjectStandAlone>
    triggerObjectMatchesByAlgorithm(std::string nameAlgorithm, bool algoCondAccepted=true) const
    { return object->triggerObjectMatchesByAlgorithm(nameAlgorithm, algoCondAccepted); }

    // from pat::PATObject<reco::BaseTau>
    const std::vector<pat::TriggerObjectStandAlone>
    triggerObjectMatchesByAlgorithm(std::string nameAlgorithm, unsigned int algoCondAccepted) const
    { return object->triggerObjectMatchesByAlgorithm(nameAlgorithm, algoCondAccepted); }

    // from pat::PATObject<reco::BaseTau>
    const std::vector<pat::TriggerObjectStandAlone>
    triggerObjectMatchesByCollection(char* coll) const
    { return object->triggerObjectMatchesByCollection(coll); }

    // from pat::PATObject<reco::BaseTau>
    const std::vector<pat::TriggerObjectStandAlone>
    triggerObjectMatchesByCollection(std::string coll) const
    { return object->triggerObjectMatchesByCollection(coll); }

    // from pat::PATObject<reco::BaseTau>
    const std::vector<pat::TriggerObjectStandAlone>
    triggerObjectMatchesByCondition(char* nameCondition) const
    { return object->triggerObjectMatchesByCondition(nameCondition); }

    // from pat::PATObject<reco::BaseTau>
    const std::vector<pat::TriggerObjectStandAlone>
    triggerObjectMatchesByCondition(std::string nameCondition) const
    { return object->triggerObjectMatchesByCondition(nameCondition); }

    // from pat::PATObject<reco::BaseTau>
    const std::vector<pat::TriggerObjectStandAlone>
    triggerObjectMatchesByFilter(char* labelFilter) const
    { return object->triggerObjectMatchesByFilter(labelFilter); }

    // from pat::PATObject<reco::BaseTau>
    const std::vector<pat::TriggerObjectStandAlone>
    triggerObjectMatchesByFilter(std::string labelFilter) const
    { return object->triggerObjectMatchesByFilter(labelFilter); }

    // from pat::PATObject<reco::BaseTau>
    const std::vector<pat::TriggerObjectStandAlone>
    triggerObjectMatchesByFilterID(unsigned int triggerObjectType) const
    { return object->triggerObjectMatchesByFilterID(triggerObjectType); }

    // from pat::PATObject<reco::BaseTau>
    const std::vector<pat::TriggerObjectStandAlone>
    triggerObjectMatchesByPath(char* namePath, bool pathLastFilterAccepted=false, bool pathL3FilterAccepted=true) const
    { return object->triggerObjectMatchesByPath(namePath, pathLastFilterAccepted, pathL3FilterAccepted); }

    // from pat::PATObject<reco::BaseTau>
    const std::vector<pat::TriggerObjectStandAlone>
    triggerObjectMatchesByPath(char* namePath, unsigned int pathLastFilterAccepted, unsigned int pathL3FilterAccepted=1) const
    { return object->triggerObjectMatchesByPath(namePath, pathLastFilterAccepted, pathL3FilterAccepted); }

    // from pat::PATObject<reco::BaseTau>
    const std::vector<pat::TriggerObjectStandAlone>
    triggerObjectMatchesByPath(std::string namePath, bool pathLastFilterAccepted=false, bool pathL3FilterAccepted=true) const
    { return object->triggerObjectMatchesByPath(namePath, pathLastFilterAccepted, pathL3FilterAccepted); }

    // from pat::PATObject<reco::BaseTau>
    const std::vector<pat::TriggerObjectStandAlone>
    triggerObjectMatchesByPath(std::string namePath, unsigned int pathLastFilterAccepted, unsigned int pathL3FilterAccepted=1) const
    { return object->triggerObjectMatchesByPath(namePath, pathLastFilterAccepted, pathL3FilterAccepted); }

    // from pat::PATObject<reco::BaseTau>
    /**
    const std::vector<pat::TriggerObjectStandAlone>
    triggerObjectMatchesByType(trigger::TriggerObjectType triggerObjectType) const
    { return object->triggerObjectMatchesByType(triggerObjectType); }
    */

    // from pat::PATObject<reco::BaseTau>
    const std::vector<pat::TriggerObjectStandAlone>
    triggerObjectMatchesByType(unsigned int triggerObjectType) const
    { return object->triggerObjectMatchesByType(triggerObjectType); }

    // from pat::PATObject<reco::BaseTau>
    edm::Ptr<reco::Candidate> userCand(std::string key) const
    { return object->userCand(key); }

    // from pat::PATObject<reco::BaseTau>
    const std::vector<std::string> userCandNames() const
    { return object->userCandNames(); }

    // from pat::PATObject<reco::BaseTau>
    const std::vector<std::string> userDataNames() const
    { return object->userDataNames(); }

    // from pat::PATObject<reco::BaseTau>
    const std::string userDataObjectType(std::string key) const
    { return object->userDataObjectType(key); }

    // from pat::PATObject<reco::BaseTau>
    float userFloat(char* key) const { return object->userFloat(key); }

    // from pat::PATObject<reco::BaseTau>
    float userFloat(std::string key) const { return object->userFloat(key); }

    // from pat::PATObject<reco::BaseTau>
    const std::vector<std::string> userFloatNames() const
    { return object->userFloatNames(); }

    // from pat::PATObject<reco::BaseTau>
    int userInt(std::string key) const { return object->userInt(key); }

    // from pat::PATObject<reco::BaseTau>
    const std::vector<std::string> userIntNames() const
    { return object->userIntNames(); }

    // from pat::Lepton<reco::BaseTau>
    /**
    float userIso(uint8_t index=0) const { return object->userIso(index); }
    */

    // from pat::Lepton<reco::BaseTau>
    /**
    pat::IsoDeposit* userIsoDeposit(uint8_t index=0) const
    { return (pat::IsoDeposit*)object->userIsoDeposit(index); }
    */

    // from pat::Lepton<reco::BaseTau>
    /**
    float userIsolation(pat::IsolationKeys key) const
    { return object->userIsolation(key); }
    */

    // from pat::Lepton<reco::BaseTau>
    float userIsolation(std::string key) const
    { return object->userIsolation(key); }

    // from reco::LeafCandidate
    const math::XYZPoint vertex() const { return object->vertex(); }

    // from reco::LeafCandidate
    double vertexChi2() const { return object->vertexChi2(); }

    // from reco::LeafCandidate
    ROOT::Math::SMatrix<double,3,3,ROOT::Math::MatRepSym<double,3> >
    vertexCovariance() const
    { return object->vertexCovariance(); }

    // from reco::LeafCandidate
    double vertexCovariance(int i, int j) const
    { return object->vertexCovariance(i, j); }

    // from reco::LeafCandidate
    double vertexNdof() const { return object->vertexNdof(); }

    // from reco::LeafCandidate
    double vertexNormalizedChi2() const
    { return object->vertexNormalizedChi2(); }

    // from reco::LeafCandidate
    double vx() const { return object->vx(); }

    // from reco::LeafCandidate
    double vy() const { return object->vy(); }

    // from reco::LeafCandidate
    double vz() const { return object->vz(); }

    // from reco::LeafCandidate
    double y() const { return object->y(); }
  };
}
#endif
