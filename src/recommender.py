import csv
from typing import List, Dict, Tuple, Optional
from dataclasses import dataclass

@dataclass
class Song:
    """
    Represents a song and its attributes.
    Required by tests/test_recommender.py
    """
    id: int
    title: str
    artist: str
    genre: str
    mood: str
    energy: float
    tempo_bpm: float
    valence: float
    danceability: float
    acousticness: float

@dataclass
class UserProfile:
    """
    Represents a user's taste preferences.
    Required by tests/test_recommender.py
    """
    favorite_genre: str
    favorite_mood: str
    target_energy: float
    likes_acoustic: bool

# --- Scoring weights (the "point-weighting strategy") ---
# Must sum to 1.0 so the final score stays on a 0-1 scale.
#
# Mood (0.35) outweighs Genre (0.20) because mood describes the emotional
# state the user wants right now, while genre is a coarser style bucket
# that can span many moods (e.g. "pop" covers both a happy song and an
# intense one in this catalog). A mood match is a stronger signal of fit
# than a genre match.
#
# Energy closeness (0.30) sits almost as high as mood because it's a
# continuous signal rather than a binary match/no-match, so it contributes
# gradient across the whole catalog instead of a coin flip.
#
# Acoustic alignment (0.15) is lightest since it's a secondary style
# preference rather than a core taste signal.
WEIGHT_GENRE = 0.20
WEIGHT_MOOD = 0.35
WEIGHT_ENERGY = 0.30
WEIGHT_ACOUSTIC = 0.15


def _weighted_score(
    genre: str,
    mood: str,
    energy: float,
    acousticness: float,
    favorite_genre: str,
    favorite_mood: str,
    target_energy: float,
    likes_acoustic: Optional[bool],
) -> Tuple[float, List[str]]:
    """
    Core scoring rule shared by the functional API (score_song) and the
    OOP API (Recommender), so the two never drift apart.
    """
    reasons: List[str] = []

    genre_match = genre.strip().lower() == favorite_genre.strip().lower()
    genre_score = 1.0 if genre_match else 0.0
    if genre_match:
        reasons.append(f"genre matches your favorite ({genre})")

    mood_match = mood.strip().lower() == favorite_mood.strip().lower()
    mood_score = 1.0 if mood_match else 0.0
    if mood_match:
        reasons.append(f"mood matches your favorite ({mood})")

    energy_score = max(0.0, 1.0 - abs(energy - target_energy))
    if energy_score >= 0.85:
        reasons.append(f"energy ({energy:.2f}) is very close to your target ({target_energy:.2f})")
    elif energy_score >= 0.6:
        reasons.append(f"energy ({energy:.2f}) is reasonably close to your target ({target_energy:.2f})")

    weights = {"genre": WEIGHT_GENRE, "mood": WEIGHT_MOOD, "energy": WEIGHT_ENERGY}
    scores = {"genre": genre_score, "mood": mood_score, "energy": energy_score}

    if likes_acoustic is None:
        # No acoustic preference given: redistribute its weight
        # proportionally instead of assuming a default preference.
        remaining = WEIGHT_GENRE + WEIGHT_MOOD + WEIGHT_ENERGY
        weights = {k: v / remaining for k, v in weights.items()}
    else:
        acoustic_score = acousticness if likes_acoustic else (1.0 - acousticness)
        weights["acoustic"] = WEIGHT_ACOUSTIC
        scores["acoustic"] = acoustic_score
        if acoustic_score >= 0.7:
            style = "acoustic" if likes_acoustic else "produced/electronic"
            reasons.append(f"leans {style}, matching your preference")

    total = sum(weights[k] * scores[k] for k in scores)

    if not reasons:
        reasons.append("closest overall match available in the catalog")

    return round(total, 4), reasons


class Recommender:
    """
    OOP implementation of the recommendation logic.
    Required by tests/test_recommender.py
    """
    def __init__(self, songs: List[Song]):
        self.songs = songs

    def recommend(self, user: UserProfile, k: int = 5) -> List[Song]:
        scored = [
            (
                song,
                _weighted_score(
                    song.genre, song.mood, song.energy, song.acousticness,
                    user.favorite_genre, user.favorite_mood, user.target_energy,
                    user.likes_acoustic,
                )[0],
            )
            for song in self.songs
        ]
        scored.sort(key=lambda pair: pair[1], reverse=True)
        return [song for song, _ in scored[:k]]

    def explain_recommendation(self, user: UserProfile, song: Song) -> str:
        _, reasons = _weighted_score(
            song.genre, song.mood, song.energy, song.acousticness,
            user.favorite_genre, user.favorite_mood, user.target_energy,
            user.likes_acoustic,
        )
        return "Recommended because " + "; ".join(reasons) + "."


def load_songs(csv_path: str) -> List[Dict]:
    """
    Loads songs from a CSV file.
    Required by src/main.py
    """
    songs = []
    with open(csv_path, newline="") as f:
        reader = csv.DictReader(f)
        for row in reader:
            songs.append({
                "id": int(row["id"]),
                "title": row["title"],
                "artist": row["artist"],
                "genre": row["genre"],
                "mood": row["mood"],
                "energy": float(row["energy"]),
                "tempo_bpm": float(row["tempo_bpm"]),
                "valence": float(row["valence"]),
                "danceability": float(row["danceability"]),
                "acousticness": float(row["acousticness"]),
            })
    return songs

def score_song(user_prefs: Dict, song: Dict) -> Tuple[float, List[str]]:
    """
    Scores a single song against user preferences.
    Required by recommend_songs() and src/main.py
    """
    return _weighted_score(
        song["genre"], song["mood"], song["energy"], song["acousticness"],
        user_prefs.get("genre", ""), user_prefs.get("mood", ""),
        user_prefs.get("energy", 0.5), user_prefs.get("likes_acoustic"),
    )

def recommend_songs(user_prefs: Dict, songs: List[Dict], k: int = 5) -> List[Tuple[Dict, float, str]]:
    """
    Functional implementation of the recommendation logic.
    Required by src/main.py
    """
    results = []
    for song in songs:
        score, reasons = score_song(user_prefs, song)
        results.append((song, score, "; ".join(reasons)))
    results.sort(key=lambda item: item[1], reverse=True)
    return results[:k]
