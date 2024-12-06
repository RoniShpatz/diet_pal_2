from PIL import Image
from io import BytesIO
from django.core.files.base import ContentFile


def crop_and_resize_image(image_file, target_width=300, target_height=300):
    """
    Crop and resize an image to a specific width and height while maintaining aspect ratio.
    
    Args:
    - image_file: The uploaded image file
    - target_width: Desired width of the final image
    - target_height: Desired height of the final image
    
    Returns:
    - Processed image file ready to be saved
    """
    # Open the image using Pillow
    img = Image.open(image_file)
    
    # Calculate the aspect ratio of the original image
    original_width, original_height = img.size
    original_ratio = original_width / original_height
    
    # Calculate target ratio
    target_ratio = target_width / target_height
    
    # Determine crop dimensions
    if original_ratio > target_ratio:
        # Image is wider than target ratio - crop width
        new_width = int(original_height * target_ratio)
        left = (original_width - new_width) // 2
        top = 0
        right = left + new_width
        bottom = original_height
    else:
        # Image is taller than target ratio - crop height
        new_height = int(original_width / target_ratio)
        top = (original_height - new_height) // 2
        left = 0
        right = original_width
        bottom = top + new_height
    
    # Crop the image
    cropped_img = img.crop((left, top, right, bottom))
    
    # Resize to exact target dimensions
    resized_img = cropped_img.resize((target_width, target_height), Image.LANCZOS)
    
    # Save the processed image to a BytesIO object
    output = BytesIO()
    resized_img.save(output, format=img.format, quality=90)
    output.seek(0)
    
    # Create a Django ContentFile from the BytesIO object
    return ContentFile(output.read())

