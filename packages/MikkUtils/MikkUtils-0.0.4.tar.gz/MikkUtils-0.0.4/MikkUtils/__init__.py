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

import os as __os__
from platform import system as __platform_system__
import struct as __struct__
from shutil import copy as __shutil_copy__
from json import loads as __json_loads__, dumps as __json_dumps__, load as __json_load__

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

    __OS__ = __platform_system__()

    if __OS__ == "Windows":
        __paths__ = [
            __os__.path.expandvars( r"%ProgramFiles(x86)%\Steam" ),
            __os__.path.expandvars( r"%ProgramFiles%\Steam" )
        ]

        for __path__ in __paths__:
            if __os__.path.exists( __path__ ):
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
            if __os__.path.exists( __path__ ):
                # Intentar obtener el directorio del ejecutable
                return __os__.path.dirname( __os__.path.abspath( __path__ ) )
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
        if __os__.path.exists( __HALFLIFE__ ):
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

            (dir_offset, dir_length) = __struct__.unpack('ii', header[4:])
            f.seek(dir_offset)
            dir_data = f.read(dir_length)

            num_files = dir_length // 64
            for i in range(num_files):
                entry = dir_data[i*64:(i+1)*64]
                name = entry[:56].rstrip(b'\x00').decode('latin-1')
                (offset, length) = __struct__.unpack('ii', entry[56:])
                self.__files__[name] = (offset, length)

    def extract(self, extract_to:str):
        '''
        Extract pak resources to the destination folder
        '''

        with open(self.__filename__, 'rb') as f:
            for name, (offset, length) in self.__files__.items():
                f.seek(offset)
                data = f.read(length)

                extract_path = __os__.path.join(extract_to, name)
                __os__.makedirs(__os__.path.dirname(extract_path), exist_ok=True)

                if __os__.path.exists(extract_path):
                    print(f"[pak] {name} exists. skipping...")
                    continue

                with open(extract_path, 'wb') as out_file:
                    out_file.write(data)

#========================================================
# Blue-Shift BSP Conversion
#========================================================

class __DHeader__:
    def __init__(self):
        self.version = 0
        self.lumps = [ [ 0, 0 ] for _ in range( 15 )]

def convert_blueshift_bsp( bsp_path : str, bsp_output : str ):
    '''
    Converts a Blue-Shift BSP to a generic goldsource BSP
    '''

    if bsp_path != bsp_output:
        __shutil_copy__( bsp_path, bsp_output )

    __LUMP_HEADER__ = 15
    __VERSION__ = 0
    __LUMPS__ = 1

    with open( bsp_output, 'rb+' ) as file:

        start = file.tell()

        if start == -1:
            raise Exception( f"Error getting start position in \"{file}\"" )

        header = [ 0, [ [ 0, 0 ] for _ in range( __LUMP_HEADER__ ) ] ]

        data = file.read( 4 + 8 * __LUMP_HEADER__ )
        header[__VERSION__] = __struct__.unpack('i', data[:4] )[0]

        for i in range( __LUMP_HEADER__ ):
            fileofs, filelen = __struct__.unpack( 'ii', data[ 4 + i * 8:4 + ( i + 1 ) * 8 ] )
            header[__LUMPS__][i] = [ fileofs, filelen ]
        
        if header[__LUMPS__][1][0] == 124:
            file.close() # Already converted, don't swap
            return

        header[__LUMPS__][0], header[__LUMPS__][1] = header[__LUMPS__][1], header[__LUMPS__][0]
        file.seek(start, __os__.SEEK_SET)

        data = __struct__.pack( 'i', header[__VERSION__] )
        for lump in header[__LUMPS__]:
            data += __struct__.pack('ii', lump[0], lump[1])

        file.write(data)

#========================================================
# starting, ending and midde wildcarding
#========================================================

def wildcard( compare : str, comparator : str, wildcard : str = '*' ) -> bool:
    '''
    Compare ``compare`` with ``comparator`` and see if they fully match or partial match by starting, ending or middle ``wildcard``
    '''
    if compare == comparator:
        return True

    elif wildcard not in comparator:
        return False

    __parts__ = comparator.split( wildcard )

    for __i__, __p__ in enumerate( __parts__ ):
        if __p__ == '':
            __parts__.pop( __i__ )

    __index__ : int = 0
    __matched__ : bool = True if len( __parts__ ) > 0 else False

    for __p__ in __parts__:
        if compare.find( __p__, __index__ ) < __index__:
            __matched__ = False
            break
        else:
            __index__ = compare.find( __p__, __index__ )

    return __matched__

