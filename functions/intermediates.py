def struturecard(level, components):
    cards = []

    if level == 'basic':
        for i in range(0, len(components.frontcard)):
            if components.newword[i] in components.frontcard[i]:
                components.frontcard[i] = components.frontcard[i].replace(components.newword[i],
                                                                          f'<b>{components.newword[i]}</b>')

            components.frontcard[i] += '<div>[sound:' + components.audio[i] + ']</div>'

            if components.translatedword[i] in components.backcard[i]:
                components.backcard[i] = components.backcard[i].replace(components.translatedword[i],
                                                                        f'<b>{components.translatedword[i]}</b>')
        cards.append(components.frontcard)
        cards.append(components.backcard)

    if level == 'intermediary':
        for i in range(0, len(components.frontcard)):
            if components.newword[i] in components.frontcard[i]:
                components.frontcard[i] = components.frontcard[i].replace(components.newword[i],
                                                                          f'<b>{components.newword[i]}</b>')

            components.frontcard[i] += '<div>[sound:' + components.audio[i] + ']</div>'
            components.backcard.append(f'<b>{components.newword[i]} {components.pron_fon_w[i]}</b><br>'
                                       f'{components.sentido[i]} {components.translatedword[i]}')
        cards.append(components.frontcard)
        cards.append(components.backcard)

    if level == 'advanced':
        pass

    return cards
