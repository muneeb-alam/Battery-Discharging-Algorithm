
from Classes import *

#==========================VPP======================================#

#(self,Name,BuyingPrice,SellingPrice,Tax,ProfitNormal,ProfitFromPR,ProfitFromGridSupport,Profit):

VPP=VirtualPowerPlant('VPP',3,29,21.6,0,0,0,0,0)
#VPP.ProfitNormal=VPP.SellingPrice-VPP.BuyingPrice-VPP.Tax
#print VPP.ProfitNormal
#VPP.Profit=VPP.ProfitNormal+VPP.ProfitFromPR+VPP.ProfitFromGridSupport 
# Profits from PR are fixed at 2 Euro/kW in one week. Grid pays 2 Euro/kW to VPP and VPP pays 10 Euro per year to HH
#print VPP.Profit


#======================HouseHolds====================================#

#(self,Name,ProfitFromPR,ProfitFromGridSupport,BuyingPrice,Profit)
H1=Household('H1',0,0,0,29,0,0)
#print H1.Profit
#H1.Profit=H1.ProfitFromPR+H1.ProfitFromGridSupport-H1.BuyingPrice
#print H1.Profit


#(self,Name,Power,Price)
H1.StandardConsumingDevices=H1.StandardConsumingDevices('StandardConsumingDevices',10,30)
#print H1.StandardConsumingDevices.Name


#(self,Name,Power,Price,FreezerTemperature)
H1.DSM=H1.DSM('DSM',0,30,25)

#(self,Name,Power,Price,rated_capacity_in_kWh,AgeingFactor,UsableCapacityInKWh,PercentageCurrentCapacity,CapacityForGrid,ChargingPrice,DischargingPrice,ProfitFromPR,ProfitFromGridSupport,ProfitNormal,Profit,ParticipationinPR)
H1.MarketBatteryStorage=H1.MarketBatteryStorage('MarketBatteryStorage',7,21,7,1,7,50,0,18,26,0,0,0,0,0,0)
#print H1.MarketBatteryStorage.UsableCapacityInKWh
#print H1.MarketBatteryStorage.Profit

#(self,Name,Power,Price,ProfitForExcessPower,ProfitNormal,Profit)
H1.MarketSolarGeneratingUnit=H1.MarketSolarGeneratingUnit('MarketSolarGeneratingUnit',400,1,0,0,0,0)

#(self,Name,Power,Price,ProfitFromGridSupport,ProfitNormal,Profit)
H1.MarketCogenerationUnit=H1.MarketCogenerationUnit('MarketCogenerationUnit',0,14,0,0,0,0)

#====================Grid====================================#

#(self,Name,Power,CostForPR,CostForGridSupport,Price,ProfitNormal,Profit):
CommonGrid1=CommonGrid('CommonGrid',-10,0,0,30,0,0,0)
#print CommonGrid1.Name

#=========================EEx=================================#

#(self,Name,Price,ExchangePriceScenario,PrimaryReserveStatus)
EEx=ElectricityStockExchange('EEx',3,'Scenario',0)
#print EEx.Name
#print EEx.PrimaryReserveStatus

#=================================DSO==================================#

#(self,Name,SwitchForGridFriendlyBehaviour,TimeWhenAllowedToCharge)
DSO=DistributionSystemOperator('DSO',0,10)


#H2=copy.copy(H1)
#print H2
#H2.Name='H2'
#print H2.Name
