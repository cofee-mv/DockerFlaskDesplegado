from sample_app import sample

def test_home_status_200():
    cliente = sample.test_client()
    respuesta = cliente.get('/')
    assert respuesta.status_code == 500
    

