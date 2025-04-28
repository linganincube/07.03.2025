from gtts import gTTS
import os

# Text to be converted into speech
text = """
The Good, the Bad, and the Robot-y
AI is like a super-smart but clueless toddler: it can do amazing things, but it doesn’t know right from wrong. Here’s how it can go sideways—and why we need to care:

Bias & Unfairness:

AI learns from data created by humans… and humans are biased. Example: A hiring AI trained on past resumes might favor men for tech jobs if historically most hires were men.

Result: Unfair decisions in jobs, loans, or policing.

Privacy Invasion:

AI loves data—your face, your shopping habits, even your texts. But who’s watching the watchers? Example: Facial recognition tracking you in public without consent.

Result: Creepy surveillance or data leaks (hello, identity theft! 👀).

Job Shake-Up:

Robots can flip burgers, drive trucks, or answer calls. Great for companies, scary for workers. Example: Self-checkout kiosks replacing cashiers.

Result: Unemployment spikes unless we retrain people for new roles.

Black Box Problem:

Some AI (like deep learning) is a mystery—even its creators don’t know how it decides. Example: A bank’s AI denies your loan… but can’t explain why.

Result: Trust issues. Would you trust a doctor who won’t explain their diagnosis? 🩺

Autonomous Weapons:

Imagine killer robots that choose targets without humans. Example: Drones that “decide” to attack.

Result: War crimes with no one to blame. Terminator vibes, anyone? 💀

Deepfakes & Misinformation:

AI can clone voices or make fake videos of politicians saying anything. Example: A fake video of a leader declaring war goes viral.

Result: Chaos, scams, or election interference. 🤯

Environmental Cost:

Training big AI models guzzles energy like a Bitcoin mine. Example: ChatGPT’s carbon footprint rivals a car driving thousands of miles.

Result: Climate harm hidden behind “smart” tech. 🌍

💡 How Do We Fix This?
Diverse Teams: Build AI with people of all backgrounds to spot bias.

Rules & Laws: Governments need to set guardrails (like the EU’s AI Act).

Transparency: Force companies to explain how their AI works.

Public Voice: Should YOU get a say in how AI is used? Heck yes!

The Bottom Line: AI isn’t inherently good or evil—it’s a tool. Like a chainsaw 🔪, it can build a house or chop off a limb. It’s up to us to steer it toward helping, not harming. Otherwise, we’re just handing toddlers chainsaws and hoping for the best. 
"""

# Language setting (e.g., 'en' for English)
language = 'en'

# Create a gTTS object
tts = gTTS(text=text, lang=language, slow=False)

# Save the audio file
audio_file = "ethical_considerations.mp3"
tts.save(audio_file)

# Optional: Play the audio file (requires playsound library)
try:
    from playsound import playsound
    print(f"Playing audio file: {audio_file}")
    playsound(audio_file)
except ImportError:
    print(f"Audio file saved as: {audio_file}. You can play it manually.")

print("Audio generation complete!")