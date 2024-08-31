# ReadPaper

This Project is using OpenAI API to transfer text into speech.

Help user to pay more attention on articles !

## Get Start
### Step 1
Create a file named .env and structed as following.
```python
#.env
API_KEY="{ Replace here with your own API key from openai }"
ARTICLE="{your alticle title}" 
OUTPUT = "./output"
INPUT="./input"
```

### Step 2
Install required python packages.
``` shell
$> pip install -r requirements.txt
```

### Step 3
Create folders / Preprocessing files.

At this step it will create folder structure if not yet existed.

``` shell
$> python preprocess.py
```

### Step 4
At this step, it will generate some mp3 files through OpenAI.

``` shell
$> python readPaper.py
```