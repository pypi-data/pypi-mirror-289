import torch
import torch.nn as nn

class DynamicQuantizedLayer(nn.Module):
    def __init__(self, layer):
        super(DynamicQuantizedLayer, self).__init__()
        if not isinstance(layer, nn.Module):
            raise TypeError("Layer must be a torch.nn.Module")
        self.layer = layer

    def forward(self, x):
        if not isinstance(x, torch.Tensor):
            raise TypeError("Input must be a torch.Tensor")
        x = x.float()  # Convert input to FloatTensor for quantization
        x = torch.quantize_per_tensor(x, scale=0.1, zero_point=0, dtype=torch.qint8)
        output = self.layer(x.dequantize())  # Dequantize before passing to the model
        
        # Extract the logits from the model's output if available
        if hasattr(output, 'logits'):
            output = output.logits
        
        # Ensure output is a tensor before quantizing
        if not isinstance(output, torch.Tensor):
            raise TypeError("Output must be a torch.Tensor")
        
        return output

    def generate(self, *args, **kwargs):
        return self.layer.generate(*args, **kwargs)