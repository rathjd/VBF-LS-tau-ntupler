//-----------------------------------------------------------------------------
// Subsystem:   ntuples
// Package:     VBF-LS-tau-ntupler
// Description: TheNtupleMaker helper class for reco::PFTau
// Created:     Mon Jun  8 16:54:45 2015
// Author:      Daniele Marconi      
//-----------------------------------------------------------------------------
#include "ntuples/VBF-LS-tau-ntupler/interface/recoPFTauHelper.h"
#include "FWCore/Framework/interface/Event.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "HLTrigger/HLTcore/interface/HLTConfigProvider.h"
//-----------------------------------------------------------------------------
using namespace std;
using namespace reco;
//-----------------------------------------------------------------------------
// This constructor is called once per job
PFTauHelper::PFTauHelper()
  : HelperFor<reco::PFTau>() {}
    
PFTauHelper::~PFTauHelper() {}

// -- Called once per event
//void PFTauHelper::analyzeEvent()
//{
//
//}

// -- Called once per object
//void PFTauHelper::analyzeObject()
//{
//
//}

// -- User access methods
//double PFTauHelper::someMethod()  const
//{
//  return  //-- some-value --
//}
