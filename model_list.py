from pysr import PySRRegressor




def model_A() :
    """"
      Model A 
    """ 

    model = PySRRegressor(
##    niterations=40,  # < Increase me for better results
     niterations=300,  # < Increase me for better results
#    denoise=True,
    binary_operators=["+", "*" , "^"],
    unary_operators=[
         "exp",
         "inv(x) = 1/x",
        # ^ Custom operator (julia syntax)
    ],
    extra_sympy_mappings={"inv": lambda x: 1 / x},
    # ^ Define operator for SymPy as well
    loss="loss(prediction, target) = (prediction - target)^2",
    # ^ Custom loss function (julia syntax)
    )


    return model

##

def model_B()  :
 """
  model B
 """
 model = PySRRegressor(
##    niterations=40,  # < Increase me for better results
#     niterations=300,  # < Increase me for better results
       niterations=1000,  # < Increase me for better results
    binary_operators=["+", "*"],
    unary_operators=[
        "cos",
        "exp",
        "sin",
        "inv(x) = 1/x",
        # ^ Custom operator (julia syntax)
    ],
    extra_sympy_mappings={"inv": lambda x: 1 / x},
    # ^ Define operator for SymPy as well
    loss="loss(prediction, target) = (prediction - target)^2",
    # ^ Custom loss function (julia syntax)
 )
 return model



def model_C()  :
 """
  model C
 """
 model = PySRRegressor(
##    niterations=40,  # < Increase me for better results
     niterations=300,  # < Increase me for better results
#       niterations=1000,  # < Increase me for better results
    binary_operators=["+", "*"],
    unary_operators=[
#        "cos",
#        "exp",
#        "sin",
        "inv(x) = 1/x",
        # ^ Custom operator (julia syntax)
    ],
    extra_sympy_mappings={"inv": lambda x: 1 / x},
    # ^ Define operator for SymPy as well
    loss="loss(prediction, target) = (prediction - target)^2",
#    elementwise_loss=elementwise_loss
    # ^ Custom loss function (julia syntax)
 )
 return model



def model_D()  :
 """
  model D
 """
 model = PySRRegressor(
     model_selection='accuracy',
##    niterations=40,  # < Increase me for better results
#     niterations=300,  # < Increase me for better results
     niterations=1000,  # < Increase me for better results
    binary_operators=["+", "*" , "/" , "-"],
    unary_operators=[
#        "cos",
#        "exp",
#        "sin",
         "square" ,
         "cube" , 
        "inv(x) = 1/x",
        # ^ Custom operator (julia syntax)
    ],
    extra_sympy_mappings={"inv": lambda x: 1 / x},
    # ^ Define operator for SymPy as well
#    loss="loss(prediction, target) = (prediction - target)^2",
    elementwise_loss="loss(prediction, target) = (prediction - target)^2",
     #    elementwise_loss=elementwise_loss
    # ^ Custom loss function (julia syntax)
 )
 return model



def model_E()  :
 """
  model E
 """
 model = PySRRegressor(procs=10,
     model_selection='accuracy',
##    niterations=40,  # < Increase me for better results
#     niterations=300,  # < Increase me for better results
     niterations=1000,  # < Increase me for better results
    binary_operators=["+", "*" , "/" , "-"],
    unary_operators=[
#        "cos",
#        "exp",
#        "sin",
         "square" ,
         "cube" , 
        "inv(x) = 1/x",
        # ^ Custom operator (julia syntax)
    ],
    extra_sympy_mappings={"inv": lambda x: 1 / x},
    # ^ Define operator for SymPy as well
#    loss="loss(prediction, target) = (prediction - target)^2",
    elementwise_loss="loss(prediction, target) = (prediction - target)^2",
     #    elementwise_loss=elementwise_loss
    # ^ Custom loss function (julia syntax)
    denoise=True,
 )
 return model




def model_F()  :
 """
  model F
 """
 model = PySRRegressor(procs=10,
     model_selection='accuracy',
##    niterations=40,  # < Increase me for better results
#     niterations=300,  # < Increase me for better results
     niterations=1000,  # < Increase me for better results
    binary_operators=["+", "*" , "/" , "-"],
    unary_operators=[
#        "cos",
#        "exp",
#        "sin",
         "square" ,
         "cube" , 
        "inv(x) = 1/x",
        # ^ Custom operator (julia syntax)
    ],
    extra_sympy_mappings={"inv": lambda x: 1 / x},
    # ^ Define operator for SymPy as well
#    loss="loss(prediction, target) = (prediction - target)^2",
    elementwise_loss="loss(prediction, target,) = (prediction - target)^2/w^2",
     #    elementwise_loss=elementwise_loss
    # ^ Custom loss function (julia syntax)
    denoise=True,
 )
 return model



def model_G()  :
 """
  model G
 """
 model = PySRRegressor(
#     model_selection='accuracy',
    niterations=40,  # < Increase me for better results
#     niterations=300,  # < Increase me for better results
    denoise=True,
#     niterations=1000,  # < Increase me for better results
    binary_operators=["+", "*" , "/" , "-"],
    unary_operators=[
#        "cos",
#        "exp",
        "tan",
         "square" ,
        "cube" , 
#        "inv(x) = 1/x",
        # ^ Custom operator (julia syntax)
    ],
#    extra_sympy_mappings={"inv": lambda x: 1 / x},
    # ^ Define operator for SymPy as well
#    loss="loss(prediction, target) = (prediction - target)^2",
    elementwise_loss="loss(prediction, target) = (prediction - target)^2",
     #    elementwise_loss=elementwise_loss
    # ^ Custom loss function (julia syntax)
 )
 return model




###
##
###

model = model_A
