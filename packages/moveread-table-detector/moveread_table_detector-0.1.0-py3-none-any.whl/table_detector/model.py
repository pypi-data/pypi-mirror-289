from jaxtyping import Int, Float, Bool
from torch import nn, Tensor
from torch.nn import TransformerDecoder, TransformerDecoderLayer
from torchvision.models import resnet18
from table_detector import Batch

def loss(
  *, y_pred: Float[Tensor, 'B N 8'],
  y_true: Float[Tensor, 'B N 8'],
  mask: Bool[Tensor, 'B N'],
  loss_fn = nn.SmoothL1Loss(reduction='none')
):
  mask = mask[..., None].expand(-1, -1, 8)
  loss = loss_fn(y_pred, y_true)
  loss = loss * mask
  return loss.sum() / mask.sum()

class BoxDetector(nn.Module):
  def __init__(self, input_size=1024, num_decoder_layers=6, d_model=512, nhead=8):
    super().__init__()

    self.input_size = input_size

    # Pretrained ResNet Backbone
    resnet = resnet18(pretrained=True)
    self.backbone = nn.Sequential(
      *list(resnet.children())[:-2]  # Remove the last FC and AvgPool layers
    )
    
    # Reduce the output channels from ResNet to match d_model
    self.conv1x1 = nn.Conv2d(512, d_model, kernel_size=1)

    self.embedding = nn.Linear(8, d_model)
    # Transformer Decoder
    decoder_layer = TransformerDecoderLayer(d_model=d_model, nhead=nhead)
    self.transformer_decoder = TransformerDecoder(decoder_layer, num_layers=num_decoder_layers)
    
    # Fully Connected layers to output box coordinates
    self.fc = nn.Linear(d_model, 8)  # (x1, y1, x2, y2, x3, y3, x4, y4)

  def forward(
    self, *, image: Int[Tensor, 'B H W 1'],
    contours: Float[Tensor, 'B N 8'],
    mask: Bool[Tensor, 'B N']
  ) -> Float[Tensor, 'B N 8']:
    # Pass input through ResNet backbone
    x = self.backbone(image)  # Shape: (B, 2048, 32, 32)
    x = self.conv1x1(x)  # Shape: (B, d_model, 32, 32)
    x = x.flatten(2)  # Shape: (B, d_model, 32*32)
    x = x.permute(2, 0, 1)  # Shape: (32*32, B, d_model)
    tgt = self.embedding(contours)  # Shape: (B, N, d_model)
    tgt = tgt.permute(1, 0, 2)  # Shape: (N, B, d_model)
    x = self.transformer_decoder(tgt, x, tgt_key_padding_mask=~mask)  # Shape: (N, B, d_model)
    
    # Predict corner coordinates for each box
    x = self.fc(x)  # Shape: (N, B, 8)
    
    return x.permute(1, 0, 2)  # Shape: (B, N, 8)
  
  def predict(self, batch: Batch) -> Float[Tensor, 'B N 8']:
    return self(image=batch['img'], contours=batch['contours'], mask=batch['mask'])