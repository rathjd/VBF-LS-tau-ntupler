#ifndef RECOPFTAUHELPER_H
#define RECOPFTAUHELPER_H
//-----------------------------------------------------------------------------
// Subsystem:   ntuples
// Package:     VBF-LS-tau-ntupler
// Description: TheNtupleMaker helper class for reco::PFTau
// Created:     Mon Jun  8 16:54:45 2015
// Author:      Daniele Marconi      
//-----------------------------------------------------------------------------
#include <algorithm>
#include <iostream>
#include <vector>
#include <map>
#include "PhysicsTools/TheNtupleMaker/interface/HelperFor.h"
#include "DataFormats/TauReco/interface/PFTau.h"
//-----------------------------------------------------------------------------
// Definitions:
//   helper:        object of class PFTauHelper
//   helped object: object of class reco::PFTau
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

namespace reco
{
  /// A helper class for reco::PFTau.
  class PFTauHelper : public HelperFor<reco::PFTau>
  {
  public:
    ///
    PFTauHelper();

    virtual ~PFTauHelper();

    // Uncomment if this class does some event-level analysis
    // virtual void analyzeEvent();
	 
    // Uncomment if this class does some object-level analysis
    // virtual void analyzeObject();

    // ---------------------------------------------------------
    // -- User access methods go here
    // ---------------------------------------------------------
	
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

    // from reco::PFTau
    float bremsRecoveryEOverPLead() const
    { return object->bremsRecoveryEOverPLead(); }

    // from reco::PFTau
    reco::PFTau::hadronicDecayMode calculateDecayMode() const
    { return object->calculateDecayMode(); }

    // from reco::PFTau
    float caloComp() const { return object->caloComp(); }

    // from reco::RecoCandidate
    CaloTowerRef caloTower() const { return object->caloTower(); }

    // from reco::LeafCandidate
    int charge() const { return object->charge(); }

    // from reco::RecoCandidate
    reco::TrackRef combinedMuon() const { return object->combinedMuon(); }

    // from reco::LeafCandidate
    reco::Candidate* daughter(size_t x0) const
    { return (reco::Candidate*)object->daughter(x0); }

    // from reco::LeafCandidate
    reco::Candidate* daughter(std::string s) const
    { return (reco::Candidate*)object->daughter(s); }

    // from reco::PFTau
    reco::PFTau::hadronicDecayMode decayMode() const
    { return object->decayMode(); }

    // from reco::LeafCandidate
    /**
    double dmass(GlobalVector v, double e) const
    { return object->dmass(v, e); }
    */

    // from reco::PFTau
    float ecalStripSumEOverPLead() const
    { return object->ecalStripSumEOverPLead(); }

    // from reco::PFTau
    bool electronPreIDDecision() const
    { return object->electronPreIDDecision(); }

    // from reco::PFTau
    float electronPreIDOutput() const { return object->electronPreIDOutput(); }

    // from reco::PFTau
    reco::TrackRef electronPreIDTrack() const
    { return object->electronPreIDTrack(); }

    // from reco::PFTau
    float emFraction() const { return object->emFraction(); }

    // from reco::LeafCandidate
    double energy() const { return object->energy(); }

    // from reco::LeafCandidate
    double et() const { return object->et(); }

    // from reco::LeafCandidate
    float eta() const { return object->eta(); }

    // from reco::RecoCandidate
    reco::GsfTrackRef gsfTrack() const { return object->gsfTrack(); }

    // from reco::PFTau
    bool hasMuonReference() const { return object->hasMuonReference(); }

    // from reco::PFTau
    float hcal3x3OverPLead() const { return object->hcal3x3OverPLead(); }

    // from reco::PFTau
    float hcalMaxOverPLead() const { return object->hcalMaxOverPLead(); }

    // from reco::PFTau
    float hcalTotOverPLead() const { return object->hcalTotOverPLead(); }

    // from reco::LeafCandidate
    bool isCaloMuon() const { return object->isCaloMuon(); }

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

    // from reco::PFTau
    const std::vector<edm::Ptr<reco::PFCandidate> > isolationPFCands() const
    { return object->isolationPFCands(); }

    // from reco::PFTau
    const std::vector<edm::Ptr<reco::PFCandidate> >
    isolationPFChargedHadrCands() const
    { return object->isolationPFChargedHadrCands(); }

    // from reco::PFTau
    float isolationPFChargedHadrCandsPtSum() const
    { return object->isolationPFChargedHadrCandsPtSum(); }

    // from reco::PFTau
    const std::vector<edm::Ptr<reco::PFCandidate> >
    isolationPFGammaCands() const
    { return object->isolationPFGammaCands(); }

    // from reco::PFTau
    float isolationPFGammaCandsEtSum() const
    { return object->isolationPFGammaCandsEtSum(); }

    // from reco::PFTau
    const std::vector<edm::Ptr<reco::PFCandidate> >
    isolationPFNeutrHadrCands() const
    { return object->isolationPFNeutrHadrCands(); }

    // from reco::PFTau
    const std::vector<reco::RecoTauPiZero> isolationPiZeroCandidates() const
    { return object->isolationPiZeroCandidates(); }

    // from reco::PFTau
    const std::vector<reco::PFRecoTauChargedHadron>
    isolationTauChargedHadronCandidates() const
    { return object->isolationTauChargedHadronCandidates(); }

    // from reco::BaseTau
    const reco::TrackRefVector isolationTracks() const
    { return object->isolationTracks(); }

