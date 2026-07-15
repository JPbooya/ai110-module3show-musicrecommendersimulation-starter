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

Paste a sample of your recommender's output here as a text block so a reader can see what it produces:

```
# e.g.:
# User profile: genre=indie, mood=chill, energy=low
# Recommendations:
#   1. ...
#   2. ...
#   3. ...
```

**Screenshot or video** *(optional)*: <!-- Insert a screenshot or demo video link here -->

---

## Experiments You Tried

Use this section to document the experiments you ran. For example:

- What happened when you changed the weight on genre from 2.0 to 0.5
- What happened when you added tempo or valence to the score
- How did your system behave for different types of users

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