#========================================================
# Entity, entity blocks from entity lumps
#========================================================

class Entity:
    '''
    Entity is basically a dict representing a entity block from a entity lump in a BSP

    Access any key-value with a dot, returns None if not set, set None to remove
    '''
    def __init__( self, KeyValueData=None ):
        self.KeyValueData = KeyValueData if isinstance( KeyValueData, dict ) else KeyValueData.ToDict() if isinstance( KeyValueData, Entity ) else {}

    def ToDict( self ):
        """
            Converts this Entity class to a dict.
        """
        return self.KeyValueData

    def get( self, value:str ):
        self.KeyValueData.get( value )

    def copy(self):
        return Entity( self.KeyValueData.copy() )

    def set( self, value:str ):
        self.KeyValueData[ value ] = value

    def pop( self, value:str ):
        self.KeyValueData.pop( value, '' )

    def __getattr__( self, key ):
        return str( self.KeyValueData.get( key, "" ) ) if key in self.KeyValueData else None

    def __setattr__( self, key, value ):
        if key == 'KeyValueData':
            super().__setattr__( key, value )
        elif value == None:
            self.KeyValueData.pop( key, '' )
        else:
            self.KeyValueData[ key ] = str( value )

    def remove( self ):
        """
        Removes this entity from the entity data
        """
        self.KeyValueData.clear()

    def __repr__(self):
        return str( self.KeyValueData )

#========================================================
# Ripent, BSP entity lump
#========================================================

__RIPENT_NONE__ = 0
__RIPENT_DATA__ = 1
__RIPENT_JSON__ = 2
__RIPENT_BSP__ = 3
__RIPENT_MAP__ = 4

