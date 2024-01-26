# Character Generator

This Python script generates characters by combining traits (images) from different folders. Each trait should have its own subfolder, and the script will create various combinations of traits to generate characters.

## Prerequisites

- Python 3.x
- Pillow (PIL) library (`pip install pillow`)

## Usage

1. Place trait images in the "input_traits" folder. You can change the input folder name from the script. Each trait should have its own subfolder starting with number underscore. This will be the order in which the different layers will be superimposed. Image files under each trait folder can have any name. 

The script expects the following structure:

input_traits/
├── 1_basebody/
│ ├── body1.png
│ ├── body2.png
│ └── ...
├── 2_hair/
│ ├── hair1.png
│ └── ...
└── ...

2. Run the script using the following command:

```bash
python character_generator.py
```

3. The script will create a timestamped folder inside "output_characters" and save character images and trait information JSON files inside it. The generated structure will look like this:
output_characters/
├── 20220101_120000/
    ├── character_1.png
    ├── character_1_traits.json
    ├── character_2.png
    ├── character_2_traits.json
    └── ...


## Configuration
You can customize the input folder, output parent folder, and supported image formats by modifying the script. 
Make sure to adjust the instructions based on your actual input folder structure and any other specific details about your implementation.