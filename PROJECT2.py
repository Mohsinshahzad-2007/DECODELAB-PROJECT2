import datetime

class CryptographicEngine:
    def __init__(self):
        self.history = []

    def process(self, text, shift, mode='encrypt'):
        # Validate shift range
        if not (1 <= shift <= 25):
            raise ValueError("Shift key must be between 1 and 25.")
            
        shift = shift if mode == 'encrypt' else -shift
        result = "".join([chr((ord(c) - (65 if c.isupper() else 97) + shift) % 26 + (65 if c.isupper() else 97)) 
                          if c.isalpha() else c for c in text])
        
        # Log the operation for audit purposes
        entry = f"[{datetime.datetime.now().strftime('%H:%M:%S')}] {mode.upper()} (Key:{abs(shift)}): '{text}' -> '{result}'"
        self.history.append(entry)
        return result

def main():
    engine = CryptographicEngine()
    while True:
        print("\n--- DECODELABS CRYPTO TOOL v1.0 ---")
        print("1. Encrypt | 2. Decrypt | 3. View History | 4. Delete History | 5. Exit")
        
        choice = input("Select option: ")
        
        if choice in ['1', '2']:
            try:
                data = input("Enter text: ")
                key = int(input("Enter shift key (1-25): "))
                mode = 'encrypt' if choice == '1' else 'decrypt'
                print(f"Result: {engine.process(data, key, mode)}")
            except ValueError as e:
                print(f"Error: {e}")
                
        elif choice == '3':
            print("\n--- AUDIT LOG ---")
            for entry in engine.history: print(entry)
        elif choice == '4':
            engine.history.clear()
            print("History cleared.")
        elif choice == '5':
            break
        else:
            print("Invalid input.")

if __name__ == "__main__":
    main()