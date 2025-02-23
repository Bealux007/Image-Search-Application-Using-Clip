import os
from PIL import Image
import torch
from torchvision import transforms
from .clip_model import CustomCLIPModel

class ImageSearch:
    def __init__(self, image_folder):
        """
        Initializes the ImageSearch class with a given image folder.
        Loads images and computes their embeddings for search.
        """
        self.image_folder = image_folder
        self.clip_model = CustomCLIPModel()
        self.image_embeddings = []
        self.image_paths = []
        
        if not os.path.exists(image_folder):
            raise FileNotFoundError(f"Error: Image folder '{image_folder}' not found.")
        
        self._load_images()

    def _load_images(self):
        """
        Loads all images from the specified folder, converts them into embeddings,
        and stores them for future similarity searches.
        """
        transform = transforms.Compose([
            transforms.Resize((224, 224)),
            transforms.ToTensor(),
        ])

        image_files = os.listdir(self.image_folder)
        if not image_files:
            raise ValueError("Error: No images found in the specified folder.")

        for image_name in image_files:
            image_path = os.path.join(self.image_folder, image_name)
            
            try:
                image = Image.open(image_path).convert("RGB")  # Ensure image is in RGB format
                image_tensor = transform(image).unsqueeze(0)  # Convert to tensor & add batch dimension
                
                # Compute image embedding
                image_embedding = self.clip_model.get_image_embedding(image_tensor)
                self.image_embeddings.append(image_embedding)
                self.image_paths.append(image_path)

            except Exception as e:
                print(f"Warning: Skipping {image_name} due to an error: {e}")

        # Combine embeddings into a single tensor
        if self.image_embeddings:
            self.image_embeddings = torch.cat(self.image_embeddings)
        else:
            raise RuntimeError("Error: No valid image embeddings were generated.")

    def search_by_text(self, text, top_k=3):
        """
        Searches for the most relevant images based on a given text query.
        Returns the top_k most similar image paths.
        """
        if not text.strip():
            raise ValueError("Error: Text query cannot be empty.")

        text_embedding = self.clip_model.get_text_embedding(text)
        similarities = torch.matmul(text_embedding, self.image_embeddings.T)
        top_k_indices = similarities.topk(top_k).indices[0]

        return [self.image_paths[i] for i in top_k_indices]

    def search_by_image(self, image, top_k=3):
        """
        Searches for the most relevant images based on a given image.
        Returns the top_k most similar image paths.
        """
        transform = transforms.Compose([
            transforms.Resize((224, 224)),
            transforms.ToTensor(),
        ])

        try:
            image_tensor = transform(image).unsqueeze(0)  # Convert to tensor & add batch dimension
            image_embedding = self.clip_model.get_image_embedding(image_tensor)

            similarities = torch.matmul(image_embedding, self.image_embeddings.T)
            top_k_indices = similarities.topk(top_k).indices[0]

            return [self.image_paths[i] for i in top_k_indices]

        except Exception as e:
            raise RuntimeError(f"Error: Unable to process the uploaded image. {e}")
