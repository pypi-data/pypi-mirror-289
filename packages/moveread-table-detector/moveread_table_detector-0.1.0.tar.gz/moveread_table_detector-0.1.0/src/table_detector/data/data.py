from typing_extensions import TypedDict, Mapping, Sequence
import io
import json
from jaxtyping import Int, Bool
import torch
from torchvision import transforms
from PIL import Image

class Sample(TypedDict):
  img: Int[torch.Tensor, 'H W 1']
  contours: Int[torch.Tensor, 'N 2']

class Batch(TypedDict):
  img: Int[torch.Tensor, 'B H W 1']
  contours: Int[torch.Tensor, 'B N 2']
  mask: Bool[torch.Tensor, 'B N']

preprocess = transforms.Compose([
  transforms.Resize((1024, 1024)),
  transforms.ToTensor(),
])


def parse(sample: Mapping) -> Sample:
  """Parse a sample from the dataset. Expects:
  - `sample['images']`: bytes image
  - `sample['contours']`: JSON string with list of contours (shape N x 4 (x1) x 2)
  """
  img = Image.open(io.BytesIO(sample['images']))
  contours = json.loads(sample['contours'])
  cnts = torch.tensor(contours) / torch.tensor(img.size)
  return { 'img': preprocess(img), 'contours': cnts.view(-1, 8) } # type: ignore


def collate(samples: Sequence[Sample]) -> Batch:
  max_len = max(sample['contours'].size(0) for sample in samples)
  imgs = torch.stack([sample['img'] for sample in samples])  # Shape: (B, H, W, 1)
  
  contours = torch.zeros((len(samples), max_len, 8), dtype=torch.float)
  mask = torch.zeros((len(samples), max_len), dtype=torch.bool)
    
  for i, sample in enumerate(samples):
    l = sample['contours'].shape[0]
    contours[i, :l, :] = sample['contours']  # Copy contours
    mask[i, :l] = True

  return {
    'img': imgs,  # Shape: (B, H, W, 1)
    'contours': contours,  # Shape: (B, N, 2)
    'mask': mask  # Shape: (B, N)
  }