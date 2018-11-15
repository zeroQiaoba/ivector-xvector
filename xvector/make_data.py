import os
import sys
import glob

if (len(sys.argv)-1 != 2):
  print ("Usage: $0 <path-to-data> <output-dir>")
  print ("e.g. $0 ./wav ./data")
  exit(1)

wav_path = sys.argv[1]
out_dir = sys.argv[2]

tmp_dir = out_dir + "/tmp"
utt2spk_path = out_dir + "/utt2spk"
wavscp_path = out_dir + "/wav.scp"

if (os.system("mkdir -p %s" %(tmp_dir)) != 0):
  print ("Error making directory %s" %(tmp_dir))


output_1 = open(utt2spk_path, 'w')
output_2 = open(wavscp_path, 'w')
for path in glob.glob(wav_path + '/*'):
	path_name, path_type = os.path.split(path)[-1].split('.')
	if path_type in ['flac', 'wav', 'sph']: # is audio
		speaker = path_name
		uttid = path_name#'%s-%s' %(speaker, path_name)
		utt2spk_temp = '%s %s\n' %(uttid, speaker)
		if path_type == 'flac': wavscp_temp = '%s flac -c -d -s %s |\n' %(uttid, path)
		if path_type == 'wav': wavscp_temp = '%s %s\n' %(uttid, path)
		if path_type == 'sph': wavscp_temp = '%s sph2pipe -f wav -p -c 1 %s\n' %(uttid, path)
	output_1.write(utt2spk_temp)
	output_2.write(wavscp_temp)

output_1.close()
output_2.close()