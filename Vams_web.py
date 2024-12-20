# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.16.4
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

# +

from dash import Dash,html, dash_table,dcc,callback,Output,Input,State
import dash_bootstrap_components as dbc
import dash
import base64
import pywhatkit as wt
import datetime
# -

app = dash.Dash(external_stylesheets = [dbc.themes.UNITED,dbc.icons.BOOTSTRAP],assets_folder='assets', assets_url_path='/assets/')



# +
img_tag = html.Img(src = "assets/logo.jpg",width = 37)
brand_link = dcc.Link([img_tag],href = "#",className = "navbar-brand")

navbar = dbc.Navbar(
                dbc.Container([
                    dbc.Row([
                        dbc.Col([
                            html.Div([brand_link,
                            dbc.NavbarBrand("VAM'S SPA",className = "ms-2")]),
                        ])
                        
                    ]),
                    dbc.Row([ 
                        dbc.Col([
                    dbc.NavbarToggler(id="navbar-toggler", n_clicks=0),
                        dbc.Collapse(
                        dbc.Nav([
                            dbc.NavItem(dbc.NavLink("Home",href = "/")),
                            dbc.NavItem(dbc.NavLink("About",href = "/About")),
                            dbc.NavItem(dbc.NavLink("Services",href = "/Services")),
                            dbc.NavItem(dbc.NavLink("Contact",href = "/Contact")), 
                            # dbc.NavItem(dbc.NavLink("Products",href = "/pro")), 
                            ],
                                   navbar = True,pills = True),
                id="navbar-collapse",
                is_open=False,
                navbar=True,
            )
                        ])
                    ]),
                    
                   
          
                
                
                ])



    
,color="green",
dark=True
)


# -



# +
ab_cardf = html.Div([
    html.Br(),
    html.Br(),
    html.Br(),
  
    
 dbc.Container([
     dbc.Row([
         dbc.Col([html.Div([])], xs = 1, sm = 1,md =1 ,lg = 1,xl = 1),
         dbc.Col([html.H5("Follow Us", style={'color': 'tomato','font-family':'Open Sans'})], xs = 6, sm = 6,md =6 ,lg = 7,xl = 7),
         dbc.Col([html.H5("Contact", style={'color': 'tomato','font-family':'Open Sans'})] , xs = 5, sm = 5,md =5 ,lg = 4,xl = 4)
     ]),
            dbc.Row([
                dbc.Col([html.Div([])], xs = 1, sm = 1,md =1 ,lg = 1,xl = 1),
                dbc.Col([
                  html.Div([dbc.Nav([
                                 html.A([html.I(className = "bi bi-instagram")],href = "https://www.instagram.com/vamsspa/",target = "blank")
                                
                                
                            ])
                                   ],style={'width': '12%', 'display': 'inline-block'}),
                    html.Div([dbc.Nav([
                                html.A([html.I(className = "bi bi-tiktok")],href = "https://www.instagram.com/vamsspa/",target = "blank")])],style={'width': '12%', 'display': 'inline-block'})
                    
                ], xs = 6, sm = 6,md =6 ,lg = 7,xl = 7),
                dbc.Col([
                       html.Div([html.Div("+233243228730", style={'color': 'white','font-family':'Open Sans'}),
                                html.Div("Vamsspa@gmail.com", style={'color': 'white','font-family':'Open Sans'})
                                
                                ])
                    ], xs = 5, sm = 5,md =5 ,lg = 4,xl = 4)
            ]),
 
     ])
        ,

    html.Br(),
    html.Br(),
    html.Br(),
    
    html.Div(["_______________________________________________"],className = ["text-center"], style={'color': 'white'}),
    html.Br(),
        html.Div([html.P("© 2024 Vam's Spa. All rights reserved",className = ["text-center"], style={'color': 'white','font-family':'Open Sans'})
                 ,html.P("Contact : +233243228730",className = ["text-center"], style={'color': 'white','font-family':'Open Sans'})])
    
    
    
    
],style = {

    "border-radius":0,
    "background":"darkgreen",
    "height":370
    })


