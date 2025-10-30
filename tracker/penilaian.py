class Penilaian:
    def __init__(self):
        self._quiz = 0
        self._tugas = 0
        self._uts = 0
        self._uas = 0

    def _validate_score(self, nilai):
        if 0 <= nilai <= 100:
            return float(nilai)
        return None
    
    @property
    def quiz(self): 
        return self._quiz

    @quiz.setter
    def quiz(self, nilai):
        v = self._validate_score(nilai)
        if v is not None: self._quiz = v

    @property
    def tugas(self): 
        return self._tugas
    
    @tugas.setter
    def tugas(self, nilai):
        v = self._validate_score(nilai)
        if v is not None: self._tugas = v

    @property
    def uts(self): 
        return self._uts
    
    @uts.setter
    def uts(self, nilai):
        v = self._validate_score(nilai)
        if v is not None: self._uts = v

    @property
    def uas(self): 
        return self._uas

    @uas.setter
    def uas(self, nilai):
        v = self._validate_score(nilai)
        if v is not None: self._uas = v
        
    def nilai_akhir(self):
        return (self._quiz*0.15) + (self._tugas*0.25) + (self._uts*0.25) + (self._uas*0.35)
