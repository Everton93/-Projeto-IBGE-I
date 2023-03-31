from dataclasses import dataclass
from Model.Estados import Estados

@dataclass
class Municipio():
        
    nomeMunicipio : str
    codigoMunicipio : int 
    estado : Estados