![](https://img.shields.io/badge/SummerFIM-v1.0.0-orange.svg)

# SummerFIM
SummerFIM is a simple File Integrity Monitor (FIM) coded in Python. Basically, this program works from SHA2 checksum comparison.

## Motivation:
I'm a datahoarder and therefore I have many HDDs and it has happened to me that some files on one of these HDDs have been corrupted and I only found out much later in a while that the backup of that HDD had been damaged, that is, I lost all those files forever. SummerFIM comes to solve this problem!

## SummerFIM usage suggestion:
Have 2 HDDs with the exact same files and every 6 months run SummerFIM on each one of them and compare the old status with the new status of each one HDD and even between the two HDD status, since they are the same, if in any of these comparisons any hash is different, certainly your HDD has corrupted files. It is very unlikely that both HDDs will corrupt at the same time, so you should replace the corrupted HDD with a new one and copy all files from the healthy HDD to the HDD that replaced the corrupted one.
And that way you will have very good accuracy in the integrity of your files.

## How to install SummerFIM:
Run the following commands in your Linux terminal:
```bash
$ cd ~/
$ git clone https://github.com/davidsf026/SummerFIM -b v1.0.0 ~/.SummerFIM
$ alias summer='cd ~/.SummerFIM ; python3 ~/.SummerFIM/main.py ; cd ~/'
$ echo "alias summer='cd ~/.SummerFIM ; python3 ~/.SummerFIM/main.py ; cd ~/'" >> ~/.bashrc
```

Set the path you want to monitore editing pathToScan key value in `~/.SummerFIM/app/settings/settings.yaml` file. Example:
```yaml
pathToScan: "/home/david/Documents/Test"
filesListWithHashesTextFilePath: "app/data/hash_file.sha2"
```

SummerFIM is now installed!

## How to use SummerFIM:

### 0. Showing all avaible commands:
Open a Linux terminal and start SummerFIM CLI with `summer` command and run `help` instruction in SummerFIM CLI:
```bash
$ summer
summer> help
help     Display this help.
init     First checksum of selected path in settings.yaml file.
update   Update checksum of selected path in settings.yaml file.
exit     Exit SummerFIM.
summer> exit
Bye bye!
```

### 1. Initializing defined path monitoring:
After installing SummerFIM correctly, the first thing you do is initialize the monitoring of defined path in `settings.yaml`:
Open a Linux terminal and start SummerFIM CLI with `summer` command and run `init` instruction in SummerFIM CLI:
```bash
$ summer
summer> init
[ 1/3 ] 917f134de9e411465a28d076e3b395ec9a9faf58dbf7e62d4bd4ee90c838c6ca */home/david/Documents/Test/1.txt
[ 2/3 ] ff5d016f12764b10f99041c02575c73517115d67bda134aeff3dd9b53ede2592 */home/david/Documents/Test/2.txt
[ 3/3 ] e6476c095dae12456964423db181068538bf6d67dc80ba8b2db80fdbddd59508 */home/david/Documents/Test/3.txt
summer> exit
Bye bye!
```

Now SummerFIM has recursively scanned the defined path and checksummed all files present, this data is saved in `~/.SummerFIM/app/data/hash_file.sha2` as demonstrated below:
```bash
$ cat ~/.SummerFIM/app/data/hash_file.sha2
917f134de9e411465a28d076e3b395ec9a9faf58dbf7e62d4bd4ee90c838c6ca */home/david/Documents/Test/1.txt
ff5d016f12764b10f99041c02575c73517115d67bda134aeff3dd9b53ede2592 */home/david/Documents/Test/2.txt
e6476c095dae12456964423db181068538bf6d67dc80ba8b2db80fdbddd59508 */home/david/Documents/Test/3.txt
```

### 2. Updating monitoring of an ALREADY INITIALIZED path:
After initializing the monitoring of the defined path and it is expected that you spend some time changing the defined path, whether deleting files or creating new ones and whenever you wish, you can update the monitoring of the defined path where the checksum of the new files will be done and added to `hash_file.sha2` and files that have been deleted in the meantime will have their data deleted from `hash_file.sha2`.
To update the defined path, open a Linux terminal and start SummerFIM CLI with `summer` command and run `update` instruction in SummerFIM CLI:
```bash
$ summer
summer> update
[ INFO ] 2 files deletions were detected:
[ 1/2 ] /home/david/Documents/Test/1.txt
[ 2/2 ] /home/david/Documents/Test/2.txt

[ INFO ] 3 new files were detected:
[ 1/3 ] 2ge5gg78f87bf23807b2398h23f08n23f9m23f80ba8b2db808h23f08n23fm2fd */home/david/Documents/Test/4.txt
[ 2/3 ] h7hdf8721386fbv12bdae12456964423db181068538bf6d67dc80ba8b2db8008 */home/david/Documents/Test/5.txt
[ 3/3 ] 308h23f08n2378f87bf23807b239086964423db1810685384423db1810685384 */home/david/Documents/Test/6.txt
summer> exit
Bye bye!
```

### 3. Checking path integrity:
Open a Linux terminal and start SummerFIM CLI with `summer` command and run TWICE `update` instruction in SummerFIM CLI:
```bash
$ summer
summer> update
[ INFO ] 2 files deletions were detected:
[ 1/2 ] /home/david/Documents/Test/1.txt
[ 2/2 ] /home/david/Documents/Test/2.txt

[ INFO ] 3 new files were detected:
[ 1/3 ] 2ge5gg78f87bf23807b2398h23f08n23f9m23f80ba8b2db808h23f08n23fm2fd */home/david/Documents/Test/4.txt
[ 2/3 ] h7hdf8721386fbv12bdae12456964423db181068538bf6d67dc80ba8b2db8008 */home/david/Documents/Test/5.txt
[ 3/3 ] 308h23f08n2378f87bf23807b239086964423db1810685384423db1810685384 */home/david/Documents/Test/6.txt
summer> update
[ INFO ] 0 files deletions were detected:

[ INFO ] 0 new files were detected:
summer> exit
Bye bye!
```
The update statement is run twice to ensure the recorded path state in `hash_file.sha2` matches the current path state.
Now run the init instruction so that a new `hash_file.sha2` is generated and thus all checksum hashes are generated again.

```bash
$ summer
summer> init
[ 1/4 ] e6476c095dae12456964423db181068538bf6d67dc80ba8b2db80fdbddd59508 */home/david/Documents/Test/3.txt
[ 2/4 ] e6476c095dae12456964423db181068538bf6d67dc80ba8b2db80fdbddd59508 */home/david/Documents/Test/4.txt
[ 3/4 ] e6476c095dae12456964423db181068538bf6d67dc80ba8b2db80fdbddd59508 */home/david/Documents/Test/5.txt
[ 4/4 ] e6476c095dae12456964423db181068538bf6d67dc80ba8b2db80fdbddd59508 */home/david/Documents/Test/6.txt
[ WARNING ] Can't save, file already exists.
Do you want to replace app/data/hash_file.sha2? yes
[ INFO ] Replacing file...
summer> exit
Bye bye!
```

Notice that in SummerFIM's data folder (`~/.SummerFIM/app/data`) we will have two files, `hash_file.sha2` and `hash_file_old.sha2`, both have data from the same files the difference is that `hash_file_old.sha2` had the hashes recalculated recently and the `hash_file_old.sha2` has hashes recorded from the init prior to the init recently run and all the update instructions prior to the init recently run, that is, if a comparison is made between these two files and some hash is different, certainly the path has corrupted files. Currently SummerFIM does not have the ability to compare `hash_file.sha2` and `hash_file_old.sha2` files, but it can easily be done with any diff checker, I recommend the following: https://www.diffchecker.com/