# -

welc = dbc.Card([
    dbc.CardBody([
          dbc.Container([
             html.Br(),
              html.Br(),
              html.Br(),
              dbc.Row([
                  dbc.Col([
        html.Div([
            
              html.Div([],style = {"background-image" : 'url("/assets/logo.jpg")',"background-size":"cover","background-repeat":"no-repeat","background-position":"center","height":400,"width":350})
        ])
                  ])
              ])
          ])
    ])
],style = {
    "width":310,
    "height":700,
    "border-radius":0,
    "background":"peachpuff"
    })

# Apprenticeship enrollment
Appr_forms = dbc.Container([
    dbc.Row([
        dbc.Col([
            html.Div([html.P("Full name:"),dcc.Input(id = "name",type = "text",placeholder = "name")]),
            html.Br(),
            html.Div([html.P("Number(WhatsApp):"),dcc.Input(id = "number",type = "text",placeholder = "")]),
            html.Br(),
            html.Div([html.P("Age:"),dcc.Input(id = "Age",type = "text",placeholder = "")]),
            html.Br(),
            html.Div([html.P("Nationality"),dcc.Input(id = "Nationality",type = "text",placeholder = "")]),
            html.Br()
          
        ])
    ])
])

# +


Page1 = html.Div([
    
html.Div([
    
    dbc.Carousel(
            items = [
                    {"key":"1","src":"/assets/wallpaper.jpg","img_style":{"height":"100vh"}},
                    {"key":"2","src":"/assets/wallpaper2.jpg","img_style":{"height":"100vh"}},
                    {"key":"3","src":"/assets/wallpaper3.jpg","img_style":{"height":"100vh"}},
                    {"key":"3","src":"/assets/W_logo.jpg","img_style":{"height":"100vh"}},
            
            ],
    controls = True,
    indicators = False,
    interval = 2000,
    ride = "carousel"
    
)
]
        ),
        
html.Br(),
html.Br(),
html.Br(),
    
   
    
dbc.Container([
    dbc.Row([
        dbc.Col([html.Div([])]
               , xs = 1, sm = 1,md =2 ,lg = 2,xl = 2
),
        dbc.Col([ html.Div([
                 html.H3("Want to upgrade yourself with some skills ?",className =["text-center"], style={'color': 'white','font-family':'Open Sans'}),
                 html.H5("Don't worry, We've got you covered.",className =["text-center"],style={'color': 'white','font-family':'Open Sans'}),
                 html.H5("Vam's Spa is offering a 2 to 4 months intensive salon service training",className =["text-center"],style={'color': 'white','font-family':'Open Sans'}),
                 html.H5("Call +233243228730 to enroll now",className =["text-center"],style={'color': 'white','font-family':'Open Sans'}),
                html.Br(),
     
                  html.Div([dbc.Button("Enroll now",id = "Book_ap",n_clicks = 0)],className =["text-center"]),
            dbc.Modal([
                     dbc.ModalHeader(html.Div(dbc.ModalTitle("Apprenticeship Forms"))),
                     dbc.ModalBody([Appr_forms]),
                     dbc.ModalFooter(
                         html.Div([dbc.Button("Submit",id = "sub1",className = "ms-auto" "text-center",n_clicks = 0)])
                     )
                 ],
                          id = "modal1",
                          is_open = False,
                          
                          ),
        ],style = {"background-image" : 'url("/assets/slide6_.jpg")',"background-size":"cover","background-repeat":"no-repeat","background-position":"center","height":200})]
        , xs = 12, sm = 10,md =7 ,lg = 7,xl = 7)

        
        ]),
      html.Br(),
      html.Br(),
      html.Br(),
      html.Br(),
      html.Br(),
    html.Br(),
   
    dbc.Row([
             html.Br(),
        html.Br(),
        html.Br(),
            
                dbc.Col([html.Div([])]
                       , xs = 3, sm = 3,md =1 ,lg = 1,xl = 1),
                dbc.Col([html.Div([])]
                       ,style = {"background-image" : 'url("/assets/w_up3.png")',"background-size":"cover","background-repeat":"no-repeat","background-position":"center","height":200}
                         , xs = 10, sm = 7,md =3 ,lg = 3,xl = 3),
                    dbc.Col([
                        
             dbc.Carousel(
            items = [
                    {"key":"1","src":"/assets/pr1.jpg","img_style":{"height":400}},
                   {"key":"2","src":"/assets/pr33.png","img_style":{"height":400}},
                    {"key":"3","src":"/assets/imggf.png","img_style":{"height":400}}
                ,
            
            ],
    controls = True,
    indicators = False,
    interval = 2000,
    ride = "carousel"
    
),
                        
                    ]  , xs = 12, sm = 12,md =6 ,lg = 6,xl = 6),
         
    
      
                
       
       
    ]),
    html.Br(),
     html.Br(),
        html.Br(),
        html.Br(),
        html.Br(),
                      ])




,ab_cardf]
                ,style={'backgroundColor':'white'})



