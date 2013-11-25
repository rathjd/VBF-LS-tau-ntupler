//-----------------------------------------------------------------------------
// Subsystem:   ntuples
// Package:     VBF-LS-tau-ntupler
// Description: TheNtupleMaker helper class for pat::Tau
// Created:     Mon Nov 18 14:23:58 2013
// Author:      Daniele Marconi      
//-----------------------------------------------------------------------------
#include "ntuples/VBF-LS-tau-ntupler/interface/patTauHelper.h"
#include "FWCore/Framework/interface/Event.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "HLTrigger/HLTcore/interface/HLTConfigProvider.h"
//-----------------------------------------------------------------------------
using namespace std;
using namespace pat;
//-----------------------------------------------------------------------------
// This constructor is called once per job
TauHelper::TauHelper()
  : HelperFor<pat::Tau>() {}
    
TauHelper::~TauHelper() {}

// -- Called once per event
//void TauHelper::analyzeEvent()
//{
//
//}

// -- Called once per object
//void TauHelper::analyzeObject()
//{
//
//}

// -- User access methods
//double TauHelper::someMethod()  const
//{
//  return  //-- some-value --
//}
