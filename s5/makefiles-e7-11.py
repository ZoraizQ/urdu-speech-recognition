from os import walk
import os
import sys
import codecs

if (len(sys.argv) != 2):
    raise Exception("Check arguments")
skip_idx = int(sys.argv[1])

rollnumber_list = ['21100130', '21100320', '21100170',
                   '21100297', '21100197']  # Z , A , R , F , H

print(skip_idx, rollnumber_list[skip_idx], "is being skipped.")

# rollnumber wise
files_rnlist = []
prus_rnlist = []
total = 708

for rollnumber in rollnumber_list:
    wav_dir = '/opt/docker/spp2/' + rollnumber

    f = []
    for (dirpath, dirnames, filenames) in walk(wav_dir):
        f.extend(filenames)
        break

    f.sort()

    print(len(f))
    files_rnlist.append(f)

    prus_file = '/opt/docker/spp2/PRUS_' + rollnumber + '.txt'
    l = []

    with codecs.open(prus_file, 'r', encoding='utf-8') as f:
        for line in f:
            l.append(line)

    print(len(l))

    prus_rnlist.append(l)

print('Wav paths read for:', len(files_rnlist))
print('Prus read for:', len(prus_rnlist))


# WRITE PRUS FILES
fo = codecs.open('data/train/text', 'w', encoding='utf-8')
for r in range(len(rollnumber_list)):
    if (r == skip_idx):
        continue

    for i in range(708):
        line = prus_rnlist[r][i]
        fo.write(line)
fo.close()

fo = codecs.open('data/test/text', 'w', encoding='utf-8')
r = skip_idx
for i in range(708):
    line = prus_rnlist[r][i]
    fo.write(line)
fo.close()

print('train test text exported')

# WRITE WAV.SCP FILES
with open('data/train/wav.scp', 'w') as fo:
    for r in range(len(rollnumber_list)):
        if r == skip_idx:
            continue

        wav_dir = '/opt/docker/spp2/' + rollnumber_list[r]
        for i in range(708):
            filename = files_rnlist[r][i]
            fo.write(filename[:-4] + ' ' +
                     os.path.join(wav_dir, filename)+'\n')

with open('data/test/wav.scp', 'w') as fo:
    r = skip_idx
    wav_dir = '/opt/docker/spp2/' + rollnumber_list[r]
    for i in range(708):
        filename = files_rnlist[r][i]
        fo.write(filename[:-4] + ' ' + os.path.join(wav_dir, filename)+'\n')


print('train test wav.scp exported')


# WRITE UTT2SPK FILES
with open('data/train/utt2spk', 'w') as fo:
    for r in range(len(rollnumber_list)):
        if r == skip_idx:
            continue

        rollnumber = rollnumber_list[r]
        for i in range(708):
            filename = files_rnlist[r][i]
            fo.write(filename[:-4] + ' ' + rollnumber + '\n')


with open('data/test/utt2spk', 'w') as fo:
    r = skip_idx
    rollnumber = rollnumber_list[r]
    for i in range(708):
        filename = files_rnlist[r][i]
        fo.write(filename[:-4] + ' ' + rollnumber + '\n')

print('train test utt2spk exported')
