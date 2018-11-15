# Summary of Kaldi for ivector and xvector

## Files List

`ivector/`
- `conf/`: configure file for mfcc and vad
- `wav/`: test audio path (you can also use your own wav path, see **Step 1**)
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
- `wav/`: test audio  path (you can also use your own wav path, see **Step 1**)
  - Only supprot flac (install flac), wav and sph (install sph2pipe )
- `exp/`: pre-trained model
- `enroll.sh`: main process fille


- `data/`: save extracted features (It's a generated file)
  - `utt2spk, wav.scp` generate two files through make_data.py
  - `spk2utt`: generate from utt2spk
  - `log/`: save all logs
  - `tmp/`: save all tmp files

`format_norm.py`: change ark format to npz format

## Extract features for each utterance

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

Step into `ivector/` or `xvector/` folder

Run `enroll.sh` to extract ivector or xvector

```sh
bash enroll.sh wav_path
# for example: bash enroll.sh ./wav
```

### Step 2: Read generate ivector and xvector

In this section, we convert ivector and xvector from ark type to array type

Step into `ivector_xvector-master/` folder

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

## Or you can change ark format to np.array format
python format_norm.py --ivector_path='ivector.txt' --xvector_path='xvector.txt' --save_path='i_x_vector.npz'
```
