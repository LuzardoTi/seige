from django.db import models

# ========================
# ALUNO
# ========================
class Aluno(models.Model):

    SEXO_CHOICES = [
        ('M', 'Masculino'),
        ('F', 'Feminino'),
        ('O', 'Outro'),
    ]

    RACA_CHOICES = [
        ('branca', 'Branca'),
        ('preta', 'Preta'),
        ('parda', 'Parda'),
        ('amarela', 'Amarela'),
        ('indigena', 'Indígena'),
        ('nao_declarada', 'Não declarada'),
    ]

    nome = models.CharField(max_length=200)
    cpf = models.CharField(max_length=14, unique=True)
    rg = models.CharField(max_length=20)

    orgao_expedidor = models.CharField(max_length=50)
    data_expedicao_rg = models.DateField()

    data_nascimento = models.DateField()
    sexo = models.CharField(max_length=1, choices=SEXO_CHOICES)
    raca_cor = models.CharField(max_length=20, choices=RACA_CHOICES)

    pcd = models.BooleanField(default=False)

    nome_pai = models.CharField(max_length=200, blank=True, null=True)
    nome_mae = models.CharField(max_length=200)

    naturalidade = models.CharField(max_length=100)
    nacionalidade = models.CharField(max_length=100)

    email = models.EmailField()
    telefone = models.CharField(max_length=20)

    endereco = models.CharField(max_length=255)
    cidade = models.CharField(max_length=100)
    estado = models.CharField(max_length=50)

    foto = models.ImageField(upload_to='fotos_alunos/', blank=True, null=True)

    ativo = models.BooleanField(default=True)

    def __str__(self):
        return self.nome


# ========================
# POLO (EAD / UNIDADE)
# ========================
class Polo(models.Model):
    nome = models.CharField(max_length=200)
    cidade = models.CharField(max_length=100)
    estado = models.CharField(max_length=50)

    def __str__(self):
        return self.nome


# ========================
# CURSO
# ========================
class Curso(models.Model):

    TIPO_CURSO = [
        ('graduacao', 'Graduação'),
        ('pos', 'Pós-graduação'),
        ('capacitacao', 'Capacitação'),
    ]

    MODALIDADE = [
        ('ead', 'EAD'),
        ('presencial', 'Presencial'),
    ]

    nome = models.CharField(max_length=200)
    tipo = models.CharField(max_length=20, choices=TIPO_CURSO)
    modalidade = models.CharField(max_length=20, choices=MODALIDADE)

    carga_horaria = models.IntegerField()

    def __str__(self):
        return self.nome


# ========================
# DISCIPLINA
# ========================
class Disciplina(models.Model):
    nome = models.CharField(max_length=200)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    carga_horaria = models.IntegerField()

    def __str__(self):
        return self.nome


# ========================
# MATRÍCULA
# ========================
class Matricula(models.Model):

    STATUS = [
        ('ativa', 'Ativa'),
        ('trancada', 'Trancada'),
        ('cancelada', 'Cancelada'),
        ('concluida', 'Concluída'),
    ]

    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    polo = models.ForeignKey(Polo, on_delete=models.SET_NULL, null=True)

    semestre = models.CharField(max_length=10)  # Ex: 2026.1

    status = models.CharField(max_length=20, choices=STATUS, default='ativa')

    data_matricula = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.aluno} - {self.curso}"
