from transformers import AutoTokenizer, AutoModel
import torch


# Load CodeBERT model
tokenizer = AutoTokenizer.from_pretrained("microsoft/codebert-base")
model = AutoModel.from_pretrained("microsoft/codebert-base")


def get_code_embedding(code):

    # Convert code into tokens
    inputs = tokenizer(code, return_tensors="pt", truncation=True)

    # Pass through CodeBERT model
    outputs = model(**inputs)

    # Average token embeddings
    embedding = outputs.last_hidden_state.mean(dim=1)

    return embedding.detach().numpy()