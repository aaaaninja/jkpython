from dataclasses import dataclass, field, InitVar
import typing

@dataclass(frozen=True)
class FuelClient:
    clientsecret: InitVar[str]
    clientid: InitVar[str]
    et_folder_client: str = field(init=False)
    def __post_init__(self, clientid, clientsecret):
        object.__setattr__(self, 'et_folder_client', clientid + clientsecret)
        
    
    def ET_Folder(self) -> str:
        return self.et_folder_client

if __name__ == '__main__':
    f = FuelClient(clientid='asdf', clientsecret='hogehoge')
    print(f)