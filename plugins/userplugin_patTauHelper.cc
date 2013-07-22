// ----------------------------------------------------------------------------
// Created: Thu May 30 14:21:40 2013 by mkhelper.py
// Author:  Lukas Vanelderen      
// ----------------------------------------------------------------------------
#include "PhysicsTools/TheNtupleMaker/interface/UserBuffer.h"
#include "PhysicsTools/TheNtupleMaker/interface/pluginfactory.h"
#include "VBFntupleProducer/VBFntupleProducer/interface/patTauHelper.h"
typedef UserBuffer<pat::Tau, pat::TauHelper, COLLECTION>
patTauHelper_t;
DEFINE_EDM_PLUGIN(BufferFactory, patTauHelper_t,
                  "patTauHelper");
