import os
import json
from PIL import Image, ImageDraw
from datetime import datetime
from tqdm import tqdm  # Import tqdm for progress bar

def collect_trait_images(trait_folder, supported_formats):
    trait_images = []
    trait_name = os.path.basename(trait_folder)

    # Collect images for each trait
    for file in os.listdir(trait_folder):
        if any(file.lower().endswith(format) for format in supported_formats):
            image_path = os.path.join(trait_folder, file)
            img = Image.open(image_path)
            trait_images.append((trait_name, img))  # Store both trait name and image object

    return trait_images

def generate_characters(input_folder, output_parent_folder, supported_formats):
    # Collect trait folders
    trait_folders = [f.path for f in sorted(os.scandir(input_folder), key=lambda x: int(x.name.split("_")[0])) if f.is_dir()]

    # Count the total number of traits to be generated
    total_traits = sum(len([file for file in os.listdir(trait_folder) if any(file.lower().endswith(format) for format in supported_formats)]) for trait_folder in trait_folders)

    # Generate a timestamped folder for output
    timestamp_folder = datetime.now().strftime("%Y%m%d_%H%M%S")
    output_folder = os.path.join(output_parent_folder, timestamp_folder)
    os.makedirs(output_folder, exist_ok=True)

    # Set up tqdm progress bar
    print("Total traits: " + str(total_traits))
    # Initialize trait combinations
    trait_combinations = [[]]

    # Iterate over trait folders
    for trait_folder in trait_folders:
        trait_images = collect_trait_images(trait_folder, supported_formats)

        # Update trait combinations with new trait images
        trait_combinations = [combo + [trait_image] for combo in trait_combinations for trait_image in trait_images]


    # Set up tqdm progress bar for character generation
    progress_bar = tqdm(total=len(trait_combinations), desc="Generating Characters", unit="character")
    start_time = datetime.now()

    # Generate characters based on trait combinations
    for i, combination in enumerate(trait_combinations):
        # Create a new image for the character
        output_image = Image.new("RGBA", combination[0][1].size, (255, 255, 255, 0))

        # Combine trait images as layers
        for trait_name, img in combination:
            output_image = Image.alpha_composite(output_image, img.convert("RGBA"))

        # Save character image
        character_name = f"character_{i+1}"
        output_image.save(os.path.join(output_folder, f"{character_name}.png"))

        # Create JSON file for trait information
        json_data = {"character_name": character_name}
        json_data.update({trait_name.split("_", 1)[1].replace(" ", "_").lower(): os.path.splitext(os.path.basename(img.filename))[0].replace(" ", "_").lower() for trait_name, img in combination})
        # Save trait information as JSON
        json_path = os.path.join(output_folder, f"{character_name}_traits.json")
        with open(json_path, 'w') as json_file:
            json.dump(json_data, json_file, indent=2)

        # Increment progress bar
        progress_bar.update(1)

    # Close the tqdm progress bar
    progress_bar.close()

    end_time = datetime.now()
    total_time = (end_time - start_time).total_seconds()

    print(f"Completed in {total_time:.2f} seconds")

if __name__ == "__main__":
    # Config variables
    input_folder = "input_traits"
    output_parent_folder = "output_characters"
    supported_formats = ['.png','.gif', '.svg']

    os.makedirs(output_parent_folder, exist_ok=True)  # Ensure the existence of the output parent folder
    generate_characters(input_folder, output_parent_folder, supported_formats)
