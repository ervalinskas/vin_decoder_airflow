from __future__ import annotations

from pathlib import Path

import loguru
import pandas as pd

from vin_decoder.config import DataConfig


class Extraction:

    def __init__(
        self, data_url: str, raw_file_path: Path, logger: loguru.Logger
    ) -> None:
        self.data_url = data_url
        self.raw_file_path = raw_file_path
        self.logger = logger

    @classmethod
    def from_config(cls, config: DataConfig, logger: loguru.Logger) -> Extraction:
        return cls(
            data_url=config.data_url, raw_file_path=config.raw_file_path, logger=logger
        )

    def extract_data(self):
        vins_df = pd.read_csv(self.data_url)
        self.raw_file_path.parent.mkdir(parents=True, exist_ok=True)
        vins_df.to_csv(self.raw_file_path, index=False)
        self.logger.info(f"✅ VINs saved to - {self.raw_file_path}")
