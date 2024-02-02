import sqlite3


class Sqlite:

    def __init__(self):
        self.clean_errors = []
        self.rows = []
        self.columns = []
        
        # Conectar ao banco de dados (isso cria o arquivo se não existir)
        self.conn = sqlite3.connect('dados.db')

        # Criar um cursor para executar comandos SQL
        self.cursor = self.conn.cursor()
        
        self.lerPrimeiroElemento()
        #self.criarTabela()
        #self.lerCSV()
        #self.connectAndcursor()
        #self.adicionarLinhas()
    

    def criarTabela(self):
        # Verificar se a tabela já existe
        self.cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='dec_fec'")
        tabela_existe = self.cursor.fetchone()

        if tabela_existe:
            print("A tabela dec_fec já existe.")
        else:
            # Criar a tabela com as colunas especificadas se ela não existir
            self.cursor.execute('''
                CREATE TABLE dec_fec (
                    DatGeracaoConjuntoDados TEXT,
                    SigAgente TEXT,
                    NumCNPJ TEXT,
                    IdeConjUndConsumidoras TEXT,
                    DscConjUndConsumidoras TEXT,
                    SigIndicador TEXT,
                    AnoIndice TEXT,
                    NumPeriodoIndice INTEGER,
                    VlrIndiceEnviado REAL
                )
            ''')
            print("A tabela dec_fec foi criada.")

            self.commitAndclose()

    def commitAndclose(self):    
        # Commit para salvar as alterações
        self.conn.commit()

        # Fechar a conexão
        self.conn.close()
    
    def connectAndcursor(self):
        # Conectar ao banco de dados (isso cria o arquivo se não existir)
        self.conn = sqlite3.connect('dados.db')

        # Criar um cursor para executar comandos SQL
        self.cursor = self.conn.cursor()

    def lerCSV(self):

        errors = []

        with open('indicadores-continuidade-coletivos-2020-2029.csv', 'rb') as fz:
            data = fz.readlines()

        for row in data:
            try:
                decoded = row.decode('utf-8')
            except Exception as e:
                errors.append(row)
                continue

            # Assuming you want to replace 'Vrin' with an empty string and split by ';'
            cleaned_row = decoded.replace('Vrin', '').split(';')
            
            self.rows.append(cleaned_row)

        #print('Errors:', len(self.errors))
        #print('Rows:', len(self.rows))

        for error in errors:
            row = ''.join(chr(i) for i in error[:-2])
            self.clean_errors.append(row.split(';'))


    def adicionarLinhas(self):

        self.columns = self.rows.pop(0)

        for row in self.rows:
            values = tuple(row)
            placeholders = ', '.join(['?'] * len(values))
            self.cursor.execute(f"INSERT INTO dec_fec ({', '.join(self.columns)}) VALUES ({placeholders})", values)
        
        for error_row in self.clean_errors:
            values = tuple(error_row)  # Usar tupla como valores
            placeholders = ', '.join(['?'] * len(values))
            self.cursor.execute(f"INSERT INTO dec_fec ({', '.join(self.columns)}) VALUES ({placeholders})", values)
        
        self.commitAndclose()

    def lerPrimeiroElemento(self):
        
        # Ler o primeiro elemento da tabela dec_fec
        self.cursor.execute("SELECT * FROM dec_fec LIMIT 1")
        primeiro_elemento = self.cursor.fetchone()

        if primeiro_elemento:
            print("Primeiro elemento da tabela:")
            print(primeiro_elemento)
        else:
            print("A tabela está vazia.")

sqlite = Sqlite()