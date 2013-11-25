//-----------------------------------------------------------------------------
// Subsystem:   ntuples
// Package:     VBF-LS-tau-ntupler
// Description: TheNtupleMaker helper class for pat::Electron
// Created:     Mon Nov 18 14:24:41 2013
// Author:      Daniele Marconi      
//-----------------------------------------------------------------------------
#include "ntuples/VBF-LS-tau-ntupler/interface/patElectronHelper.h"
#include "FWCore/Framework/interface/Event.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "HLTrigger/HLTcore/interface/HLTConfigProvider.h"
//-----------------------------------------------------------------------------
using namespace std;
using namespace pat;
//-----------------------------------------------------------------------------
// This constructor is called once per job
ElectronHelper::ElectronHelper()
  : HelperFor<pat::Electron>() {}
    
ElectronHelper::~ElectronHelper() {}

// -- Called once per event
//void ElectronHelper::analyzeEvent()
//{
//
//}

// -- Called once per object
//void ElectronHelper::analyzeObject()
//{
//
//}

// -- User access methods
//double ElectronHelper::someMethod()  const
//{
//  return  //-- some-value --
//}