class Ripent:
    '''
    Ripent, access to BSP's entity lumps
    '''
    def __init__( self, input : str | list[Entity] ):
        '''
        ``input`` Full path to a BSP, MAP or JSON file, it could also be a list[Entity] wich is the representation of the JSON format
        '''

        if isinstance( input, list ):
            self.format = __RIPENT_NONE__
        elif input.endswith( '.bsp' ):
            self.format = __RIPENT_BSP__
        elif input.endswith( '.map' ):
            self.format = __RIPENT_MAP__
        elif input.endswith( '.json' ):
            self.format = __RIPENT_JSON__
        else:
            self.format = __RIPENT_NONE__

        if isinstance( input, str ):
            self.path = input

    def __manipulate_lump__( self, ent_data = None ) -> list[Entity]:

        with open( self.path, 'rb+' ) as bsp_file:

            bsp_file.read(4) # BSP version.
            entities_lump_start_pos = bsp_file.tell()
            read_start = int.from_bytes( bsp_file.read(4), byteorder='little' )
            read_len = int.from_bytes( bsp_file.read(4), byteorder='little' )
            bsp_file.seek( read_start )

            if ent_data != None:

                newdata = ''

                for entblock in ent_data:

                    if isinstance( entblock, Entity ):
                        entblock = entblock.ToDict()

                    if len(entblock) <= 0:
                        continue

                    newdata += '{\n'
                    for key, value in entblock.items():
                        newdata += f'"{key}" "{value}"\n'
                    newdata += '}\n'

                writedata_bytes = newdata.encode('ascii')
                new_len = len(writedata_bytes)

                if new_len <= read_len:
                    bsp_file.write(writedata_bytes)
                    if new_len < read_len:
                        bsp_file.write(b'\x00' * (read_len - new_len))
                else:
                    bsp_file.seek(0, __os__.SEEK_END)
                    new_start = bsp_file.tell()
                    bsp_file.write(writedata_bytes)

                    bsp_file.seek(entities_lump_start_pos)
                    bsp_file.write(new_start.to_bytes(4, byteorder='little'))
                    bsp_file.write(new_len.to_bytes(4, byteorder='little'))
            else:

                map_entities:str
                entities_lump = bsp_file.read( read_len )

                try:
                    map_entities = entities_lump.decode('ascii', errors='strict').splitlines()
                except UnicodeDecodeError:
                    map_entities = entities_lump.decode('utf-8', errors='ignore').splitlines()
                    print( f'Possible broken entity data in a map, Check and patch "{self.path}"' )
                    #raise Warning( f'Possible broken entity data in a map, Check and patch "{self.path}"' )

                entblock = {}
                entdata = []
                oldline = ''

                for line in map_entities:

                    if line == '{':
                        continue

                    line = line.strip()

                    if not line.endswith( '"' ):
                        oldline = line
                    elif oldline != '' and not line.startswith( '"' ):
                        line = f'{oldline}{line}'

                    __LastIndex__ = 0
                    while line.find( '\\', __LastIndex__ ) != -1:
                        __LastIndex__ = line.find( '\\', __LastIndex__ )
                        if line[ __LastIndex__ -1 : __LastIndex__ ] != '\\' and line[ __LastIndex__ + 1 : __LastIndex__ + 2 ] != '\\':
                            line = line[ : __LastIndex__ + 1 ] + line[ __LastIndex__ : ]
                        __LastIndex__ += 2

                    line = line.strip( '"' )

                    if not line or line == '':
                        continue

                    if line.startswith( '}' ): # startswith due to [NULL]
                        try:
                            lump = __json_dumps__( entblock )
                            block = __json_loads__( lump )
                            entity = Entity( block )
                            entdata.append( entity )
                            entblock.clear()
                        except Exception:
                            entblock.clear()
                    else:
                        keyvalues = line.split( '" "' )
                        if len( keyvalues ) == 2:
                            entblock[ keyvalues[0] ] = keyvalues[1]
                return entdata
        return None

    def __write_json__( self, entdata ):

        __fformat__ = '.bsp' if self.format == __RIPENT_BSP__ else '.map' if self.format == __RIPENT_MAP__ else None

        if __fformat__:

            with open( self.path.replace( __fformat__, '.json' ), 'w' ) as jsonfile:

                jsonfile.write( '[\n' )
                FirstBlockOf = True
                FirstKeyOf = True

                for entblock in entdata:

                    if FirstBlockOf:
                        FirstBlockOf = False
                    else:
                        jsonfile.write( ',\n' )

                    FirstKeyOf = True

                    jsonfile.write( '\t{\n' )

                    for key, value in entblock.ToDict().items():

                        if FirstKeyOf:
                            FirstKeyOf = False
                        else:
                            jsonfile.write( ',\n' )

                        jsonfile.write( f'\t\t"{key}": "{value}"' )

                    jsonfile.write( '\n\t}' )

                jsonfile.write( '\n]\n' )
                jsonfile.close()

    # Dafuk why can not i name it "import" >:[
    def import_( self, entity_data : list[Entity] = None, delete_json : bool = False ):
        '''
        Import the entity data if this Ripent instance is a BSP or MAP file

        ``entity_data`` if **None** we'll look for a valid JSON file within the BSP/MAP Path

        ``delete_json`` if **True** delete the json file used, if any.
        '''

        if not entity_data:

            __fformat__ = '.bsp' if self.format == __RIPENT_BSP__ else '.map' if self.format == __RIPENT_MAP__ else None

            if __fformat__:

                jsonpath = self.path.replace( __fformat__, '.json' )

                if __os__.path.exists( jsonpath ):

                    with open( jsonpath, 'r' ) as jsonfile:
                        entity_data = __json_load__( jsonfile )
                        self.__manipulate_lump__( entity_data )
                        jsonfile.close()

                    if delete_json:
                        __os__.remove( jsonpath )

                else:
                    print( f"{jsonpath} Doesn't exists!" )

        else:
            self.__manipulate_lump__( entity_data )

    def export( self, create_json : bool = False ) -> list[Entity] | None:
        '''
        Export the entity data if this Ripent instance is a BSP or MAP file else returns **None**

        ``create_json`` if **True** a json file will be generated at the BSP/MAP destination
        '''

        if self.format != __RIPENT_MAP__ and self.format != __RIPENT_BSP__:
            return None

        entdata = self.__manipulate_lump__()

        if create_json:
            self.__write_json__( entdata )

        return entdata

    def __repr__(self):
        return '{' + f'\'format\': \'{self.format}\', \'path\': \'{self.path}\'' + '}'
