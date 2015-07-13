// ----------------------------------------------------------------------------
// Created: Mon Jun  8 16:54:45 2015 by mkhelper.py
// Author:  Daniele Marconi      
// ----------------------------------------------------------------------------
#include "PhysicsTools/TheNtupleMaker/interface/UserBuffer.h"
#include "PhysicsTools/TheNtupleMaker/interface/pluginfactory.h"
#include "ntuples/VBF-LS-tau-ntupler/interface/recoPFTauHelper.h"
typedef UserBuffer<reco::PFTau, reco::PFTauHelper, COLLECTION>
recoPFTauHelper_t;
DEFINE_EDM_PLUGIN(BufferFactory, recoPFTauHelper_t,
                  "recoPFTauHelper");
