def cipher(text, mode):
    result = ""
    # "3" ده المفتاح السري بتاعك
    key = 3 if mode == 'enc' else -3
    for char in text:
        if char.isalpha():
            start = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - start + key) % 26 + start)
        else:
            result += char
    return result

print("--- أداة تشفير مشروع عجينة ---")
choice = input("عايز (1) تشفير ولا (2) فك تشفير؟ ")
msg = input("اكتب الرسالة (بالإنجليزي): ")

if choice == '1':
    print("الرسالة المشفرة: " + cipher(msg, 'enc'))
elif choice == '2':
    print("الرسالة الأصلية: " + cipher(msg, 'dec'))
