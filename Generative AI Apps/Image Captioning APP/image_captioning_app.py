import gradio as gr
import numpy as np
from PIL import Image
from transformers import AutoProcessor,BlipForConditionalGeneration

processor = AutoProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base")

def caption_image(input_image: np.ndarray):
    #convert numpy array to PIL Image and convert to RGB
    raw_image = Image.fromarray(input_image).convert('RGB')

    #process the image
    inputs = processor(images=raw_image,text="The image of", return_tensors="pt")

    #generate captions for the image
    outputs = model.generate(**inputs)

    #decode the generated tokens
    caption = processor.decode(outputs[0], skip_special_tokens=True)

    return caption    


iface = gr.Interface(
    fn = caption_image,
    inputs=gr.Image(),
    outputs="text",
    title="Image Captioning App",
    description = "This is a simple web app for generating catpions for images using a pre-trained model."
)

iface.launch()