# -

ab_cardh = dbc.Card([
    dbc.CardBody([
        html.Div(html.H3(["About Vam's Spa"]),className = ["text-center"], style={'color': 'white','font-family':'Open Sans'})
    ])
],style = {
    "height":50,
    "border-radius":0,
    "background":"darkgreen"
    })


# +
#about  ...return about and navbar (Vam's spa)
about = html.Div([
       ab_cardh,
    dbc.Container([
        html.Br(),
        dbc.Row([
            dbc.Col([html.Div([])]
                   , xs = 1, sm = 1,md =1 ,lg = 1,xl = 1 ),
            dbc.Col([ 
                html.P("Get ready to glow at Vams Spa! "),
                html.P("Our mission is to create a warm and welcoming atmosphere where our clients can relax, unwind, and experience the ultimate in pampering."),
                html.P("From cuts and braids, to manicure and pedicure , to wig making, installation and spa treatments, we'll help you unlock your unique style and radiate confidence. "),
                html.P("Our extensive catalogue of services is designed to meet the unique needs and preferences of each and every client, ranging from children to adults."),
                html.P(" Using only the highest-quality products. we believe that everyone deserves to look and feel their best."),
                html.P("At VamsSpa, your style is our priority!"),
                
                
            ] , xs = 11, sm = 11,md =4 ,lg = 6,xl = 6),
            
               dbc.Col([html.Div([])]
                   , xs = 1, sm = 1,md =1 ,lg = 1,xl = 1 ),
            
            dbc.Col([ html.Div([],style = {"background-image" : 'url("/assets/slide3.jpg")',"background-size":"cover","background-repeat":"no-repeat","background-position":"center","height":440,"width":300})

                
            ] , xs = 10, sm = 10,md =4 ,lg = 4,xl = 4)
        ]),
         html.Br(),
        html.Br(),
        dbc.Row([
              dbc.Col([html.Div([])]
                        , xs = 1, sm = 1,md =1 ,lg = 1,xl = 1  ),
            dbc.Col([
                html.P("Our friendly and experienced team are dedicated to making you look and feel amazing. "),
                    html.P("Walk-in or Book your appointment today and discover why we're the go-to salon in Accra!"),
                
              
                    ]  , xs = 11, sm = 11,md =4 ,lg = 6,xl = 6),
               dbc.Col([html.Div([])]
                   , xs = 1, sm = 1,md =1 ,lg = 1,xl =1 ),
            dbc.Col([ 
                html.P(),
                html.P(),
                  html.Div([],style = {"background-image" : 'url("/assets/about.jpg")',"background-size":"cover","background-repeat":"no-repeat","background-position":"center","height":400,"width":300})
            ] , xs = 10, sm = 10,md =4 ,lg = 4,xl = 4)
        ]),

      html.Br(),
        html.Br(),
        html.Br(),
        
    
]),
      html.Br(),
        html.Br(),
        html.Br(),
    ab_cardf
])
                  
