from transformers import BlipProcessor, BlipForConditionalGeneration
from PIL import Image

processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base")

'''
Raw Image/Text
      ↓
Processor
      ↓
Tensors (pixel_values, input_ids)
      ↓
BLIP Model
      ↓
Generated Tokens
      ↓
Processor.decode()
      ↓
Human-readable text

'''
image = Image.open("../test_images/image_1.jpg")
print("Data"+ image)