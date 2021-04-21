from os import walk
import os

rollnumber = '21100130'
wav_dir = '/opt/kaldi/spp2/' + rollnumber

f = []
for (dirpath, dirnames, filenames) in walk(wav_dir):
    f.extend(filenames)
    break

f.sort()

print(len(f))

with open('wav.scp', 'w') as fout:
    with open('wav-test.scp', 'w') as fout_test:
        for i in range(600):
            filename = f[i]
            fout.write(filename[:-4] + ' ' + os.path.join(wav_dir, filename)+'\n')

        for i in range(600,len(f)):
            filename = f[i]
            fout_test.write(filename[:-4] + ' ' + os.path.join(wav_dir, filename)+'\n')


print('wav.scp exported for', rollnumber)

with open('utt2spk', 'w') as fout:
    with open('utt2spk-test', 'w') as fout_test:
        for i in range(600):
            filename = f[i]
            fout.write(filename[:-4] + ' ' + rollnumber + '\n')

        for i in range(600,len(f)):
            filename = f[i]
            fout_test.write(filename[:-4] + ' ' + rollnumber + '\n')


print('utt2spk exported for', rollnumber)
