# Sistema de controle de estoque
controle de estoque

## Como rodar o projeto?
Clone esse repositório.
Crie um virtualenv com Python 3.
Ative o virtualenv.
Instale as dependências.
Rode as migrações.

git clone https://github.com/jonathan-mothe/estoque.git <br>
cd estoque <br>
python3 -m venv .venv <br>
source .venv/bin/activate <br>
pip install -r requirements.txt <br>
python contrib/env_gen.py <br>
python manage.py migrate <br>
python manage.py createsuperuser <br>
python manage.py runserver <br>
