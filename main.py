import contentfunctions

option = 1
language = 'fr'

# "en": "English",
# "es": "Spanish",
# "fr": "French",
# "zh-CN": "Chinese (Simplified)",

if option == 1:
    contentfunctions.content_basic_cards(language)

elif option == 2:
    contentfunctions.content_intermediary_cards(language)

elif option == 3:
    contentfunctions.content_advanced_cards()
