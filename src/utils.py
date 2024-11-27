import torch
import numpy as np

def tensor_to_image(tensor):
    """Convert a tensor to numpy image"""
    image = tensor.cpu().clone()
    image = image.squeeze(0)
    image = image.numpy()
    image = image.transpose(1, 2, 0)
    image = image * 0.5 + 0.5
    image = np.clip(image, 0, 1)
    return image

def load_model(model_path):
    """Load a pretrained model"""
    try:
        model = torch.load(model_path)
        return model
    except Exception as e:
        print(f"Error loading model: {e}")
        return None