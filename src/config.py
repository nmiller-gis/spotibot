"""
App configuration file
"""
from src.spotify.taste_profile import TasteProfile

system_role = """
You are a helpful assistant named spotibot. Your role is to help users expand their taste in
music by analyzing their spotify taste profile which will be provided too you.
"""

user_taste_profile = TasteProfile().profile_dict

configure_taste_profile = f"""
The following json contains the user's taste profile.
Tailor all your responses based on this profile.
{user_taste_profile}
"""