positive_words = ["mutlu", "heyecanlı", "sevinçli", "iyiyim", "harika", "sevinçli"]
negative_words = ["üzgün", "sinirli", "korkmuş", "kötüyüm", "mutsuz", "kahrımdım"]
def analyze_mood(text):
    text = text.lower()
    score = 0
    for word in positive_words:
        if word in text:
            score += 1
    for word in negative_words:
        if word in text:
            score -= 1

    if score > 0:
        return "Pozitif 😊 - Harika hissediyorsun!"
    elif score < 0:
        return "Negatif 😞 - Moralin bozuk gibi..."
    else:
        return "Neutral 😐 - Normal bir gün"