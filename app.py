#neil young songs hangman game

from flask import Flask, render_template, request, session, redirect, url_for
import random
import os

app = Flask(__name__)
app.secret_key = 'neil_young_is_legend'

# 🎵 Some BRIGHT EYES song titles
SONGS = [
    "Act of Contrition",
    "All of the Truth",
    "Amy in the White Coat",
    "Another Travelin' Song",
    "Approximate Sunlight",
    "Arc of Time",
    "Arienette",
    "At the Bottom of Everything",
    "An Attempt to Tip the Scales",
    "Away in a Manger",
    "Awful Sweetness of Escaping Sweat",
    "Bad Blood",
    "Beginner's Mind",
    "The Big Picture",
    "Black Comedy",
    "Blue Angels Air Show",
    "Blue Christmas",
    "Bowl of Oranges",
    "Burn Rubber",
    "Calais to Dover",
    "The Calendar Hung Itself...",
    "Cartoon Blues",
    "A Celebration Upon Completion",
    "The Center of the World",
    "The City Has Sex",
    "Clairaudients",
    "Classic Cars",
    "Cleanse Song",
    "Coat Check Dream Song",
    "Contrast and Compare",
    "Comet Song",
    "Coyote Song",
    "Cremation",
    "Dance and Sing",
    "Devil in the Details",
    "Devil Town",
    "The Difference in the Shades",
    "Don't Know When But a Day's Gonna Come",
    "Down in a Rabbit Hole",
    "Driving Fast Through a Big City at Night",
    "Drunk Kid Catholic",
    "Easy/Lucky/Free",
    "Emily, Sing Something Sweet",
    "Empty Canyon, Empty Canteen",
    "Endless Entertainment",
    "Entry Way Song",
    "Exaltation on a Cool Kitchen Floor",
    "Falling Out of Love at this Volume",
    "False Advertising",
    "Feb. 15th",
    "The 'Feel Good' Revolution",
    "Feeling It",
    "Few Minutes on Friday",
    "Firewall",
    "First Day of My Life",
    "Forced Convalescence",
    "Four Winds",
    "From a Balance Beam",
    "Go Find Yourself a Dry Place",
    "God Rest Ye Merry Gentlemen",
    "Going for the Gold",
    "Gold Mine Gutted",
    "Haile Selassie",
    "Haligh, Haligh, a Lie, Haligh",
    "Happy Accident",
    "Happy Birthday to Me",
    "Have You Ever Heard Of Jandek Before?",
    "Have Yourself a Merry Little Christmas",
    "Hit the Switch",
    "Hot Car in the Sun",
    "Hot Knives",
    "How Many Lights Do You See?",
    "Hungry for a Holiday",
    "I'll Be Your Friend",
    "I've Been Eating",
    "I Believe in Symmetry",
    "I Know You",
    "I Must Belong Somewhere",
    "I Watched You Taking Off",
    "I Will Be Grateful for This Day, I Will Be Grateful for Each Day to Come",
    "I Woke Up with this Song in My Head this Morning",
    "I Won't Ever Be Happy Again",
    "If the Brakeman Turns My Way",
    "If Winter Ends",
    "In the Real World",
    "The Invisible Gardener",
    "It's Cool, We Can Still Be Friends",
    "Jejune Stars",
    "Jetsabel Removes the Undesirables",
    "The Joy in Discovery",
    "The Joy in Forgetting/The Joy in Acceptance",
    "June on the West Coast",
    "Just Once in the World",
    "Kathy with a K's Song",
    "Ladder Song",
    "Lake Havasu",
    "Landlocked Blues",
    "Laura Laurent",
    "Let's Not Shit Ourselves",
    "Let the Distance Bring Us Together",
    "Light Pollution",
    "Lila",
    "Lime Tree",
    "A Line Allows Progress, a Circle Does Not",
    "Little Drummer Boy",
    "Loose Leaves",
    "Lover I Don't Have to Love",
    "Lovers Turn Into Monsters",
    "Lua",
    "A Machine Spiritual",
    "Make a Plan to Love Me",
    "Make War",
    "Man Named Truth",
    "Mariana Trench",
    "Messenger Bird's Song",
    "Method Acting",
    "Middleman",
    "Mirrors and Fevers",
    "Motion Sickness",
    "The Movement of a Hand",
    "Napoleon's Hat",
    "Neely O'Hara",
    "A New Arrangement",
    "The Night Before Christmas",
    "No Lies, Just Love",
    "No One Would Riot For Less",
    "No Prayer",
    "North of the City",
    "Nothing Gets Crossed Out",
    "Oh Little Town of Bethlehem",
    "Oh, You Are the Roots That Sleep Beneath My Feet and Hold the Earth in Place",
    "Old Soul Song",
    "On My Way to Work",
    "One and Done",
    "One for You, One for Me",
    "One Foot in Front of the Other",
    "One Straw",
    "Padraic My Prince",
    "Pageturner's Rag",
    "Pan and Broom",
    "Patient Hope in New Snow",
    "A Perfect Sonnet",
    "Persona Non Grata",
    "Pioneer's Park",
    "A Poetic Retelling of an Unfortunate Seduction",
    "Poison Oak",
    "Puella Quam Amo Est Pulchra",
    "Pull My Hair",
    "Racing Towards The New",
    "Reinvent the Wheel",
    "Road to Joy",
    "Saturday As Usual",
    "A Scale, a Mirror and Those Indifferent Clocks",
    "Seashell Tale",
    "Shell Games",
    "Ship in a Bottle",
    "Silent Night",
    "Singularity",
    "Silver Bells",
    "Smoke Without Fire",
    "Solid Jackson",
    "Something Vague",
    "A Song to Pass the Time",
    "Soon You Will Be Leaving Your Man",
    "Soul Singer in a Session Band",
    "Southern State",
    "Spent on Rainy Days",
    "A Spindle, a Darkness, a Fever, and a Necklace",
    "Spring Cleaning",
    "Stairwell Song",
    "Stray Dog Freedom",
    "Sunrise, Sunset",
    "Supriya",
    "Susan Miller Rag",
    "Take It Easy",
    "Tereza and Tomas",
    "Theme From Pinata",
    "Tilt-A-Whirl",
    "Time Code",
    "To Death's Heart",
    "Touch",
    "Tourist Trap",
    "Train Under Water",
    "Trees Get Wheeled Away",
    "Triple Spiral",
    "True Blue",
    "The Vanishing Act",
    "Waste of Paint",
    "We Are Free Men",
    "We Are Nowhere and It's Now",
    "Weather Reports",
    "Well Whiskey",
    "When the Curious Girl Realizes She Is Under Glass",
    "When the Curious Girl Realizes She Is Under Glass Again",
    "When the President Talks to God",
    "White Christmas",
    "You Get Yours",
    "You Will. You? Will. You? Will. You? Will.",
    "Five Dice",
    "Bells and Whistles",
    "El Capitan",
    "Bas Jan Ader",
    "Tiny Suicides",
    "All Threes",
    "Rainbow Overpass",
    "Hate",
    "Real Feel 105",
    "Spun Out",
    "Trains Still Run on Time",
    "The Time I Have Left",
    "Tin Soldier Boy"
]


