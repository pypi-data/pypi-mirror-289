from ActionKeyword.CheckActionKeywordApp import VerificationKeywords
from ActionKeyword.ClickActionKeywordApp import ClickKeywords
from ActionKeyword.InputActionKeywordApp import InputActionKeywords
from ActionKeyword.ScrollActionKeywordApp import ScrollActionKeywords
from ActionKeyword.SelectActionKeywordApp import SelectActionKeywords
from ComponentKeyword.LoginPageComponentKeywordApp import LoginPageComponentKeywords
from DataTypeKeyword.StringDataTypeKeywordApp import StringDataTypeKeywords
from UtilKeyword.JsonKeywordApp import JsonKeywords
from UtilKeyword.ReplaceElementUtilKeywordApp import ReplaceElementUtilKeywords
from AppiumLibrary import AppKeywords
from Settings.CommonSetting import CommonSetting
from Settings.ConstantAppSetting import ConstantAppSetting
from Settings.ConstantSetting import ConstantSetting

class MobileAutomationLibrary(VerificationKeywords, ClickKeywords, InputActionKeywords, ScrollActionKeywords, SelectActionKeywords, LoginPageComponentKeywords, StringDataTypeKeywords, JsonKeywords, ReplaceElementUtilKeywords, AppKeywords):
    """Biblioteca de automação mobile para uso com Robot Framework"""

    def __init__(self):
        VerificationKeywords.__init__(self)
        ClickKeywords.__init__(self)
        InputActionKeywords.__init__(self)
        ScrollActionKeywords.__init__(self)
        SelectActionKeywords.__init__(self)
        LoginPageComponentKeywords.__init__(self)
        StringDataTypeKeywords.__init__(self)
        JsonKeywords.__init__(self)
        ReplaceElementUtilKeywords.__init__(self)
        AppKeywords.__init__(self)
