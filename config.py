import re
from os import getenv
# ------------------------------------
# ------------------------------------
from dotenv import load_dotenv
from pyrogram import filters
# ------------------------------------
# ------------------------------------
load_dotenv()
# ------------------------------------
# -----------------------------------------------------
API_ID = int(getenv("API_ID", "21194358"))
API_HASH = getenv("API_HASH", "9623f07eca023e4e3c561c966513a642")
# ------------------------------------------------------
BOT_TOKEN = getenv("BOT_TOKEN","7123283070:AAH9kkVtrBbky4zkCXpwhgEP6suzr-_yerg")
# -------------------------------------------------------
OWNER_USERNAME = getenv("OWNER_USERNAME","Kapalimmmm")
# --------------------------------------------------------
BOT_USERNAME = getenv("BOT_USERNAME" , "sumeyyemusicbot")
# --------------------------------------------------------
BOT_NAME = getenv("BOT_NAME" , "Sümeyye music")
# ---------------------------------------------------------
ASSUSERNAME = getenv("ASSUSERNAME" , "Kapalimmmm")
# ---------------------------------------------------------


#---------------------------------------------------------------
#---------------------------------------------------------------
MONGO_DB_URI = getenv("MONGO_DB_URI", "mongodb+srv://kurt67143:nays@cluster0.vjg7bma.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
#---------------------------------------------------------------
#---------------------------------------------------------------

# ----------------------------------------------------------------
DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", 17000))
# ----------------------------------------------------------------

# ----------------------------------------------------------------
LOGGER_ID = int(getenv("LOGGER_ID", "-1002065943011"))
# ----------------------------------------------------------------
# ----------------------------------------------------------------
OWNER_ID = int(getenv("OWNER_ID", "6997506255"))
# -----------------------------------------------------------------
# -----------------------------------------------------------------

# ----------------------------------------------------------------
# ----------------------------------------------------------------
# ----------------------------------------------------------------
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
# ----------------------------------------------------------------
HEROKU_API_KEY = getenv("HEROKU_API_KEY")
# ----------------------------------------------------------------
# ----------------------------------------------------------------
# ----------------------------------------------------------------
UPSTREAM_REPO = getenv(
    "UPSTREAM_REPO",
    "https://github.com/DAXXTEAM/DAXXMUSIC",
)
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "Master")
GIT_TOKEN = getenv(
    "GIT_TOKEN", None
)  # ----------------------------------------------------------------
# -------------------------------------------------------------------
# --------------------------------------------------------------------
# --------------------------------------------------------------------



# ------------------------------------------------------------------------
# -------------------------------------------------------------------------
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/masaldestekkanal")
SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/masaldestek")
# ------------------------------------------------------------------------------
# -------------------------------------------------------------------------------







# --------------------------------------------------------------------------------
# --------------------------------------------------------------------------------
# --------------------------------------------------------------------------------
# --------------------------------------------------------------------------------
AUTO_LEAVING_ASSISTANT = getenv("AUTO_LEAVING_ASSISTANT", "True")
AUTO_LEAVE_ASSISTANT_TIME = int(getenv("ASSISTANT_LEAVE_TIME", "9000"))
SONG_DOWNLOAD_DURATION = int(getenv("SONG_DOWNLOAD_DURATION", "9999999"))
SONG_DOWNLOAD_DURATION_LIMIT = int(getenv("SONG_DOWNLOAD_DURATION_LIMIT", "9999999"))
# --------------------------------------------------------------------------------
# --------------------------------------------------------------------------------
# --------------------------------------------------------------------------------

# ---------------------------------------------------------------------------------
SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", "1c21247d714244ddbb09925dac565aed")
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", "709e1a2969664491b58200860623ef19")
# ----------------------------------------------------------------------------------




# -----------------------------------------------------------------------------------
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", 25))
# ------------------------------------------------------------------------------------

# ------------------------------------------------------------------------------------
TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", "5242880000"))
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", "5242880000"))
# --------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------



