#========================================================================================================================================
# CyborgAI CC BY-NC-ND 4.0 Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International  https://github.com/cyborg-ai-git 
#========================================================================================================================================

from evo_framework import *
from evo_package_assistant.entity import *
from evo_framework.core.evo_core_api.entity.EApiQuery import EApiQuery

#<
#OTHER IMPORTS ...
#>
# ---------------------------------------------------------------------------------------------------------------------------------------
# UAssistantApi
# ---------------------------------------------------------------------------------------------------------------------------------------
"""UAssistantApi
"""
class UAssistantApi():
    __instance = None
# ---------------------------------------------------------------------------------------------------------------------------------------
    def __init__(self):   
        if UAssistantApi.__instance != None:
            raise Exception("ERROR:SINGLETON")
        else:
            super().__init__()
            UAssistantApi.__instance = self
            self.currentPath = os.path.dirname(os.path.abspath(__file__))
            
# ---------------------------------------------------------------------------------------------------------------------------------------
    """getInstance Singleton

    Raises:
        Exception:  api exception

    Returns:
        _type_: UAssistantApi instance
    """
    @staticmethod
    def getInstance():
        if UAssistantApi.__instance is None:
            uObject = UAssistantApi()  
            uObject.doInit()  
        return UAssistantApi.__instance
# ---------------------------------------------------------------------------------------------------------------------------------------
    """doInit

    Raises:
        Exception: api exception

    Returns:

    """   
    def doInit(self):   
        try:
#<
            #INIT ...
            pass
#>   
        except Exception as exception:
            IuLog.doException(__name__,exception)
            raise
# ---------------------------------------------------------------------------------------------------------------------------------------
    async def doOnSet(self, eAction:EAction) -> EAction:
        """doOnSet utility callback
            input: EAssistantAdmin
            output: EAssistant

            Raises:
                Exception: api exception

            Returns:
                EAction:  EObject 
        """   
        try:

            eAssistantAdmin:EAssistantAdmin = eAction.doGetInput(EAssistantAdmin)
           
            #Dispose eAction.input for free memory
            eAction.input = b''

            if eAssistantAdmin is None:
                raise Exception("ERROR_REQUIRED|eAssistantAdmin|")

#<        
            #Add other check
            '''
            if eAssistantAdmin. is None:
                raise Exception("ERROR_REQUIRED|eAssistantAdmin.|")
            '''
   
            eAssistant = EAssistant()
            eAssistant.doGenerateID()
            eAssistant.doGenerateTime()

            eAction.enumApiAction = EnumApiAction.COMPLETE
            eAction.doSetOutput(eAssistant)        
            yield eAction
#>
        except Exception as exception:
            IuLog.doException(__name__,exception)
            raise
# ---------------------------------------------------------------------------------------------------------------------------------------
    async def doOnGet(self, eAction:EAction) -> EAction:
        """doOnGet utility callback
            input: EApiQuery
            output: EAssistant

            Raises:
                Exception: api exception

            Returns:
                EAction:  EObject 
        """   
        try:

            eApiQuery:EApiQuery = eAction.doGetInput(EApiQuery)
           
            #Dispose eAction.input for free memory
            eAction.input = b''

            if eApiQuery is None:
                raise Exception("ERROR_REQUIRED|eApiQuery|")

#<        
            #Add other check
            '''
            if eApiQuery. is None:
                raise Exception("ERROR_REQUIRED|eApiQuery.|")
            '''
   
            eAssistant = EAssistant()
            eAssistant.doGenerateID()
            eAssistant.doGenerateTime()

            eAction.enumApiAction = EnumApiAction.COMPLETE
            eAction.doSetOutput(eAssistant)        
            yield eAction
#>
        except Exception as exception:
            IuLog.doException(__name__,exception)
            raise
# ---------------------------------------------------------------------------------------------------------------------------------------
    async def doOnDel(self, eAction:EAction) -> EAction:
        """doOnDel utility callback
            input: EAssistantAdmin
            output: EAssistant

            Raises:
                Exception: api exception

            Returns:
                EAction:  EObject 
        """   
        try:

            eAssistantAdmin:EAssistantAdmin = eAction.doGetInput(EAssistantAdmin)
           
            #Dispose eAction.input for free memory
            eAction.input = b''

            if eAssistantAdmin is None:
                raise Exception("ERROR_REQUIRED|eAssistantAdmin|")

#<        
            #Add other check
            '''
            if eAssistantAdmin. is None:
                raise Exception("ERROR_REQUIRED|eAssistantAdmin.|")
            '''
   
            eAssistant = EAssistant()
            eAssistant.doGenerateID()
            eAssistant.doGenerateTime()

            eAction.enumApiAction = EnumApiAction.COMPLETE
            eAction.doSetOutput(eAssistant)        
            yield eAction
#>
        except Exception as exception:
            IuLog.doException(__name__,exception)
            raise
# ---------------------------------------------------------------------------------------------------------------------------------------
    async def doOnQuery(self, eAction:EAction) -> EAction:
        """doOnQuery utility callback
            input: EApiQuery
            output: EAssistantMap

            Raises:
                Exception: api exception

            Returns:
                EAction:  EObject 
        """   
        try:

            eApiQuery:EApiQuery = eAction.doGetInput(EApiQuery)
           
            #Dispose eAction.input for free memory
            eAction.input = b''

            if eApiQuery is None:
                raise Exception("ERROR_REQUIRED|eApiQuery|")

#<        
            #Add other check
            '''
            if eApiQuery. is None:
                raise Exception("ERROR_REQUIRED|eApiQuery.|")
            '''
   
            eAssistantMap = EAssistantMap()
            eAssistantMap.doGenerateID()
            eAssistantMap.doGenerateTime()

            eAction.enumApiAction = EnumApiAction.COMPLETE
            eAction.doSetOutput(eAssistantMap)        
            yield eAction
#>
        except Exception as exception:
            IuLog.doException(__name__,exception)
            raise
# ---------------------------------------------------------------------------------------------------------------------------------------

#<
#OTHER METHODS ...
#>
# ---------------------------------------------------------------------------------------------------------------------------------------
