# coding: utf-8

from trans import Engine, Groups
from config import Config, Translation

# ---------------------------------------------------------------------------------------------------------------------
translation = Translation("look", "en", "pt")
config = Config( translation )

engine = Engine( config )
# ---------------------------------------------------------------------------------------------------------------------

r =  engine.trans()
print r
print
print r[0]
print
print r[1]
print

groups = Groups(r)

print groups.related