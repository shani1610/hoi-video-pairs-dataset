#!/bin/bash

cd ProPainter

# Define the input directory containing subdirectories
input_video_dir="./../data/pairs/original"
input_mask_frames_dirs="./../data/pairs/original_mask_frames"
output_dir="./../data/pairs/inpainted"

# Loop through each file in the input directory
for file in "$input_video_dir"/*; do
    # Extract the base name of the file without the extension
    file_name=$(basename "$file" .mp4)

    # Print the name of the file being processed
    echo "Processing file: $file_name"

    # Print the mask frames directory being checked
    mask_frames_dir="$input_mask_frames_dirs/$file_name"
    echo "Checking if directory exists: $mask_frames_dir"

    # Check if the corresponding mask frames directory exists
    if [ -d "$mask_frames_dir" ]; then
        echo "Directory exists: $mask_frames_dir"
        # Run inference_propainter.py script with appropriate arguments
        python inference_propainter.py \
            -i "$input_video_dir/$file_name.mp4" \
            -m "$mask_frames_dir" \
            -o "$output_dir/$file_name"
    else
        echo "Directory does not exist: $mask_frames_dir"
    fi
done

cd ..

#chmod +x ./scripts/ppainter_intercap.sh
#./scripts/ppainter_intercap.sh
