 UPLOADER        David Snyder 
 DATE            2017-10-03
 KALDI VERSION   e082c17

 This directory contains files generated from the recipe in egs/sre16/v2/.
 It's contents should be placed in a similar directory, with access to
 sid/, steps/, etc. This was created when Kaldi's master branch was at git
 log e082c17d4a8f8a791428ae4d9f7ceb776aef3f0b.


 I. Files list
 ------------------------------------------------------------------------------
 
 ./
     README.txt               This file
     run.sh                   The recipe that was in egs/sre16/v2/run.sh

 local/nnet3/xvector/tuning/
     run_xvector_1a.sh        Generated the configs, egs, and trained the model

 conf/
     vad.conf                 Energy VAD configration
     mfcc.conf                MFCC configuration

 exp/xvector_nnet_1a/ 
     final.raw                The pretrained model
     nnet.config              An nnet3 config file for instantiating the model
     extract.config           An nnet3 config file for extracting xvectors
     min_chunk_size           Min chunk size used (see extract_xvectors.sh)
     max_chunk_size           Max chunk size used (see extract_xvectors.sh)
     srand                    The RNG seed used

 exp/xvectors_sre_combined/
     mean.vec                 Vector for centering, from augmented SRE 04-10
     plda                     PLDA model, trained on augmented SRE 04-10
     transform.mat            LDA matrix, trained on augmented SRE 04-10

 exp/xvectors_sre16_major/
     mean.vec                 Vector for centering, from SRE16 major
     plda_adapt               The first PLDA model, adapted to SRE16 major


 II. Citation
 ------------------------------------------------------------------------------

 Currently, the best way to cite this in a paper is using the following bibtex:

 @article{snyder2017xvector,
  title={Deep Neural Network Embeddings for Text-Independent Speaker Verification},
  author={Snyder, David and Garcia-Romero, Daniel and Povey, Daniel and Khudanpur, Sanjeev},
  journal={Proc. Interspeech 2017},
  pages={999--1003},
  year={2017}
 }
 

 III. Recipe README.txt
 ------------------------------------------------------------------------------

 The following text is the README.txt from egs/sre16/v2 at the time this
 archive was created.


 This recipe replaces iVectors used in the v1 recipe with embeddings extracted
 from a deep neural network.  In the scripts, we refer to these embeddings as
 "xvectors."  The recipe is based on 
 http://www.danielpovey.com/files/2017_interspeech_embeddings.pdf but with
 improvements due to augmentation in the DNN training data.

 The recipe uses the following data for system development.  This is in
 addition to the NIST SRE 2016 dataset used for evaluation (see ../README.txt).
 
     Corpus              LDC Catalog No.
     SWBD2 Phase 1       LDC98S75
     SWBD2 Phase 2       LDC99S79
     SWBD2 Phase 3       LDC2002S06
     SWBD Cellular 1     LDC2001S13
     SWBD Cellular 2     LDC2004S07
     SRE2004             LDC2006S44
     SRE2005 Train       LDC2011S01
     SRE2005 Test        LDC2011S04
     SRE2006 Train       LDC2011S09
     SRE2006 Test 1      LDC2011S10
     SRE2006 Test 2      LDC2012S01
     SRE2008 Train       LDC2011S05
     SRE2008 Test        LDC2011S08
     SRE2010 Eval        LDC2017S06
     Mixer 6             LDC2013S03

 The following datasets are used in data augmentation.

     MUSAN               http://www.openslr.org/17
     RIR_NOISES          http://www.openslr.org/28
