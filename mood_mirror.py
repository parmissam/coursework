import cv2
from deepface import DeepFace
from customtkinter import *
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import webbrowser

class MusicPlayer:
    def __init__(self, client_id, client_secret):
        self.sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(
            client_id=client_id,
            client_secret=client_secret
        ))

    def play_music_for_emotion(self, emotion):
        emotion_keywords = {
            "happy": "happy upbeat",
            "sad": "sad emotional",
            "angry": "aggressive metal",
            "surprise": "electronic surprise",
            "fear": "dark ambient",
            "neutral": "chill instrumental",
            "disgust": "grunge rock"
        }

        keyword = emotion_keywords.get(emotion.lower(), "mood")
        results = self.sp.search(q=keyword, type='track', limit=1)

        try:
            track = results['tracks']['items'][0]
            url = track['external_urls']['spotify']
            webbrowser.open(url)
        except:
            print(" Could not find track for emotion:", emotion)


class Mood:
    def __init__(self):
        pass

    def capture_face(self):
        cap = cv2.VideoCapture(0)
        ret, frame = cap.read()
        cap.release()
        return frame if ret else None

    def get_emotion(self, img):
        try:
            result = DeepFace.analyze(img, actions=['emotion'], enforce_detection=False)
            return result[0]['dominant_emotion']
        except Exception as e:
            print("Error in emotion detection:", e)
            return "Unknown"

class App:
    def __init__(self, window):
        self.window = window
        self.mood_detector = Mood()
        self.music_player = MusicPlayer(client_id="88af884f0c51426b82364cf1bb69f9b3", client_secret="c697cf06f01c4207b161ac5dda3900c5")
        self.app_setup()  

    def app_setup(self):
        set_appearance_mode("dark")
        self.window.geometry("300x200")
        self.window.title("Mood Detector")
        self.mode_button = CTkButton(master=self.window, text="Detect Emotion", font=('Arial', 20),
                                     corner_radius=32, fg_color="#8A50C8", hover_color="#579CD0",
                                     command=self.detect_mood)
        self.mode_button.place(relx=0.5, rely=0.4, anchor="center")

        self.label = CTkLabel(master=self.window, text="", font=('Arial', 16), text_color="#B8B046")
        self.label.place(relx=0.5, rely=0.6, anchor="center")

    def detect_mood(self):
        img = self.mood_detector.capture_face()
        if img is not None:
            emotion = self.mood_detector.get_emotion(img)
            self.label.configure(text=f"You are feeling: {emotion}")
            self.music_player.play_music_for_emotion(emotion)
        else:
            self.label.configure(text=" Could not capture image.")


if __name__ == '__main__':
    window = CTk()
    app = App(window)
    window.mainloop()
