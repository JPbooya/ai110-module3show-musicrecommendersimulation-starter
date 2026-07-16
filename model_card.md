# 🎧 Model Card: Music Recommender Simulation

## 1. Model Name  

Give your model a short, descriptive name.  
Example: **VibeFinder 1.0**  

---

## 2. Intended Use  

Describe what your recommender is designed to do and who it is for. 

Prompts:  

- What kind of recommendations does it generate  
- What assumptions does it make about the user  
- Is this for real users or classroom exploration  

---

## 3. How the Model Works  

Explain your scoring approach in simple language.  

Prompts:  

- What features of each song are used (genre, energy, mood, etc.)  
- What user preferences are considered  
- How does the model turn those into a score  
- What changes did you make from the starter logic  

Avoid code here. Pretend you are explaining the idea to a friend who does not program.

---

## 4. Data  

Describe the dataset the model uses.  

Prompts:  

- How many songs are in the catalog  
- What genres or moods are represented  
- Did you add or remove data  
- Are there parts of musical taste missing in the dataset  

---

## 5. Strengths  

Where does your system seem to work well  

Prompts:  

- User types for which it gives reasonable results  
- Any patterns you think your scoring captures correctly  
- Cases where the recommendations matched your intuition  

---

## 6. Limitations and Bias 

Where the system struggles or behaves unfairly. 

**Energy dominates over genre and mood.** Genre and mood only score points on an exact match — no match means zero, no partial credit. Energy is different: it always gives some points based on how close it is to what the user wants, even if it's not a perfect match. So once a song doesn't match a user's genre or mood, those two drop out of the score entirely, and energy is the only thing left deciding the ranking. Since most genres and moods in this catalog only have one song each, most songs don't share a genre or mood with any given user — so energy ends up deciding most of the rankings by default, not because it's picked first, but because it's the only value still doing any work.

Prompts:  

- Features it does not consider  
- Genres or moods that are underrepresented  
- Cases where the system overfits to one preference  
- Ways the scoring might unintentionally favor some users  

---

## 7. Evaluation  

How you checked whether the recommender behaved as expected. 

One of the clearest examples was the **User A vs. User B test**: two profiles with completely opposite taste. User A wanted `jazz`/`relaxed` songs, User B wanted `metal`/`angry` songs, but both had the same energy target (0.4). I expected their recommendation lists to look totally different since their genre and mood preferences don't overlap at all. Instead, the surprising result was that 3 of their top 5 songs were identical (Focus Flow, Midnight Coding, Dust Road Home), songs that don't even match either user's genre or mood. They only showed up because their energy happened to sit close to 0.4. So instead of two very different playlists, the system gave two mostly overlapping ones, which wasn't the outcome I expected going in. It exposed how much energy alone can steer the results once genre and mood stop mattering.

I also compared three other profiles (see README's Experiments section) two at a time to see what changed and why:

- **Profile 1 vs Profile 2** — In Profile 1, Gym Hero got a mood match ("intense"), which was worth more points, so it scored 0.74. In Profile 2, Gym Hero only got a genre match ("pop") instead, which is worth fewer points, so it dropped to 0.56, even though its energy score stayed the same. This makes sense because mood matches were worth more than genre matches at the time.

- **Profile 2 vs Profile 3** — Just lowering the target energy from 1.0 to 0.8 flipped the order of the top two songs. Sunrise City (energy 0.82) is now closer to 0.80 than Gym Hero (energy 0.93), so it moved into first place. The #3 song also changed, from Iron Verdict (energy 0.98, close to the old target) to Rooftop Lights (energy 0.76, close to the new target). This makes sense because energy score is just about how close a song is to the target, so moving the target changes which songs count as "close."

- **Profile 1 vs Profile 3** — These two change genre, mood, and target energy all at once, so almost everything about the results changes. Profile 1's top song won on a mood match, Profile 3's top song won on a genre match instead. Even the bottom of the list looks totally different: Profile 1's bottom songs are lofi tracks that only got points for genre, while Profile 3's bottom songs are unrelated genres that only got points for having energy close to 0.80. This makes sense because changing all three inputs at once changes what's actually deciding the ranking.

Prompts:  

- Which user profiles you tested  
- What you looked for in the recommendations  
- What surprised you  
- Any simple tests or comparisons you ran  

No need for numeric metrics unless you created some.

---

## 8. Future Work  

Ideas for how you would improve the model next.  

Prompts:  

- Additional features or preferences  
- Better ways to explain recommendations  
- Improving diversity among the top results  
- Handling more complex user tastes  

---

## 9. Personal Reflection  

A few sentences about your experience.  

Prompts:  

- What you learned about recommender systems  
- Something unexpected or interesting you discovered  
- How this changed the way you think about music recommendation apps  
