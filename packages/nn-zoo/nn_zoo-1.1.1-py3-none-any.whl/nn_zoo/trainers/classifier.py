import torch
import torch.nn as nn

from lightning import LightningDataModule
from lightning.pytorch import LightningModule
from torchmetrics.functional.classification import accuracy

from nn_zoo.trainers.utils import get_optim, get_scheduler

__all__ = ["ClassifierTrainer"]


class ClassifierTrainer(LightningModule):
    def __init__(
        self,
        model: nn.Module,
        dm: LightningDataModule,
        optim: str,
        optim_kwargs: dict,
        scheduler: str | None = None,
        scheduler_args: dict | None = None,
    ):
        super(ClassifierTrainer, self).__init__()
        self.model = model
        self.dm = dm
        self.optim = get_optim(optim)
        self.optim_kwargs = optim_kwargs
        self.scheduler = get_scheduler(scheduler) if scheduler else None
        self.scheduler_kwargs = scheduler_args if scheduler else None

    def forward(self, *args, **kwargs):
        return self.model(*args, **kwargs)

    def training_step(
        self, batch: tuple[torch.Tensor, torch.Tensor], batch_idx: int
    ) -> torch.Tensor:
        x, y = batch

        preds = self.model(x, y)
        loss = self.model.loss(preds, y)

        self.log("train_loss", loss)
        self.log(
            "train_acc",
            accuracy(
                preds.softmax(1),
                y,
                task="multiclass",
                num_classes=self.dm.num_classes(),
            ),
        )

        return loss

    def validation_step(
        self, batch: tuple[torch.Tensor, torch.Tensor], batch_idx: int
    ) -> torch.Tensor:
        x, y = batch

        preds = self.model(x, y)
        loss = self.model.loss(preds, y)

        self.log("val_loss", loss)
        self.log(
            "val_acc",
            accuracy(
                preds.softmax(1),
                y,
                task="multiclass",
                num_classes=self.dm.num_classes(),
            ),
        )

        return loss

    def test_step(
        self, batch: tuple[torch.Tensor, torch.Tensor], batch_idx: int
    ) -> torch.Tensor:
        x, y = batch

        preds = self.model(x, y)
        loss = self.model.loss(preds, y)

        self.log("test_loss", loss)
        self.log(
            "test_acc",
            accuracy(
                preds.softmax(1),
                y,
                task="multiclass",
                num_classes=self.dm.num_classes(),
            ),
        )

        return loss

    def configure_optimizers(self):
        optimizer = self.optim(self.model.parameters(), **self.optim_kwargs)
        scheduler = (
            self.scheduler(optimizer, **self.scheduler_kwargs)  # type: ignore
            if self.scheduler
            else None
        )

        if scheduler:
            return [optimizer], [scheduler]
        else:
            return optimizer

    def prepare_data(self) -> None:
        self.dm.prepare_data()

    def setup(self, stage):
        if stage == "fit":
            self.dm.setup("fit")
        elif stage == "test":
            self.dm.setup("test")

    def train_dataloader(self):
        return self.dm.train_dataloader()

    def val_dataloader(self):
        return self.dm.val_dataloader()

    def test_dataloader(self):
        return self.dm.test_dataloader()