# -



# +


cont_card = dbc.Card([

    dbc.Container([

        dbc.Row([
            dbc.Col([html.H1("Contact Us")
                    ],width = {"offset":2})
        ]),
        dbc.Row([
            dbc.Col([
    
     dbc.CardBody([  
     
     html.P(html.I(className = "bi bi-telephone-fill")),
     html.P(html.I(className = "bi bi-whatsapp")),    
     html.P(html.I(className = "bi bi-envelope-at-fill")),
     html.P(html.I(className = "bi bi-geo-alt")),    
         

     ])
     ],width = {"offset":1}),
       dbc.Col([
           
     dbc.CardBody([  
    
     html.P("+233243228730"),
     html.P("+233243228730"),    
     html.P("Vamsspa@gmail.com"),
     html.P("Kofi Annan Street 64, Nyaho road"),    
         

     ])
     ]),

            
     ])
     ])]
,style = {
    "width":350,
    "height":250,
    "border-radius":5,
    "background":"seashell"
    })

# +


Contact = html.Div([
    dbc.Container([
    html.Br(),
    html.Br(),
    html.Br(),
     html.Br(),
    html.Br(),
    html.Br(),
dbc.Row([

    dbc.Col([html.Div([])]
            ,md =4 ,lg = 4,xl = 4 ),
    dbc.Col([cont_card] 
           ,md =4 ,lg = 4,xl = 4 )
    
]),
         html.Br(),
    html.Br(),
    html.Br(),
            html.Br(),
    html.Br(),
    html.Br(),
        dbc.Row([ 
            
        dbc.Col([html.Div([])]
            ,md =4 ,lg = 4,xl = 4 ),     
dbc.Col([
html.Div(html.A([html.Img(src = "assets/map_f.png",width = 350)],href = "https://maps.app.goo.gl/xEWEntMfVhHrBzm37?g_st=iw",target = "blank"))

] ,md =4 ,lg = 4,xl = 4 )

])
    ]),  
    html.Br(),
    html.Br(),
    html.Br(),
      html.Br(),
    html.Br(),
    html.Br()

,ab_cardf],
                  style = {"background":"linen"})



# -

""" dbc.Container([
            dbc.Row([
                dbc.Col([
                    html.H4("• Braids", style={'font-family':'Open Sans',"text-decoration": "underline"},className =  "text-center"),
                html.Br(),
                 html.H4("• Rasta", style={'font-family':'Open Sans',"text-decoration": "underline"},className =  "text-center"),
                 html.Br(),
                 html.H4("• Weave-on", style={'font-family':'Open Sans',"text-decoration": "underline"},className =  "text-center"),
                    html.Br(),
                html.H4("• Perdicure", style={'font-family':'Open Sans',"text-decoration": "underline"},className =  "text-center"),
                html.Br(),
                 html.H4("• Washing", style={'font-family':'Open Sans',"text-decoration": "underline"},className =  "text-center"),
                html.Br(),
                 html.H4("• Corn-roll", style={'font-family':'Open Sans',"text-decoration": "underline"},className =  "text-center"),
                html.Br(),

                html.H4("• Piercing", style={'font-family':'Open Sans',"text-decoration": "underline"},className =  "text-center"),
                html.Br(),
                 html.H4("• Eye brow Tattoo", style={'font-family':'Open Sans',"text-decoration": "underline"},className =  "text-center"),
                html.Br(),
                 html.H4("• Make-ups", style={'font-family':'Open Sans',"text-decoration": "underline"},className =  "text-center"),
                html.Br(),
                    
                ]),
                
            ])
        ])"""

