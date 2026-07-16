# 🎵 Music Recommender Simulation

## Project Summary

In this project you will build and explain a small music recommender system.

Your goal is to:

- Represent songs and a user "taste profile" as data
- Design a scoring rule that turns that data into recommendations
- Evaluate what your system gets right and wrong
- Reflect on how this mirrors real world AI recommenders

Replace this paragraph with your own summary of what your version does.

---

## How The System Works

- Song features: each Song has a genre, mood, energy, tempo_bpm, valence, danceability, and acousticness, taken from songs.csv.

- UserProfile stores what the user likes: a favorite_genre, a favorite_mood, a target_energy (the energy level they want, not just "high" or "low"), and likes_acoustic (true or false).

- Scoring: for each song, score_song() checks four things and adds them up with different weights:

- Mood match (0.35) — 1 point if the song's mood matches the favorite, 0 if not
Energy closeness (0.30) — how close the song's energy is to the target energy
Genre match (0.20) — 1 point if the song's genre matches the favorite, 0 if not
Acoustic fit (0.15) — rewards high acousticness if the user likes acoustic, low acousticness if not

score = 0.35(mood) + 0.30(energy) + 0.20(genre) + 0.15(acoustic)
Mood counts the most, then energy, then genre and acoustic fit as smaller tie-breakers.

- Choosing songs: recommend_songs() scores every song, sorts them from highest to lowest, and returns the top k.

- Possible biases:

Close matches score the same as no match at all. Genre and mood only give points for an exact match. A song that's almost the right genre gets the same score (0) as a song that's nothing like it.
Telling songs apart depends on luck, not real understanding. Once a song isn't the exact favorite genre or mood, all the scoring comes from energy and acoustic fit alone. This only works well if energy and acoustic values happen to line up with genre in the data. Two very different songs (like intense rock and moody synthwave) could end up with almost the same score if their energy and acoustic values are similar.


## Getting Started

### Setup

1. Create a virtual environment (optional but recommended):

   ```bash
   python -m venv .venv
   source .venv/bin/activate      # Mac or Linux
   .venv\Scripts\activate         # Windows

2. Install dependencies

```bash
pip install -r requirements.txt
```

3. Run the app:

```bash
python -m src.main
```

### Running Tests

Run the starter tests with:

```bash
pytest
```

You can add more tests in `tests/test_recommender.py`.

---

## Sample Recommendation Output

Example run using the profile `{"genre": "pop", "mood": "happy", "energy": 0.8}`:

```
==================================================
 Top 5 Recommendations
==================================================

1. Sunrise City
   Score: 0.99
   Why:
     - genre matches your favorite (pop)
     - mood matches your favorite (happy)
     - energy (0.82) is very close to your target (0.80)

2. Rooftop Lights
   Score: 0.75
   Why:
     - mood matches your favorite (happy)
     - energy (0.76) is very close to your target (0.80)

3. Backroad Sunshine
   Score: 0.72
   Why:
     - mood matches your favorite (happy)
     - energy (0.68) is very close to your target (0.80)

4. Gym Hero
   Score: 0.54
   Why:
     - genre matches your favorite (pop)
     - energy (0.93) is very close to your target (0.80)

5. Night Drive Loop
   Score: 0.34
   Why:
     - energy (0.75) is very close to your target (0.80)
```

---

## Experiments You Tried

Ran the recommender against three different user profiles to see how the ranking shifts:

**Profile 1**
```
==================================================
 Top 5 Recommendations
==================================================

1. Gym Hero
   Score: 0.74
   Why:
     - mood matches your favorite (intense)
     - energy (0.93) is very close to your target (1.00)

2. Storm Runner
   Score: 0.73
   Why:
     - mood matches your favorite (intense)
     - energy (0.91) is very close to your target (1.00)

3. Midnight Coding
   Score: 0.38
   Why:
     - genre matches your favorite (lofi)

4. Focus Flow
   Score: 0.38
   Why:
     - genre matches your favorite (lofi)

5. Library Rain
   Score: 0.36
   Why:
     - genre matches your favorite (lofi)
```

**Profile 2**
```
==================================================
 Top 5 Recommendations
==================================================

1. Gym Hero
   Score: 0.56
   Why:
     - genre matches your favorite (pop)
     - energy (0.93) is very close to your target (1.00)

2. Sunrise City
   Score: 0.52
   Why:
     - genre matches your favorite (pop)
     - energy (0.82) is reasonably close to your target (1.00)

3. Iron Verdict
   Score: 0.35
   Why:
     - energy (0.98) is very close to your target (1.00)

4. Neon Pulse
   Score: 0.34
   Why:
     - energy (0.97) is very close to your target (1.00)

5. Storm Runner
   Score: 0.32
   Why:
     - energy (0.91) is very close to your target (1.00)
```

**Profile 3**
```
==================================================
 Top 5 Recommendations
==================================================

1. Sunrise City
   Score: 0.58
   Why:
     - genre matches your favorite (pop)
     - energy (0.82) is very close to your target (0.80)

2. Gym Hero
   Score: 0.54
   Why:
     - genre matches your favorite (pop)
     - energy (0.93) is very close to your target (0.80)

3. Rooftop Lights
   Score: 0.34
   Why:
     - energy (0.76) is very close to your target (0.80)

4. Night Drive Loop
   Score: 0.34
   Why:
     - energy (0.75) is very close to your target (0.80)

5. Concrete Dreams
   Score: 0.34
   Why:
     - energy (0.85) is very close to your target (0.80)
```

---

## Limitations and Risks

Summarize some limitations of your recommender.

Examples:

- It only works on a tiny catalog
- It does not understand lyrics or language
- It might over favor one genre or mood

You will go deeper on this in your model card.

---

## Reflection

Read and complete `model_card.md`:

[**Model Card**](model_card.md)

Write 1 to 2 paragraphs here about what you learned:

- about how recommenders turn data into predictions
- about where bias or unfairness could show up in systems like this



