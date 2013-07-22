//-----------------------------------------------------------------------------
// Subsystem:   VBFntupleProducer
// Package:     VBFntupleProducer
// Description: TheNtupleMaker helper class for pat::Electron
// Created:     Fri Apr  5 14:39:07 2013
// Author:      Daniele Marconi      
//-----------------------------------------------------------------------------
#include "VBFntupleProducer/VBFntupleProducer/interface/patElectronHelper.h"
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
