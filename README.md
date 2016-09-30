ClaRNA_play
-------------------------------------------------------------------------------

    clarna_run.py -ipdb 1xjr.pdb > 1xjr.pdb.CL

    clarna_anal.py -iref 1xjr.pdb.outCR -ichk 1xjr.pdb.outCR
    1xjr.pdb.outCR                               1xjr.pdb.outCR      1.000      NA         1.000      1.000      1.000      1.000      1.000      1.000

Tested with ClaRNA only.

    ➜  magnus clarna_run.py -ipdb 1xjr.pdb
    Classifier: Clarna
    A    4   A   46          bp G U                  WW_cis   0.7957
    A    5   A   45          bp U A                  WW_cis   0.9186
    A    6   A   44          bp U A                  WW_cis   0.9299
    A    7   A   43          bp C G                  WW_cis   0.9177
    A    8   A   42          bp A U                  WW_cis   0.9332
    A    9   A   41          bp C G                  WW_cis   0.9209
    A   10   A   40          bp C A                  WW_cis   0.6129
    A   11   A   33          bp G A                  SS_cis   0.7598
    A   13   A   39          bp G C                  WW_cis   0.8812
    A   14   A   37          bp G U                  WW_cis   0.8378
    A   15   A   36          bp C G                  WW_cis   0.9079
    A   16   A   35          bp C G                  WW_cis   0.9229
    A   17   A   34          bp A G                  WW_cis   0.8822
    A   18   A   32          bp C G                  WW_cis   0.9262
    A   19   A   31          bp G C                  WW_cis   0.8962
    A   19   A   20          bp G C                  SS_cis   0.7453
    A   20   A   28          bp C G                  WW_cis   0.7902
    A   21   A   27          bp G C                  WW_cis   0.8676
    A   22   A   26          bp G A                 SH_tran   0.7988
    A   28   A   31          bp G C                  SS_cis   0.6844
    A   38   A   39          bp A C                  SH_cis   0.8775

Install
-------------------------------------------------------------------------------

This is a really impossible mess!

Anyway, the last time I got this thing running (August 30th, 2016), I
did the following states.

1. Download clarna from gitlab
place in an appropriate directory such as 

/home/wdawson/python/clarna

unzip and rename to ClaRNAlib

https://gitlab.genesilico.pl/RNA/clarna

2. Check the readme file at for updates!!!!

https://gitlab.genesilico.pl/RNA/clarna/blob/master/README.md

3. Make sure to install json, networkx and scipy in the fixed version

> sudo pip install simplejson==2.6.1 networkx==1.8.1 scipy

4. Make sure the following directories are in your PATH 

# in ${HOME}/.bash_profile, set
export PATH=$PATH:${YOUR_PATH_TO_CLARNA}
export PATH=$PATH:${YOUR_PATH_TO_CLARNA}/bin

e.g., /home/wdawson/python/clarna

where bin provides some additional scripts

5. Make sure the following directory is in your PYTHONPATH

# in ${HOME}/.bash_profile, set
export PYTHONPATH=${YOUR_PATH_TO_CLARNA}


6. In the current directory, you must change the following line in
run_clarna.py to your particular path.

CLARNA_PATH = "${YOUR_PATH_TO_CARNA}/ClaRNAlib/"

(line 18 currently).

7 (optional). To include additional 3rd party options in the
functionality such as RNAVIEW, MC_ANNOTATE or FR3D, you must modify
the python program

${YOUR_PATH_TO_THIS_DIR}/ClaRNAlib/cl_settings_global.py

to your particular environment specifying the paths for RNAVIEW,
mc_annotate, and FR3D-dev.


8. Given that everything is working, now you can use ClaRNA. 

8a) To evalute a single pdb file by the following command line

>  run_clarna.py [-Clarna] -ipdb 1kd5_A_minE-000001_AA.pdb \
   		 -thresh 0.5 -stack > x.outCR

for a full list of options, please type "run_clarna.py -h". 

The default option -Clarna is not necessary in this case. To run a
different binary analyzer, one can type (for example)

