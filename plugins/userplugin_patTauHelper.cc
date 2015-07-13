// ----------------------------------------------------------------------------
// Created: Mon Jun  8 16:57:57 2015 by mkhelper.py
// Author:  Daniele Marconi      
// ----------------------------------------------------------------------------
#include "PhysicsTools/TheNtupleMaker/interface/UserBuffer.h"
#include "PhysicsTools/TheNtupleMaker/interface/pluginfactory.h"
#include "ntuples/VBF-LS-tau-ntupler/interface/patTauHelper.h"
typedef UserBuffer<pat::Tau, pat::TauHelper, COLLECTION>
patTauHelper_t;
DEFINE_EDM_PLUGIN(BufferFactory, patTauHelper_t,
                  "patTauHelper");
