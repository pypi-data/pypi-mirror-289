"""
The MIT License (MIT)

Copyright (c) 2024 Mikk

Permission is hereby granted, free of charge, to any person obtaining a
copy of this software and associated documentation files (the "Software"),
to deal in the Software without restriction, including without limitation
the rights to use, copy, modify, merge, publish, distribute, sublicense,
and/or sell copies of the Software, and to permit persons to whom the
Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS
OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
DEALINGS IN THE SOFTWARE.
"""

import struct
import os
import re
import platform
from json import loads as __json_loads__

#========================================================
# jsonc
#========================================================

def jsonc( obj : list[str] | str ) -> dict | list:

    '''
    Loads a text file and skips single-line commentary before loading a json object
    '''

    __js_split__ = ''

    __lines__: list[str]

    if isinstance( obj, list ):
        __lines__ = obj
    else:
        __lines__ = open( obj, 'r' ).readlines()

    for __line__ in __lines__:

        __line__ = __line__.strip()

        if __line__ and __line__ != '' and not __line__.startswith( '//' ):

            __js_split__ = f'{__js_split__}\n{__line__}'

    return __json_loads__( __js_split__ )

#========================================================
# format
#========================================================

def format( string: str, arguments: list[str] | dict, cut_not_matched : bool = False ) -> str:
    '''
    Formats the given string replacing all the closed brackets with the corresponding indexes of arguments
    '''

    if isinstance( arguments, list ):

        for __arg__ in arguments:

            string = string.replace( "{}", str( __arg__ ), 1 )

        if cut_not_matched and string.find( '{}' ) != -1:

            string.replace( '{}', '' )

    elif isinstance( arguments, dict ):

        for __oarg__, __narg__ in arguments.items():

            string = string.replace( "{"+__oarg__+"}", str( __narg__ ) )

            #if cut_not_matched: -TODO find open-bracket and check until closes for removing
    else:

        raise Exception( 'arguments is not a list or dict')

    return string

#========================================================
# Vector
#========================================================

class Vector:
    '''
    Vector class
    '''
    def __init__( self, x:int|str=0, y=0, z=0 ):

        if isinstance( x, str ):

            __values__ = x.split( ',' ) if x.find( ',' ) != -1 else x.split()

            if len( __values__ ) < 3:
                __values__ += [ '0' ] * ( 3 - len( __values__ ) )

            self.x, self.y, self.z = [ self.__parse_value__(v) for v in __values__[:3] ]

        else:
            self.x = self.__parse_value__(x) if isinstance( x, ( float, int ) ) else 0
            self.y = self.__parse_value__(y) if isinstance( y, ( float, int ) ) else 0
            self.z = self.__parse_value__(z) if isinstance( z, ( float, int ) ) else 0

    def __parse_value__( self, __value__ ):

        __value__ = float( __value__ )

        if __value__.is_integer() or __value__ == int( __value__ ):

            return int( __value__ )
        
        return __value__

    def to_string( self, quoted : bool = False ):
        '''
        Converts the vector to string
        
        ``quoted`` if true, returns separating each number by a quote
        '''
        _y = str(self.y).split('.')[0] if str(self.y).endswith( '.0' ) else self.y
        _z = str(self.z).split('.')[0] if str(self.z).endswith( '.0' ) else self.z
        _x = str(self.x).split('.')[0] if str(self.x).endswith( '.0' ) else self.x

        if quoted:
            return f'{_x}, {_y}, {_z}'
        return f'{_x} {_y} {_z}'

    def __add__(self, other):

        return Vector(self.x + other.x, self.y + other.y, self.z + other.z)

    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y, self.z - other.z)

    def __mul__(self, scalar):
        if isinstance( scalar, Vector ):
            return Vector(self.x * scalar.x, self.y * scalar.y, self.z * scalar.z)
        return Vector(self.x * scalar, self.y * scalar, self.z * scalar)

    def __eq__( self, other ):
        if isinstance( other, Vector):
            return ( self.x == other.x and self.z == other.z and self.y == other.y )
        return False

    def __ne__( self, other ):
        return not self.__eq__(other)

    def __getitem__( self, ang ):

        if ang == 0:
            return self.x

        elif ang == 1:
            return self.y

        elif ang == 2:
            return self.z

        else:
            raise Exception(f"No matching {ang}")

    def __setitem__(self, ang, new):

        if ang == 0:
            self.x = self.__parse_value__( new )

        elif ang == 1:
            self.y = self.__parse_value__( new )

        elif ang == 2:
            self.z = self.__parse_value__( new )

        else:
            raise Exception(f"No matching {ang}")

    def __repr__(self):
        return f"Vector( {self.x}, {self.y}, {self.z} )"

