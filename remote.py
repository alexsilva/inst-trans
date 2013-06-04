# coding: utf-8

# ---------------------------------------------------------------------------------------------------------------------
class Remote(object):
    """
    Guard source parameters translation.
    """

    source = "https://translate.google.com.br/translate_a/t"

    _params = [
        ("client", 't'),
        ("hl", 'pt-BR'), ## page locale
        ("sl", ''),      ## source translation
        ("tl", ''),      ## translation language
        ("q",  ''),      ## query translation
        ("ie", 'UTF-8'),
        ("oe", 'UTF-8'),
        ("multires", 1),
        ("prev", 'btn'),
        ("ssel", 0),
        ("tsel", 0),
        ("sc", 1)
    ]

    opts = [
        ('af', 'Afrikaans'),
        ('sq', 'Albanian'),
        ('ar', 'Arabic'),
        ('hy', 'Armenian'),
        ('az', 'Azerbaijani'),
        ('eu', 'Basque'),
        ('be', 'Belarusian'),
        ('bn', 'Bengali'),
        ('bs', 'Bosnian'),
        ('bg', 'Bulgarian'),
        ('ca', 'Catalan'),
        ('ceb', 'Cebuano'),
        ('zh-CN', 'Chinese (Simplified)'),
        ('zh-TW', 'Chinese (Traditional)'),
        ('hr', 'Croatian'),
        ('cs', 'Czech'),
        ('da', 'Danish'),
        ('nl', 'Dutch'),
        ('eo', 'Esperanto'),
        ('et', 'Estonian'),
        ('tl', 'Filipino'),
        ('fi', 'Finnish'),
        ('fr', 'French'),
        ('gl', 'Galician'),
        ('ka', 'Georgian'),
        ('de', 'German'), ('el', 'Greek'),
        ('gu', 'Gujarati'),
        ('ht', 'Haitian Creole'),
        ('iw', 'Hebrew'),
        ('hi', 'Hindi'),
        ('hmn', 'Hmong'),
        ('hu', 'Hungarian'),
        ('is', 'Icelandic'),
        ('id', 'Indonesian'),
        ('ga', 'Irish'),
        ('it', 'Italian'),
        ('ja', 'Japanese'),
        ('jw', 'Javanese'),
        ('kn', 'Kannada'),
        ('km', 'Khmer'),
        ('ko', 'Korean'),
        ('lo', 'Lao'),
        ('la', 'Latin'), ('lv', 'Latvian'),
        ('lt', 'Lithuanian'),
        ('mk', 'Macedonian'),
        ('ms', 'Malay'),
        ('mt', 'Maltese'),
        ('mr', 'Marathi'),
        ('no', 'Norwegian'),
        ('fa', 'Persian'),
        ('pl', 'Polish'),
        ('pt', 'Portuguese'),
        ('ro', 'Romanian'),
        ('ru', 'Russian'),
        ('sr', 'Serbian'),
        ('sk', 'Slovak'),
        ('sl', 'Slovenian'),
        ('es', 'Spanish'),
        ('sw', 'Swahili'),
        ('sv', 'Swedish'),
        ('ta', 'Tamil'),
        ('te', 'Telugu'),
        ('th', 'Thai'),
        ('tr', 'Turkish'),
        ('uk', 'Ukrainian'),
        ('ur', 'Urdu'),
        ('vi', 'Vietnamese'),
        ('cy', 'Welsh'),
        ('yi', 'Yiddish')
    ]

    @property
    def params(self):
        return dict(self._params)
