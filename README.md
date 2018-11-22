# Summary of Kaldi for ivector and xvector

## Files List

 `ivector/`
  - `conf/`: configure file for mfcc and vad
  - `wav/`: test audio  (you can also use your own wav path, see **Step 1**)
    - Only supprot flac (install flac), wav and sph (install sph2pipe )
  - `model_3000h/`: pre-trained model
  - `enroll.sh`: main process fille


  - `data/`: save extracted features (It's a generated file)
    - `utt2spk, wav.scp` generate two files through make_data.py
    - `spk2utt`: generate from utt2spk
    - `log/`: save all logs
    - `tmp/`: save all tmp files


`xvector/`

- `conf/`: configure file for mfcc and vad
- `wav/`: test audio  (you can also use your own wav path, see **Step 1**)
  - Only supprot flac (install flac), wav and sph (install sph2pipe )
- `exp/`: pre-trained model
- `enroll.sh`: main process fille


- `data/`: save extracted features (It's a generated file)
  - `utt2spk, wav.scp` generate two files through make_data.py
  - `spk2utt`: generate from utt2spk
  - `log/`: save all logs
  - `tmp/`: save all tmp files

`format_norm.py`: change ark format to npz format

## Extract features: ivector and xvector

### Step 0: Preparation

- First, install [Kaldi](https://github.com/kaldi-asr/kaldi). 
- Then, step into `ivector/` or `xvector/` folder


- Change KALDI_ROOT in `path.sh` to your own kaldi root
- Add link:

```sh
ln -s $KALDI_ROOT/egs/sre16/v2/steps ./
ln -s $KALDI_ROOT/egs/sre16/v2/sid ./
ln -s $KALDI_ROOT/egs/sre16/v2/utils ./
```

### Step 1: Extract ivector and xvector

Refers to [pre-trained xvector model in kaldi](http://www.kaldi-asr.org/models/m3) and [kaidi-sre-code](https://github.com/kaldi-asr/kaldi/tree/master/egs/sre16)

- Extract ivector: cd `ivector` and run `enroll.sh` to extract ivector

```sh
bash enroll.sh wav_path
# for example: bash enroll.sh ./wav
```

- Extract xvector: cd `xvector` and run `enroll.sh` to extract ivector

```sh
## Case 1: extract xvector without speaker infos
#          for example: bash enroll.sh ./wav 1
bash enroll.sh wav_path 1

## Case 2: extract xvector with speaker infos
####Step 1: Generate speaker.txt files
####Only suitable for files like 'wav_root/speaker_id/wav_name'
####Other format, you should write your own generate_speaker.py
python generate_speaker.py wav_dir speaker.txt
####Step 2: extract xvector with speaker infos
####For example, bash enroll.sh ./speaker.txt 2
bash enroll.sh ./speaker.txt 2
```

### Step 2: Read generate ivector and xvector

In this section, we convert ivector and xvector from ark type to array type

i-vector in `data/feat/ivectors_enroll_mfcc`

- `spk_ivector.ark` i-vector for each speaker
- `ivector.1.ark`: i-vector for each utturance (400-d i-vector)

x-vector in `data/feat/xvectors_enroll_mfcc`

- `spk_xvector.ark` x-vector for each speaker
- `xvector.1.ark`: x-vector for each utturance (512-d x-vector)

```sh
## print name and feats from ark to txt
$KALDI_ROOT/src/bin/copy-vector ark:ivector/data/feat/ivectors_enroll_mfcc/ivector.1.ark ark,t:- >ivector.txt

$KALDI_ROOT/src/bin/copy-vector ark:xvector/data/feat/xvectors_enroll_mfcc/xvector.1.ark ark,t:- >xvector.txt

## Or you can change ark format to np.array format, which has (data_path ['pic_path'], ivector or xvector)
python format_norm.py --vector_path='xvector.txt' --save_path='x_vector.npz'
python format_norm.py --vector_path='ivector.txt' --save_path='i_vector.npz'
```

# Other summary

```sh
## combine different files
utils/combine_data.sh

## make xxx fits to the kaldi format
utils/fix_data_dir.sh xxx

## gain subset of data
utils/subset_data_dir.sh

## file exists and dir exists
if [ -d "./data" ];then # dictionary exists
if [ -f "./data/1.txt" ];then # file exists

## xvector/run.sh
Has four folder: 
	sre_combined (source domain, argument data, for training)
	sre16_major (unlabeded target domain for model adaption)
	sre16_eval_enroll(labeded target domain for train)
	sre16_eval_test(unlabeded target domain for test)
Main stream: xvector->mean->transform(LDA)->len normalize->classifier(PLDA/adapt-PLDA)

## ark: split by space and print the third one
echo '1 2 3' |awk '{print $3}'  # print 3
```

