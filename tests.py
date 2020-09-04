# coding: utf-8

from translator import Engine


def translate(text):
    engine = Engine(backends=['translator.backends.google_engine'])
    results = engine.translate(text=text,
                               source="pt",
                               target="en")

    for backend in results:
        print "backend: ", backend
        print results


if __name__ == '__main__':
    print "Ctr+C to exit..."
    print
    while True:
        try:
            text = raw_input("Translation [en to pt]: ")
            translate(text.strip() or "empty")
        except KeyboardInterrupt:
            break
