# **Audio Breakaway Labels for Ultrix Database**

This is a short, simple script that will take a list of source names and output a CSV of the audio breakouts.

The GUI interface is pretty simple. It asks for a source list filename, a number of audio channels, and an output filename. Once all of those are provided, just hit the `Go` button and it should provide a CSV file depending on the data structure of the input file. More on that below.

![image](https://user-images.githubusercontent.com/19508086/123015888-099cff00-d38f-11eb-8156-769ed0e8111a.png)

## **Input Data Structure**

Data can be input as a list of sources as a txt file or a table of source names and input ports as a csv. Follow the below structures to ensure consistent output.

### *List Input*

If you have a list of input names, you can just put each name on a new line in a standard text file. The script will then output a csv of those names appended with audio channels numbers.

Input File:

```txt
Source 1
Source 2
Source 3
Source 4
```

Output File:

```csv
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

The CSV input will take a source name and an Ultrix input in the format `name.slotnumber.in[input number]`. For example: `Ultrix.slot1.in[1]`. The script will then create an output file that closely matches the layout of an Ultrix database.

Notice that the CSV input does NOT include the Ultrix sdi or audio level information in the list (`.sdi.ch1` or `.audio.ch1`). This is done to maintain consistency and simplicity. The script only needs to know what input to use.

Input File:

```csv
Source 1,Ultrix.slot1.in[1]
Source 2,Ultrix.slot1.in[2]
Source 3,Ultrix.slot1.in[3]
Source 4,Ultrix.slot1.in[4]
```

Output File:

```csv
Name,Description,Video,Audio 1,Audio 2,Audio 3,Audio 4,Audio 5,Audio 6,Audio 7,Audio 8,Audio 9,Audio 10,Audio 11,Audio 12,Audio 13,Audio 14,Audio 15,Audio 16
Source 1 CH01,,,Ultrix.slot1.in[1].audio.ch1,Ultrix.slot1.in[1].audio.ch1,Ultrix.slot1.in[1].audio.ch1,Ultrix.slot1.in[1].audio.ch1,Ultrix.slot1.in[1].audio.ch1,Ultrix.slot1.in[1].audio.ch1,Ultrix.slot1.in[1].audio.ch1,Ultrix.slot1.in[1].audio.ch1,Ultrix.slot1.in[1].audio.ch1,Ultrix.slot1.in[1].audio.ch1,Ultrix.slot1.in[1].audio.ch1,Ultrix.slot1.in[1].audio.ch1,Ultrix.slot1.in[1].audio.ch1,Ultrix.slot1.in[1].audio.ch1,Ultrix.slot1.in[1].audio.ch1,Ultrix.slot1.in[1].audio.ch1
Source 1 CH02,,,Ultrix.slot1.in[1].audio.ch2,Ultrix.slot1.in[1].audio.ch2,Ultrix.slot1.in[1].audio.ch2,Ultrix.slot1.in[1].audio.ch2,Ultrix.slot1.in[1].audio.ch2,Ultrix.slot1.in[1].audio.ch2,Ultrix.slot1.in[1].audio.ch2,Ultrix.slot1.in[1].audio.ch2,Ultrix.slot1.in[1].audio.ch2,Ultrix.slot1.in[1].audio.ch2,Ultrix.slot1.in[1].audio.ch2,Ultrix.slot1.in[1].audio.ch2,Ultrix.slot1.in[1].audio.ch2,Ultrix.slot1.in[1].audio.ch2,Ultrix.slot1.in[1].audio.ch2,Ultrix.slot1.in[1].audio.ch2
Source 1 CH03,,,Ultrix.slot1.in[1].audio.ch3,Ultrix.slot1.in[1].audio.ch3,Ultrix.slot1.in[1].audio.ch3,Ultrix.slot1.in[1].audio.ch3,Ultrix.slot1.in[1].audio.ch3,Ultrix.slot1.in[1].audio.ch3,Ultrix.slot1.in[1].audio.ch3,Ultrix.slot1.in[1].audio.ch3,Ultrix.slot1.in[1].audio.ch3,Ultrix.slot1.in[1].audio.ch3,Ultrix.slot1.in[1].audio.ch3,Ultrix.slot1.in[1].audio.ch3,Ultrix.slot1.in[1].audio.ch3,Ultrix.slot1.in[1].audio.ch3,Ultrix.slot1.in[1].audio.ch3,Ultrix.slot1.in[1].audio.ch3
Source 1 CH04,,,Ultrix.slot1.in[1].audio.ch4,Ultrix.slot1.in[1].audio.ch4,Ultrix.slot1.in[1].audio.ch4,Ultrix.slot1.in[1].audio.ch4,Ultrix.slot1.in[1].audio.ch4,Ultrix.slot1.in[1].audio.ch4,Ultrix.slot1.in[1].audio.ch4,Ultrix.slot1.in[1].audio.ch4,Ultrix.slot1.in[1].audio.ch4,Ultrix.slot1.in[1].audio.ch4,Ultrix.slot1.in[1].audio.ch4,Ultrix.slot1.in[1].audio.ch4,Ultrix.slot1.in[1].audio.ch4,Ultrix.slot1.in[1].audio.ch4,Ultrix.slot1.in[1].audio.ch4,Ultrix.slot1.in[1].audio.ch4
Source 1 CH05,,,Ultrix.slot1.in[1].audio.ch5,Ultrix.slot1.in[1].audio.ch5,Ultrix.slot1.in[1].audio.ch5,Ultrix.slot1.in[1].audio.ch5,Ultrix.slot1.in[1].audio.ch5,Ultrix.slot1.in[1].audio.ch5,Ultrix.slot1.in[1].audio.ch5,Ultrix.slot1.in[1].audio.ch5,Ultrix.slot1.in[1].audio.ch5,Ultrix.slot1.in[1].audio.ch5,Ultrix.slot1.in[1].audio.ch5,Ultrix.slot1.in[1].audio.ch5,Ultrix.slot1.in[1].audio.ch5,Ultrix.slot1.in[1].audio.ch5,Ultrix.slot1.in[1].audio.ch5,Ultrix.slot1.in[1].audio.ch5
...
...
...
Source 4 CH11,,,Ultrix.slot1.in[4].audio.ch11,Ultrix.slot1.in[4].audio.ch11,Ultrix.slot1.in[4].audio.ch11,Ultrix.slot1.in[4].audio.ch11,Ultrix.slot1.in[4].audio.ch11,Ultrix.slot1.in[4].audio.ch11,Ultrix.slot1.in[4].audio.ch11,Ultrix.slot1.in[4].audio.ch11,Ultrix.slot1.in[4].audio.ch11,Ultrix.slot1.in[4].audio.ch11,Ultrix.slot1.in[4].audio.ch11,Ultrix.slot1.in[4].audio.ch11,Ultrix.slot1.in[4].audio.ch11,Ultrix.slot1.in[4].audio.ch11,Ultrix.slot1.in[4].audio.ch11,Ultrix.slot1.in[4].audio.ch11
Source 4 CH12,,,Ultrix.slot1.in[4].audio.ch12,Ultrix.slot1.in[4].audio.ch12,Ultrix.slot1.in[4].audio.ch12,Ultrix.slot1.in[4].audio.ch12,Ultrix.slot1.in[4].audio.ch12,Ultrix.slot1.in[4].audio.ch12,Ultrix.slot1.in[4].audio.ch12,Ultrix.slot1.in[4].audio.ch12,Ultrix.slot1.in[4].audio.ch12,Ultrix.slot1.in[4].audio.ch12,Ultrix.slot1.in[4].audio.ch12,Ultrix.slot1.in[4].audio.ch12,Ultrix.slot1.in[4].audio.ch12,Ultrix.slot1.in[4].audio.ch12,Ultrix.slot1.in[4].audio.ch12,Ultrix.slot1.in[4].audio.ch12
Source 4 CH13,,,Ultrix.slot1.in[4].audio.ch13,Ultrix.slot1.in[4].audio.ch13,Ultrix.slot1.in[4].audio.ch13,Ultrix.slot1.in[4].audio.ch13,Ultrix.slot1.in[4].audio.ch13,Ultrix.slot1.in[4].audio.ch13,Ultrix.slot1.in[4].audio.ch13,Ultrix.slot1.in[4].audio.ch13,Ultrix.slot1.in[4].audio.ch13,Ultrix.slot1.in[4].audio.ch13,Ultrix.slot1.in[4].audio.ch13,Ultrix.slot1.in[4].audio.ch13,Ultrix.slot1.in[4].audio.ch13,Ultrix.slot1.in[4].audio.ch13,Ultrix.slot1.in[4].audio.ch13,Ultrix.slot1.in[4].audio.ch13
Source 4 CH14,,,Ultrix.slot1.in[4].audio.ch14,Ultrix.slot1.in[4].audio.ch14,Ultrix.slot1.in[4].audio.ch14,Ultrix.slot1.in[4].audio.ch14,Ultrix.slot1.in[4].audio.ch14,Ultrix.slot1.in[4].audio.ch14,Ultrix.slot1.in[4].audio.ch14,Ultrix.slot1.in[4].audio.ch14,Ultrix.slot1.in[4].audio.ch14,Ultrix.slot1.in[4].audio.ch14,Ultrix.slot1.in[4].audio.ch14,Ultrix.slot1.in[4].audio.ch14,Ultrix.slot1.in[4].audio.ch14,Ultrix.slot1.in[4].audio.ch14,Ultrix.slot1.in[4].audio.ch14,Ultrix.slot1.in[4].audio.ch14
Source 4 CH15,,,Ultrix.slot1.in[4].audio.ch15,Ultrix.slot1.in[4].audio.ch15,Ultrix.slot1.in[4].audio.ch15,Ultrix.slot1.in[4].audio.ch15,Ultrix.slot1.in[4].audio.ch15,Ultrix.slot1.in[4].audio.ch15,Ultrix.slot1.in[4].audio.ch15,Ultrix.slot1.in[4].audio.ch15,Ultrix.slot1.in[4].audio.ch15,Ultrix.slot1.in[4].audio.ch15,Ultrix.slot1.in[4].audio.ch15,Ultrix.slot1.in[4].audio.ch15,Ultrix.slot1.in[4].audio.ch15,Ultrix.slot1.in[4].audio.ch15,Ultrix.slot1.in[4].audio.ch15,Ultrix.slot1.in[4].audio.ch15
Source 4 CH16,,,Ultrix.slot1.in[4].audio.ch16,Ultrix.slot1.in[4].audio.ch16,Ultrix.slot1.in[4].audio.ch16,Ultrix.slot1.in[4].audio.ch16,Ultrix.slot1.in[4].audio.ch16,Ultrix.slot1.in[4].audio.ch16,Ultrix.slot1.in[4].audio.ch16,Ultrix.slot1.in[4].audio.ch16,Ultrix.slot1.in[4].audio.ch16,Ultrix.slot1.in[4].audio.ch16,Ultrix.slot1.in[4].audio.ch16,Ultrix.slot1.in[4].audio.ch16,Ultrix.slot1.in[4].audio.ch16,Ultrix.slot1.in[4].audio.ch16,Ultrix.slot1.in[4].audio.ch16,Ultrix.slot1.in[4].audio.ch16
```

Table Representation:

| Name          | Description | Video | Audio 1                       | Audio 2                       | Audio 3                       | Audio 4                       | Audio 5                       | Audio 6                       | Audio 7                       | Audio 8                       | Audio 9                       | Audio 10                      | Audio 11                      | Audio 12                      | Audio 13                      | Audio 14                      | Audio 15                      | Audio 16                      |
| ------------- | ----------- | ----- | ----------------------------- | ----------------------------- | ----------------------------- | ----------------------------- | ----------------------------- | ----------------------------- | ----------------------------- | ----------------------------- | ----------------------------- | ----------------------------- | ----------------------------- | ----------------------------- | ----------------------------- | ----------------------------- | ----------------------------- | ----------------------------- |
| Source 1 CH01 |             |       | Ultrix.slot1.in[1].audio.ch1  | Ultrix.slot1.in[1].audio.ch1  | Ultrix.slot1.in[1].audio.ch1  | Ultrix.slot1.in[1].audio.ch1  | Ultrix.slot1.in[1].audio.ch1  | Ultrix.slot1.in[1].audio.ch1  | Ultrix.slot1.in[1].audio.ch1  | Ultrix.slot1.in[1].audio.ch1  | Ultrix.slot1.in[1].audio.ch1  | Ultrix.slot1.in[1].audio.ch1  | Ultrix.slot1.in[1].audio.ch1  | Ultrix.slot1.in[1].audio.ch1  | Ultrix.slot1.in[1].audio.ch1  | Ultrix.slot1.in[1].audio.ch1  | Ultrix.slot1.in[1].audio.ch1  | Ultrix.slot1.in[1].audio.ch1  |
| Source 1 CH02 |             |       | Ultrix.slot1.in[1].audio.ch2  | Ultrix.slot1.in[1].audio.ch2  | Ultrix.slot1.in[1].audio.ch2  | Ultrix.slot1.in[1].audio.ch2  | Ultrix.slot1.in[1].audio.ch2  | Ultrix.slot1.in[1].audio.ch2  | Ultrix.slot1.in[1].audio.ch2  | Ultrix.slot1.in[1].audio.ch2  | Ultrix.slot1.in[1].audio.ch2  | Ultrix.slot1.in[1].audio.ch2  | Ultrix.slot1.in[1].audio.ch2  | Ultrix.slot1.in[1].audio.ch2  | Ultrix.slot1.in[1].audio.ch2  | Ultrix.slot1.in[1].audio.ch2  | Ultrix.slot1.in[1].audio.ch2  | Ultrix.slot1.in[1].audio.ch2  |
| Source 1 CH03 |             |       | Ultrix.slot1.in[1].audio.ch3  | Ultrix.slot1.in[1].audio.ch3  | Ultrix.slot1.in[1].audio.ch3  | Ultrix.slot1.in[1].audio.ch3  | Ultrix.slot1.in[1].audio.ch3  | Ultrix.slot1.in[1].audio.ch3  | Ultrix.slot1.in[1].audio.ch3  | Ultrix.slot1.in[1].audio.ch3  | Ultrix.slot1.in[1].audio.ch3  | Ultrix.slot1.in[1].audio.ch3  | Ultrix.slot1.in[1].audio.ch3  | Ultrix.slot1.in[1].audio.ch3  | Ultrix.slot1.in[1].audio.ch3  | Ultrix.slot1.in[1].audio.ch3  | Ultrix.slot1.in[1].audio.ch3  | Ultrix.slot1.in[1].audio.ch3  |
| Source 1 CH04 |             |       | Ultrix.slot1.in[1].audio.ch4  | Ultrix.slot1.in[1].audio.ch4  | Ultrix.slot1.in[1].audio.ch4  | Ultrix.slot1.in[1].audio.ch4  | Ultrix.slot1.in[1].audio.ch4  | Ultrix.slot1.in[1].audio.ch4  | Ultrix.slot1.in[1].audio.ch4  | Ultrix.slot1.in[1].audio.ch4  | Ultrix.slot1.in[1].audio.ch4  | Ultrix.slot1.in[1].audio.ch4  | Ultrix.slot1.in[1].audio.ch4  | Ultrix.slot1.in[1].audio.ch4  | Ultrix.slot1.in[1].audio.ch4  | Ultrix.slot1.in[1].audio.ch4  | Ultrix.slot1.in[1].audio.ch4  | Ultrix.slot1.in[1].audio.ch4  |
| Source 1 CH05 |             |       | Ultrix.slot1.in[1].audio.ch5  | Ultrix.slot1.in[1].audio.ch5  | Ultrix.slot1.in[1].audio.ch5  | Ultrix.slot1.in[1].audio.ch5  | Ultrix.slot1.in[1].audio.ch5  | Ultrix.slot1.in[1].audio.ch5  | Ultrix.slot1.in[1].audio.ch5  | Ultrix.slot1.in[1].audio.ch5  | Ultrix.slot1.in[1].audio.ch5  | Ultrix.slot1.in[1].audio.ch5  | Ultrix.slot1.in[1].audio.ch5  | Ultrix.slot1.in[1].audio.ch5  | Ultrix.slot1.in[1].audio.ch5  | Ultrix.slot1.in[1].audio.ch5  | Ultrix.slot1.in[1].audio.ch5  | Ultrix.slot1.in[1].audio.ch5  |
| ...           |             |       |                               |                               |                               |                               |                               |                               |                               |                               |                               |                               |                               |                               |                               |                               |                               |                               |
| ...           |             |       |                               |                               |                               |                               |                               |                               |                               |                               |                               |                               |                               |                               |                               |                               |                               |                               |
| ...           |             |       |                               |                               |                               |                               |                               |                               |                               |                               |                               |                               |                               |                               |                               |                               |                               |                               |
| Source 4 CH11 |             |       | Ultrix.slot1.in[4].audio.ch11 | Ultrix.slot1.in[4].audio.ch11 | Ultrix.slot1.in[4].audio.ch11 | Ultrix.slot1.in[4].audio.ch11 | Ultrix.slot1.in[4].audio.ch11 | Ultrix.slot1.in[4].audio.ch11 | Ultrix.slot1.in[4].audio.ch11 | Ultrix.slot1.in[4].audio.ch11 | Ultrix.slot1.in[4].audio.ch11 | Ultrix.slot1.in[4].audio.ch11 | Ultrix.slot1.in[4].audio.ch11 | Ultrix.slot1.in[4].audio.ch11 | Ultrix.slot1.in[4].audio.ch11 | Ultrix.slot1.in[4].audio.ch11 | Ultrix.slot1.in[4].audio.ch11 | Ultrix.slot1.in[4].audio.ch11 |
| Source 4 CH12 |             |       | Ultrix.slot1.in[4].audio.ch12 | Ultrix.slot1.in[4].audio.ch12 | Ultrix.slot1.in[4].audio.ch12 | Ultrix.slot1.in[4].audio.ch12 | Ultrix.slot1.in[4].audio.ch12 | Ultrix.slot1.in[4].audio.ch12 | Ultrix.slot1.in[4].audio.ch12 | Ultrix.slot1.in[4].audio.ch12 | Ultrix.slot1.in[4].audio.ch12 | Ultrix.slot1.in[4].audio.ch12 | Ultrix.slot1.in[4].audio.ch12 | Ultrix.slot1.in[4].audio.ch12 | Ultrix.slot1.in[4].audio.ch12 | Ultrix.slot1.in[4].audio.ch12 | Ultrix.slot1.in[4].audio.ch12 | Ultrix.slot1.in[4].audio.ch12 |
| Source 4 CH13 |             |       | Ultrix.slot1.in[4].audio.ch13 | Ultrix.slot1.in[4].audio.ch13 | Ultrix.slot1.in[4].audio.ch13 | Ultrix.slot1.in[4].audio.ch13 | Ultrix.slot1.in[4].audio.ch13 | Ultrix.slot1.in[4].audio.ch13 | Ultrix.slot1.in[4].audio.ch13 | Ultrix.slot1.in[4].audio.ch13 | Ultrix.slot1.in[4].audio.ch13 | Ultrix.slot1.in[4].audio.ch13 | Ultrix.slot1.in[4].audio.ch13 | Ultrix.slot1.in[4].audio.ch13 | Ultrix.slot1.in[4].audio.ch13 | Ultrix.slot1.in[4].audio.ch13 | Ultrix.slot1.in[4].audio.ch13 | Ultrix.slot1.in[4].audio.ch13 |
| Source 4 CH14 |             |       | Ultrix.slot1.in[4].audio.ch14 | Ultrix.slot1.in[4].audio.ch14 | Ultrix.slot1.in[4].audio.ch14 | Ultrix.slot1.in[4].audio.ch14 | Ultrix.slot1.in[4].audio.ch14 | Ultrix.slot1.in[4].audio.ch14 | Ultrix.slot1.in[4].audio.ch14 | Ultrix.slot1.in[4].audio.ch14 | Ultrix.slot1.in[4].audio.ch14 | Ultrix.slot1.in[4].audio.ch14 | Ultrix.slot1.in[4].audio.ch14 | Ultrix.slot1.in[4].audio.ch14 | Ultrix.slot1.in[4].audio.ch14 | Ultrix.slot1.in[4].audio.ch14 | Ultrix.slot1.in[4].audio.ch14 | Ultrix.slot1.in[4].audio.ch14 |
| Source 4 CH15 |             |       | Ultrix.slot1.in[4].audio.ch15 | Ultrix.slot1.in[4].audio.ch15 | Ultrix.slot1.in[4].audio.ch15 | Ultrix.slot1.in[4].audio.ch15 | Ultrix.slot1.in[4].audio.ch15 | Ultrix.slot1.in[4].audio.ch15 | Ultrix.slot1.in[4].audio.ch15 | Ultrix.slot1.in[4].audio.ch15 | Ultrix.slot1.in[4].audio.ch15 | Ultrix.slot1.in[4].audio.ch15 | Ultrix.slot1.in[4].audio.ch15 | Ultrix.slot1.in[4].audio.ch15 | Ultrix.slot1.in[4].audio.ch15 | Ultrix.slot1.in[4].audio.ch15 | Ultrix.slot1.in[4].audio.ch15 | Ultrix.slot1.in[4].audio.ch15 |
| Source 4 CH16 |             |       | Ultrix.slot1.in[4].audio.ch16 | Ultrix.slot1.in[4].audio.ch16 | Ultrix.slot1.in[4].audio.ch16 | Ultrix.slot1.in[4].audio.ch16 | Ultrix.slot1.in[4].audio.ch16 | Ultrix.slot1.in[4].audio.ch16 | Ultrix.slot1.in[4].audio.ch16 | Ultrix.slot1.in[4].audio.ch16 | Ultrix.slot1.in[4].audio.ch16 | Ultrix.slot1.in[4].audio.ch16 | Ultrix.slot1.in[4].audio.ch16 | Ultrix.slot1.in[4].audio.ch16 | Ultrix.slot1.in[4].audio.ch16 | Ultrix.slot1.in[4].audio.ch16 | Ultrix.slot1.in[4].audio.ch16 | Ultrix.slot1.in[4].audio.ch16 |
