from utils import analyze_mood
import random

def load_examples(file_path="examples.txt"):
    """examples.txt dosyasındaki cümleleri yükler"""
    examples = []
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if line and not line.startswith("#"):  # yorum satırlarını atla
                    examples.append(line)
    except FileNotFoundError:
        print("⚠️ examples.txt bulunamadı, sadece manuel girdi kullanılacak.")
    return examples

# Örnekleri yükle
examples = load_examples()

print("📊 TextMood AI Profesyonel Simülasyonu")

while True:
    print("\nSeçenekler:")
    print("1: Manuel cümle gir")
    print("2: examples.txt içinden rastgele cümle test et")
    print("q: Çıkış")

    choice = input("Seçiminiz: ").strip().lower()

    if choice == "q":
        break
    elif choice == "1":
        sentence = input("Cümle yazın: ")
        print(analyze_mood(sentence))
    elif choice == "2":
        if examples:
            sentence = random.choice(examples)
            print("Örnek cümle:", sentence)
            print("AI Tahmini:", analyze_mood(sentence))
        else:
            print("⚠️ examples.txt boş veya bulunamadı.")
    else:
        print("⚠️ Geçersiz seçenek, lütfen tekrar deneyin.")