>  run_clarna.py [-rnaview] -ipdb 1kd5_A_minE-000001_AA.pdb \
   		 -thresh 0.5 -stack > x.outRV

8b) To evaluate a set of outputs from SimRNA, the script 

> build_clarna_dataset.sh [threshold]

is provided. The threshold defaults to 0.6 and, in general, this is
what should be used. Currently, build_clarna_dataset.sh requires that
the following directories be present in the directory where the
program is run.

all_1_2_3_clusts_pdbs_pdbsAA 
all_lowestE_pdbs_pdbAA
all_lowestRMSD_pdbs_pdbsAA 
all_natives

If everything is successful, then in each of these directories, there
should be an output file with the extension "outCR".

For example, in tests/DasBaker_dataset_folded_denovo, you will find

> ls all_lowestE_pdbs_pdbsAA/
157d_A_minE-000001_AA.pdb        1l2x_A_minE-000001.ss_detected
157d_A_minE-000001_AA.pdb.outCR  1mhk_A_minE-000001_AA.pdb
157d_A_minE-000001.pdb           1mhk_A_minE-000001_AA.pdb.outCR
157d_A_minE-000001.ss_detected   1mhk_A_minE-000001.pdb
1a4d_A_minE-000001_AA.pdb        1mhk_A_minE-000001.ss_detected
1a4d_A_minE-000001_AA.pdb.outCR  1q9a_A_minE-000001_AA.pdb
1a4d_A_minE-000001.pdb           1q9a_A_minE-000001_AA.pdb.outCR
1a4d_A_minE-000001.ss_detected   1q9a_A_minE-000001.pdb
1csl_A_minE-000001_AA.pdb        1q9a_A_minE-000001.ss_detected
1csl_A_minE-000001_AA.pdb.outCR  1xjr_A_minE-000001_AA.pdb
1csl_A_minE-000001.pdb           1xjr_A_minE-000001_AA.pdb.outCR
1csl_A_minE-000001.ss_detected   1xjr_A_minE-000001.pdb
1dqf_A_minE-000001_AA.pdb        1xjr_A_minE-000001.ss_detected
1dqf_A_minE-000001_AA.pdb.outCR  1zih_A_minE-000001_AA.pdb
1dqf_A_minE-000001.pdb           1zih_A_minE-000001_AA.pdb.outCR
1dqf_A_minE-000001.ss_detected   1zih_A_minE-000001.pdb
1i9x_A_minE-000001_AA.pdb        1zih_A_minE-000001.ss_detected
1i9x_A_minE-000001_AA.pdb.outCR  255d_A_minE-000001_AA.pdb
1i9x_A_minE-000001.pdb           255d_A_minE-000001_AA.pdb.outCR
1i9x_A_minE-000001.ss_detected   255d_A_minE-000001.pdb
1j6s_A_minE-000001_AA.pdb        255d_A_minE-000001.ss_detected
1j6s_A_minE-000001_AA.pdb.outCR  283d_A_minE-000001_AA.pdb
1j6s_A_minE-000001.pdb           283d_A_minE-000001_AA.pdb.outCR
1j6s_A_minE-000001.ss_detected   283d_A_minE-000001.pdb
1kd5_A_minE-000001_AA.pdb        283d_A_minE-000001.ss_detected
1kd5_A_minE-000001_AA.pdb.outCR  2a43_A_minE-000001_AA.pdb
1kd5_A_minE-000001.pdb           2a43_A_minE-000001_AA.pdb.outCR
1kd5_A_minE-000001.ss_detected   2a43_A_minE-000001.pdb
1l2x_A_minE-000001_AA.pdb        2a43_A_minE-000001.ss_detected
1l2x_A_minE-000001_AA.pdb.outCR  x.out
1l2x_A_minE-000001.pdb

if the program worked correctly, these files should be generated.

9.  If everything has worked up to here, then you can now try to
analyze the data.

9a) It is rather cumbersome to do analysis on an individual file;
however, it is possible. For an individual pair of ClaRNA outputs,
you can run the following program anal_clarna.py.

9b) For bulk analysis with SimRNA.

analyze_using_CR_wRMSD.sh