# ------------------------------------
# ------------------------------------
# ------------------------------------
# ------------------------------------
STRING1 = getenv("STRING_SESSION", "BAGXyHkAgtBy4Vjt_E7zNAjxdccS2NuB1_jhQZzsQdrkqzv6ap_H2L-eP4g37YE3eeeUM6KY64Ag8XGcVwCQGJbPumOe_B9-NEFehsxiv19bgg97DRLQoG8z3lQcoRFQ2buSTrJMEDlKeMs13HU4Q53QZwIpgKytIzSGnwbc-3ZxZ1s0gPWnA0zQZOYH1ZoUwaiEaaCj30-98j06J7SxMZGemIlE2Uv7xKYnqCN9RozQmIq0SmVmpGE1ruNWd4x3PIERTaXGxRgqYF_BGU3JX_CoSzS_XcppmEr1q6j7hsq0sYp1nK2qE-lQSw0d2w9K_U04ktR2UgfjlqCHtcIOOAl3eP2D4wAAAAGhFXjPAA")
STRING2 = getenv("STRING_SESSION2", None)
STRING3 = getenv("STRING_SESSION3", None)
STRING4 = getenv("STRING_SESSION4", None)
STRING5 = getenv("STRING_SESSION5", None)
STRING6 = getenv("STRING_SESSION6", None)
STRING7 = getenv("STRING_SESSION7", None)
BANNED_USERS = filters.user()
adminlist = {}
lyrical = {}
votemode = {}
autoclean = []
confirmer = {}

# ------------------------------------
# ------------------------------------
# ------------------------------------
# ------------------------------------

# ------------------------------------------------------------------------
# ------------------------------------------------------------------------
# ------------------------------------------------------------------------
# ------------------------------------------------------------------------
# ------------------------------------------------------------------------
# ------------------------------------------------------------------------
# ------------------------------------------------------------------------
START_IMG_URL = getenv(
    "START_IMG_URL", "https://graph.org/file/a8d0706741cbf01ec3602.jpg"
)
PING_IMG_URL = getenv(
    "PING_IMG_URL", "https://graph.org/file/a8d0706741cbf01ec3602.jpg"
)
PLAYLIST_IMG_URL = "https://graph.org/file/a8d0706741cbf01ec3602.jpg"
STATS_IMG_URL = "https://graph.org/file/a8d0706741cbf01ec3602.jpg"
TELEGRAM_AUDIO_URL = "https://graph.org/file/a8d0706741cbf01ec3602.jpg"
TELEGRAM_VIDEO_URL = "https://graph.org/file/a8d0706741cbf01ec3602.jpg"
STREAM_IMG_URL = "https://graph.org/file/a8d0706741cbf01ec3602.jpg"
SOUNCLOUD_IMG_URL = "https://graph.org/file/a8d0706741cbf01ec3602.jpg"
YOUTUBE_IMG_URL = "https://graph.org/file/a8d0706741cbf01ec3602.jpg"
SPOTIFY_ARTIST_IMG_URL = "https://graph.org/file/a8d0706741cbf01ec3602.jpg"
SPOTIFY_ALBUM_IMG_URL = "https://graph.org/file/a8d0706741cbf01ec3602.jpg"
SPOTIFY_PLAYLIST_IMG_URL = "https://graph.org/file/a8d0706741cbf01ec3602.jpg"

# ------------------------------------------------------------------------
# ------------------------------------------------------------------------
# ------------------------------------------------------------------------
# ------------------------------------------------------------------------
def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60**i for i, x in enumerate(reversed(stringt.split(":"))))


DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))

# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------
# ------------------------------------------------------------------------------
if SUPPORT_CHANNEL:
    if not re.match("(?:http|https)://", SUPPORT_CHANNEL):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHANNEL url is wrong. Please ensure that it starts with https://"
        )

if SUPPORT_CHAT:
    if not re.match("(?:http|https)://", SUPPORT_CHAT):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHAT url is wrong. Please ensure that it starts with https://"
        )
# ---------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------
