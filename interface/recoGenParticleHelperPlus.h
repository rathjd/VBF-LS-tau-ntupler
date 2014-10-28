#ifndef RECOGENPARTICLEHELPERPLUS_H
#define RECOGENPARTICLEHELPERPLUS_H
//-----------------------------------------------------------------------------
// Subsystem:   ntuples
// Package:     VBF-LS-tau-ntupler
// Description: TheNtupleMaker helper class for reco::GenParticle
// Created:     Mon Nov 18 14:27:14 2013
// Author:      Daniele Marconi      
//-----------------------------------------------------------------------------
#include <algorithm>
#include <iostream>
#include <vector>
#include <map>
#include "PhysicsTools/TheNtupleMaker/interface/HelperFor.h"
#include "DataFormats/HepMCCandidate/interface/GenParticle.h"
//-----------------------------------------------------------------------------
// Definitions:
//   helper:        object of class GenParticleHelperPlus
//   helped object: object of class reco::GenParticle
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
  /// A helper class for reco::GenParticle.
  class GenParticleHelperPlus : public HelperFor<reco::GenParticle>
  {
  public:
	///
	GenParticleHelperPlus();

	virtual ~GenParticleHelperPlus();

	///
	virtual void analyzeEvent();
	///
	virtual void analyzeObject();
	///
	int charge() const;
	///
	int pdgId() const;
	///
	int status() const;
	///
	double energy() const;
	///
	double pt() const;
	///
	double eta() const;
	///
	double phi() const;
	///
	double mass() const;
	///
	int firstMother() const;
	///
	int lastMother() const;
	///
	int firstDaughter() const;
	///
	int lastDaughter() const;
	
  private:
    // -- User internals
    
    std::vector<double> pdfWeights; 

    // Filled once per cached object
    std::vector<int> mothers_;
    std::vector<int> daughters_;

    // Filled once per event
    std::map<std::string, int> amap;

  public:
    // ---------------------------------------------------------
    // -- Access Methods
    // ---------------------------------------------------------

	// WARNING: some methods may fail to compile because of coding
	//          problems in one of the CMSSW base classes. If so,
	//          just comment out the offending method and try again.
  


    // from reco::LeafCandidate
    math::XYZVector boostToCM() const { return object->boostToCM(); }

    // from reco::GenParticle
    int collisionId() const { return object->collisionId(); }

    // from reco::CompositeRefCandidateT<edm::RefVector<std::vector<reco::GenParticle>,reco::GenParticle,edm::refhelper::FindUsingAdvance<std::vector<reco::GenParticle>,reco::GenParticle> > >
    reco::Candidate* daughter(size_t i) const
    { return (reco::Candidate*)object->daughter(i); }

    // from reco::CompositeRefCandidateT<edm::RefVector<std::vector<reco::GenParticle>,reco::GenParticle,edm::refhelper::FindUsingAdvance<std::vector<reco::GenParticle>,reco::GenParticle> > >
    reco::GenParticleRef daughterRef(size_t i) const
    { return object->daughterRef(i); }

    // from reco::CompositeRefCandidateT<edm::RefVector<std::vector<reco::GenParticle>,reco::GenParticle,edm::refhelper::FindUsingAdvance<std::vector<reco::GenParticle>,reco::GenParticle> > >
    const edm::RefVector<std::vector<reco::GenParticle>,reco::GenParticle,edm::refhelper::FindUsingAdvance<std::vector<reco::GenParticle>,reco::GenParticle> >
    daughterRefVector() const
    { return object->daughterRefVector(); }

    // from reco::LeafCandidate
    double et() const { return object->et(); }

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

    // from reco::LeafCandidate
    bool isPhoton() const { return object->isPhoton(); }

    // from reco::LeafCandidate
    bool isStandAloneMuon() const { return object->isStandAloneMuon(); }

    // from reco::LeafCandidate
    bool isTrackerMuon() const { return object->isTrackerMuon(); }

    // from reco::LeafCandidate
    bool longLived() const { return object->longLived(); }

    // from reco::LeafCandidate
    bool massConstraint() const { return object->massConstraint(); }

    // from reco::LeafCandidate
    double massSqr() const { return object->massSqr(); }

    // from reco::LeafCandidate
    math::XYZVector momentum() const { return object->momentum(); }

    // from reco::CompositeRefCandidateT<edm::RefVector<std::vector<reco::GenParticle>,reco::GenParticle,edm::refhelper::FindUsingAdvance<std::vector<reco::GenParticle>,reco::GenParticle> > >
    reco::Candidate* mother(size_t i=0) const
    { return (reco::Candidate*)object->mother(i); }

    // from reco::CompositeRefCandidateT<edm::RefVector<std::vector<reco::GenParticle>,reco::GenParticle,edm::refhelper::FindUsingAdvance<std::vector<reco::GenParticle>,reco::GenParticle> > >
    reco::GenParticleRef motherRef(size_t i=0) const
    { return object->motherRef(i); }

    // from reco::CompositeRefCandidateT<edm::RefVector<std::vector<reco::GenParticle>,reco::GenParticle,edm::refhelper::FindUsingAdvance<std::vector<reco::GenParticle>,reco::GenParticle> > >
    const edm::RefVector<std::vector<reco::GenParticle>,reco::GenParticle,edm::refhelper::FindUsingAdvance<std::vector<reco::GenParticle>,reco::GenParticle> >
    motherRefVector() const
    { return object->motherRefVector(); }

    // from reco::LeafCandidate
    double mt() const { return object->mt(); }

    // from reco::LeafCandidate
    double mtSqr() const { return object->mtSqr(); }

    // from reco::CompositeRefCandidateT<edm::RefVector<std::vector<reco::GenParticle>,reco::GenParticle,edm::refhelper::FindUsingAdvance<std::vector<reco::GenParticle>,reco::GenParticle> > >
    size_t numberOfDaughters() const { return object->numberOfDaughters(); }

    // from reco::CompositeRefCandidateT<edm::RefVector<std::vector<reco::GenParticle>,reco::GenParticle,edm::refhelper::FindUsingAdvance<std::vector<reco::GenParticle>,reco::GenParticle> > >
    size_t numberOfMothers() const { return object->numberOfMothers(); }

    // from reco::LeafCandidate
    size_t numberOfSourceCandidatePtrs() const
    { return object->numberOfSourceCandidatePtrs(); }

    // from reco::LeafCandidate
    double p() const { return object->p(); }

    // from reco::LeafCandidate
    const math::XYZTLorentzVector p4() const { return object->p4(); }

    // from reco::LeafCandidate
    const math::PtEtaPhiMLorentzVector polarP4() const
    { return object->polarP4(); }

    // from reco::LeafCandidate
    double px() const { return object->px(); }

    // from reco::LeafCandidate
    double py() const { return object->py(); }

    // from reco::LeafCandidate
    double pz() const { return object->pz(); }

    // from reco::LeafCandidate
    double rapidity() const { return object->rapidity(); }

    // from reco::LeafCandidate
    reco::CandidatePtr sourceCandidatePtr(size_t i) const
    { return object->sourceCandidatePtr(i); }

    // from reco::LeafCandidate
    double theta() const { return object->theta(); }

    // from reco::LeafCandidate
    int threeCharge() const { return object->threeCharge(); }

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
