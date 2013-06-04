# coding: utf-8

from trans import Engine, Groups
from config import Config, Translation

# ---------------------------------------------------------------------------------------------------------------------
def translate(text):
    translation = Translation(text, "en", "pt")
    config = Config( translation )

    engine = Engine( config )
    result =  engine.trans()

    groups = Groups( result )
    related = groups.related

    # -----------------------------------------------------------------------------------------------------------------
    print
    print "translation - "+(": ".join(related["simple"]))
    print
    for cls in related["class"]:
        print "class: "+cls

        words = related["class"][ cls ][:-1]
        details = related["class"][ cls ][-1]["details"]

        print "\twords: %s."%("; ".join(words))

        for word in words:
            d = "; ".join(details[word])

            print "\t\t%s >> %s"%(word, d)
    print
# ---------------------------------------------------------------------------------------------------------------------
print "Crt+C to exit..."
print
while True:
    try:
        text = raw_input("Translation [en to pt]: ")
        translate(text.strip() or "empty")
    except KeyboardInterrupt:
        break