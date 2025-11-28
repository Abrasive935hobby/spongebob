# Step 1 — Encrypt plaintext.txt
with open("plaintext.txt", "r", encoding="utf-8") as f:
    plaintext = f.read()

step = int(input("Enter shift value (1–26): "))

ciphertext = ""
for ch in plaintext:
    if 'a' <= ch <= 'z':
        base = ord('a')
        offset = ord(ch) - base
        ciphertext += chr(base + ((offset + step) % 26))
    elif 'A' <= ch <= 'Z':
        base = ord('A')
        offset = ord(ch) - base
        ciphertext += chr(base + ((offset + step) % 26))
    else:
        ciphertext += ch

with open("ciphertext.txt", "w", encoding="utf-8") as f:
    f.write(ciphertext)

# Step 2 — Decrypt with known step
decrypted = ""
for ch in ciphertext:
    if 'a' <= ch <= 'z':
        base = ord('a')
        offset = ord(ch) - base
        decrypted += chr(base + ((offset - step) % 26))
    elif 'A' <= ch <= 'Z':
        base = ord('A')
        offset = ord(ch) - base
        decrypted += chr(base + ((offset - step) % 26))
    else:
        decrypted += ch

with open("decrypted_known_step.txt", "w", encoding="utf-8") as f:
    f.write(decrypted)

# Step 3 — Brute-force decryption
words = set()
with open("dictionary.txt", "r", encoding="utf-8") as f:
    for line in f:
        words.add(line.strip().lower())

best_match = 0
best_step = None
best_text = ""

for s in range(1, 26):
    candidate = ""
    for ch in ciphertext:
        if 'a' <= ch <= 'z':
            base = ord('a')
            offset = ord(ch) - base
            candidate += chr(base + ((offset - s) % 26))
        elif 'A' <= ch <= 'Z':
            base = ord('A')
            offset = ord(ch) - base
            candidate += chr(base + ((offset - s) % 26))
        else:
            candidate += ch

    match_count = 0
    for word in candidate.split():
        if word.lower() in words:
            match_count += 1

    if match_count > best_match:
        best_match = match_count
        best_step = s
        best_text = candidate

with open("decrypted_bruteforce.txt", "w", encoding="utf-8") as f:
    f.write(f"Best shift found: {best_step}\n\n")
    f.write(best_text)

# Reflection:
# 1. Encryption turns readable text into unreadable text using a rule or key. Decryption reverses that process and turns it back into readable text.

# 2. Method B (using ord/chr) is superior because it works directly with the real Unicode/ASCII code values of characters, avoids long lookup lists and handles shifts more efficiently and cleanly.

# 3. The script preserves all non-alphabetic characters correctly, including spaces, punctuation, numbers, and symbols.

# 4. A brute-force attack breaks a Caesar cipher easily because there are only 25 possible shifts to try, so a computer can test all of them quickly and detect which one produces real words.

# 5. The part that helped me understand text processing the most was using ord() and chr() to convert characters to numbers and back, because it showed how text is manipulated at a low level.
