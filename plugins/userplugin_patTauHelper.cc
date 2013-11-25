// ----------------------------------------------------------------------------
// Created: Mon Nov 18 14:23:58 2013 by mkhelper.py
// Author:  Daniele Marconi      
// ----------------------------------------------------------------------------
#include "PhysicsTools/TheNtupleMaker/interface/UserBuffer.h"
#include "PhysicsTools/TheNtupleMaker/interface/pluginfactory.h"
#include "ntuples/VBF-LS-tau-ntupler/interface/patTauHelper.h"
typedef UserBuffer<pat::Tau, pat::TauHelper, COLLECTION>
patTauHelper_t;
DEFINE_EDM_PLUGIN(BufferFactory, patTauHelper_t,
                  "patTauHelper");
