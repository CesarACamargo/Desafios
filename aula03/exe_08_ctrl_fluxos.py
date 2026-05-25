### Exercício 8. Filtragem de Dados Faltantes
# Objetivo:** Dada uma lista de dicionários representando dados de usuários, filtrar 
# aqueles que têm um campo específico faltando

usuarios = [
    {
        "id": 1,
        "nome": "Ana",
        "idade": 25,
        "email": "ana@email.com",
        "cidade": "São Paulo"
    },
    {
        "id": 2,
        "nome": "Carlos",
        "idade": 30,
        "cidade": "Rio de Janeiro"
    },
    {
        "id": 3,
        "nome": "Marina",
        "idade": 22,
        "email": "marina@email.com"
    },
    {
        "id": 4,
        "nome": "João",
        "email": "joao@email.com",
        "cidade": "Curitiba"
    },
    {
        "id": 5,
        "nome": "Fernanda",
        "idade": 28,
        "email": "fernanda@email.com",
        "cidade": "Belo Horizonte"
    },
    {
        "id": 6,
        "nome": "Pedro",
        "idade": 35
    }
]

# Filtrando usuarios com campos especificos faltando.
for x in usuarios:

    # Verifica se falta "email"
    if "email" not in x:
        print(f"\nUsuario {x['nome']} sem e-mail.")

    # Verifica se falta "idade"
    if "idade" not in x:
        print(f"\nUsuario {x['nome']} sem a idade informada.")

    # Verifica se falta "cidade"
    if "cidade" not in x:
        print(f"\nUsuario {x['nome']} sem a cidade informada.")
