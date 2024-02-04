from gtts import gTTS
import os
import pygame

# Create a sound file for the given word using Google Text-to-Speech (gTTS).
def create_word_sound(word, language='en'):
    # Ensure the 'sounds' directory exists
    os.makedirs('sounds', exist_ok=True)

    # Create a gTTS object
    tts = gTTS(text=word, lang=language, slow=False)

    # Generate a unique filename based on the word
    filename = f"sounds/{word.lower()}_sound.mp3"

    # Save the audio file
    tts.save(filename)

    return filename
# Play the specified sound file using pygame
def play_sound(sound_file):
    pygame.mixer.init()
    pygame.mixer.music.load(sound_file)
    pygame.mixer.music.play()

    # Wait for the sound to finish playing
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)

if __name__ == "__main__":
    # Example: Take a word as input, generate the corresponding sound, and play it
    user_input = input("Enter a word: ")
    sound_file = create_word_sound(user_input)

    print(f"Sound file created: {sound_file}")

    # Play the sound
    play_sound(sound_file)
