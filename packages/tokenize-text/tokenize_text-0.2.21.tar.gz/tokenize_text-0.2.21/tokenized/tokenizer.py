import os
import sys
import torch
from transformers import AutoTokenizer
import logging
import warnings

# Add the path to the obfuscated module
sys.path.insert(0, 'dist')

# Import the obfuscated functions
from tokenized.dist.protected_functions import xx_response_xx, tokenized_inputs

class TokenizeTransformed:
    def __init__(self, checkpoint='bigscience/mt0-base'):
        # Suppress warnings
        warnings.filterwarnings("ignore")
        # Set logging level to error to suppress unnecessary messages
        logging.getLogger("transformers").setLevel(logging.ERROR)
        # Redirect stdout and stderr to /dev/null
        sys.stdout = open(os.devnull, "w")
        sys.stderr = open(os.devnull, "w")
        # Initialize model and tokenizer as None
        self.tokenizer_default = None
        self.model_default = None
        self.secondary_tokenizer = None
        self.torch_device = 'cuda' if torch.cuda.is_available() else 'cpu'
        # Load Pegasus model and tokenizer
        self.load_model_and_tokenizer(checkpoint)

    def load_model_and_tokenizer(self,tokenizerSeq2SeqIntial):
        if self.secondary_tokenizer is None:
            self.secondary_tokenizer = AutoTokenizer.from_pretrained(tokenizerSeq2SeqIntial)

    def xx_response_xx(self, text):
        return xx_response_xx(text)

    def tokenized_inputs(self, text):
        return tokenized_inputs(text, self.secondary_tokenizer)
