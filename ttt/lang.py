import os
from pathlib import Path

import i18n
from babel import Locale

LANGS_PATH = Path.cwd() / 'locale'

i18n.load_path.append(str(LANGS_PATH.resolve()))

# HACK GitHub set env LANG = 'C' - crash tests
lang = os.environ.get('LANG', 'en_US')

if lang.lower() == 'c':
    lang = 'en_US'

locale = Locale.parse(lang)
i18n.set('locale', locale.language)
