library(shiny)
library(reticulate)


use_python("/Library/Frameworks/Python.framework/Versions/3.10/bin/python3")

py_install("pandas")
py_install("numpy")
py_install("sympy")



source_python("../back-end/quaratic.py")
source_python("../back-end/rosenbrocks.py")


shinyServer(function(input, output) {
  
  quadraticCalculate<-eventReactive(
    input$solveQuadratic, {
    Q<-(input$Q[1])
    c<-(input$c[1])
    x_0<-(input$x_0[1])
    k_max<-as.integer(input$k_max[1])
    a_k<-(input$a_k[1])
    epsilon<-as.double(input$epsilon[1])
    outs<-quadratic_function(x_0, Q, c, k_max, a_k, epsilon)
    print(outs)
    return (outs)
  })
  
  rosenbrockCalculate<-eventReactive(input$solveRosenbrock, {
    x_0<-input$x_r_0[1]
    k_max<-as.integer(input$k_r_max[1])
    a_k <-as.double(input$a_r_k[1])
    epsilon<-as.double(input$r_epsilon[1])
    outs<-rosenbrocks_function(x_0, k_max, a_k, epsilon)
    print(outs)
    return (outs)
  })
  
  
  output$quadraticTable<-renderTable({
    quadraticCalculate()
  })
  
  output$rosenbrockTable<-renderTable({
    rosenbrockCalculate()
  }, digits = 10)
})
