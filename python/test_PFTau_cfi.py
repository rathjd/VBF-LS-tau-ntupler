#-------------------------------------------------------------------------
# Created: Mon Mar 25 11:10:49 2013 by /afs/naf.desy.de/user/m/marconi/scratch/SingleTau/ntupleProducer/CMSSW_5_3_7_patch4/src/VBFntupleProducer/VBFntupleProducer/python/test_PFTau_cfi.py
#-------------------------------------------------------------------------
import FWCore.ParameterSet.Config as cms
demo =\
cms.EDAnalyzer("TheNtupleMaker",
               ntupleName = cms.untracked.string("ntuple.root"),
               analyzerName = cms.untracked.string("analyzer.cc"),

               buffers =
               cms.untracked.
               vstring(
    'recoPFTau',
    'recoPFTau1'
    ),
               recoPFTau =
               cms.untracked.
               vstring(
    'recoPFTau                       hpsPFTauProducer                200',
    #---------------------------------------------------------------------
    'int  charge()',
    'double  p()',
    'double  energy()',
    'double  et()',
    'double  px()',
    'double  py()',
    'double  pz()',
    'double  pt()',
    'double  phi()',
    'double  eta()',
#    'double  leadPFChargedHadrCand()->p()',
#    'double  leadPFChargedHadrCand()->energy()',
#    'double  leadPFChargedHadrCand()->et()',
#    'double  leadPFChargedHadrCand()->mass()',
#    'double  leadPFChargedHadrCand()->massSqr()',
#    'double  leadPFChargedHadrCand()->mt()',
#    'double  leadPFChargedHadrCand()->mtSqr()',
#    'double  leadPFChargedHadrCand()->px()',
#    'double  leadPFChargedHadrCand()->py()',
#    'double  leadPFChargedHadrCand()->pz()',
#    'double  leadPFChargedHadrCand()->pt()',
#    'double  leadPFChargedHadrCand()->phi()',
#    'double  leadPFChargedHadrCand()->theta()',
#    'double  leadPFChargedHadrCand()->eta()',
#    'double  leadPFChargedHadrCand()->rapidity()',
#    'double  leadPFChargedHadrCand()->y()'
    ),
               recoPFTau1 =
               cms.untracked.
               vstring(
    'recoPFTau                       hpsPFTauProducerSansRefs        200',
    #---------------------------------------------------------------------
    'int  charge()',
    'double  p()',
    'double  energy()',
    'double  et()',
    'double  px()',
    'double  py()',
    'double  pz()',
    'double  pt()',
    'double  phi()',
    'double  eta()',
#    'double  leadPFChargedHadrCand()->p()',
#    'double  leadPFChargedHadrCand()->energy()',
#    'double  leadPFChargedHadrCand()->et()',
#    'double  leadPFChargedHadrCand()->mass()',
#    'double  leadPFChargedHadrCand()->massSqr()',
#    'double  leadPFChargedHadrCand()->mt()',
#    'double  leadPFChargedHadrCand()->mtSqr()',
#    'double  leadPFChargedHadrCand()->px()',
#    'double  leadPFChargedHadrCand()->py()',
#    'double  leadPFChargedHadrCand()->pz()',
#    'double  leadPFChargedHadrCand()->pt()',
#    'double  leadPFChargedHadrCand()->phi()',
#    'double  leadPFChargedHadrCand()->theta()',
#    'double  leadPFChargedHadrCand()->eta()',
#    'double  leadPFChargedHadrCand()->rapidity()',
#    'double  leadPFChargedHadrCand()->y()'
    )
               )