#========================================================
# Steam Path
#========================================================

def STEAM() -> str:

    '''
    Get steam's installation path
    '''

    __OS__ = platform.system()

    if __OS__ == "Windows":
        __paths__ = [
            os.path.expandvars( r"%ProgramFiles(x86)%\Steam" ),
            os.path.expandvars( r"%ProgramFiles%\Steam" )
        ]

        for __path__ in __paths__:
            if os.path.exists( __path__ ):
                return __path__

        try:
            import winreg
            with winreg.OpenKey(winreg.HKEY_CURRENT_USER, r"Software\Valve\Steam") as key:
                return winreg.QueryValueEx(key, "SteamPath")[0]
        except (ImportError, FileNotFoundError, OSError, PermissionError):
            return None

    elif __OS__ == "Linux":
        __paths__ = [
            "/usr/bin/steam",
            "/usr/local/bin/steam"
        ]    

        for __path__ in __paths__:
            if os.path.exists( __path__ ):
                # Intentar obtener el directorio del ejecutable
                return os.path.dirname( os.path.abspath( __path__ ) )
        return None

    else:
        raise NotImplementedError(f"Unsupported Operative System {__OS__}")

def HALFLIFE() -> str:
    '''
    Get "Half-Life" folder within a steam installation
    '''

    __STEAM__ = STEAM()

    if __STEAM__:
        __HALFLIFE__ = f'{__STEAM__}\steamapps\common\Half-Life'
        if os.path.exists( __HALFLIFE__ ):
            return __HALFLIFE__

    try:
        from __main__ import halflife
        return halflife
    except Exception:
        raise Exception( 'Can not find Steam installation\nPlease define halflife="(Path to halflife) in the main script.')


#========================================================
# pak
#========================================================

class pak:
    '''
    Manage .pak files
    '''

    def __init__(self, filename):
        self.__filename__ = filename
        self.__files__ = {}
        self.__read_pak_file__()

    def __read_pak_file__(self):
        with open(self.__filename__, 'rb') as f:
            header = f.read(12)
            if header[:4] != b'PACK':
                raise ValueError('Not a valid PAK file')

            (dir_offset, dir_length) = struct.unpack('ii', header[4:])
            f.seek(dir_offset)
            dir_data = f.read(dir_length)

            num_files = dir_length // 64
            for i in range(num_files):
                entry = dir_data[i*64:(i+1)*64]
                name = entry[:56].rstrip(b'\x00').decode('latin-1')
                (offset, length) = struct.unpack('ii', entry[56:])
                self.__files__[name] = (offset, length)

    def extract(self, extract_to:str):
        '''
        Extract pak resources to the destination folder
        '''

        with open(self.__filename__, 'rb') as f:
            for name, (offset, length) in self.__files__.items():
                f.seek(offset)
                data = f.read(length)

                extract_path = os.path.join(extract_to, name)
                os.makedirs(os.path.dirname(extract_path), exist_ok=True)

                if os.path.exists(extract_path):
                    print(f"[pak] {name} exists. skipping...")
                    continue

                with open(extract_path, 'wb') as out_file:
                    out_file.write(data)
