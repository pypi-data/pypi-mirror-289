from dataclasses import dataclass
from typing import Optional

@dataclass
class JenkinsPlugin:
    shortName: str
    longName: str
    hasUpdate: bool
    enabled: bool
    detached: bool
    downgradable: bool
    url: Optional[str] = ""
    version: Optional[str] = ""
    
    
    def __post_init__(self):
        self.version = str(self.version)
