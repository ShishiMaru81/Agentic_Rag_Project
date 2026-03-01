from utils.model_loader import ModelLoader
from prompt_library.prompt import SYSTEM_PROMPT
from langgraph.graph import StateGraph, MessagesState, END, START
from langgraph.prebuilt import ToolNode, tools_condition
#from tools.weather_info_tool import WeatherInfoTool
#from tools.place_search_tool import PlaceSearchTool
#from tools.expense_calculator_tool import CalculatorTool
#from tools.currency_conversion_tool import CurrencyConverterTool





class Graph_Builder:
    def __init__(self):
        self.tools=[

        ]
        self.system_prompt=SYSTEM_PROMPT

    def agent_func(self,state=MessagesState):
        user_query=state["messages"]
        print(user_query)
        input_qurey=[self.system_prompt]+user_query
        response=self.llm_with_toolsinvoke(input_qurey)
        return {"Displaying messages":[response]}


        
        


        


    def build_graph(self):
        build_graph=StateGraph(MessagesState)
        build_graph.add_node("agent",self.agent_func)
        build_graph.add_node("tools",ToolNode(tools=self.tools))
        build_graph.add_edge(START,"agent")
        build_graph.add_conditional_edges("agent",tools_condition)
        build_graph.add_edge("tools","agent")
        build_graph.add_edge("agent",END)
        build_graph=build_graph.compile()
        return build_graph

        

    def __call__(self, *args, **kwds):
        
        return self.build_graph()
        


