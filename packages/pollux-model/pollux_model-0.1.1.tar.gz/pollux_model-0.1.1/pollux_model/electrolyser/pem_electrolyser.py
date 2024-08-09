from pollux_model.model_abstract import Model
import os

path = os.path.dirname(__file__)


class PEMElectrolyser(Model):
    """ Class of ESP

        Class to calculate ESP power, efficiency and head
    """

    def __init__(self):
        """ Model initialization
        """
        self.parameters = {}
        self.output = {}

    def update_parameters(self, parameters):
        """ To update model parameters

        Parameters
        ----------
        parameters: dict
            parameters dict as defined by the model
        """
        for key, value in parameters.items():
            self.parameters[key] = value

    def initialize_state(self, x):
        """ generate an initial state based on user parameters """
        pass

    def update_state(self, u, x):
        """update the state based on input u and state x"""
        pass

    def calculate_output(self, u, x):
        """calculate output based on input u and state x"""
        # get input
        # pump_freq = u['pump_freq']
        # pump_flow = u['pump_flow']

        # TODO: define required functions in the bottom of this .py file for the calculations
        # calculate model
        # pump_head = self.head_function(pump_flow, pump_freq)
        # pump_power = self.power_function(pump_flow, pump_freq)
        # pump_eff = self.efficiency_function(pump_flow, pump_head, pump_power)

        # write output
        # self.output['pump_head'] = pump_head
        # self.output['pump_power'] = pump_power
        # self.output['pump_eff'] = pump_eff
        self.output['output'] = 'output_value'

    def get_output(self):
        """get output of the model"""
        return self.output
