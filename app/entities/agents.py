'''
This file defines the active entities of the application
Those entities are the ones who initialize a transaction and therefore
the ones who are going to receive intermediate and final KPI's
'''

class SingleAgentClass():
    '''The person associated to a given Task'''

    agentId: str
    agentPosition: str #Junior, Pleno ou Senior

    mainAssignment: str # Principais atribuições do consultor (Nac, Inter, Nac+Inter, Multiplicador, Emissão)
    taskList: dict

    associatedAccountIds: dict # Valores de accountId atualmente associados ao consultor

    agentRate: int # A target variable, represents the agent’s final score


class AccountClass():
    '''Client group, served company
    It’s score is updated whenever an associated single agent gets new points'''

    accountId: str
    taskList: dict

    accountSize: str # Local, Regional, Global ou PME
    pricingCategory: str # Transacional, consultivo ou simples

    associatedBranchOfficeIds: dict # Geralmente cada conta contém apenas uma chave ('ID') e valor ('int')
    serviceType: str # OBT ou FULLSERVICE (Offline)

    accountRate: int # A target variable, represents the agent’s final score


class BranchOfficeClass():
    '''PT-BR: Filial'''

    branchId: str
    taskList: dict

    branchOfficeRate: int # A target variable, represents the agent’s final score

class BusinessUnityClass():
    '''Third Party Sales Representative
    PT-BR: Representantes comerciais (terceiros)'''

    businessUnityId: str
    taskList: dict
