//-----------------------------------------------------------------------------
// Subsystem:   ntuples
// Package:     VBF-LS-tau-ntupler
// Description: TheNtupleMaker helper class for edm::Event
// Created:     Wed Oct 29 08:09:46 2014
// Author:      Shakepeare's ghost      
//-----------------------------------------------------------------------------
#include "ntuples/VBF-LS-tau-ntupler/interface/edmEventHelperExtra.h"
#include "FWCore/Framework/interface/Event.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "HLTrigger/HLTcore/interface/HLTConfigProvider.h"
#include "TROOT.h"
#include "TTree.h"
#include "TFile.h"
//-----------------------------------------------------------------------------
using namespace std;
using namespace edm;
//-----------------------------------------------------------------------------
// This constructor is called once per job
EventHelperExtra::EventHelperExtra()
  : HelperFor<edm::Event>() {
	  string ntupleName = config->getUntrackedParameter<string>("ntupleName");
	  TFile * f = gROOT->GetFile(ntupleName.c_str());
	  TTree * t = (TTree*)f->Get("Events");
	  string branchName;
	  branchName = "doubles_pdfWeights_cteq66_PATuple";
	  t->Branch(branchName.c_str(),&pdfWeights);
}
    
EventHelperExtra::~EventHelperExtra() {}

// -- Called once per event
void EventHelperExtra::analyzeEvent()
{
	pdfWeights.clear();
	edm::Handle<vector<double> > _pdfWeights;
	event->getByLabel(edm::InputTag("pdfWeights","cteq66"),_pdfWeights);
	pdfWeights.insert(pdfWeights.begin(),_pdfWeights->begin(),_pdfWeights->end());
}

// -- Called once per object
//void EventHelperExtra::analyzeObject()
//{
//
//}

// -- User access methods
//double EventHelperExtra::someMethod()  const
//{
//  return  //-- some-value --
//}
