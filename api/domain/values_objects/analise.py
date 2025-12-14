


class Analise:
    
    # def __init__(self):
    #     #self.__s = SentimentIntensityAnalyzer()
        
        
        
    
    # def analisar_sentimento(self,texto:str):
    #     try:
    #         if not texto or texto.strip()== "" or texto.strip()=="-":
    #             return None
            
    #         resultado = self.__s.polarity_scores(texto)
    #         compound = resultado["compound"]
    #         norm = (compound+1)/2
    #         return norm
    #     except Exception as error:
    #         return None
        
    def sentimento_para_likert(score):
        if score is None:
            return None

        if score >= 0.75:
            return 5
        elif score >= 0.5:
            return 4
        elif score >= 0.4:
            return 3
        elif score >= 0.25:
            return 2
        else:
            return 1
        
    def calcular_likert(self, valor: int):       
        if valor is None:
            return None

        # Normaliza o valor para escala 0..1
        norm = (valor - 1) / (7 - 1)

        # Converte o normalizado para likert 1..5
        if norm >= 0.75:
            return 5
        elif norm >= 0.50:
            return 4
        elif norm >= 0.33:
            return 3
        elif norm >= 0.17:
            return 2
        else:
            return 1

    def calcular_favorabilidade(self,likerts):
        valores = [v for v in likerts if v is not None]

        if not valores:
            return {"favoravel_pct": 0, "neutro_pct": 0, "desfavoravel_pct": 0, "total_respostas": 0}

        total = len(valores)
        favoravel = sum(1 for v in valores if v in (4,5))
        neutro = sum(1 for v in valores if v == 3)
        desfavoravel = sum(1 for v in valores if v in (1,2))

        return {
            "favoravel_pct": round((favoravel / total) * 100, 2),
            "neutro_pct": round((neutro / total) * 100, 2),
            "desfavoravel_pct": round((desfavoravel / total) * 100, 2),
            "total_respostas": total
        }
        
    def calcular_enps(self,dados):
        notas = [item["enps"] for item in dados if item["enps"] is not None]

        total = len(notas)

        promotores = sum(1 for n in notas if n >= 9)
        neutros    = sum(1 for n in notas if 7 <= n <= 8)
        detratores = sum(1 for n in notas if n <= 6)

        enps = ((promotores - detratores) / total) * 100

        return {
            "total_respostas": total,
            "promotores": promotores,
            "neutros": neutros,
            "detratores": detratores,
            "enps": round(enps, 2)
        }