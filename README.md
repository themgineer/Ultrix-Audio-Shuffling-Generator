# **Audio Breakaway Labels**
This is a short, simple script that will take a list of source names and output a CSV of the audio breakouts.

One thing to keep in mind is that this will overwrite any output files that already exist if you use the generic
file name or do not specify a unique output filename.

## **Input Data Structure**
Data can be input into the script through a txt file or a csv. Follow the below structures to ensure consistent output.

### *List Input*
Input File:
``` 
Source 1
Source 2
Source 3
Source 4
```

Output File:
```
Source 1 CH01
Source 1 CH02
Source 1 CH03
Source 1 CH04
Source 1 CH05
...
...
...
Source 4 CH11
Source 4 CH12
Source 4 CH13
Source 4 CH14
Source 4 CH15
Source 4 CH16
```

### *CSV Input*
Input File[^csvnote]:
```
Source 1, Ultrix.slot1.in[1]
Source 2, Ultrix.slot1.in[1]
Source 3, Ultrix.slot1.in[1]
Source 4, Ultrix.slot1.in[1]
```

Output File:
```
Name,Description,Video,Audio 1,Audio 2,Audio 3,Audio 4,Audio 5,Audio 6,Audio 7,Audio 8,Audio 9,Audio 10,Audio 11,Audio 12,Audio 13,Audio 14,Audio 15,Audio 16
Source 1 CH01,,, Ultrix.slot1.in[1].audio.ch1, Ultrix.slot1.in[1].audio.ch1, Ultrix.slot1.in[1].audio.ch1, Ultrix.slot1.in[1].audio.ch1, Ultrix.slot1.in[1].audio.ch1, Ultrix.slot1.in[1].audio.ch1, Ultrix.slot1.in[1].audio.ch1, Ultrix.slot1.in[1].audio.ch1, Ultrix.slot1.in[1].audio.ch1, Ultrix.slot1.in[1].audio.ch1, Ultrix.slot1.in[1].audio.ch1, Ultrix.slot1.in[1].audio.ch1, Ultrix.slot1.in[1].audio.ch1, Ultrix.slot1.in[1].audio.ch1, Ultrix.slot1.in[1].audio.ch1, Ultrix.slot1.in[1].audio.ch1
Source 1 CH02,,, Ultrix.slot1.in[1].audio.ch2, Ultrix.slot1.in[1].audio.ch2, Ultrix.slot1.in[1].audio.ch2, Ultrix.slot1.in[1].audio.ch2, Ultrix.slot1.in[1].audio.ch2, Ultrix.slot1.in[1].audio.ch2, Ultrix.slot1.in[1].audio.ch2, Ultrix.slot1.in[1].audio.ch2, Ultrix.slot1.in[1].audio.ch2, Ultrix.slot1.in[1].audio.ch2, Ultrix.slot1.in[1].audio.ch2, Ultrix.slot1.in[1].audio.ch2, Ultrix.slot1.in[1].audio.ch2, Ultrix.slot1.in[1].audio.ch2, Ultrix.slot1.in[1].audio.ch2, Ultrix.slot1.in[1].audio.ch2
Source 1 CH03,,, Ultrix.slot1.in[1].audio.ch3, Ultrix.slot1.in[1].audio.ch3, Ultrix.slot1.in[1].audio.ch3, Ultrix.slot1.in[1].audio.ch3, Ultrix.slot1.in[1].audio.ch3, Ultrix.slot1.in[1].audio.ch3, Ultrix.slot1.in[1].audio.ch3, Ultrix.slot1.in[1].audio.ch3, Ultrix.slot1.in[1].audio.ch3, Ultrix.slot1.in[1].audio.ch3, Ultrix.slot1.in[1].audio.ch3, Ultrix.slot1.in[1].audio.ch3, Ultrix.slot1.in[1].audio.ch3, Ultrix.slot1.in[1].audio.ch3, Ultrix.slot1.in[1].audio.ch3, Ultrix.slot1.in[1].audio.ch3
Source 1 CH04,,, Ultrix.slot1.in[1].audio.ch4, Ultrix.slot1.in[1].audio.ch4, Ultrix.slot1.in[1].audio.ch4, Ultrix.slot1.in[1].audio.ch4, Ultrix.slot1.in[1].audio.ch4, Ultrix.slot1.in[1].audio.ch4, Ultrix.slot1.in[1].audio.ch4, Ultrix.slot1.in[1].audio.ch4, Ultrix.slot1.in[1].audio.ch4, Ultrix.slot1.in[1].audio.ch4, Ultrix.slot1.in[1].audio.ch4, Ultrix.slot1.in[1].audio.ch4, Ultrix.slot1.in[1].audio.ch4, Ultrix.slot1.in[1].audio.ch4, Ultrix.slot1.in[1].audio.ch4, Ultrix.slot1.in[1].audio.ch4
Source 1 CH05,,, Ultrix.slot1.in[1].audio.ch5, Ultrix.slot1.in[1].audio.ch5, Ultrix.slot1.in[1].audio.ch5, Ultrix.slot1.in[1].audio.ch5, Ultrix.slot1.in[1].audio.ch5, Ultrix.slot1.in[1].audio.ch5, Ultrix.slot1.in[1].audio.ch5, Ultrix.slot1.in[1].audio.ch5, Ultrix.slot1.in[1].audio.ch5, Ultrix.slot1.in[1].audio.ch5, Ultrix.slot1.in[1].audio.ch5, Ultrix.slot1.in[1].audio.ch5, Ultrix.slot1.in[1].audio.ch5, Ultrix.slot1.in[1].audio.ch5, Ultrix.slot1.in[1].audio.ch5, Ultrix.slot1.in[1].audio.ch5
...
...
...
Source 4 CH11,,, Ultrix.slot1.in[1].audio.ch11, Ultrix.slot1.in[1].audio.ch11, Ultrix.slot1.in[1].audio.ch11, Ultrix.slot1.in[1].audio.ch11, Ultrix.slot1.in[1].audio.ch11, Ultrix.slot1.in[1].audio.ch11, Ultrix.slot1.in[1].audio.ch11, Ultrix.slot1.in[1].audio.ch11, Ultrix.slot1.in[1].audio.ch11, Ultrix.slot1.in[1].audio.ch11, Ultrix.slot1.in[1].audio.ch11, Ultrix.slot1.in[1].audio.ch11, Ultrix.slot1.in[1].audio.ch11, Ultrix.slot1.in[1].audio.ch11, Ultrix.slot1.in[1].audio.ch11, Ultrix.slot1.in[1].audio.ch11
Source 4 CH12,,, Ultrix.slot1.in[1].audio.ch12, Ultrix.slot1.in[1].audio.ch12, Ultrix.slot1.in[1].audio.ch12, Ultrix.slot1.in[1].audio.ch12, Ultrix.slot1.in[1].audio.ch12, Ultrix.slot1.in[1].audio.ch12, Ultrix.slot1.in[1].audio.ch12, Ultrix.slot1.in[1].audio.ch12, Ultrix.slot1.in[1].audio.ch12, Ultrix.slot1.in[1].audio.ch12, Ultrix.slot1.in[1].audio.ch12, Ultrix.slot1.in[1].audio.ch12, Ultrix.slot1.in[1].audio.ch12, Ultrix.slot1.in[1].audio.ch12, Ultrix.slot1.in[1].audio.ch12, Ultrix.slot1.in[1].audio.ch12
Source 4 CH13,,, Ultrix.slot1.in[1].audio.ch13, Ultrix.slot1.in[1].audio.ch13, Ultrix.slot1.in[1].audio.ch13, Ultrix.slot1.in[1].audio.ch13, Ultrix.slot1.in[1].audio.ch13, Ultrix.slot1.in[1].audio.ch13, Ultrix.slot1.in[1].audio.ch13, Ultrix.slot1.in[1].audio.ch13, Ultrix.slot1.in[1].audio.ch13, Ultrix.slot1.in[1].audio.ch13, Ultrix.slot1.in[1].audio.ch13, Ultrix.slot1.in[1].audio.ch13, Ultrix.slot1.in[1].audio.ch13, Ultrix.slot1.in[1].audio.ch13, Ultrix.slot1.in[1].audio.ch13, Ultrix.slot1.in[1].audio.ch13
Source 4 CH14,,, Ultrix.slot1.in[1].audio.ch14, Ultrix.slot1.in[1].audio.ch14, Ultrix.slot1.in[1].audio.ch14, Ultrix.slot1.in[1].audio.ch14, Ultrix.slot1.in[1].audio.ch14, Ultrix.slot1.in[1].audio.ch14, Ultrix.slot1.in[1].audio.ch14, Ultrix.slot1.in[1].audio.ch14, Ultrix.slot1.in[1].audio.ch14, Ultrix.slot1.in[1].audio.ch14, Ultrix.slot1.in[1].audio.ch14, Ultrix.slot1.in[1].audio.ch14, Ultrix.slot1.in[1].audio.ch14, Ultrix.slot1.in[1].audio.ch14, Ultrix.slot1.in[1].audio.ch14, Ultrix.slot1.in[1].audio.ch14
Source 4 CH15,,, Ultrix.slot1.in[1].audio.ch15, Ultrix.slot1.in[1].audio.ch15, Ultrix.slot1.in[1].audio.ch15, Ultrix.slot1.in[1].audio.ch15, Ultrix.slot1.in[1].audio.ch15, Ultrix.slot1.in[1].audio.ch15, Ultrix.slot1.in[1].audio.ch15, Ultrix.slot1.in[1].audio.ch15, Ultrix.slot1.in[1].audio.ch15, Ultrix.slot1.in[1].audio.ch15, Ultrix.slot1.in[1].audio.ch15, Ultrix.slot1.in[1].audio.ch15, Ultrix.slot1.in[1].audio.ch15, Ultrix.slot1.in[1].audio.ch15, Ultrix.slot1.in[1].audio.ch15, Ultrix.slot1.in[1].audio.ch15
Source 4 CH16,,, Ultrix.slot1.in[1].audio.ch16, Ultrix.slot1.in[1].audio.ch16, Ultrix.slot1.in[1].audio.ch16, Ultrix.slot1.in[1].audio.ch16, Ultrix.slot1.in[1].audio.ch16, Ultrix.slot1.in[1].audio.ch16, Ultrix.slot1.in[1].audio.ch16, Ultrix.slot1.in[1].audio.ch16, Ultrix.slot1.in[1].audio.ch16, Ultrix.slot1.in[1].audio.ch16, Ultrix.slot1.in[1].audio.ch16, Ultrix.slot1.in[1].audio.ch16, Ultrix.slot1.in[1].audio.ch16, Ultrix.slot1.in[1].audio.ch16, Ultrix.slot1.in[1].audio.ch16, Ultrix.slot1.in[1].audio.ch16

```
## **Help Output**
Available options can be viewed by using the `-h` or `--help` argument.

```
usage: audio_shuffle.py [-h] [-c {2,4,8,16}] [-l LIST] [-o OUTPUT]

optional arguments:
  -h, --help            show this help message and exit
  -c {2,4,8,16}, --channels {2,4,8,16}
                        Number of audio channels. Choose 2, 4, 8, or 16.
  -l LIST, --list LIST  Path or filename with list of sources.
  -o OUTPUT, --output OUTPUT
                        Path or filename of output CSV file.
```

[^csvnote]: Notice that the Ultrix input does NOT include the sdi or audio level information in the csv (.sdi.ch1 or .audio.ch1). This is done to maintain consistency and simplicity. The script only needs to know what input to use.
