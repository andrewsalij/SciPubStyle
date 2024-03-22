import string
import roman
'''
Functions for handling text according to style rules
'''

def create_subtitle_list(num_subtitles, subtitle_style_dict):
    subtitle_list = []
    for i in range(num_subtitles):
       if "numbering" in subtitle_style_dict:
           if subtitle_style_dict["numbering"] == "arabic":
                base_subtitle = f"{i+1}" #i+1 since i beginas at 0
           elif subtitle_style_dict["numbering"] == "roman_lower":
               base_subtitle = roman.toRoman(i+1).lower()
           elif subtitle_style_dict["numbering"] == "roman_upper":
               base_subtitle = roman.toRoman(i+1)
           elif subtitle_style_dict["numbering"] == "alphabet_lower":
                base_subtitle = string.ascii_lowercase[i]
           elif subtitle_style_dict["numbering"] == "alphabet_upper":
                base_subtitle = string.ascii_uppercase[i]
       else:
           base_subtitle = ""
       subtitle_list.append(base_subtitle)
    return subtitle_list