    // from reco::LeafCandidate
    bool isPhoton() const { return object->isPhoton(); }

    // from reco::LeafCandidate
    bool isStandAloneMuon() const { return object->isStandAloneMuon(); }

    // from reco::LeafCandidate
    bool isTrackerMuon() const { return object->isTrackerMuon(); }

    // from reco::PFTau
    const reco::PFJetRef jetRef() const { return object->jetRef(); }

    // from reco::PFTau
    const reco::PFCandidatePtr leadPFCand() const
    { return object->leadPFCand(); }

    // from reco::PFTau
    const reco::PFCandidatePtr leadPFChargedHadrCand() const
    { return object->leadPFChargedHadrCand(); }

    // from reco::PFTau
    float leadPFChargedHadrCandsignedSipt() const
    { return object->leadPFChargedHadrCandsignedSipt(); }

    // from reco::PFTau
    const reco::PFCandidatePtr leadPFNeutralCand() const
    { return object->leadPFNeutralCand(); }

    // from reco::PFTau
    reco::PFRecoTauChargedHadronRef leadTauChargedHadronCandidate() const
    { return object->leadTauChargedHadronCandidate(); }

    // from reco::BaseTau
    reco::TrackRef leadTrack() const { return object->leadTrack(); }

    // from reco::LeafCandidate
    bool longLived() const { return object->longLived(); }

    // from reco::LeafCandidate
    /**
    double magd(GlobalVector v) const { return object->magd(v); }
    */

    // from reco::LeafCandidate
    float mass() const { return object->mass(); }

    // from reco::LeafCandidate
    bool massConstraint() const { return object->massConstraint(); }

    // from reco::LeafCandidate
    float massSqr() const { return object->massSqr(); }

    // from reco::PFTau
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

    // from reco::PFTau
    bool muonDecision() const { return object->muonDecision(); }

    // from reco::LeafCandidate
    size_t numberOfDaughters() const { return object->numberOfDaughters(); }

    // from reco::LeafCandidate
    size_t numberOfMothers() const { return object->numberOfMothers(); }

    // from reco::PFTau
    size_t numberOfSourceCandidatePtrs() const
    { return object->numberOfSourceCandidatePtrs(); }

    // from reco::RecoCandidate
    size_t numberOfTracks() const { return object->numberOfTracks(); }

    // from reco::RecoCandidate
    /**
    bool overlap(reco::Candidate x0) const { return object->overlap(x0); }
    */

    // from reco::LeafCandidate
    double p() const { return object->p(); }

    // from reco::LeafCandidate
    const math::XYZTLorentzVector p4() const { return object->p4(); }

    // from reco::LeafCandidate
    int pdgId() const { return object->pdgId(); }

    // from reco::PFTau
    const reco::PFTauTagInfoRef pfTauTagInfoRef() const
    { return object->pfTauTagInfoRef(); }

    // from reco::LeafCandidate
    float phi() const { return object->phi(); }

    // from reco::LeafCandidate
    const math::PtEtaPhiMLorentzVector polarP4() const
    { return object->polarP4(); }

    // from reco::LeafCandidate
    float pt() const { return object->pt(); }

    // from reco::LeafCandidate
    double px() const { return object->px(); }

    // from reco::LeafCandidate
    double py() const { return object->py(); }

    // from reco::LeafCandidate
    double pz() const { return object->pz(); }

    // from reco::LeafCandidate
    double rapidity() const { return object->rapidity(); }

    // from reco::PFTau
    float segComp() const { return object->segComp(); }

    // from reco::PFTau
    const std::vector<edm::Ptr<reco::PFCandidate> > signalPFCands() const
    { return object->signalPFCands(); }

    // from reco::PFTau
    const std::vector<edm::Ptr<reco::PFCandidate> >
    signalPFChargedHadrCands() const
    { return object->signalPFChargedHadrCands(); }

    // from reco::PFTau
    const std::vector<edm::Ptr<reco::PFCandidate> > signalPFGammaCands() const
    { return object->signalPFGammaCands(); }

    // from reco::PFTau
    const std::vector<edm::Ptr<reco::PFCandidate> >
    signalPFNeutrHadrCands() const
    { return object->signalPFNeutrHadrCands(); }

    // from reco::PFTau
    const std::vector<reco::RecoTauPiZero> signalPiZeroCandidates() const
    { return object->signalPiZeroCandidates(); }

    // from reco::PFTau
    const std::vector<reco::PFRecoTauChargedHadron>
    signalTauChargedHadronCandidates() const
    { return object->signalTauChargedHadronCandidates(); }

    // from reco::BaseTau
    const reco::TrackRefVector signalTracks() const
    { return object->signalTracks(); }

    // from reco::PFTau
    reco::CandidatePtr sourceCandidatePtr(size_t i) const
    { return object->sourceCandidatePtr(i); }

    // from reco::RecoCandidate
    reco::TrackRef standAloneMuon() const { return object->standAloneMuon(); }

    // from reco::LeafCandidate
    int status() const { return object->status(); }

    // from reco::RecoCandidate
    reco::SuperClusterRef superCluster() const
    { return object->superCluster(); }

    // from reco::LeafCandidate
    double theta() const { return object->theta(); }

    // from reco::LeafCandidate
    int threeCharge() const { return object->threeCharge(); }

    // from reco::RecoCandidate
    reco::TrackRef track() const { return object->track(); }

    // from reco::RecoCandidate
    reco::TrackRef track(size_t x0) const { return object->track(x0); }

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
