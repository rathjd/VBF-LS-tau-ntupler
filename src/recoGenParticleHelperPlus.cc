//-----------------------------------------------------------------------------
// Subsystem:   ntuples
// Package:     VBF-LS-tau-ntupler
// Description: TheNtupleMaker helper class for reco::GenParticle
// Created:     Wed Oct 30 15:31:24 2013
// Author:      Lukas Vanelderen      
//-----------------------------------------------------------------------------
#include "ntuples/VBF-LS-tau-ntupler/interface/recoGenParticleHelperPlus.h"
//-----------------------------------------------------------------------------
using namespace std;
using namespace reco;
//-----------------------------------------------------------------------------
// This constructor is called once per job
GenParticleHelperPlus::GenParticleHelperPlus()
  : HelperFor<reco::GenParticle>() {}
    
GenParticleHelperPlus::~GenParticleHelperPlus() {}

// Called once per event
void
GenParticleHelperPlus::analyzeEvent()
{
  // Initialize string representation/position map
  if ( event == 0 )
    throw edm::Exception(edm::errors::Configuration,
                         "\nGenParticleHelperPlus - " 
                         "event pointer is ZERO");
  
  // Get genparticles:
  edm::Handle<GenParticleCollection> handle;
  // For now, hard-code getByLabel
  event->getByLabel("genParticles", handle);
  if (!handle.isValid())
    throw edm::Exception(edm::errors::Configuration,
                         "\nGenParticleHelperPlus - " 
                         "GenParticle handle is invalid");

  // Write a unique string for each genparticle
  // keeping only particles with status=3
  // Note: these occur first in particle list

  amap.clear();

  int n_stored = 0;
  for(unsigned int i = 0; i < handle->size(); i++) 
    {
      const GenParticle* p = &((*handle)[i]);
    
      //if ( p->status() != 3 ) break;

      bool store = false;
      //store particles with status 3
      if(p->status()==3)
        store = true;
      //store the decaying b and c hadrons 
      //(allways status 2)
      else if(p->status()==2)
        {
          int p_h = abs(p->pdgId()%1000/100);
          int p_t = abs(p->pdgId()%10000/1000);
          int taste = -1;
          //if the particle is a b meson or baryon
          if(p_h==5 || p_t == 5)
            taste = 5;
          //if the particle is a c meson or baryon
          else if(p_h==4 || p_t == 4)
            taste = 4;
          if(taste >0)
            {
              //store the particle
              store = true;
              //if it decays to a particle of different 'taste'
              for(unsigned int d = 0;d<p->numberOfDaughters();++d)
                {
                  int d_h = abs(p->daughter(d)->pdgId()%1000/100);
                  int d_t = abs(p->daughter(d)->pdgId()%10000/1000);
                  if(d_h==taste||d_t==taste)
                    store = false;
                }
            }
        }
      else if(p->status()==1)
        {
          if(p->pt() > 2)
            store = ( abs(p->pdgId()) == 11 || abs(p->pdgId()) == 13 || abs(p->pdgId())== 15);
        }

      // special treatment for taus
      if (abs(p->pdgId())==15)
	store = true;
      else
	for (unsigned int m =0;m<p->numberOfMothers();++m){
	  if(abs(p->mother(m)->pdgId())==15)
	    {
	      store = true;
	    }
	  // sometimes the decay is stored with intermediate steps...
	  else if(abs(p->mother(m)->pdgId())==24){
	    for (unsigned int m2 =0;m2<p->mother(m)->numberOfMothers();++m2){
	      if(abs(p->mother(m)->mother(m2)->pdgId())==15)
		{
		  store = true;
		  break;
		}
	    }
	  }
	  if(store)
	    break;
	}
      
      if ( !store ) continue;

      char particle[255];
      sprintf(particle,"%d%d%f%f%f%f",
              p->pdgId(), 
              p->status(), 
              p->px(), 
              p->py(), 
              p->pz(), 
              p->energy());
      amap[string(particle)] = n_stored;
      n_stored++;
    }
}

