import gettext
import os

import locale

languages = [locale.getlocale()[0], 'en_US']

current_path = os.path.dirname(os.path.abspath(__file__))
t = gettext.translation('messages', os.path.join(current_path, "locale"), languages=languages, fallback=True)
i18n = t.gettext