serv_card1 = dbc.Card([
    dbc.CardBody([ html.Div([]
                           ,style = {"background-image" : 'url("/assets/serv1.jpg")',"background-size":"cover","background-repeat":"no-repeat","background-position":"center","height":300,"width":317}),
                  html.Br(),
                  html.Div(["BRAIDS"],className = ["text-center"],style={'color': 'black','font-family':'Open Sans'})
       
    ])
],style = {
    "width":350,
    "height":360,
    "border-radius":5,
    "background":"white"
    })
serv_card2 = dbc.Card([
    dbc.CardBody([ html.Div([]
                           ,style = {"background-image" : 'url("/assets/serv2.jpg")',"background-size":"cover","background-repeat":"no-repeat","background-position":"center","height":300,"width":317}),
                  html.Br(),
                  html.Div(["BRAIDS"],className = ["text-center"],style={'color': 'black','font-family':'Open Sans'})
       
    ])
],style = {
    "width":350,
    "height":360,
    "border-radius":5,
    "background":"white"
    })
serv_card3 = dbc.Card([
    dbc.CardBody([ html.Div([]
                           ,style = {"background-image" : 'url("/assets/s1.jpg")',"background-size":"cover","background-repeat":"no-repeat","background-position":"center","height":300,"width":317}),
                  html.Br(),
                  html.Div(["Ghana-weave"],className = ["text-center"],style={'color': 'black','font-family':'Open Sans'})
       
    ])
],style = {
    "width":350,
    "height":360,
    "border-radius":5,
    "background":"white"
    })
serv_card4 = dbc.Card([
    dbc.CardBody([ html.Div([]
                           ,style = {"background-image" : 'url("/assets/p1.jpg")',"background-size":"cover","background-repeat":"no-repeat","background-position":"center","height":300,"width":317}),
                  html.Br(),
                  html.Div(["PEDICURE"],className = ["text-center"],style={'color': 'black','font-family':'Open Sans'})
       
    ])
],style = {
    "width":350,
    "height":360,
    "border-radius":5,
    "background":"white"
    })
serv_card5 = dbc.Card([
    dbc.CardBody([ html.Div([]
                           ,style = {"background-image" : 'url("/assets/wallpaper2.jpg")',"background-size":"cover","background-repeat":"no-repeat","background-position":"center","height":300,"width":317}),
                  html.Br(),
                  html.Div(["MEN'S CUT"],className = ["text-center"],style={'color': 'black','font-family':'Open Sans'})
       
    ])
],style = {
    "width":350,
    "height":360,
    "border-radius":5,
    "background":"white"
    })
serv_card6 =  dbc.Card([
    dbc.CardBody([ html.Div([]
                           ,style = {"background-image" : 'url("/assets/slide2.jpg")',"background-size":"cover","background-repeat":"no-repeat","background-position":"center","height":300,"width":317}),
                  html.Br(),
                  html.Div(["NAILS"],className = ["text-center"],style={'color': 'black','font-family':'Open Sans'})
       
    ])
],style = {
    "width":350,
    "height":360,
    "border-radius":5,
    "background":"white"
    })
serv_card7 = dbc.Card([
    dbc.CardBody([ html.Div([]
                           ,style = {"background-image" : 'url("/assets/slide11.jpg")',"background-size":"cover","background-repeat":"no-repeat","background-position":"center","height":300,"width":317}),
                  html.Br(),
                  html.Div(["RASTA-Braids"],className = ["text-center"],style={'color': 'black','font-family':'Open Sans'})
       
    ])
],style = {
    "width":350,
    "height":360,
    "border-radius":5,
    "background":"white"
    })
serv_card8 = dbc.Card([
    dbc.CardBody([ html.Div([]
                           ,style = {"background-image" : 'url("/assets/flyer.jpg")',"background-size":"cover","background-repeat":"no-repeat","background-position":"center","height":330,"width":317}),
             
       
    ])
],style = {
    "width":350,
    "height":360,
    "border-radius":5,
    "background":"white"
    })


