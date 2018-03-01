# -*- coding: utf-8 -*-
"""
tomorrow night eighties
---------------------

Port of the Tomorrow Night Eighties colour scheme https://github.com/chriskempson/tomorrow-theme
"""

from pygments.style import Style
from pygments.token import Keyword, Name, Comment, String, Error, Text, \
     Number, Operator, Generic, Whitespace, Punctuation, Other, Literal


BACKGROUND = "#2d2d2d"
CURRENT_LINE = "#393939"
SELECTION = "#515151"
FOREGROUND = "#cccccc"
COMMENT = "#999999"
RED = "#f2777a"
ORANGE = "#f99157"
YELLOW = "#ffcc66"
GREEN = "#99cc99"
AQUA = "#66cccc"
BLUE = "#6699cc"
PURPLE = "#cc99cc"


class TomorrownighteightiesStyle(Style):

    """
    Port of the Tomorrow Night Eighties colour scheme https://github.com/chriskempson/tomorrow-theme
    """

    default_style = ''

    background_color = BACKGROUND
    highlight_color = SELECTION

    styles = {
        # No corresponding class for the following:
        Text:                      FOREGROUND,  # class:  ''
        Whitespace:                "",          # class: 'w'
        Error:                     RED,         # class: 'err'
        Other:                     "",          # class 'x'

        Comment:                   AQUA,      # class: 'c'
        Comment.Multiline:         COMMENT,   # class: 'cm'
        Comment.Preproc:           PURPLE,    # class: 'cp'
        Comment.Single:            "italic " + COMMENT,   # class: 'c1'
        Comment.Special:           COMMENT,   # class: 'cs'

        Keyword:                   GREEN,      # class: 'k'
        Keyword.Constant:          GREEN,        # class: 'kc'
        Keyword.Declaration:       YELLOW,    # class: 'kd'
        Keyword.Namespace:         AQUA,      # class: 'kn'
        Keyword.Pseudo:            GREEN,        # class: 'kp'
        Keyword.Reserved:          GREEN,        # class: 'kr'
        Keyword.Type:              BLUE,      # class: 'kt'

        Operator:                  FOREGROUND,      # class: 'o'
        Operator.Word:             "",        # class: 'ow' - like keywords

        Punctuation:               FOREGROUND,  # class: 'p'

        Name:                      FOREGROUND,  # class: 'n'
        Name.Attribute:            BLUE,        # class: 'na' - to be revised
        Name.Builtin:              "",          # class: 'nb'
        Name.Builtin.Pseudo:       "",          # class: 'bp'
        Name.Class:                BLUE,      # class: 'nc' - to be revised
        Name.Constant:             RED,         # class: 'no' - to be revised
        Name.Decorator:            AQUA,        # class: 'nd' - to be revised
        Name.Entity:               YELLOW,          # class: 'ni'
        Name.Exception:            RED,         # class: 'ne'
        Name.Function:             ORANGE,        # class: 'nf'
        Name.Property:             "",          # class: 'py'
        Name.Label:                "",          # class: 'nl'
        Name.Namespace:            YELLOW,      # class: 'nn' - to be revised
        Name.Other:                BLUE,        # class: 'nx'
        Name.Tag:                  AQUA,        # class: 'nt' - like a keyword
        Name.Variable:             RED,         # class: 'nv' - to be revised
        Name.Variable.Class:       YELLOW,          # class: 'vc' - to be revised
        Name.Variable.Global:      YELLOW,          # class: 'vg' - to be revised
        Name.Variable.Instance:    YELLOW,          # class: 'vi' - to be revised

        Number:                    BLUE,    # class: 'm'
        Number.Float:              "",        # class: 'mf'
        Number.Hex:                "",        # class: 'mh'
        Number.Integer:            "",        # class: 'mi'
        Number.Integer.Long:       "",        # class: 'il'
        Number.Oct:                "",        # class: 'mo'

        Literal:                   ORANGE,    # class: 'l'
        Literal.Date:              GREEN,     # class: 'ld'

        String:                    AQUA,       # class: 's'
        String.Backtick:           "",          # class: 'sb'
        String.Char:               FOREGROUND,  # class: 'sc'
        String.Doc:                COMMENT,     # class: 'sd' - like a comment
        String.Double:             "",          # class: 's2'
        String.Escape:             ORANGE,      # class: 'se'
        String.Heredoc:            "",          # class: 'sh'
        String.Interpol:           ORANGE,      # class: 'si'
        String.Other:              "",          # class: 'sx'
        String.Regex:              "",          # class: 'sr'
        String.Single:             "",          # class: 's1'
        String.Symbol:             "",          # class: 'ss'

        Generic:                   GREEN,                    # class: 'g'
        Generic.Deleted:           RED,                   # class: 'gd',
        Generic.Emph:              "italic",              # class: 'ge'
        Generic.Error:             "",                    # class: 'gr'
        Generic.Heading:           "bold " + FOREGROUND,  # class: 'gh'
        Generic.Inserted:          GREEN,                 # class: 'gi'
        Generic.Output:            "",                    # class: 'go'
        Generic.Prompt:            "bold " + COMMENT,     # class: 'gp'
        Generic.Strong:            "bold",                # class: 'gs'
        Generic.Subheading:        "bold " + AQUA,        # class: 'gu'
        Generic.Traceback:         "",                    # class: 'gt'
    }
