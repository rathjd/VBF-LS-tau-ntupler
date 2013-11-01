//
//--------------------------------------------------------------------
#include "VBFntupleProducer/VBFntupleProducer/interface/patElectronHelper.h"
#include "VBFntupleProducer/VBFntupleProducer/interface/patTauHelper.h"
#include "ntuples/VBF-LS-tau-ntupler/interface/recoGenParticleHelperPlus.h"


namespace
{
  HelperFor<pat::Electron> t_patElectronHelper;
  HelperFor<pat::Tau> t_patTauHelper;
  HelperFor<reco::GenParticle> t_recoGenParticleHelperPlus;
}
