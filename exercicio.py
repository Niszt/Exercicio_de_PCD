from abc import ABC, abstractmethod

class Observador(ABC):
    @abstractmethod
    def analisar_dados(self, estado: str, nome_rio: str, temperatura: float, ph: float, ura: float, pa: float):
        pass

class PCD_Abstrato(ABC): 
    @abstractmethod
    def add_universidades(self, universidade: Observador):
        pass
        
    @abstractmethod
    def rmv_universidade(self, universidade: Observador):
        pass
        
    @abstractmethod
    def notificar_universidades(self):
        pass

class Universidade(Observador):
    def __init__(self, nome: str, estado_sede: str):
        self.nome = nome
        self.estado_sede = estado_sede
    def analisar_dados(self, estado_rio: str, nome_rio: str, temperatura: float, ph: float, ura: float, pa: float):
        print(f"[{self.nome} - Sede: {self.estado_sede}] Analisando novos dados do {nome_rio} ({estado_rio})..")

        if temperatura > 25.0:
            print(f"Temp. subiu para {temperatura}C")
        if ura < 50.0:
            print(f"Umidade (URA) caiu para {ura}%")
        if ph < 6.5 or ph > 8.5:
            print(f" pH fora do padrao: {ph}")
        if pa < 1000.0:
            print(f"  Pressao atmosférica baixa ({pa} hPa). Possibilidade de chuvas fortes.")
            
        print("-_-_" * 15)


class RioPCD(PCD_Abstrato):
    def __init__(self, nome_rio: str, estado: str):
        self.nome_rio = nome_rio
        self.estado = estado
        self.temperatura = 0.0
        self.ura = 0.0
        self.ph = 0.0
        self.pa = 0.0
        self._universidades_inscritas = []

    def add_universidades(self, universidade: Observador):
        self._universidades_inscritas.append(universidade)
        print(f"{universidade.nome} agora está monitorando o {self.nome_rio}.")

    def rmv_universidade(self, universidade: Observador):
        self._universidades_inscritas.remove(universidade)

    def notificar_universidades(self):
        for universidade in self._universidades_inscritas:
            universidade.analisar_dados(
                self.estado, 
                self.nome_rio, 
                self.temperatura, 
                self.ph, 
                self.ura, 
                self.pa
            )

    def atualizar_sensores(self, nova_temp: float, novo_ph: float, nova_ura: float, nova_pa: float):
        print(f"\nPCD do {self.nome_rio} registrou dados: Temp {nova_temp}°C | pH {novo_ph} | URA {nova_ura}% | PA {nova_pa}hPa")
        self.temperatura = nova_temp
        self.ph = novo_ph
        self.ura = nova_ura
        self.pa = nova_pa
        
        self.notificar_universidades()

if __name__ == "__main__":
   

    rio_amazonas = RioPCD("Rio Amazonas", "Amazonas")
    rio_negro = RioPCD("Rio Negro", "Amazonas")
    ufam = Universidade("UFAM", "Amazonas")
    usp = Universidade("USP", "Sao Paulo")
    unb = Universidade("UnB", "Distrito Federal")
    unifesp = Universidade("UNIFESP", "Sao Paulo")
    
    rio_amazonas.add_universidades(ufam)
    rio_negro.add_universidades(ufam)
    rio_amazonas.add_universidades(usp)
    rio_amazonas.add_universidades(unifesp)
    rio_negro.add_universidades(unb)

    rio_amazonas.atualizar_sensores(nova_temp=26.5, novo_ph=7.0, nova_ura=85.0, nova_pa=1012.0)
    rio_negro.atualizar_sensores(nova_temp=31.2, novo_ph=5.8, nova_ura=45.0, nova_pa=998.0)
