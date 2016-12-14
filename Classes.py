class VirtualPowerPlant:
    
    def __init__(self,Name,BuyingPrice,SellingPrice,Tax,ProfitNormal,ProfitFromPR,ProfitFromGridSupport,Profit,ActualProfit):
        self.Name=Name
        self.BuyingPrice=BuyingPrice
        self.SellingPrice=SellingPrice
        self.Tax=Tax
        self.ProfitNormal=ProfitNormal # ProfitNormal=Selling Price-Buying Price
        self.ProfitFromPR=ProfitFromPR
        self.ProfitFromGridSupport=ProfitFromGridSupport
        self.Profit=Profit  #Profit= ProfitNormal+ProfitFromPR+ProfitFromGridSupport
        self.ActualProfit=ActualProfit
        
class Household:  
    def __init__(self,Name,ProfitFromPR,ProfitFromGridSupport,BuyingPrice,Profit,ActualProfit):
        self.Name=Name
        self.ProfitFromPR=ProfitFromPR
        self.ProfitFromGridSupport=ProfitFromGridSupport
        self.BuyingPrice=BuyingPrice # To meet demand of StandardConsumingDevices and DSM
        self.Profit=Profit # Profit=ProfitFromPR+ProfitFromGridSupport-BuyingPrice
        self.ActualProfit=ActualProfit
                
    class StandardConsumingDevices:
        def __init__(self,Name,Power,Price):
            self.Name=Name
            self.Power = Power
            self.Price=Price
                
    class DSM:
        def __init__(self,Name,Power,Price,FreezerTemperature):
            self.Name=Name
            self.Power = Power
            self.Price=Price
            self.FreezerTemperature=FreezerTemperature
    
    class MarketBatteryStorage:
        def __init__(self,Name,Power,Price,RatedCapacityInKkWh,AgeingFactor,UsableCapacityInKWh,PercentageCurrentCapacity,CapacityForGrid,ChargingPrice,DischargingPrice,ProfitFromPR,ProfitFromGridSupport,ProfitNormal,Profit,ParticipationinPR,ActualProfit):
            self.Name=Name
            self.Power = Power
            self.Price=Price
            self.RatedCapacityInKkWh=RatedCapacityInKkWh
            self.AgeingFactor=AgeingFactor
            self.UsableCapacityInKWh=RatedCapacityInKkWh*AgeingFactor
            self.PercentageCurrentCapacity=PercentageCurrentCapacity
            self.CapacityForGrid=CapacityForGrid
            self.ChargingPrice=ChargingPrice
            self.DischargingPrice=DischargingPrice
            self.ProfitFromPR=ProfitFromPR
            self.ProfitFromGridSupport=ProfitFromGridSupport
            self.ProfitNormal=ProfitNormal
            self.Profit=Profit #ProfitNormal+ProfitFromGridSupport+ProfitFromPR
            self.ParticipationinPR=ParticipationinPR
            self.ActualProfit=ActualProfit
                    
    class MarketSolarGeneratingUnit:
        def __init__(self,Name,Power,Price,ProfitForExcessPower,ProfitNormal,Profit,ActualProfit):
            self.Name=Name
            self.Power = Power
            self.Price=Price
            self.ProfitForExcessPower=ProfitForExcessPower
            self.ProfitNormal=ProfitNormal
            self.Profit=Profit # ProfitNormal+ProfitForExcessPower
            self.ActualProfit=ActualProfit
        
    class MarketCogenerationUnit:
        def __init__(self,Name,Power,Price,ProfitFromGridSupport,ProfitNormal,Profit,ActualProfit):
            self.Name=Name
            self.Power=Power
            self.Price=Price
            self.ProfitFromGridSupport=ProfitFromGridSupport
            self.ProfitNormal=ProfitNormal
            self.Profit=Profit# Profit= ProfitNormal+ProfitFromGridSupport
            self.ActualProfit=ActualProfit
            
    class FeedInTariff: 
        def __init__(self,Name,Power,Price,FeedInPremier,Profit,ActualProfit):
            self.Name=Name
            self.Power=Power
            self.Price=Price        
            self.FeedInPremier=FeedInPremier
            self.Profit=Profit
            self.ActualProfit=ActualProfit
                    
class CommonGrid:
    def __init__(self,Name,Power,CostForPR,CostForGridSupport,Price,ProfitNormal,Profit,ActualProfit):
        self.Name=Name
        self.Power=Power
        self.CostForPR=CostForPR
        self.CostForGridSupport=CostForGridSupport
        self.Price=Price
        self.ProfitNormal=ProfitNormal
        self.Profit=Profit # Price-CostForPR-CostForGridSupport
        self.ActualProfit=ActualProfit

class ElectricityStockExchange:
    def __init__(self,Name,Price,ExchangePriceScenario,PrimaryReserveStatus):
        self.Name=Name
        self.Price=Price
        self.ExchangePriceScenario=ExchangePriceScenario
        self.PrimaryReserveStatus=PrimaryReserveStatus

class DistributionSystemOperator:
    def __init__(self,Name,SwitchForGridFriendlyBehaviour,TimeWhenAllowedToCharge):
        self.Name=Name
        self.SwitchForGridFriendlyBehaviour=SwitchForGridFriendlyBehaviour
        self.TimeWhenAllowedToCharge=TimeWhenAllowedToCharge


