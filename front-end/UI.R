library(shiny)
library(shinydashboard)

# Define UI for application that draws a histogram
dashboardPage(
    dashboardHeader(title = "Algoritmos en la Ciencia de Datos"),
    dashboardSidebar(
        sidebarMenu(
            menuItem("Problema 1", tabName = "quadratic"),
            menuItem("Problema 2", tabName = "rosenbrock")
        )
    ),
    dashboardBody(
        tabItems(
            tabItem("quadratic",
                    h1("Función Cuadrática"),
                    box(
                        textInput("Q", "Ingrese Q"),
                        textInput("c", "Ingrese c"),
                        textInput("x_0", "Ingrese x"),
                        textInput("k_max", "Ingrese el iteraciones"),
                        textInput("a_k", "Ingrese el step size"),
                        textInput("epsilon", "Ingrese el error")),
                    actionButton("solveQuadratic", "Resolver"),
                    tableOutput("quadraticTable")),
            
            tabItem("rosenbrock",
                    h1("Función de Rosenbrock"),
                    box(
                        textInput("x_r_0", "Ingrese el valor inicial"),
                        textInput("k_r_max", "Ingrese el iteraciones"),
                        textInput("a_r_k", "Ingrese la tasa de aprendizaje"),
                        textInput("r_epsilon", "Ingrese el error")),
                    actionButton("solveRosenbrock", "Resolver"),
                    tableOutput("rosenbrockTable"))
        )
    )
)
