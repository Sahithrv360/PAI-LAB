from pgmpy.models import DiscreteBayesianNetwork
from pgmpy.factors.discrete import TabularCPD
from pgmpy.inference import VariableElimination

model = DiscreteBayesianNetwork([('Rain','Sprinkler'),
                        ('Rain','WetGrass'),
                        ('Sprinkler','WetGrass')]
                    )
cpd_rain = TabularCPD(  variable='Rain',variable_card=2,values=[[0.8],[0.2]] )

cpd_sprinkler = TabularCPD( variable='Sprinkler',variable_card=2,
                            values=([0.99, 0.6],
                                   [0.01, 0.4]),
                            evidence=['Rain'],
                            evidence_card=[2] )

cpd_wetgrass = TabularCPD(variable='WetGrass',variable_card=2,
                          values=[[0.01, 0.1, 0.1, 0.01],
                                  [0.99, 0.9, 0.9, 0.99]],
                          evidence=['Rain','Sprinkler'],
                          evidence_card=[2,2]
                          )
model.add_cpds(cpd_rain,cpd_sprinkler,cpd_wetgrass)
print(model.check_model())

infer = VariableElimination(model)
query_result = infer.query(['Rain'],evidence={'WetGrass' : 0})
print(query_result)