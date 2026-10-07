# File: surprise.py

# Below is a dictionary of targets you want to observe.

# If you are an observational astronomer or instrumentalist, picking the correct targets
# to point the telescope at is very important. Let's practice below.

targets = {
    "Vega": {
        "RA": "18h 36m 56.3s",
        "Dec": "+38° 47′ 01″",
        "Magnitude": 0.03,
        "Spectral Type": "A0Va"
    },
    "Betelgeuse": {
        "RA": "05h 55m 10.3s",
        "Dec": "+07° 24′ 25″",
        "Magnitude": 0.42,
        "Spectral Type": "M1-M2 Ia-Ib"
    },
    "Sirius": {
        "RA": "06h 45m 08.9s",
        "Dec": "-16° 42′ 58″",
        "Magnitude": -1.46,
        "Spectral Type": "A1V"
    },
    "Rigel": {
        "RA": "05h 14m 32.3s",
        "Dec": "-08° 12′ 06″",
        "Magnitude": 0.12,
        "Spectral Type": "B8Ia"
    },
    "Polaris": {
        "RA": "02h 31m 49.1s",
        "Dec": "+89° 15′ 51″",
        "Magnitude": 1.97,
        "Spectral Type": "F7Ib"
    }
}

# --- Questions ---
# 1) Write a function that uses a loop to print the name of each star.
# 2) Write a function that uses a loop to print the name of each star with its spectral type.
# 3) Write a function that uses a conditional to find stars with magnitudes greater than 0.1 mag.
# 4) Look up another target, add all the necessary information to the targets list. 
# 5) Write a function that finds the brightest star whose Declination is closest to 20°.
# 6) What is your favorite constellation?

# Question 1

def printname(targets):
    for star in targets:
        print(star)

printname(targets)

# Question 2

def printspectral(targets):
    for (name, category) in targets.items():
        print(name, category["Spectral Type"])

printspectral(targets)

# Question 3

def bigstars(targets):
    for (name, category) in targets.items():
        if category["Magnitude"] > 0.1:
            print(name, category["Magnitude"])

bigstars(targets)

# Question 4

targets["Alpha Centauri"] = {
    "RA" : "14h 39m 36.5s",
    "Dec" : "-60 50' 02″",
    "Magnitude" : -0.01,
    "Spectral Type" : "G2V"
}
print(targets)

# Question 5

def declination(targets):
    closest_star = None
    closest_diff = float("inf")
    brightest_mag = float("inf")

    for name, info in targets.items():
        dec_string = info["Dec"]

        for symbol in ["°", "′", "″", "'", '"', "+"]:
            dec_string = dec_string.replace(symbol, "")
        dec_string = dec_string.strip()

        parts = dec_string.split()
        deg = float(parts[0])
        min_ = float(parts[1]) if len(parts) > 1 else 0
        sec = float(parts[2]) if len(parts) > 2 else 0

        declination = deg + (min_ / 60) + (sec / 3600)

        magnitude = float(info["Magnitude"])
        diff = abs(declination - 20)

        print(f"{name}: declination={declination}, magnitude={magnitude}, diff={diff}")

        if diff < closest_diff or (diff == closest_diff and magnitude < brightest_mag):
            closest_star = name
            closest_diff = diff
            brightest_mag = magnitude

    return(closest_star)

print(declination(targets))

# Question 6

# Cassiopeia!
