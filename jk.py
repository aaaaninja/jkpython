import dataclasses
import typing

@dataclasses.dataclass #(frozen=True)
class FuelClient:
    clientsecret: dataclasses.InitVar[str]
    clientid: dataclasses.InitVar[str]
    et_folder_client: str = dataclasses.field(init=False)
    def __post_init__(self, clientid, clientsecret):
        self.et_folder_client = clientid + clientsecret
        
    
    def ET_Folder(self) -> str:
        return self.et_folder_client

if __name__ == '__main__':
    f = FuelClient(clientid='asdf', clientsecret='hogehoge')
    print(f)