// ----------------------------------------------------------------------------
// Created: Mon Nov 18 14:24:41 2013 by mkhelper.py
// Author:  Daniele Marconi      
// ----------------------------------------------------------------------------
#include "PhysicsTools/TheNtupleMaker/interface/UserBuffer.h"
#include "PhysicsTools/TheNtupleMaker/interface/pluginfactory.h"
#include "ntuples/VBF-LS-tau-ntupler/interface/patElectronHelper.h"
typedef UserBuffer<pat::Electron, pat::ElectronHelper, COLLECTION>
patElectronHelper_t;
DEFINE_EDM_PLUGIN(BufferFactory, patElectronHelper_t,
                  "patElectronHelper");