MAX_GUESSES = 6

def pick_random_song():
    return random.choice(SONGS).upper()
    
def choose_new_song():
# Initialize the list if not in session yet
    if 'used_songs' not in session:
        session['used_songs'] = []

    # Get list of unused songs
    unused = [song for song in SONGS if song not in session['used_songs']]

    if not unused:
        session['used_songs'] = []  # reset after all have been used
        unused = SONGS.copy()

    song = random.choice(unused)
    session['used_songs'].append(song)
    session.modified = True  # ensure session gets updated

    return song

def mask_title(title, guesses):
    masked = []
    for word in title.split():
        masked_word = []
        for char in word:
            if not char.isalpha():
                masked_word.append(char)
            elif char.upper() in guesses:
                masked_word.append(char.upper())
            else:
                masked_word.append('_')
        masked.append(masked_word)
    return masked

@app.route("/", methods=["GET", "POST"])

def index():
    if 'title' not in session:
        session['title'] = choose_new_song()
        session['guesses'] = []
        session['wrong'] = 0
        session['won'] = False
        session['lost'] = False
        print("Wrong guess count:", session['wrong'])

    if request.method == "POST":
        guess = request.form["guess"].upper()
        if guess.isalpha() and len(guess) == 1 and guess not in session['guesses']:
            session['guesses'].append(guess)
            if guess not in session['title'].upper():
                session['wrong'] += 1
                print("Wrong guess count:", session['wrong'])
        masked = mask_title(session['title'], session['guesses'])
        session['won'] = all('_' not in word for word in masked)
        session['lost'] = session['wrong'] >= MAX_GUESSES

    return render_template("index.html",
        masked=mask_title(session['title'], session['guesses']),
        guesses=session['guesses'],
        wrong=session['wrong'],
        remaining=MAX_GUESSES - session['wrong'],
        won=session['won'],
        lost=session['lost'],
        full_title=session['title'] if session['won'] or session['lost'] else None
    )

@app.route("/reset")
def reset():
    session.clear()
    return redirect(url_for("index"))
    
@app.route('/manifest.json')
def manifest():
    return app.send_static_file('manifest.json')

if __name__ == "__main__":
        port = int(os.environ.get("PORT", 5000))
        app.run(host="0.0.0.0", port=port)
