import unicodedata
import os
import codecs
import sys

project_folder = '.'


if len(sys.argv) < 2:
    print('Please provide second cmd parameter for rollnumber (e.g. 21100000).')
    exit(1)

# your roll number
rollnumber = sys.argv[1]

# absolute path of your PRUS.txt
input_text_file = os.path.join(project_folder,'PRUS.txt')

# absolute path of new PRUS.txt
output_text_file = os.path.join(project_folder,'PRUS_'+rollnumber+'.txt')

# absolute path of your recordings folder
wav_input_folder = os.path.join(project_folder,rollnumber)

f = codecs.open(input_text_file, 'r', encoding='utf-8')
p = codecs.open(output_text_file, 'w', encoding='utf-8')

i = 1
for line in f:
    line = line.replace(u'\ufeff','')
    line = line.replace(u'\u200C','')
    line = unicodedata.normalize('NFC',line)
    p.write(rollnumber + '_' + str(i).zfill(3) + ' ' +line.strip() + '\n')
    i += 1
f.close()
p.close()
print("Done writing new file at: ", output_text_file)

for filename in os.listdir(wav_input_folder):
    source =  os.path.join(wav_input_folder, filename)
    dest =  os.path.join(wav_input_folder, rollnumber + '_' + filename[:-4].replace(' ', '').zfill(3) + filename[-4:])
    os.rename(source, dest)

print("Done renaming wav files at: ", wav_input_folder)

