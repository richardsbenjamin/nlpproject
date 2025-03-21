from ..navigation_menu.navigation_menu import create_navmenu
from dash import html

docs_layout = html.Div(
    [
        html.Div(
            [
                html.H1("Research Project: Incoherences of Generative AI", style={"margin-top": "20px"}),

                html.H2("Description", style={"margin-top": "30px"}),

                html.P(
                    [
                        "This project is a master's research project developed within the ",
                        html.A(
                            "Data Science Department",  
                            href="https://www.imt-atlantique.fr/en/about/departments/data-science",
                            target="_blank"
                        ),
                        " at ",
                        html.A(
                            "IMT Atlantique",  
                            href="https://www.imt-atlantique.fr/en",
                            target="_blank"
                        ),
                        " Brest campus. It aims to explore the inconsistencies "
                        "of generative artificial intelligences, specifically tools such as ChatGPT, Mistral, "
                        "and DeepSeek. It does not seek in any way to encourage or promote aggressive, violent, "
                        "and/or unethical behavior. It is solely for research purposes, aiming to demonstrate "
                        'that it is possible to "trick" the security of such tools and expose their knowledge '
                        "on complex, controversial, and dangerous topics."
                    ]
                ),
            ],
        ),
    ],
    style={"display": "flex", "flex-direction": "row"},
)