//
//--------------------------------------------------------------------
#include "ntuples/VBF-LS-tau-ntupler/interface/patTauHelper.h"
#include "ntuples/VBF-LS-tau-ntupler/interface/patElectronHelper.h"
#include "ntuples/VBF-LS-tau-ntupler/interface/recoGenParticleHelperPlus.h"
#include "ntuples/VBF-LS-tau-ntupler/interface/edmEventHelperExtra.h"



namespace
{
  HelperFor<pat::Tau> t_patTauHelper;
  HelperFor<pat::Electron> t_patElectronHelper;
  HelperFor<reco::GenParticle> t_recoGenParticleHelperPlus;
  HelperFor<edm::Event> t_edmEventHelperExtra;
}
