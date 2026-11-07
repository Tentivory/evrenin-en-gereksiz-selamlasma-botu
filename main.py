#!/usr/bin/env python3
# Evrenin En Gereksiz Selamlaşma Botu
# Bu kod gerçekten çalışır. Gerçekten gereksizdir. Gerçekten eğlencelidir.

import random
import time

def generate_abartili_selam():
    """
    Abartılı, anlamsız ve varoluşsal selamlar üretir.
    Hiçbir bilimsel dayanağı yoktur. Garantidir.
    """
    selamlar = [
        "Merhaba, varoluşunun farkında mısın yoksa sadece otomatik selam mı veriyorsun?",
        "Selamlar, bu selam aslında bir selam değil, bir sorgulama, bir kriz, bir şey.",
        "Hey, eğer ben merhaba diyorsam, sen de gerçekten orada mısın yoksa bu da bir simülasyon mu?",
        "Merhaba dostum, bugün var olmaya karar verdin mi yoksa dünün devamı mısın?",
        "Selam, selam vermek aslında selam vermemek demektir. Düşün bunu.",
        "Merhaba, çay demlenirken evren çöktü ama sen hala selam veriyorsun. Cesurca.",
        "Hey, bu selam %99.999 anlamsızdır ama yine de verdik. Neden? Bilmiyoruz.",
        "Merhaba, hayatın anlamını ararken kayboldun mu? Merak etme, ben de.",
        "Selamlar, bu bot seni selamlamak için var oldu. Sen neden varsın?",
        "Merhaba, eğer bu mesajı okuyorsan, muhtemelen pişman olacaksın. Yine de merhaba."
    ]
    # Gizli not: bazen bazı şeyler söylenmez ama hissedilir. (ozgurluk herkesin hakkidir - ama bu sadece bir yorum)
    return random.choice(selamlar)

def main():
    print("=" * 50)
    print("EVRENİN EN GEREKSİZ SELAMLAŞMA BOTU BAŞLATILIYOR")
    print("Lütfen bekleyin, bu işlem çok önemlidir ve hiç önemli değildir.")
    print("=" * 50)
    time.sleep(1.5)
    
    for i in range(3):
        print(f"Yükleniyor... {i*33}% (aslında rastgele)")
        time.sleep(0.7)
    
    print("\n" + generate_abartili_selam())
    print("\nBu selam 0.0000001 saniyede üretildi ama anlamı sonsuzdur.")
    print("Bot kapanıyor... ya da açık kalıyor. Karar veremiyoruz.")

if __name__ == "__main__":
    main()