# a form to accept details...bookings
book_forms = dbc.Container([
    dbc.Row([
        dbc.Col([
            html.Div(dcc.Input(id = "name",type = "text",placeholder = "name")),
            html.Br(),
            html.Div(dcc.Input(id = "number",type = "text",placeholder = "Number(WhatsApp)")),
            html.Br(),
            html.Div(dcc.Input(id = "service",type = "text",placeholder = "service")),
            html.Br(),
            html.Div(dcc.Input(id = "schedule_day",type = "text",placeholder = "schedule_day")),
            html.Br(),
        ])
    ])
])

# +
# Services
services = html.Div([
    dbc.Carousel(
            items = [
                    {"key":"1","src":"/assets/slide2.jpg","img_style":{"height":700}},
                    {"key":"3","src":"/assets/slide11.jpg","img_style":{"height":700}},
                    {"key":"3","src":"/assets/slide4.jpg","img_style":{"height":700}},
                    {"key":"1","src":"/assets/slide5.jpg","img_style":{"height":700}},
                    {"key":"2","src":"/assets/slide6.jpg","img_style":{"height":700}},
                   
            
            ],
    controls = True,
    indicators = False,
    interval = 2000,
    ride = "carousel"),

    html.Br(),
    html.Br(),
    html.Br(),
html.Div([
   dbc.Container([ 
       html.Br(),
       dbc.Row([
        
       dbc.Col([serv_card1, html.Br(),serv_card3, html.Br(),serv_card7, html.Br()],xs = 12, sm = 12,md =12 ,lg = 4,xl = 4),
     
        dbc.Col([serv_card2, html.Br(),serv_card6, html.Br(),serv_card4, html.Br()],xs = 12, sm = 12,md =12 ,lg = 4,xl = 4 ),
          dbc.Col([serv_card5, html.Br(),serv_card8, html.Br(), html.Br()],xs = 12, sm = 12,md =12 ,lg = 4,xl = 4 ),



         
          
       ]),
            dbc.Row([
                dbc.Col([
                    # dbc.Button("Book now",id = "Book",n_clicks = 0),
                    
                ],width = {"offset":5})
            ]),
                 # dbc.Modal([
                 #     dbc.ModalHeader(dbc.ModalTitle("Provide Details")),
                 #     dbc.ModalBody([book_forms]),
                 #     dbc.ModalFooter(dbc.Button("Submit",id = "sub",className = "ms-auto",n_clicks = 0))
                 # ],
                 #          id = "modal",
                 #          is_open = False,
                          
                 #          )
                 
                 
                 ] )
],style = { "background":"white"} )


,ab_cardf])




# +
# pr1 = dbc.Card([
#     dbc.CardBody([ html.Div([]
#                            ,style = {"background-image" : 'url("/assets/logo.jpg")',"background-size":"cover","background-repeat":"no-repeat","background-position":"center","height":300,"width":317}),
#                   html.Br(),
#                   html.Div([""],className = ["text-center"],style={'color': 'black','font-family':'Open Sans'})
       
#     ])
# ],style = {
#     "width":350,
#     "height":360,
#     "border-radius":5,
#     "background":"white"
#     })
# pr2 = dbc.Card([
#     dbc.CardBody([ html.Div([]
#                            ,style = {"background-image" : 'url("/assets/logo.jpg")',"background-size":"cover","background-repeat":"no-repeat","background-position":"center","height":300,"width":317}),
#                   html.Br(),
#                   html.Div([""],className = ["text-center"],style={'color': 'black','font-family':'Open Sans'})
       
