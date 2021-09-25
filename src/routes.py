from src.api import Charts


def initialize_routes(api):
    # List users
    api.add_resource(Net_Worth_Chart, '/api/Net_Worth_Over_Time')
    api.add_resource(Monthly_Expense_Chart, '/api/Total_Monthly_Expense')
    api.add_resource(Expense_Breakdown_Chart, '/api/Expense_Breakdown')



 
