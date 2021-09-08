''' 
This file defines the active entities of the application
Those entities are the ones who initialize a transaction and therefore
the ones who are going to receive intermediate and final KPI's
'''

class ConsultantClass():
    '''Travel Agent'''

    consultantId: str
    consultantPosition: str #Junior, Pleno ou Senior

    mainAssignment: str # Principais atribuições do consultor (Nac, Inter, Nac+Inter, Multiplicador, Emissão)
    taskList: dict
    
    associatedAccountIds: dict # Valores de accountId atualmente associados ao consultor
    associatedAccountIds

    

class AccountClass():
    '''Client group, served company''' 
    
    accountId: str
    taskList: dict

    accountSize: str # Local, Regional, Global ou PME
    pricingCategory: str # Transacional, consultivo ou simples

    associatedBranchOfficeIds: dict # Geralmente cada conta contém apenas uma chave ('ID') e valor ('int')
    serviceType: str # OBT ou FULLSERVICE (Offline)

    
class BranchOfficeClass():
    '''PT-BR: Filial'''
    
    branchId: str
    taskList: dict

class BusinessUnityClass():
    '''Sales Representative
    PT-BR: Representantes comerciais (terceiros)'''

    businessUnityId: str
    taskList: dict