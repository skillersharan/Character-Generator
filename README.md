# Character Generator

This Python script generates characters by combining traits (images) from different folders. Each trait should have its own subfolder, and the script will create various combinations of traits to generate characters.

## Prerequisites

- Python 3.x
- Pillow (PIL) library (`pip install pillow`)

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
Input traits :

![image](https://github.com/skillersharan/Character-Generator/assets/7269794/4bf53288-6dc3-4abb-91e2-8c99179d70c3)

Example trait

![image](https://github.com/skillersharan/Character-Generator/assets/7269794/57ecb164-de3a-4967-8336-368cecafebc3)



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
Example output : 
![image](https://github.com/skillersharan/Character-Generator/assets/7269794/8cc79ac5-d9a3-4930-bb6f-e5ac221cae87)

Character metadata generated
```JSON
{
  "character_name": "character_1",
  "Bg": "Blue",
  "Body": "outline",
  "Sweater": "Sweater Blue",
  "Hair": "Braid",
  "Eyes": "Annoyed",
  "Earrings": "Berry"
}
```

## Configuration
You can customize the input folder, output parent folder, and supported image formats by modifying the script. 
Make sure to adjust the instructions based on your actual input folder structure and any other specific details about your implementation.
