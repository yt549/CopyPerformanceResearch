# Problem

Engineers at QwickType Software found they spend so much time copying and pasting code
that they decided to build their own text editor to speed up their development workflow.
After implementing their editor they found it was even slower than what they had before. They
have given you their current text processing logic and have tasked you with reimplementing it
with a focus on performance.

# What I have done:
1. Analysis different approach to copy and paste the *.py files in "CopyFrom" folder to "CopyTo" folder;
2. Measure the time efficiency for each approach
3. Clear out the "CopyTo" directory after each measurement
4. Output the best approach ranking according to each time consumption
5. Use PySimpleGUI to create a interface. input: outsource/inputsource directory

# Conclusion:
Research on different approach:
1. shutil copyfile():  0:00:00.013696
2. shutil CopyObj():  0:00:00.007557
3. thread:  0:00:00.014585
4. muliple process:  0:00:00.056398

In general:
the best performance to worst performance:  ['shutil copyfile()', 'shutil CopyObj()', 'thread', 'muliple process']

Due to focus on time efficiency, I test five different approach copy & paste, the best one is CopyFile() from shutil package. The GUI can extend to any specifc type of files. Users only need to specify the In/Out directory and then the selected type of file would be transferred!


Even though I only measuring copy python files efficiency, the code can quickly adapt to measure other type/size files!

## Installation

PySimpleGUI
```
pip install pysimplegui
or
pip3 install pysimplegui
```

### Makes This Window

![image](https://github.com/yt549/CopyPerformanceResearch/blob/master/GUI.png)

## Usage

```python
import sys
import shutil
from threading import Thread
from datetime import datetime
import os
import glob
from multiprocessing import Process
import subprocess
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.
Please make sure to update tests as appropriate.
