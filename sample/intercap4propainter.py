import os
import cv2
import argparse

def process_videos(input_path, output_path, resize_factor=3):
    # Iterate over files in the given directory
    for filename in os.listdir(input_path):
        if filename.endswith(".mp4") and "_mask_obj" not in filename and "_mask_hum" not in filename:
            # Extract base name without extension
            base_name = os.path.splitext(filename)[0]

            # Create main directory for each video
            main_dir = os.path.join(output_path, base_name)
            os.makedirs(main_dir, exist_ok=True)

            # Create subdirectory for frames
            frames_dir = os.path.join(main_dir, base_name)
            os.makedirs(frames_dir, exist_ok=True)

            # Create subdirectory for mask frames
            mask_dir = os.path.join(main_dir, base_name + "_mask")
            os.makedirs(mask_dir, exist_ok=True)

            # Path to original video
            video_path = os.path.join(input_path, filename)

            # Path to mask object video
            mask_obj_path = os.path.join(input_path, base_name + "_mask_obj.mp4")

            # Open original video
            cap = cv2.VideoCapture(video_path)
            count = 1

            # Read frames from original video
            while cap.isOpened():
                ret, frame = cap.read()
                if not ret:
                    break

                # Resize frame
                resized_frame = cv2.resize(frame, (frame.shape[1] // resize_factor, frame.shape[0] // resize_factor))

                # Save resized frame
                frame_path = os.path.join(frames_dir, f"frame{count:04d}.jpg")
                cv2.imwrite(frame_path, resized_frame)

                count += 1

            # Release original video capture
            cap.release()

            # Open mask object video
            cap_mask = cv2.VideoCapture(mask_obj_path)
            count = 1

            # Read frames from mask object video
            while cap_mask.isOpened():
                ret, frame = cap_mask.read()
                if not ret:
                    break

                # Resize frame
                resized_frame = cv2.resize(frame, (frame.shape[1] // resize_factor, frame.shape[0] // resize_factor))

                # Save resized frame
                mask_path = os.path.join(mask_dir, f"frame{count:04d}.jpg")
                cv2.imwrite(mask_path, resized_frame)

                count += 1

            # Release mask object video capture
            cap_mask.release()


def main():
    parser = argparse.ArgumentParser(description="Process videos and masks.")
    parser.add_argument("-i", "--input_path", type=str, default="./data/intercap-video-sample/train", help="Input directory path")
    parser.add_argument("-o", "--output_path", type=str, default="./data/images_for_ppainter", help="Output directory path")
    parser.add_argument("-r", "--resize_factor", type=int, default=3, help="Resize factor")
    args = parser.parse_args()

    process_videos(args.input_path, args.output_path, args.resize_factor)

if __name__ == "__main__":
    main()
