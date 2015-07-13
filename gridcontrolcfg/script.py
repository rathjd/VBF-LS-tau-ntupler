#!/usr/bin/env python

import sys,os,glob

##################################
# read command line arguments and environment
##################################

MYPROJECTDIR = os.environ['MYPROJECTDIR']
INPUT = sys.argv[1]
print 'input:',INPUT
WORKDIR="/nfs/dust/cms/user/dmarconi/workdir/gridcontrol"
ANALYZERS=["analyzer"]
ODIR="/nfs/dust/cms/user/dmarconi/workdir/gridcontrol/results"

##################################
# list all input files
##################################
pos = INPUT.find('[')
# get the name of the filelist
INPUT_name = INPUT
if pos >= 0:
    INPUT_name = INPUT_name[0:pos]
# the range of files to be processed
INPUT_start = 0
INPUT_stop = -1
if pos >= 0:
    INPUT_range = INPUT.replace(INPUT_name,"")
    [INPUT_start,INPUT_stop] = [int(x.strip('[').strip(']')) for x in INPUT_range.split(':')]
# read the files in
FILE = open(MYPROJECTDIR + '/data/filelists/' + INPUT_name + '.txt')
ifiles = FILE.read().split('\n')
FILE.close()
if INPUT_stop < 0:
    ifiles = len(ifiles) -1
ifiles = ifiles[INPUT_start:INPUT_stop]
# print file list
print 'all input files:'
for ifile in ifiles:
    print ' - ' + ifile

##################################
# create local filelist(s)
##################################
os.mkdir('filelists')
filelists = []

for ifile in ifiles:
    filelists.append('filelists/' + os.path.split(ifile)[1].replace('.root','.txt'))
    FILE = open(filelists[-1],'w')
    FILE.write(ifile + '\n')
    FILE.close()
sys.stdout.flush()

##################################
# run analyzers and copy output
##################################
for analyzer in ANALYZERS:
    output = 'results/' + analyzer + '/' + INPUT_name
    os.makedirs(output)
    for filelist in filelists:
        inputbase = os.path.split(filelist)[1]
        pos = inputbase.rfind(".")
        inputbase = inputbase[0:pos]
        output = 'results/' + analyzer + '/' + INPUT_name + '/' + inputbase + "_j" + str(os.environ["MY_JOBID"]) + '.root'
        command = WORKDIR + '/' + analyzer + ' ' + filelist + ' ' + output
        print command
        os.system(command)
        ofiles = glob.glob(output + '*')
        print 'copy output'
        for ofile in ofiles:
            command = 'cp ' + ofile + ' ' + ODIR + '/' + analyzer + '/' + INPUT_name
            print command
            os.system(command)
