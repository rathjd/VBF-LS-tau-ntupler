#ifndef EDMEVENTHELPEREXTRA_H
#define EDMEVENTHELPEREXTRA_H
//-----------------------------------------------------------------------------
// Subsystem:   ntuples
// Package:     VBF-LS-tau-ntupler
// Description: TheNtupleMaker helper class for edm::Event
// Created:     Wed Oct 29 08:09:46 2014
// Author:      Shakepeare's ghost      
//-----------------------------------------------------------------------------
#include <algorithm>
#include <iostream>
#include <vector>
#include <map>
#include "PhysicsTools/TheNtupleMaker/interface/HelperFor.h"
#include "FWCore/Framework/interface/Event.h"
//-----------------------------------------------------------------------------
// Definitions:
//   helper:        object of class EventHelperExtra
//   helped object: object of class edm::Event
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

namespace edm
{
  /// A helper class for edm::Event.
  class EventHelperExtra : public HelperFor<edm::Event>
  {
  public:
	///
	EventHelperExtra();

	virtual ~EventHelperExtra();

	// Uncomment if this class does some event-level analysis
	 virtual void analyzeEvent();
	 
	// Uncomment if this class does some object-level analysis
	// virtual void analyzeObject();

	// ---------------------------------------------------------
	// -- User access methods go here
	// ---------------------------------------------------------

	
  private:
    // -- User internals

	std::vector<double> pdfWeights;

  public:
    // ---------------------------------------------------------
    // -- Access Methods
    // ---------------------------------------------------------

	// WARNING: some methods may fail to compile because of coding
	//          problems in one of the CMSSW base classes. If so,
	//          just comment out the offending method and try again.
  

  };
}
#endif