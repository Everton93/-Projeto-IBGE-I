
from Municipio import Municipio

from dataclasses import dataclass

@dataclass
class MunicipioInfo():
    
        municipio : Municipio  
        prefeito : str
        gentílico : str               
        areaTerritorial : int
        populacaoEstimada : int 
        densidadeDemografica : int
        escolarizacao : int
        indiceDesenvolvimentoHumanoMunicipal : int
        mortalidadeInfantil : int
        receitasRealizadas : int
        receitasEmpenhadas : int
        pibPerCapita : int