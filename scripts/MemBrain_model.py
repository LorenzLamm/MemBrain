import torch
from torch.nn import functional as F
from torch import nn
from pytorch_lightning.core.lightning import LightningModule
from torch.optim import Adam


class MemBrain_model(LightningModule):
    def __init__(self, box_range):
        super().__init__()
        self.box_range = box_range
        self.conv1 = nn.Conv3d(1, 32, (3, 3, 3), stride=1, padding=0, dilation=1, groups=1, bias=True,
                                     padding_mode='zeros')
        self.conv1b = nn.Conv3d(32, 32, (3, 3, 3), stride=1, padding=1, dilation=1, groups=1, bias=True,
                                      padding_mode='zeros')
        self.conv2 = nn.Conv3d(32, 32, (3, 3, 3), stride=1, padding=0, dilation=1, groups=1, bias=True,
                                     padding_mode='zeros')
        self.conv2b = nn.Conv3d(32, 32, (3, 3, 3), stride=1, padding=1, dilation=1, groups=1, bias=True,
                                      padding_mode='zeros')
        self.mlp_fac = int((self.box_range * 2 - 4) ** 3 / 2)
        self.batchnorm1 = torch.nn.BatchNorm3d(32)
        self.batchnorm2 = torch.nn.BatchNorm3d(32)
        self.batchnorm3 = torch.nn.BatchNorm3d(32)
        self.batchnorm4 = torch.nn.BatchNorm3d(32)
        self.mlp1 = torch.nn.Linear(self.mlp_fac * 64, 1)

    def forward(self, x):
        x = x.float()
        x = self.conv1(x)
        x = self.batchnorm1(x)
        x = F.relu(x)
        x = self.conv1b(x)
        x = self.batchnorm2(x)
        x = F.relu(x)
        x = self.conv2(x)
        x = self.batchnorm3(x)
        x = F.relu(x)
        x = self.conv2b(x)
        x = self.batchnorm4(x)
        x = F.relu(x)
        x = x.view(-1, self.mlp_fac * 64)
        x = self.mlp1(x)
        return x

    def training_step(self, batch, batch_idx):
        x, y = batch
        y = y.float()
        logits = self(x)
        loss = F.mse_loss(logits, y)
        self.log("Train_Loss", loss)
        return loss

    def validation_step(self, batch, batch_idx):
        x, y = batch
        y = y.float()
        logits = self(x)
        loss = F.mse_loss(logits, y)
        self.log("Val_Loss", loss)
        return loss

    def configure_optimizers(self):
        return Adam(self.parameters(), lr=1e-5)