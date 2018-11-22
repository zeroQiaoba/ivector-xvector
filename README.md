## Summary of Kaldi for ivector and xvector

### Files:

- `ivector/`
  - `conf/`: configure file for mfcc and vad
  - `wav/`: test audio  (you can also use your own wav path, see **Step 1**)
    - Only supprot flac (install flac), wav and sph (install sph2pipe )
  - `model_3000h/`: pre-trained model
  - `enroll.sh`: main process fille


  - `data/`: save extracted features (It's a generated file)
    - `utt2spk, wav.scp` generate two files through make_data.py
    - `spk2utt`: generate from utt2spk
    - `log/`: save all logs
    - `feat/`: save all feats
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
  - `feat/`: save all feats
  - `tmp/`: save all tmp files

`format_norm.py`: change ark format to npz format

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

Extract xvector: 

- first cd `xvector/`
- We can choose two extraction approach: with speaker info and without speaker info

```sh
# Extract xvector without speaker infos.
# For example: bash enroll.sh ./wav type=1
bash enroll.sh wav_path 1

# Extract xvector with speaker infos.
# step 1: generate speaker.txt for folders like "wav_root/speaker_id/wav_name"
#         speaker.txt has items (wav_path, speaker) in each line
#         code: enerate_speaker.py wav_root save_path
python generate_speaker.py wav_root speaker.txt
# step 2: extract xvector
#         For example: bash enroll.sh speaker.txt type=2
bash enroll.sh speaker_path 2
```

Extract ivector: 

- first cd `ivector/`
- We can only choose: without speaker info

```sh
# Extract xvector without speaker infos.
# For example: bash enroll.sh ./wav type=1
bash enroll.sh wav_path
```

### Step 2: Read generate ivector and xvector

In this section, we convert ivector and xvector from ark type to array type

i-vector in `ivector/data/feat/ivectors_enroll_mfcc`

- `spk_ivector.ark` i-vector for each speaker
- `ivector.1.ark`: i-vector for each utturance (400-d i-vector)

x-vector in `xvector/data/feat/xvectors_enroll_mfcc`

- `spk_xvector.ark` x-vector for each speaker
- `xvector.1.ark`: x-vector for each utturance (512-d x-vector)

```sh
## print name and feats from ark to txt
$KALDI_ROOT/src/bin/copy-vector ark:ivector/data/feat/ivectors_enroll_mfcc/ivector.1.ark ark,t:-|head >ivector.txt

$KALDI_ROOT/src/bin/copy-vector ark:xvector/data/feat/xvectors_enroll_mfcc/xvector.1.ark ark,t:-|head >xvector.txt

## Then analyze xxxx.txt to np.array type
python format_norm.py --ivector_path='ivector.txt' --xvector_path='xvector.txt' --save_path='i_x_vector.npz'
```



## Other summary

```sh
## combine different files
utils/combine_data.sh

## 将不同文件夹下面的spk2utt等文件整合，排序，使得他符合kaldi的格式
utils/fix_data_dir.sh

## gain subset of data
utils/subset_data_dir.sh
```

