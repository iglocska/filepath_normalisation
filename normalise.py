import re

class Normalise:
    def normalise(self, value):
        for rule in self.regex_rules:
            if rule['prefilter'] and rule['prefilter'] in value:
                value = re.sub(rule['regex'], rule['replacement'], value)
        return value


    regex_rules = [
        {
            'regex': r'.:.ProgramData.',
            'replacement': '%ALLUSERSPROFILE%\\\\',
            'prefilter': 'ProgramData'
        },
        {
            'regex': r'.:.Documents and Settings.All Users.',
            'replacement': '%ALLUSERSPROFILE%\\\\',
            'prefilter': 'Documents and Settings'
        },
        {
            'regex': r'.:.Program Files.Common Files.',
            'replacement': '%COMMONPROGRAMFILES%\\\\',
            'prefilter': 'Program Files\\Common Files'
        },
        {
            'regex': r'.:.Program Files (x86).Common Files.',
            'replacement': '%COMMONPROGRAMFILES(x86)%\\',
            'prefilter': 'Program Files (x86)\\Common Files'
        },
        {
            'regex': r'.:.Users\\(.*?)\\AppData.Local.Temp.',
            'replacement': '%TEMP%\\',
            'prefilter': 'AppData\\Local\\Temp'
        },
        {
            'regex': r'.:.ProgramData.',
            'replacement': '%PROGRAMDATA%\\\\',
            'prefilter': 'ProgramData'
        },
        {
            'regex': r'.:.Program Files.',
            'replacement': '%PROGRAMFILES%\\\\',
            'prefilter': 'Program Files'
        },
        {
            'regex': r'.:.Program Files (x86).',
            'replacement': '%PROGRAMFILES(X86)%\\\\',
            'prefilter': 'Program Files (x86)'
        },
        {
            'regex': r'.:.Users.Public.',
            'replacement': '%PUBLIC%\\',
            'prefilter': 'Users\Public'
        },
        {
            'regex': r'.:.Documents and Settings\\(.*?)\\Local Settings.Temp.',
            'replacement': '%TEMP%\\\\',
            'prefilter': 'Local Settings\\Temp'
        },
        {
            'regex': r'.:.Users\\(.*?)\\AppData.Local.Temp.',
            'replacement': '%TEMP%\\\\',
            'prefilter': 'AppData\Local\\Temp'
        },
        {
            'regex': r'.:.Users\\(.*?)\\AppData.Local.',
            'replacement': '%LOCALAPPDATA%\\\\',
            'prefilter': 'AppData\\Local'
        },
        {
            'regex': r'.:.Users\\(.*?)\\AppData.Roaming.',
            'replacement': '%APPDATA%\\\\',
            'prefilter': 'AppData\\Roaming'
        },
        {
            'regex': r'.:.Users\\(.*?)\\Application Data.',
            'replacement': '%APPDATA%\\\\',
            'prefilter': 'Application Data'
        },
        {
            'regex': r'.:.Windows\\(.*?)\\Application Data.',
            'replacement': '%APPDATA%\\\\',
            'prefilter': 'Application Data'
        },
        {
            'regex': r'.:.Users\\(.*?)',
            'replacement': '%USERPROFILE%\\\\',
            'prefilter': 'Users'
        },
        {
            'regex': r'.:.DOCUME~1.\\(.*?)',
            'replacement': '%USERPROFILE%\\\\',
            'prefilter': 'DOCUME~1'
        },
        {
            'regex': r'.:.Documents and Settings\\(.*?)',
            'replacement': '%USERPROFILE%\\\\',
            'prefilter': 'Documents and Settings'
        },
        {
            'regex': r'.:.Windows.',
            'replacement': '%WINDIR%\\\\',
            'prefilter': 'Windows'
        },
        {
            'regex': r'.REGISTRY.USER.S(-[0-9]{1}){2}-[0-9]{2}(-[0-9]{9}){1}(-[0-9]{10}){1}-[0-9]{9}-[0-9]{4}',
            'replacement': 'HKCU',
            'prefilter': 'REGISTRY\\USER\\S'
        },
        {
            'regex': r'.REGISTRY.USER.S(-[0-9]{1}){2}-[0-9]{2}(-[0-9]{10}){2}-[0-9]{9}-[0-9]{4}',
            'replacement': 'HKCU',
            'prefilter': 'REGISTRY\\USER\\S'
        },
        {
            'regex': r'.REGISTRY.USER.S(-[0-9]{1}){2}-[0-9]{2}(-[0-9]{10}){3}-[0-9]{4}',
            'replacement': 'HKCU',
            'prefilter': 'REGISTRY\\USER\\S'
        },
        {
            'regex': r'.REGISTRY.MACHINE.',
            'replacement': 'HKLM\\\\',
            'prefilter': 'REGISTRY\\MACHINE'
        },
        {
            'regex': r'.Registry.Machine.',
            'replacement': 'HKLM\\\\',
            'prefilter': 'Registry\\Machine'
        }
    ]

