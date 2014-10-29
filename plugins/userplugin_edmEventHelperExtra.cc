// ----------------------------------------------------------------------------
// Created: Wed Oct 29 08:09:46 2014 by mkhelper.py
// Author:  Shakepeare's ghost      
// ----------------------------------------------------------------------------
#include "PhysicsTools/TheNtupleMaker/interface/UserBuffer.h"
#include "PhysicsTools/TheNtupleMaker/interface/pluginfactory.h"
#include "ntuples/VBF-LS-tau-ntupler/interface/edmEventHelperExtra.h"
typedef UserBuffer<edm::Event, edm::EventHelperExtra, SINGLETON>
edmEventHelperExtra_t;
DEFINE_EDM_PLUGIN(BufferFactory, edmEventHelperExtra_t,
                  "edmEventHelperExtra");
