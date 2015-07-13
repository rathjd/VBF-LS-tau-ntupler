#!/bin/sh

source /afs/desy.de/user/d/dmarconi/VBF-LS-tau/setenv.sh

export MY_SCRATCH=/nfs/dust/cms/user/dmarconi/workdir/gridcontrol_makeSamples
echo "LHENAME    = " @LHENAME@
echo "MY_SCRATCH = " $MY_SCRATCH
echo "CMSSW_BASE = " $CMSSW_BASE

# Settings

#Step 1

cmsRun ZEE_13TeV_cfi_GEN_SIM.py
#eval `scram unsetenv -sh`

#Step 2


#source /afs/desy.de/user/d/dmarconi/VBF-LS-tau/setenv.sh
cmsRun step2_DIGI_L1_DIGI2RAW_HLT_RAW2DIGI_L1Reco_PU.py
#eval `scram unsetenv -sh`

#Step 3

#source /afs/desy.de/user/d/dmarconi/VBF-LS-tau/setenv.sh
cmsRun step3_RAW2DIGI_L1Reco_RECO_PU.py
#eval `scram unsetenv -sh`

#Step 4

#source /afs/desy.de/user/d/dmarconi/VBF-LS-tau/setenv.sh
cmsRun step5_PAT.py

#Copy Output

#lcg-cp -b -U ZEE_13TeV_AODSIM.root $MY_SCRATCH/results/@LHENAME@_AODSIM_@MY_JOBID@.root
#lcg-cp -b -U ZEE_13TeV_MINIAODSIM.root $MY_SCRATCH/results/@LHENAME@_MINIAODSIM_@MY_JOBID@.root
cp ZEE_13TeV_AODSIM.root $MY_SCRATCH/results/@LHENAME@_AODSIM_@MY_JOBID@.root
cp ZEE_13TeV_MINIAODSIM.root $MY_SCRATCH/results/@LHENAME@_MINIAODSIM_@MY_JOBID@.root
eval `scram unsetenv -sh`
