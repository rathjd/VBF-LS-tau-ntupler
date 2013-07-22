// ----------------------------------------------------------------------------
// Created: Fri Apr  5 14:39:07 2013 by mkhelper.py
// Author:  Daniele Marconi      
// ----------------------------------------------------------------------------
#include "PhysicsTools/TheNtupleMaker/interface/UserBuffer.h"
#include "PhysicsTools/TheNtupleMaker/interface/pluginfactory.h"
#include "VBFntupleProducer/VBFntupleProducer/interface/patElectronHelper.h"
typedef UserBuffer<pat::Electron, pat::ElectronHelper, COLLECTION>
patElectronHelper_t;
DEFINE_EDM_PLUGIN(BufferFactory, patElectronHelper_t,
                  "patElectronHelper");
