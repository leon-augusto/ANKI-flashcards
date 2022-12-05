import gtts

def gen_audios(phrases, language):
    list_files = []
    for phrase in phrases:
        tts = gtts.gTTS(phrase, lang=language)
        file_name = phrase.replace('.', '').lower().replace(' ', '-')[:] + '.mp3'
        tts.save(file_name)
        list_files.append(file_name)
    return list_files
