import os
import pandas as pd
from PIL import Image
import tensorflow as tf
from pkg_resources import resource_filename

def list_available_datasets():
    """
    List all available datasets in the library's data folder.
    :return: List of dataset filenames.
    """
    data_dir = resource_filename(__name__, 'data')
    
    if not os.path.exists(data_dir):
        return []
    
    datasets = []
    # List all CSV files
    datasets += [f[:-4] for f in os.listdir(data_dir) if f.endswith('.csv')]
    # List all directories (image datasets)
    datasets += [d for d in os.listdir(data_dir) if os.path.isdir(os.path.join(data_dir, d))]
    
    return datasets

def load_dataset(dataset_name, as_tensorflow_dataset=False):
    """
    Load a specified dataset (tabular or image) from the library's data folder.
    :param dataset_name: Name of the dataset (e.g., 'iris' or 'flipkart').
    :param as_tensorflow_dataset: Whether to return images as a TensorFlow dataset.
    :return: DataFrame for tabular data, TensorFlow dataset for images, or a list of images.
    """
    # Determine the base data path
    data_dir = resource_filename(__name__, 'data')
    
    # Check if it's an image dataset (directory)
    image_dir = os.path.join(data_dir, dataset_name)
    if os.path.exists(image_dir) and os.path.isdir(image_dir):
        image_paths = [os.path.join(image_dir, img_name) for img_name in os.listdir(image_dir) if img_name.endswith(('.jpg', '.png'))]
        
        if not image_paths:
            print(f"No image files found in the directory: {image_dir}")
            return None

        if as_tensorflow_dataset:
            # Load images as TensorFlow dataset
            def load_image(img_path):
                img = tf.io.read_file(img_path)
                img = tf.image.decode_image(img, channels=3)
                img = tf.image.resize(img, [224, 224])  # Resize images if needed
                img = tf.cast(img, tf.float32) / 255.0  # Normalize to [0, 1] range
                return img
            
            image_ds = tf.data.Dataset.from_tensor_slices(image_paths)
            image_ds = image_ds.map(load_image)
            return image_ds
        else:
            # Load images as PIL objects
            images = [Image.open(img_path) for img_path in image_paths]
            return images
    
    # If the dataset is not found
    available_datasets = list_available_datasets()
    print(f"Dataset '{dataset_name}' was not found.")
    print("Available datasets:")
    for dataset in available_datasets:
        print(f" - {dataset}")
    return None

