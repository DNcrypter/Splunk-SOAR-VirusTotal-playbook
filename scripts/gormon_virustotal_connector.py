#!/usr/bin/python
from __future__ import print_function, unicode_literals

import phantom.app as phantom
from phantom.base_connector import BaseConnector
from phantom.action_result import ActionResult

from gorman_virustotal_consts import *


def handle_test_connectivity(self, param):
    # add an action result object to self (BaseConnector) to represent the action for this param
    action_result = self.add_action_result(ActionResult(dict(param)))


    self.save_progress("Connecting to endpoint")
    # make rest call

    # Optional values should use the .get() function
    #optional_parameter = param.get('optional_parameter', 'default_value')----------------> X

# make rest call
params = {'apikey': self._api_key, 'resource': hash}
ret_val, response = self._make_rest_call(
    '/file/report', action_result, params=params, headers=None
)

if phantom.is_fail(ret_val):
    # the call to the 3rd party device or service failed, action result should contain all the error details
    # for now the return is commented out, but after implementation, return from here
    # return action_result.get_status()
    pass

# Now post process the data, uncomment code as you deem fit

# Add the response into the data section
action_result.add_data(response)

# Add a dictionary that is made up of the most important values from data into the summary
summary = action_result.update_summary({})
# summary['num_data'] = len(action_result['data'])

# Return success, no need to set the message, only the status
# BaseConnector will create a textual message based off of the summary dictionary
return action_result.set_status(phantom.APP_SUCCESS)

# For now return Error with a message, in case of success we don't set the message, but use the summary
# return action_result.set_status(phantom.APP_ERROR, "Action not yet implemented")


def _handle_file_reputation(self, param):
    # Implement the handler here
    # use self.save_progress(...) to send progress messages back to the platform
    self.save_progress("In action handler for: {0}".format(self.get_action_identifier()))

    # Add an action result object to self (BaseConnector) to represent the action for this param
    action_result = self.add_action_result(ActionResult(dict(param)))

    # Access action parameters passed in the 'param' dictionary

    # Required values can be accessed directly
    hash = param['hash']

    # Optional values should use the .get() function
    # optional_parameter = param.get('optional_parameter', 'default_value')

    # make rest call
    ret_val, response = self._make_rest_call(
        '/file/report', action_result, params=None, headers=None
    )

    if phantom.is_fail(ret_val):
        # the call to the 3rd party device or service failed, action result should contain all.



class Gorman_VirustotalConnector(BaseConnector):

    def __init__(self):
        # Call the BaseConnectors init first
        super(Gorman_VirustotalConnector, self).__init__()

        self._state = None

        # Variable to hold a base_url in case the app makes REST calls
        # Do note that the app json defines the asset config, so please
        # modify this as you deem fit.
        self._base_url = 'https://www.virustotal.com/vtapi/v2'
        self._api_key = config['api_key']




def initialize(self):
    # Load the state in initialize, use it to store data
    # that needs to be accessed across actions
    self._state = self.load_state()

    # get the asset config
    config = self.get_config()
    
    """
    # Access values in asset config by the name
    
    # Required values can be accessed directly
    required_config_name = config['required_config_name']
    
    # Optional values should use the .get() function
    optional_config_name = config.get('optional_config_name')
    """

    self._base_url = 'https://www.virustotal.com/vtapi/v2'
    self._api_key = config['api_key']

    return phantom.APP_SUCCESS





