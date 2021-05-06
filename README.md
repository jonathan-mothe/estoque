# Sistema de controle de estoque
controle de estoque

## Como rodar o projeto?
Clone esse repositório.
Crie um virtualenv com Python 3.
Ative o virtualenv.
Instale as dependências.
Rode as migrações.

git clone https://github.com/jonathan-mothe/estoque.git
cd estoque
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python contrib/env_gen.py
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
