import joblib
from happytransformer import HappyTextToText
from happytransformer import TTSettings

# Load trained model
model_path = 'models/happy_tt.pkl'
happy_tt = joblib.load(model_path)

def fix_sentence(input_sentence):
    # Fix the input sentence using the trained model
    beam_settings =  TTSettings(min_length=1, max_length=20)
    corrected_sentence = happy_tt.generate_text(input_sentence, args = beam_settings)
    return corrected_sentence.text

def main():
    while True:
        # Get user input
        user_input = input("Enter a sentence to be corrected (press 'q' to quit): ")

        if user_input.lower() == 'q':
            print("Exiting...")
            break

        # Fix the user input sentence
        corrected_sentence = fix_sentence(user_input)

        # Print the corrected sentence
        print("Corrected sentence:", corrected_sentence)

if __name__ == "__main__":
    main()
