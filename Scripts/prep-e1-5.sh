cd data/local/lang
cp /docker/spp2/PRUS_21100197.txt .
cut -d ' ' -f 2- PRUS_21100197.txt | sed 's/ /\n/g' | sort -u > words.txt
python filter_dict.py
wc -l words.txt
cp PRUS_21100297.txt ../../train/text 
cd ../../test
cat ../train/text | tail -108 > text  
cd ../train
mv text text.bak
cat text.bak | head -600 > text
cd ../..
python3 makefiles.py 21100197