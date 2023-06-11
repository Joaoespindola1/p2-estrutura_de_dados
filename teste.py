import sqlite3

banco = sqlite3.connect('exemplo.db')

# Crie um cursor para executar comandos SQL
leitor = banco.cursor()

sql_create_table = '''
    CREATE TABLE IF NOT EXISTS person (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        first_name VARCHAR(50) NOT NULL,
        last_name VARCHAR(50) NOT NULL,
        email VARCHAR(150) NOT NULL,
        number VARCHAR(11) NOT NULL
    )
'''

# Execute o script para criar a tabela
leitor.execute(sql_create_table)

#adicionando valores

dados =  (
    input('Escreva o primeiro nome: '),
    input('Escreva o último nome: '),
    input('Escreva o email: '),
    input('Escreva o número: ')
)
leitor.execute('INSERT INTO person (first_name, last_name, email, number) VALUES (?, ?, ?, ?)', dados)
banco.commit() #salvando alteração

#lendo a tabela
read = leitor.fetchall()

for read in leitor.execute('SELECT * FROM person'):
    print(read)

banco.close()