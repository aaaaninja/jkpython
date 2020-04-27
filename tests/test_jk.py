from jk import FuelClient

def test_get_name():
    assert FuelClient(clientid="asdf", clientsecret="hohoh").et_folder_client == "hohohasdf"
