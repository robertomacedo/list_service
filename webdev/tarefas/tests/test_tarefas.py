from django.urls import reverse


def test_status_code(client):
    resposta = client.get(reverse('tarefas:home'))
    assert resposta.status_code == 200
