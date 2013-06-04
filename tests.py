# coding: utf-8

from trans import Engine
from config import Config, Translation

# ---------------------------------------------------------------------------------------------------------------------
translation = Translation("book", "en", "pt")
config = Config( translation )

engine = Engine( config )
# ---------------------------------------------------------------------------------------------------------------------

print engine.trans()