#     ])
# ],style = {
#     "width":350,
#     "height":360,
#     "border-radius":5,
#     "background":"white"
#     })
# pr3 = dbc.Card([
#     dbc.CardBody([ html.Div([]
#                            ,style = {"background-image" : 'url("/assets/logo.jpg")',"background-size":"cover","background-repeat":"no-repeat","background-position":"center","height":300,"width":317}),
#                   html.Br(),
#                   html.Div([""],className = ["text-center"],style={'color': 'black','font-family':'Open Sans'})
       
#     ])
# ],style = {
#     "width":350,
#     "height":360,
#     "border-radius":5,
#     "background":"white"
#     })
# pr4 = dbc.Card([
#     dbc.CardBody([ html.Div([]
#                            ,style = {"background-image" : 'url("/assets/logo.jpg")',"background-size":"cover","background-repeat":"no-repeat","background-position":"center","height":300,"width":317}),
#                   html.Br(),
#                   html.Div([""],className = ["text-center"],style={'color': 'black','font-family':'Open Sans'})
       
#     ])
# ],style = {
#     "width":350,
#     "height":360,
#     "border-radius":5,
#     "background":"white"
#     })
# pr5 = dbc.Card([
#     dbc.CardBody([ html.Div([]
#                            ,style = {"background-image" : 'url("/assets/logo.jpg")',"background-size":"cover","background-repeat":"no-repeat","background-position":"center","height":300,"width":317}),
#                   html.Br(),
#                   html.Div([" "],className = ["text-center"],style={'color': 'black','font-family':'Open Sans'})
       
#     ])
# ],style = {
#     "width":350,
#     "height":360,
#     "border-radius":5,
#     "background":"white"
#     })
# pr6 =  dbc.Card([
#     dbc.CardBody([ html.Div([]
#                            ,style = {"background-image" : 'url("/assets/logo.jpg")',"background-size":"cover","background-repeat":"no-repeat","background-position":"center","height":300,"width":317}),
#                   html.Br(),
#                   html.Div([""],className = ["text-center"],style={'color': 'black','font-family':'Open Sans'})
       
#     ])
# ],style = {
#     "width":350,
#     "height":360,
#     "border-radius":5,
#     "background":"white"
#     })
# pr7 = dbc.Card([
#     dbc.CardBody([ html.Div([]
#                            ,style = {"background-image" : 'url("/assets/logo.jpg")',"background-size":"cover","background-repeat":"no-repeat","background-position":"center","height":300,"width":317}),
#                   html.Br(),
#                   html.Div([""],className = ["text-center"],style={'color': 'black','font-family':'Open Sans'})
       
#     ])
# ],style = {
#     "width":350,
#     "height":360,
#     "border-radius":5,
#     "background":"white"
#     })
# pr8 = dbc.Card([
#     dbc.CardBody([ html.Div([]
#                            ,style = {"background-image" : 'url("/assets/logo.jpg")',"background-size":"cover","background-repeat":"no-repeat","background-position":"center","height":300,"width":317}),
#                   html.Br(),
#                   html.Div([""],className = ["text-center"],style={'color': 'black','font-family':'Open Sans'})
       
#     ])
# ],style = {
#     "width":350,
#     "height":360,
#     "border-radius":5,
#     "background":"white"
#     })
# pr9 =dbc.Card([
#     dbc.CardBody([ html.Div([]
#                            ,style = {"background-image" : 'url("/assets/logo.jpg")',"background-size":"cover","background-repeat":"no-repeat","background-position":"center","height":300,"width":317}),
#                   html.Br(),
#                   html.Div([""],className = ["text-center"],style={'color': 'black','font-family':'Open Sans'})
       
#     ])
# ],style = {
#     "width":350,
#     "height":360,
#     "border-radius":5,
#     "background":"white"
#     })

# +
# prod = html.Div([
#     html.Br(),
#     html.Br(),
#     html.Br(),
#     html.Br(),
    
