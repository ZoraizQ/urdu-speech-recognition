from os import walk
import os
import sys

if len(sys.argv) < 2:
	print ("Please provide the rollnumber as second param")

rollnumber = sys.argv[1]
wav_dir = '/opt/docker/spp2/' + rollnumber

f = []
for (dirpath, dirnames, filenames) in walk(wav_dir):
	f.extend(filenames)
	break

f.sort()

print(len(f))

with open('data/train/wav.scp', 'w') as fout:
	for i in range(600):
		filename = f[i]
		fout.write(filename[:-4] + ' ' + os.path.join(wav_dir, filename)+'\n')

with open('data/test/wav.scp', 'w') as fout_test:
	for i in range(600,len(f)):
		filename = f[i]
		fout_test.write(filename[:-4] + ' ' + os.path.join(wav_dir, filename)+'\n')


print('train test wav.scp exported for', rollnumber)

with open('data/train/utt2spk', 'w') as fout:
	for i in range(600):
		filename = f[i]
		fout.write(filename[:-4] + ' ' + rollnumber + '\n')

with open('data/test/utt2spk', 'w') as fout_test:
	for i in range(600,len(f)):
		filename = f[i]
		fout_test.write(filename[:-4] + ' ' + rollnumber + '\n')


print('train test utt2spk exported for', rollnumber)
