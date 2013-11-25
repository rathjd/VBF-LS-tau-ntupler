// ----------------------------------------------------------------------------
// Created: Mon Nov 18 14:27:14 2013 by mkhelper.py
// Author:  Daniele Marconi      
// ----------------------------------------------------------------------------
#include "PhysicsTools/TheNtupleMaker/interface/UserBuffer.h"
#include "PhysicsTools/TheNtupleMaker/interface/pluginfactory.h"
#include "ntuples/VBF-LS-tau-ntupler/interface/recoGenParticleHelperPlus.h"
typedef UserBuffer<reco::GenParticle, reco::GenParticleHelperPlus, COLLECTION>
recoGenParticleHelperPlus_t;
DEFINE_EDM_PLUGIN(BufferFactory, recoGenParticleHelperPlus_t,
                  "recoGenParticleHelperPlus");
