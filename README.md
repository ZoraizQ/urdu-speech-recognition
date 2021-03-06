# Urdu Speech Recognition
Urdu Speech Recognition using the Kaldi ASR toolkit, by training Triphone Acoustic Gaussian Mixture Models using the PRUS dataset and lexicon in a team of 5 students for the course CS 433 Speech Processing taught by Dr. Agha Ali Raza at Lahore University of Management Sciences.
- [Zoraiz Qureshi](https://github.com/ZoraizQ)
- [Ahmed Farhan](https://github.com/AhmedFarhan252)
- [Ramez Salman](https://github.com/ramzyraz)
- [Farrukh Rasool](https://github.com/farrukhras)
- [Hamza Farooq](https://github.com/hamzafarooq009)


## Run
### Current directory:
- s5 (Main corpus training directory)
- Experiments (Final .mdl, best_wer, corresponding wer stats and per_spk stats for each experiment)
- Scripts (Helper scripts)
- .wav folders for each of the 5 speakers by their speaker ID (21100XXX)
- PRUS_21100XXX.txt generated corpus, speakerID wise for the PRUS dataset made using PronouncUR [1].


### Instructions:
- Run `makefiles.py` and its other experiment counterparts used for generating training data in the correct format.
- Set correct Kaldi root directory paths in `path.sh`
- Set the HMM States / Gaussians at every stage and the number of jobs for feature extraction, training and decoding/testing in `run.sh`
- Set the language model to use as well (LM1 or LM2), or add your own.
- Execute `run.sh` and check decode results in `exp/tri3/decode`.


## Experiments
- **Experiments 1-5**: Trained a GMM based tri-phone acoustic model on the first 600 sentences of the corpus (PRUS.txt) and tested it on the rest of the 108 sentences of the corpus of each specific speaker, so 5 different models (SP1-SP5). Used LM1.gz while decoding.

- **Experiment 6**: Trained a GMM based tri-phoneacoustic model on the first 600 sentences of each speakers’ corpus (combine first 600 sentences of each member to form one large training corpus) and test it onthe rest of the 108 sentences of each speaker’s corpus (combine 108 sentences of each member to form one testing corpus). Used LM1.gz while decoding. 108 sentences of the corpus will still be unseen as before so WER scores willremain high.

- **Experiments 7-11**: Trained a GMM based tri-phone acoustic model on the complete corpus(708 sentences) of n-1 speakers and tested it on the complete corpus of the remaining 1 speaker, so 5 different models (leaving out SP1-SP5). Used LM2.gz while decoding.


## References
[1] Zia, Haris & Raza, Agha Ali & Athar, Awais. (2018). PronouncUR: An Urdu Pronunciation Lexicon Generator. https://arxiv.org/ftp/arxiv/papers/1801/1801.00409.pdf
