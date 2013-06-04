# coding: utf-8

from translator.config import Config, Translation
from translator import Engine

# ---------------------------------------------------------------------------------------------------------------------
def translate(text):
    translation = Translation(text, "en", "pt")
    config = Config(translation)

    engine = Engine(config)
    related = engine.transl()

    # -----------------------------------------------------------------------------------------------------------------
    print
    print ": ".join(related["simple"])
    print "=" * 20
    for cls in related["class"]:
        print "class: "+cls["name"]
        print " words: %s."%("; ".join(cls["words"]))

        for word in cls["words"]:
            d = "; ".join(cls["details"][word])
            print (" "*2)+"%s = %s"%(word, d)
    print
# ---------------------------------------------------------------------------------------------------------------------
print "Ctr+C to exit..."
print
while True:
    try:
        text = raw_input("Translation [en to pt]: ")
        translate(text.strip() or "empty")
    except KeyboardInterrupt:
        break