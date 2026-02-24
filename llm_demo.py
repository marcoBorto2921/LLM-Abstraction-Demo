
---

# 🐍 llm_demo.py

```python
from abc import ABC, abstractmethod
import random

# --- 1. Abstract class ---
class LLMProvider(ABC):
    """Abstract interface for any language model."""

    @abstractmethod
    def train(self, data):
        """Train the model on the given dataset."""
        pass

    @abstractmethod
    def predict(self, prompt):
        """Make predictions using the model."""
        pass

# --- 2. Concrete implementations with simulated training ---
class GPTProvider(LLMProvider):
    def __init__(self):
        self.knowledge = {}

    def train(self, data):
        print("Training GPT model with data...")
        for i, text in enumerate(data):
            # Simulate learning by reversing the text
            self.knowledge[i] = text[::-1]
        print("GPT training complete!\n")

    def predict(self, prompt):
        if not self.knowledge:
            return "Model not trained yet!"
        key = random.choice(list(self.knowledge.keys()))
        return f"GPT response to '{prompt}': {self.knowledge[key]}"

class GeminiProvider(LLMProvider):
    def __init__(self):
        self.memory = []

    def train(self, data):
        print("Training Gemini model with data...")
        # Simulate learning by storing text lengths
        self.memory = [len(text) for text in data]
        print("Gemini training complete!\n")

    def predict(self, prompt):
        if not self.memory:
            return "Model not trained yet!"
        avg_len = sum(self.memory) // len(self.memory)
        return f"Gemini response to '{prompt}': generated length ~{avg_len}"

# --- 3. Agnostic function ---
def ask_model(model: LLMProvider, prompt: str):
    """Use any model through the abstract interface."""
    return model.predict(prompt)

# --- 4. Example usage ---
if __name__ == "__main__":
    training_data = [
        "Hello world",
        "This is an example of training data",
        "Machine learning is fun"
    ]
    prompt = "Hi, how are you?"

    # Use GPT
    gpt_model = GPTProvider()
    gpt_model.train(training_data)
    print(ask_model(gpt_model, prompt))

    # Switch to Gemini without changing any logic
    gemini_model = GeminiProvider()
    gemini_model.train(training_data)
    print(ask_model(gemini_model, prompt))
