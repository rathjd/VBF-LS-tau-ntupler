// ----------------------------------------------------------------------------
// Created: Mon Jun  8 15:27:21 2015 by mkhelper.py
// Author:  Daniele Marconi      
// ----------------------------------------------------------------------------
#include "PhysicsTools/TheNtupleMaker/interface/UserBuffer.h"
#include "PhysicsTools/TheNtupleMaker/interface/pluginfactory.h"
#include "ntuples/VBF-LS-tau-ntupler/interface/recoGenParticleHelper2.h"
typedef UserBuffer<reco::GenParticle, reco::GenParticleHelper2, COLLECTION>
recoGenParticleHelper2_t;
DEFINE_EDM_PLUGIN(BufferFactory, recoGenParticleHelper2_t,
                  "recoGenParticleHelper2");
