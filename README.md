Give it input & output directories.

### For Photos:

Set the maximum height & width.

Run it.

### For Audio:

Set the desired kbps.

Run it.

### For Video

Set desired level of compression.

Run it.

---

#### Structure:

```
iCompress/
│
├── audio/
│ ├── **init**.py
│ └── audio_compress.py
│
├── video/
│ ├── **init**.py
│ └── video_compress.py
│
├── photo/
│ ├── **init**.py
│ └── photo_compress.py
│
└── setup.py
│
└── README.md

```

---

Dependencies: PIL aka pillow (photo), pydub(audio), ffmpeg(video)

---

Ido