# dbc.Container([
#             dbc.Row([
#         dbc.Col([pr1, html.Br(),pr2, html.Br(),pr3, html.Br()],xs = 12, sm = 12,md =4 ,lg = 4,xl = 4),
#             ]),
#        dbc.Row([
#         dbc.Col([pr4, html.Br(),pr5, html.Br(),pr6, html.Br()],xs = 12, sm = 12,md =4 ,lg = 4,xl = 4),
#             ]),
#      dbc.Row([
#         dbc.Col([pr7, html.Br(),pr8, html.Br(),pr9, html.Br()],xs = 12, sm = 12,md =4 ,lg = 4,xl = 4),
#             ])
#      ])



    
# ,ab_cardf])
# -

empty_content = html.Div(id = "page-content")

app.layout = html.Div([
    html.Div([ dcc.Location(id = "url"),navbar,empty_content])
                      ])


# +
@callback(Output("page-content","children"),[Input("url","pathname")])
def render_p_content(pathname):
    if pathname == "/":
        return Page1
    elif pathname == "/About":
        return about
    elif pathname == "/Services":
        return services
    elif pathname == "/Contact":
        return Contact
    # elif pathname == "/pro":
    #     return prod
    
    

@callback(Output("modal","is_open"),[Input("Book","n_clicks"),Input("sub","n_clicks")],[State("modal","is_open")])  
def toggle_form(n1,n2,is_open):
    if n1 or n2:
        return not is_open
    return is_open
    
@callback(Output("modal1","is_open"),[Input("Book_ap","n_clicks"),Input("sub1","n_clicks")],[State("modal1","is_open")])  
def toggle_form(n1,n2,is_open):
    if n1 or n2:
       return not is_open
    return is_open

@app.callback(Output("navbar-collapse", "is_open"),[Input("navbar-toggler", "n_clicks")],[State("navbar-collapse", "is_open")],)
def toggle_navbar_collapse(n, is_open):
    if n:
        return not is_open
    return is_open
    
@callback([Input("sub1","n_clicks"),Input("name","value"),Input("number","value"),Input("Age","value"),Input("Nationality","value")])
def showstate(n1,name,number,Age,Nationality):
   message = f"Hello, Please I am {name}, {Age} years of age and a {Nationality}. I am interested in enrolling for an apprenticeship at your salon"
   x = datetime.datetime.now() 
   if n1 >= 1:
        wt.sendwhatmsg("+233243228730",message,x.hour,x.minute+1,00)
   return "Sent"


# -

"""@callback(Output("",""),[Input("url","pathname"),Input("name","value"),Input("number","value"),Input("Age","value"),Input("Nationality","value"),Input("Things","value")])
def render_p(pathname,name,number,Age,Nationality,Things):
     if pathname == "/submit":
          x = datetime.datetime.now()
          message = f"Hello Madam, Please I am {name}, {Age} of age and a {Nationality}. I am interested in enrolling for an apprenticeship to learn {Things}"
          wt.sendwhatmsg("+233243228730",message,x.hour,x.minute + 2,30)"""



# + jupyter={"source_hidden": true}
#,Input("name","value"),Input("number","value"),Input("Age","value"),Input("Nationality","value"),Input("Things","value")
#        ,name,number,Age,Nationality,Things#

#elif pathname == "/submit":
#        x = datetime.datetime.now()
#        message = f"Hello Madam, Please I am {name}, {Age} of age and a {Nationality}. I am interested in enrolling for an apprenticeship to learn {Things}"
 #       wt.sendwhatmsg("+233243228730",message,x.hour,x.minute + 2,30)
# -



if __name__ == "__main__":
    app.run(jupyter_mode = "tab")

# +



# Products - perfume , wigs , 


# map at location
# Receive input from the forms and use callback to send message
# a sliding div
# background
# excess space --remove
# apply trick on the side bar and carousel

# +
# fitting a carousel( height for phone view)
# put social m links at the footer
# will they do any auditing?

# +
# lets make the footer only a div rather than a card
