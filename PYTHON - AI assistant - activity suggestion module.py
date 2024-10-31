import random
from datetime import datetime

# List of categories for daily activities
productivity_activities = [
    "Read a chapter of a book 📚",
    "Write a journal entry 📝",
    "Plan your week 📅",
    "Declutter a small area of your home 🧹",
    "Set a goal for today 🎯",
    "Practice meditation or deep breathing 🧘",
    "Do 10-15 minutes of stretching or exercise 💪",
    "Try a new recipe for a meal 🍲",
    "Learn a few words in a new language 🌍",
    "Connect with a friend or family member ☎️",
]

learning_activities = [
    "Watch a TED Talk 🎥",
    "Listen to a podcast on a topic you're interested in 🎧",
    "Spend 30 minutes on a new skill (like coding or drawing) ✍️",
    "Take an online course 🖥️",
    "Read an article on recent industry news 📰",
    "Practice a foreign language 🗣️",
    "Write down things you've learned today 💡",
    "Research an interesting historical event 🏛️",
    "Do a puzzle or brain game 🧠",
    "Read a random Wikipedia article 📖",
]

wellness_activities = [
    "Take a 10-minute walk outside 🚶",
    "Drink a glass of water 💧",
    "Spend 5 minutes practicing gratitude 🙏",
    "Do a creative activity like drawing or crafting 🎨",
    "Write a list of things you're grateful for 🌈",
    "Limit screen time in the evening 📱",
    "Plan your meals for the day 🍽️",
    "Organize a small part of your workspace 🗄️",
    "Take a few deep breaths 🌬️",
    "Practice yoga or stretching 🧘",
]

# Group all activities in a master list
all_activities = productivity_activities + learning_activities + wellness_activities

# Function to select 10 random activities for the day
def daily_activity_suggestions():
    today_date = datetime.now().strftime("%Y-%m-%d")
    suggested_activities = random.sample(all_activities, 10)
    
    print(f"Here are your 10 suggested activities for {today_date}:\n")
    for i, activity in enumerate(suggested_activities, 1):
        print(f"{i}. {activity}")

# Run the assistant
daily_activity_suggestions()
