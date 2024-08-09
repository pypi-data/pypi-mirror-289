import numpy as np
import matplotlib.pyplot as plt


def normalize_image(image: np.ndarray) -> np.ndarray:
    """
    Normalize the image for display, regardless of the value range.

    This function adjusts the image data to a standard range for display purposes.
    It handles different data types and scales the image values accordingly.

    Args:
        image (np.ndarray): The input image as a NumPy array.

    Returns:
        np.ndarray: The normalized image.
    """
    # Check the data type and normalize accordingly
    if image.dtype == np.uint16:
        # For 16-bit unsigned integer images, scale to the range [0, 1]
        image = image.astype(np.float32) / 65535.0
    elif image.dtype == np.float32:
        # For floating-point images, clip values to the range [0, 1]
        image = np.clip(image, 0, 1)
    else:
        # For other data types, normalize to the range [0, 1]
        image = image.astype(np.float32)
        image_min = np.min(image)
        image_max = np.max(image)
        # Avoid division by zero if the image has a uniform value
        if image_max > image_min:
            image = (image - image_min) / (image_max - image_min)
        else:
            image = np.zeros_like(image)

    return image


def display_multiband_tiffs(image1: np.ndarray, image2: np.ndarray) -> None:
    """
    Display two TIFF images with appropriate normalization and visualization.

    This function displays two images side by side. It handles different numbers of channels and normalizes
    the images for better visualization. It supports single-channel, multi-channel (e.g., RGB), and images
    with more than three channels.

    Args:
        image1 (np.ndarray): The first image as a NumPy array (HxWxC or HxW).
        image2 (np.ndarray): The second image as a NumPy array (HxWxC or HxW).

    Returns:
        None
    """
    plt.figure(figsize=(10, 5))

    # Normalize images for display
    image1 = normalize_image(image1)
    image2 = normalize_image(image2)

    plt.subplot(1, 2, 1)
    plt.title('Image 1')
    if image1.ndim == 3:
        if image1.shape[2] == 1:
            # Display single-channel image as grayscale
            plt.imshow(image1[:, :, 0], cmap='gray')
        if image1.shape[2] == 2:
            # Display  a two-channel image
            plt.imshow(image1[:, :, :1])
        elif image1.shape[2] == 3:
            # Display RGB image
            plt.imshow(image1)
        else:
            # Display the first three channels of an image with more than 3 channels
            img_to_show = image1[:, :, :3]
            # Normalize data for better visualization
            img_to_show = (img_to_show - np.min(img_to_show)) / (np.max(img_to_show) - np.min(img_to_show))
            plt.imshow(img_to_show)
    elif image1.ndim == 2:
        # Display grayscale image
        plt.imshow(image1, cmap='gray')
    plt.axis('off')

    # Display Image 2
    plt.subplot(1, 2, 2)
    plt.title('Image 2')
    if image2.ndim == 3:
        if image2.shape[2] == 1:
            # Display single-channel image as grayscale
            plt.imshow(image2[:, :, 0], cmap='gray')
        if image2.shape[2] == 2:
            # Display a two-channel image
            plt.imshow(image2[:, :, :1])
        elif image2.shape[2] == 3:
            # Display RGB image
            plt.imshow(image2)
        else:
            # Display the first three channels of an image with more than 3 channels
            img_to_show = image2[:, :, :3]
            # Normalize data for better visualization
            img_to_show = (img_to_show - np.min(img_to_show)) / (np.max(img_to_show) - np.min(img_to_show))
            plt.imshow(img_to_show)
    elif image2.ndim == 2:
        # Display grayscale image
        plt.imshow(image2, cmap='gray')
    plt.axis('off')

    plt.show()