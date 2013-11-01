// ----------------------------------------------------------------------------
// Created: Wed Oct 30 15:31:24 2013 by mkhelper.py
// Author:  Lukas Vanelderen      
// ----------------------------------------------------------------------------
#include "PhysicsTools/TheNtupleMaker/interface/UserBuffer.h"
#include "PhysicsTools/TheNtupleMaker/interface/pluginfactory.h"
#include "ntuples/VBF-LS-tau-ntupler/interface/recoGenParticleHelperPlus.h"
typedef UserBuffer<reco::GenParticle, reco::GenParticleHelperPlus, COLLECTION>
recoGenParticleHelperPlus_t;
DEFINE_EDM_PLUGIN(BufferFactory, recoGenParticleHelperPlus_t,
                  "recoGenParticleHelperPlus");