void 
GenParticleHelperPlus::analyzeObject()
{
  if ( object == 0 )
    throw edm::Exception(edm::errors::Configuration,
                         "\nGenParticleHelperPlus - " 
                         "object pointer is ZERO");

  // save only status = 3 particles

  
  bool store = false;
  //store particles with status 3
  if(object->status()==3)
    store = true;
  //store the decaying b and c hadrons 
  //(allways status 2)
  else if(object->status()==2)
    {
      int p_h = abs(object->pdgId()%1000/100);
      int p_t = abs(object->pdgId()%10000/1000);
      int taste = -1;
      //if the particle is a b meson or baryon
      if(p_h==5 || p_t == 5)
        taste = 5;
      //if the particle is a c meson or baryon
      else if(p_h==4 || p_t == 4)
        taste = 4;
      if(taste >0)
        {
          //store the particle
          store = true;
          //if it decays to a particle of different 'taste'
          for(unsigned int d = 0;d<object->numberOfDaughters();++d)
            {
              int d_h = abs(object->daughter(d)->pdgId()%1000/100);
              int d_t = abs(object->daughter(d)->pdgId()%10000/1000);
              if(d_h==taste||d_t==taste)
                store = false;
            }
        }
    }
  else if(object->status()==1)
    {
      if(object->pt() > 2)
        store = ( abs(object->pdgId()) == 11 || abs(object->pdgId()) == 13 || abs(object->pdgId())== 15);
    }
  if (abs(object->pdgId())==15)
    store = true;
  else
    for (unsigned int m =0;m<object->numberOfMothers();++m){
      if(abs(object->mother(m)->pdgId())==15)
	{
	  store = true;
	}
      // sometimes the decay is stored with intermediate steps...
      else if(abs(object->mother(m)->pdgId())==24){
	for (unsigned int m2 =0;m2<object->mother(m)->numberOfMothers();++m2){
	  if(abs(object->mother(m)->mother(m2)->pdgId())==15)
	    {
	      store = true;
	      break;
	    }
	}
      }
      if(store)
	break;
    }
  if ( !store )
    {
      count = 0;
      return;
    }
  
  // Find the ordinal value of first and last mothers by comparing the 
  // string representation of mothers with the string representation of 
  // each gen-particle in the list:

  char particle[255];

  mothers_.clear();
  for(unsigned int j=0; j < object->numberOfMothers(); j++) 
    {
      const GenParticle* m = 
        dynamic_cast<const GenParticle*>(object->mother(j));
      if ( m == 0 ) continue;
      sprintf(particle,"%d%d%f%f%f%f",
              m->pdgId(), 
              m->status(), 
              m->px(), 
              m->py(), 
              m->pz(), 
              m->energy());
      if ( amap.find(string(particle)) != amap.end() ) 
        mothers_.push_back( amap[string(particle)] );
    }

  // Find the ordinal value of first and last daughters by comparing the 
  // string representation of daughters with the string representation of 
  // each gen-particle in the list:

  daughters_.clear();
  for(unsigned int j=0; j < object->numberOfDaughters(); j++) 
    {
      const GenParticle* d = 
        dynamic_cast<const GenParticle*>(object->daughter(j));
      if ( d == 0 ) continue;
      sprintf(particle,"%d%d%f%f%f%f", 
              d->pdgId(),  
              d->status(), 
              d->px(), 
              d->py(), 
              d->pz(), 
              d->energy());
      
      if ( amap.find(string(particle)) != amap.end() ) {
        daughters_.push_back( amap[string(particle)] );
      }
    }
}

int      GenParticleHelperPlus::charge() const { return object->charge(); }
int      GenParticleHelperPlus::pdgId()  const { return object->pdgId(); }
int      GenParticleHelperPlus::status() const { return object->status(); }
double   GenParticleHelperPlus::energy() const { return object->energy(); }
double   GenParticleHelperPlus::pt()     const { return object->pt(); }
double   GenParticleHelperPlus::eta()    const { return object->eta(); }
double   GenParticleHelperPlus::phi()    const { return object->phi(); }
double   GenParticleHelperPlus::mass()   const { return object->mass(); }

int 
GenParticleHelperPlus::firstMother() const
{
  if ( mothers_.size() > 0 )
    return mothers_.front();
  else
    return -1;
}

int 
GenParticleHelperPlus::lastMother() const
{
  if ( mothers_.size() > 0 )
    return mothers_.back();
  else
    return -1;
}

int 
GenParticleHelperPlus::firstDaughter() const
{
  if ( daughters_.size() > 0 )
    return daughters_.front();
  else
    return -1;
}

int 
GenParticleHelperPlus::lastDaughter() const
{
  if ( daughters_.size() > 0 )
    return daughters_.back();
  else
    return -1;
}


