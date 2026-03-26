def cipher(text, shift, mode):
    result = ""
    key = shift if mode == 'enc' else -shift
    for char in text:
        if char.isalpha():
            start = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - start + key) % 26 + start)
        else:
            result += char
    return result

print("--- خزنة Agina المشفرة ---")
try:
    user_key = int(input("اكتب رقمك السري: "))
    choice = input("عايز (1) تشفير ولا (2) فك تشفير؟ ")
    msg = input("اكتب الرسالة: ")
    
    output = cipher(msg, user_key, 'enc' if choice == '1' else 'dec')
    print("النتيجة: " + output)

    # الجزء الجديد: حفظ النتيجة في ملف vault.txt
    with open("vault.txt", "a") as file:
        file.write(f"Key: {user_key} | Result: {output}\n")
    print("✅ تم حفظ النتيجة في ملف vault.txt")

except ValueError:
    print("خطأ: لازم تكتب رقم!")

