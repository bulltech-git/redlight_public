# 🔴 Red Light For Your Vision - Public Audio Assets

This repository hosts the high-fidelity audio soundscapes and meditation tracks used in the **Red Light For Your Vision** app on **iOS** and **visionOS** (Apple Vision Pro).

By hosting our asset library here, we ensure the main application remains lightweight (~30MB) while offering users a diverse, high-quality selection of relaxation audio via on-demand downloading.

## 📱 Download the App
Experience the full immersive therapy session with physics-based interactions and spatial audio.

[**📲 Download on the App Store**](https://apps.apple.com/app/id6449202094) *(Replace this with your actual App Store Link)*

---

## 🎧 Audio Library & Sources

The soundscapes in this collection are curated to enhance **Red Light Therapy**, **4-7-8 Breathing**, and **Deep Relaxation** sessions.

We gratefully acknowledge the talented creators at **[Pixabay](https://pixabay.com/)** for providing the majority of these royalty-free audio assets. Their community enables developers to create immersive wellness experiences.

### Track List (Manifest)

| Filename | Type | Description | Source |
| :--- | :--- | :--- | :--- |
| `binaural_40hz.mp3` | Focus | Gamma waves for mental clarity. | Pixabay |
| `rain_sounds.mp3` | Nature | Heavy rain for white noise isolation. | Pixabay |
| `ocean_waves.mp3` | Nature | Rhythmic waves for breathing sync. | Pixabay |
| `forest_ambience.mp3` | Nature | Birds and wind for grounding. | Pixabay |
| `white_noise.mp3` | Sleep | Pure static for blocking distractions. | Pixabay |
| `silence.mp3` | Utility | Zero-byte track for pure silent mode. | Internal |

---

## 🛠 For Developers: How it Works

The app utilizes a custom **Download Manager** that interfaces with this repository:

1.  **Manifest Automation:** A GitHub Action automatically scans this repository for `.mp3`, `.m4a`, and `.wav` files.
2.  **JSON Generation:** It generates a `music.json` file listing all available tracks.
3.  **Client-Side Fetching:** The iOS/visionOS app fetches this JSON to display the latest available music without requiring an App Store update.

### Adding New Tracks
To add new music to the app:
1.  Upload a valid audio file to the `main` branch.
2.  The GitHub Action will auto-update the manifest.
3.  Users will see the new track appear in the "Soundscape" card instantly.

---

## 📄 License & Attribution

* **Code:** The source code/scripts in this repository are proprietary to **BullTech**.
* **Audio:** Audio files are sourced from **Pixabay** under their [Content License](https://pixabay.com/service/license/) (Royalty-Free) or are proprietary internal assets.
    * *If you are a copyright holder and believe a file is here in error, please open an Issue.*

---

**Keywords:** *Red Light Therapy, Apple Vision Pro, visionOS, iOS, Relaxation, Meditation, 670nm, Binaural Beats, Mindful Minutes, HealthKit, Spatial Audio, SwiftUI.*
