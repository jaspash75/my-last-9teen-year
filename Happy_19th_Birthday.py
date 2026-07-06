"""
=========================================================
        HAPPY 19TH BIRTHDAY TO ME! 🎉🎂
              Author : Pash Kaur
              Date   : 6 July 2026
=========================================================
This program celebrates my 19th birthday while
demonstrating basic Python concepts.
"""

from datetime import datetime

# --------------------------------------------------
# Variables
# --------------------------------------------------
name = "Pash Kaur"
age = 19
birthday = "6 July 2026"

print("=" * 70)
print("🎉 HAPPY 19TH BIRTHDAY TO ME! 🎂")
print("=" * 70)

print(f"Name     : {name}")
print(f"Age      : {age}")
print(f"Birthday : {birthday}")
print("Last Teenage Year : 19 → 20")

# --------------------------------------------------
# Operators
# --------------------------------------------------
print("\n" + "=" * 70)
print("OPERATORS")
print("=" * 70)

next_age = age + 1
print("Current Age :", age)
print("Next Age    :", next_age)
print("Age == 19 :", age == 19)
print("Age > 18  :", age > 18)
print("Age < 18  :", age < 18)

# --------------------------------------------------
# If Else
# --------------------------------------------------
print("\n" + "=" * 70)
print("IF ELSE")
print("=" * 70)

today = datetime.now()

if today.day == 6 and today.month == 7 and today.year == 2026:
    print("🎂 Today is my 19th Birthday!")
else:
    print("Today is not my birthday.")

# --------------------------------------------------
# Nested If
# --------------------------------------------------
print("\n" + "=" * 70)
print("NESTED IF")
print("=" * 70)

if age >= 18:
    print("I am an adult.")
    if age == 19:
        print("This is my last teenage year!")
else:
    print("I am still a teenager under 18.")

# --------------------------------------------------
# Goals List
# --------------------------------------------------
goals = [
    "Be a kind and compassionate human being.",
    "Learn Punjabi.",
    "Explore people, places, books and technology.",
    "Love learning and earn a great CGPA.",
    "Become disciplined and punctual.",
    "Improve myself every day.",
    "Use social media wisely.",
    "Start my YouTube channel.",
    "Complete courses, hackathons and projects.",
    "Master AI, ML, Data Science, DSA, Cloud , CyberSecurity and DevOps.",
    "Build meaningful friendships.",
    "Become healthier mentally and physically.",
    "Say yes to opportunities.",
    "Choose progress over perfection.",
    "Start working on my startup ideas.",
    "Protect my peace.",
    "Learn from my mistakes.",
    "Enjoy life and smile more.",
    "Make my last teenage year unforgettable."
]

print("\n" + "=" * 70)
print("🌟 MY GOALS BEFORE I TURN 20")
print("=" * 70)

for i in range(len(goals)):
    print(f"{i + 1}. {goals[i]}")

# --------------------------------------------------
# Gratitude List
# --------------------------------------------------
gratitude = [
    "❤️ My Five Pillars (Mummy, Super Mummy, Papa, Daddyji & Naniji , Mamaji and his family & Badi Naniji)",
    "🙏 Waheguru Ji",
    "🧠 My Mind & Curiosity",
    "💪 My Resilience",
    "📚 Education & Lifelong Learning",
    "🌸 Health, Healing & My Smile",
    "⚔️ Being a Kaur",
    "✨ Wisdom & Knowledge",
    "🌿 Values & Integrity",
    "🌱 Growth & Maturity",
    "🤍 Acceptance & Gratitude",
    "🌍 Dreams with Open Eyes",
    "🧭 Exploration & Discovery",
    "📖 Lessons & Experiences",
    "🎨 Creativity "
    "🎨  Innovation",
    "🚀 Purpose, Vision",
    "🌅 Turning 19 — A New Chapter",
    "❤️ My Life"
]

print("\n" + "=" * 70)
print("🙏 19 THINGS I'M GRATEFUL FOR")
print("=" * 70)

count = 1
while count <= len(gratitude):
    print(f"{count}. {gratitude[count - 1]}")
    count += 1

# --------------------------------------------------
# Function
# --------------------------------------------------
def birthday_wish(person):
    print("\n" + "=" * 70)
    print("🎂 PERSONAL BIRTHDAY MESSAGE")
    print("=" * 70)
    print(f"Happy 19th Birthday, {person}!")
    print("May this year be filled with learning,")
    print("growth, happiness and success.")
    print("Keep believing in yourself! ❤️")


birthday_wish(name)

# --------------------------------------------------
# Dictionary
# --------------------------------------------------
about_me = {
    "Name": "Pash Kaur",
    "Age": 19,
    "Birthday": "06/07/2026",
    "Branch": "Computer Science & Business Systems",
    "Dream": "Be a good human being: Learn, Explore, Create, Innovate and Inspire.",
}

print("\n" + "=" * 70)
print("👩 ABOUT ME")
print("=" * 70)

for key, value in about_me.items():
    print(f"{key} : {value}")

# --------------------------------------------------
# Match Case (Switch Case)
# --------------------------------------------------
print("\n" + "=" * 70)
print("MATCH CASE")
print("=" * 70)

today_type = "birthday"

match today_type:
    case "birthday":
        print("🎉 Today is my Birthday!")
    case "holiday":
        print("Enjoy your holiday!")
    case "exam":
        print("Best of luck for your exams!")
    case _:
        print("Have a wonderful day!")

# --------------------------------------------------
# Letter to Future Me
# --------------------------------------------------
print("\n" + "=" * 70)
print("💌 LETTER TO FUTURE PASH KAUR")
print("=" * 70)

print(f"""
Dear Future {name},

If you're reading this on your 20th birthday,
I hope you remember that this year was never
about becoming perfect.

It was about becoming YOU.

I hope you:
✔ Stayed kind.
✔ Learned something new every day.
✔ Built meaningful projects.
✔ Made amazing memories.
✔ Stayed true to yourself.
✔ Never gave up.

Remember:
Progress > Perfection
Learning > Fear
Consistency > Motivation

Happy 20th Birthday, Future Me!

Love,
19-year-old Pash ❤️
""")

# --------------------------------------------------
# Final Message
# --------------------------------------------------
print("=" * 70)
print("🎉 HAPPY LAST TEEN YEAR! 🎉")
print("=" * 70)

print("This is my last year as a teenager.")
print("I will dream big.")
print("I will work hard.")
print("I will stay humble.")
print("I will keep learning.")
print("I will keep exploring.")
print("I will never stop believing in myself.")

print("\n❤️ Happy 19th Birthday to Me!")
print("📅 6 July 2026") 
meme = "67"
print(meme)
print(f"Love,\n{name}")

print("=" * 70)


