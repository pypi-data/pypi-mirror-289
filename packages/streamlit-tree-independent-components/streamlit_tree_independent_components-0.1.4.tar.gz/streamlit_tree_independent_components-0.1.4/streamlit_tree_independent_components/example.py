import streamlit as st
from streamlit_tree_independent_components import tree_independent_components

# Add some test code to play with the component while it's in development.
# During development, we can run this just as we would any other Streamlit
# app: `$ streamlit run my_component/example.py`

st.subheader("Component with input args")

# Create an instance of our component with a constant `name` arg, and
# print its output value.
treeItems = {
   "id":"0",
   "name":"Scorecard",
   "icon":"folder",
   "disable":False,
   "children":[
      {
         "id":"1",
         "name":"(01) Consol IT Charges",
         "icon":"document",
         "disable":False,
         "children":[
            {
               "id":"2",
               "name":"(02) IT Charges Margins Computation",
               "icon":"document",
               "disable":False,
               "children":[
                  {
                     "id":"3",
                     "name":"(02i Output) Intragroup and non-intragroup for Tagetik Loading",
                     "icon":"document",
                     "disable":False
                  },
                  {
                     "id":"4",
                     "name":"(03) ITCO and TPC DB REPORT",
                     "icon":"document",
                     "disable":False,
                     "children":[
                        {
                           "id":"5",
                           "name":"(03i Input) Manual Loading of Data into ITCO and TPCDB",
                           "icon":"document",
                           "disable":False,
                           "children":[
                              {
                                 "id":"6",
                                 "name":"(04) ITCO and TPC DB Add Two Columns for Users",
                                 "icon":"document",
                                 "disable":False,
                                 "children":[
                                    {
                                       "id":"7",
                                       "name":"(04 Input) ITCO and TPCDB Upload CleanUp Two Columns",
                                       "icon":"document",
                                       "disable":False,
                                       "children":[
                                          {
                                             "id":"8",
                                             "name":"(04ii Output) Generate BU Report",
                                             "icon":"document",
                                             "disable":False
                                          },
                                          {
                                             "id":"9",
                                             "name":"(05) Scorecard Report",
                                             "icon":"document",
                                             "disable":False,
                                             "children":[
                                                {
                                                   "id":"10",
                                                   "name":"(05I Input) Manual Loading of Data into Scorecard Report",
                                                   "icon":"document",
                                                   "disable":False
                                                },
                                                {
                                                   "id":"11",
                                                   "name":"(06) After Scorecard Report",
                                                   "icon":"document",
                                                   "disable":False
                                                }
                                             ]
                                          }
                                       ]
                                    }
                                 ]
                              }
                           ]
                        }
                     ]
                  }
               ]
            }
         ]
      }
   ]
}
checkItems = ["0","1","2","3","4","5","6","7","9","8"]
result = tree_independent_components(treeItems, checkItems)

try:
  st.write(sorted(result["setSelected"], key=int))
except:
  pass

# Create a second instance of our component whose `name` arg will vary
# based on a text_input widget.
#
# We use the special "key" argument to assign a fixed identity to this
# component instance. By default, when a component's arguments change,
# it is considered a new instance and will be re-mounted on the frontend
# and lose its current state. In this case, we want to vary the component's
# "name" argument without having it get recreated.
#name_input = st.text_input("Enter a name", value="Streamlit")
#num_clicks = my_component(name_input, key="foo")
#st.markdown("You've clicked %s times!" % int(num_clicks))
