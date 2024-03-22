from pydantic.v1.utils import deep_update
import copy
'''Library of various base dictionaries that correspond to various journal formatting requirements'''

'''See https://www.nature.com/documents/aj-artworkguidelines.pdf'''

mm_to_inches = .03937

NATURE = {"default_fontsize":7,
         "max_fontsize":7,
         "min_fontsize":5,
         "axes.labelsize":7,
         "axes.titlesize":7,
         "figure.titlesize":7,
         "figure.labelsize":7,
         "xtick.labelsize":6,
         "ytick.labelsize":6,
         "font.size":7,
         "font.family":"sans-serif",
         "1col_width": 85*mm_to_inches,
         "2col_width": 175*mm_to_inches,
          "default_figtype":".pdf",
         "dpi":500,
         "subtitle_style_dict":{"numbering":"alphabet_lower","weight":"bold"}}

NATURE_RESEARCH = copy.deepcopy(NATURE)
NATURE_RESEARCH_UPDATE = {"1col_width":88*mm_to_inches,
                        "2col_width":180*mm_to_inches}
NATURE_RESEARCH = deep_update(NATURE_RESEARCH,NATURE_RESEARCH_UPDATE)
'''See https://cdn.journals.aps.org/files/styleguide-pr.pdf'''
PHYSICAL_REVIEW = {"default_fontsize":12,
                   "1col_width": 3.4, #inches
                     "2col_width": 7.0} #inches

'''See https://journals.aps.org/prl/authors'''
PHYSICAL_REVIEW_LETTERS = copy.deepcopy(PHYSICAL_REVIEW)
PHYSICAL_REIVEW_LETTERS_UPDATE = {"1col_width":3.375}
PHYSICAL_REVIEW_LETTERS = deep_update(PHYSICAL_REVIEW_LETTERS,PHYSICAL_REIVEW_LETTERS_UPDATE)

''' See https://publish.acs.org/publish/author_guidelines?coden=jacsat#resolution'''
ACS = {"default_fontsize":12,
       "1col_width":3.33,
       "2col_width":7.0,
       "dpi":600,
       "dpi_high":1200} #for black and white




