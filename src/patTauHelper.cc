//-----------------------------------------------------------------------------
// Subsystem:   VBFntupleProducer
// Package:     VBFntupleProducer
// Description: TheNtupleMaker helper class for pat::Tau
// Created:     Thu May 30 14:21:40 2013
// Author:      Lukas Vanelderen      
//-----------------------------------------------------------------------------
#include "VBFntupleProducer/VBFntupleProducer/interface/patTauHelper.h"
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
