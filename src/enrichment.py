import os
import google.generativeai as genai
from PIL import Image

def load_image(image_path: str) -> Image.Image:
    """Loads an image from the specified path."""
    try:
        return Image.open(image_path)
    except Exception as e:
        print(f"Error loading image '{image_path}': {e}")
        return None

def analyze_photo(image_path: str, prompt: str = "Describe this image in detail, including key objects, setting, and mood. Format as JSON with 'description', 'objects', and 'tags' keys.") -> str:
    """Analyzes a photograph using the Gemini API."""
    # Ensure API key is configured
    api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key:
        return "Error: GEMINI_API_KEY environment variable not set. Please set it to use the AI analysis feature."

    genai.configure(api_key=api_key)

    img = load_image(image_path)
    if not img:
        return "Failed to load image."

    try:
        # Using gemini-1.5-flash as the standard multimodal model
        model = genai.GenerativeModel('gemini-1.5-flash')
        response = model.generate_content([prompt, img])
        return response.text
    except Exception as e:
        return f"Error during Gemini API call: {e}"

if __name__ == "__main__":
    print("Multimodal Photo Manager - AI Core Initialized.")
    print("Usage: Import `analyze_photo` to process images with Gemini.")

