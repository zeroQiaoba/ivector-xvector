import os
import sys
import glob
import numpy as np

if (len(sys.argv)-1 != 2):
	print ("Usage: $0 <label-to-data> <output-dir>")
	print ("e.g. $0 speaker.txt ./data")
	exit(1)

label_path = sys.argv[1]
out_dir = sys.argv[2]

if (os.system("mkdir -p %s" %(out_dir)) != 0):
  print ("Error making directory %s" %(out_dir))
  
### generate utt2spk and wav.scp for iemocap_enroll
output_1 = open(out_dir + "/utt2spk", 'w')
output_2 = open(out_dir + "/wav.scp", 'w')

## read data from label_path
f = open(label_path)
for line in f.readlines():
	wav_path, speaker = line.strip().split(' ')
	wav_name = os.path.split(wav_path)[-1]
	wav_name, path_type = wav_name.split('.')
	if path_type in ['flac', 'wav', 'sph']: # is audio
		uttid = '%s-%s' %(speaker, wav_name)
		utt2spk_temp = '%s %s\n' %(uttid, speaker)
		if path_type == 'flac': wavscp_temp = '%s flac -c -d -s %s |\n' %(uttid, wav_path)
		if path_type == 'wav': wavscp_temp = '%s %s\n' %(uttid, wav_path)
		if path_type == 'sph': wavscp_temp = '%s sph2pipe -f wav -p -c 1 %s\n' %(uttid, wav_path)
	output_1.write(utt2spk_temp)
	output_2.write(wavscp_temp)

output_1.close()
output_2.close()

