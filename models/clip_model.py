from transformers import CLIPProcessor, CLIPModel
# define text and image embeddings model using CLIP

class CustomCLIPModel:
    def __init__(self):
        self.model = CLIPModel.from_pretrained("openai/clip-vit-base-patch32")
        self.processor = CLIPProcessor.from_pretrained("openai/clip-vit-base-patch32")

    def get_image_embedding(self, image):
        inputs = self.processor(images=image, return_tensors="pt")
        image_features = self.model.get_image_features(**inputs)
        return image_features
    
    def get_text_embedding(self, text):
        inputs = self.processor(text=text, return_tensors="pt", padding=True)
        text_features = self.model.get_text_features(**inputs)
        return text_features