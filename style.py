import matplotlib.pyplot as plt
import os
class BaseStyle:
    '''Base class for handling styles'''
    def __init__(self,style_dict):
        self._style_dict = style_dict
    @property
    def get_attribute(self, attribute):
        '''Returns the value of the attribute in the style dictionary'''
        return self._style_dict[attribute]
class MatplotlibStyle(BaseStyle):
    '''Class for handling styles in matplotlib'''
    def __init__(self,style_dict):
        super().__init__(style_dict)
        self._matplotlib_style_dict = self._convert_dict()
    def _convert_dict(self):
        '''Converts base style dictionary to one for use in matplotlib.'''
        #At present, these are identical, but this is included for future extension
        new_dict = dict()
        for key, value in self._style_dict.items():
            new_dict[key] = value
        return new_dict
    def set_style(self):
        '''Sets the rcParams in matplotlib to the values in the style dictionary'''
        for key, value in self._matplotlib_style_dict.items():
            mpl_keys = self.matplotlib_key_update(key)
            for mpl_key in mpl_keys:
                plt.rcParams[mpl_key] = value
    def export_style_sheet(self, filename):
        '''Exports the style sheet to a file'''
        base, ext = os.path.splitext(filename)
        with open(filename+".mplstyle", "w") as file:
            for key, value in self._matplotlib_style_dict.items():
                file.write(f"{key} : {value}\n")
    def use_style_sheet(self, filename):
        '''Loads style sheet ".mplstyle" file'''
        plt.style.use(filename)
    @staticmethod
    def matplotlib_key_update(key):
        if key == "default_fontsize": #default_fontsize must be listed first in style dictionary such that it is overwritten if desired
                return_keys = ("font.size",
                               "axes.titlesize", "axes.labelsize",
                               "figure.titlesize", "figure.labelsize",
                               "xtick.labelsize", "ytick.labelsize",
                               "legend.fontsize")
        else:
            return_keys = (key,)
        return return_keys