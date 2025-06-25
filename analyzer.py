from zxcvbn import zxcvbn
import argparse

leet_dict = {
    'a': ['4', '@'],
    'e': ['3'],
    'i': ['1', '!'],
    'o': ['0'],
    's': ['$', '5'],
    't': ['7']
}

def analyze_password(password):
    results = zxcvbn(password)
    score = results['score']
    feedback = results['feedback']['suggestions']
    print(f"\nPassword: {password}")
    print(f"Score (0-4): {score}")
    print("Feedback:", feedback or "Strong password!")

def generate_variants(base):
    variants = set()
    for word in base:
        for i in range(0, 100):
            variants.add(word + str(i))
        variants.add(word + "123")
        variants.add(word + "2025")
        leet = ''.join(leet_dict.get(c, [c])[0] if c in leet_dict else c for c in word)
        variants.add(leet)
    return variants

def main():
    parser = argparse.ArgumentParser(description="Password Strength Analyzer + Wordlist Generator")
    parser.add_argument('--analyze', help="Analyze a password's strength")
    parser.add_argument('--genwordlist', action='store_true', help="Generate custom wordlist")
    parser.add_argument('--inputs', nargs='+', help="Personal info like name, pet, dob")
    parser.add_argument('--output', help="Output filename for wordlist (.txt)")
    args = parser.parse_args()

    if args.analyze:
        analyze_password(args.analyze)

    if args.genwordlist and args.inputs:
        wordlist = generate_variants(args.inputs)
        filename = args.output or "custom_wordlist.txt"
        with open(filename, "w") as f:
            for word in wordlist:
                f.write(word + "\n")
        print(f"[+] Wordlist saved to {filename}")

if __name__ == "__main__":
    main()
