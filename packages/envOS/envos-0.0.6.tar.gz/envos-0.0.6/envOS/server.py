from os import environ
import json

_SERVER:dict=None

class ENV:
  def __init__(self):
    '''Read system variables defined in settings.json'''
    global _SERVER
    if not _SERVER:
      with open(environ.get('envOS')) as key:
        _SERVER = json.load(key)

  # DEFAULT
  @property
  def RELOAD_SERVER_SETTINGS(self)->None:
    global _SERVER
    with open(environ.get('envOS')) as key:
      _SERVER = json.load(key)      
  @property
  def SERVER_SETTINGS(self)->dict:
    '''General configuration'''
    global _SERVER
    return _SERVER
  
  # SYSTEM
  @property
  def ENVIROMENT(self)->int:
    '''
    Runtime environment
    - localhost : `-1`
    - development : `0`
    - production : `1`
    '''
    global _SERVER
    return _SERVER['SYSTEM']['ENVIROMENT']   
    # PATHS WELLDOCS
  # PATHS WELLDOCS
  @property
  def FILES_WELLDOCS(self)->str:
    '''Welldocs system documents path'''
    global _SERVER
    return _SERVER['SYSTEM']['PATHS_WELLDOCS']['FILES_WELLDOCS']
  @property
  def ACCES_PUBLIC_WELLDOCS(self)->str:
    '''Welldocs folders with public visibility'''
    global _SERVER
    return _SERVER['SYSTEM']['PATHS_WELLDOCS']['PUBLIC_WELLDOCS']
    # PATHS SIR
  # PATHS SIR
  @property
  def CARGA_FACTURAS_EXCEL(self)->str:
    '''SIR folder where the excel files are exported to update the invoices'''
    global _SERVER
    return _SERVER['SYSTEM']['PATHS_SIR']['CARGA_FACTURAS_EXCEL']
  
  # SERVERS
  @property
  def URL_SERVER(self)->dict:
    '''
    Base URL for every servers
    - `WELLDOCS_INTER`
    - `WELLDOCS_PUBLIC`
    - `PYVERT_INTER`
    - `PYVERT_PUBLIC`
    - `WDAI_PUBLIC`
    '''
    global _SERVER
    return _SERVER['SERVERS']
  
  def URL_WELLDOCS(self, Option:str='PUBLIC')->str:
    '''
    Base URL
    - `INTER`
    - `PUBLIC`
    '''
    global _SERVER
    return _SERVER['SERVERS'][f'WELLDOCS_{Option}']
  
  def URL_PYVERT(self, Option:str='PUBLIC')->str:
    '''
    Base URL python server
    - `INTER`
    - `PUBLIC`
    '''
    global _SERVER
    return _SERVER['SERVERS'][f'PYVERT_{Option}']
  
  @property
  def URL_WDAI(self)->str:
    '''Base URL for wdai service'''
    global _SERVER
    return _SERVER['SERVERS']['WDAI_PUBLIC']
  
  # DATA_BASE
  @property
  def DB_WELLDOCS(self)->dict:
    '''Welldocs database credentials'''
    global _SERVER
    return _SERVER['DATA_BASE']['WELLDOCS']
  @property
  def DB_SIR(self)->str:
    '''SIR database credentials'''
    global _SERVER
    return _SERVER['DATA_BASE']['SIR']  
  
  # GOOGLE
  @property
  def POLLUX_STORAGE_KEY(self)->str:
    '''Key access for Pollux project'''
    global _SERVER
    return _SERVER['GOOGLE']['STORAGE']['KEY_POLLUX']
  