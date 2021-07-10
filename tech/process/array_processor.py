import json
from io import TextIOWrapper
from typing import List

from tech.entities.processed_lingo import ProcessedLingo
from tech.process.lingo_processor import LingoProcessor


class LingoArrayProcessor(LingoProcessor):
    def __init__(self):
        self.lingos: List[ProcessedLingo] = list()

    def process(self, processed: ProcessedLingo):
        self.lingos.append(processed)
