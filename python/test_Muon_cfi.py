#-------------------------------------------------------------------------
# Created: Thu Apr  4 16:14:54 2013 by /afs/naf.desy.de/user/m/marconi/scratch/SingleTau/ntupleProducer/CMSSW_5_3_7_patch4/src/VBFntupleProducer/VBFntupleProducer/python/test_Muon_cfi.py
#-------------------------------------------------------------------------
import FWCore.ParameterSet.Config as cms
demo =\
cms.EDAnalyzer("TheNtupleMaker",
               ntupleName = cms.untracked.string("ntuple.root"),
               analyzerName = cms.untracked.string("analyzer.cc"),

               buffers =
               cms.untracked.
               vstring(
    'patMuon'
    ),
               patMuon =
               cms.untracked.
               vstring(
    'patMuon                         patMuons                        200',
    #---------------------------------------------------------------------
    'double  p()',
    'double  energy()',
    'double  et()',
    'double  px()',
    'double  py()',
    'double  pz()',
    'double  pt()',
    'double  phi()',
    'double  eta()',
    'bool  isGlobalMuon()',
    'bool  isTrackerMuon()',
    'bool  isPFMuon()',
    'float  pfIsolationR03()->sumChargedHadronPt',
    'float  pfIsolationR03()->sumChargedParticlePt',
    'float  pfIsolationR03()->sumNeutralHadronEt',
    'float  pfIsolationR03()->sumNeutralHadronEtHighThreshold',
    'float  pfIsolationR03()->sumPhotonEt',
    'float  pfIsolationR03()->sumPhotonEtHighThreshold',
    'float  pfIsolationR03()->sumPUPt',
    'float  pfIsolationR04()->sumChargedHadronPt',
    'float  pfIsolationR04()->sumChargedParticlePt',
    'float  pfIsolationR04()->sumNeutralHadronEt',
    'float  pfIsolationR04()->sumNeutralHadronEtHighThreshold',
    'float  pfIsolationR04()->sumPhotonEt',
    'float  pfIsolationR04()->sumPhotonEtHighThreshold',
    'float  pfIsolationR04()->sumPUPt',
    'int  numberOfMatchedStations()',
    'double  innerTrack()->normalizedChi2()',
    'double  innerTrack()->dxy()',
    'double  innerTrack()->dz()',
    'int  innerTrack()->hitPattern().numberOfValidPixelHits()',
    'int  innerTrack()->hitPattern().pixelLayersWithMeasurement()',
    'double  globalTrack()->normalizedChi2()',
    'int  globalTrack()->hitPattern().numberOfValidMuonHits()',
    'double  muonBestTrack()->dxy()',
    'double  muonBestTrack()->dz()'
    )
               )
