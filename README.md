# Character Generator

This Python script generates characters by combining traits (images) from different folders. Each trait should have its own subfolder, and the script will create various combinations of traits to generate characters.

## Prerequisites

- Python 3.x
- Install requirements (`pip install -r requirements.txt`)

## Usage

1. Place trait images in the "input_traits" folder. You can change the input folder name from the script. Each trait should have its own subfolder starting with number underscore. This will be the order in which the different layers will be superimposed. Image files under each trait folder can have any name. 

The script expects the following structure:

```bash
input_traits/
├── 1_basebody/
│ ├── body1.png
│ ├── body2.png
│ └── ...
├── 2_hair/
│ ├── hair1.png
│ └── ...
└── ...
```

Example: 

![image](https://github.com/skillersharan/Character-Generator/assets/7269794/2edbc6c6-c510-4a84-a218-7a0f389cdda6)

![image](https://github.com/skillersharan/Character-Generator/assets/7269794/df9b1aa9-caf4-4a14-9488-48331727c353)


2. Run the script using the following command:

```bash
python character_generator.py
```

3. The script will create a timestamped folder inside "output_characters" and save character images and trait information JSON files inside it. The generated structure will look like this:
```bash
output_characters/
├── 20220101_120000/
    ├── character_1.png
    ├── character_1_traits.json
    ├── character_2.png
    ├── character_2_traits.json
    └── ...
```
![image](https://github.com/skillersharan/Character-Generator/assets/7269794/6c1574e1-b462-47ad-852e-04970d8d7789)

Character metadata generated
```JSON
{
  "character_name": "character_1",
  "face": "Brown",
  "mouth": "Sad",
  "eyes": "Eyes",
  "hairstyle": "Afro"
}
```

## Configuration
You can customize the input folder, output parent folder, and supported image formats by modifying the script. 
Make sure to adjust the instructions based on your actual input folder structure and any other specific details about your implementation.
