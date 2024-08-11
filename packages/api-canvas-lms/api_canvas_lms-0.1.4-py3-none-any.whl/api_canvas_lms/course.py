""" 
Programa : Course module for Canvas
Fecha Creacion : 11/08/2024
Fecha Update : None
Version : 1.0.0
Actualizacion : None
Author : Jaime Gomez
"""

import logging
from .base import BaseCanvas

NAME =  'name'

# Create a logger for this module
logger = logging.getLogger(__name__)

class Course(BaseCanvas):

    def __init__(self, course_id, access_token):
        super().__init__(access_token)
        # 
        self.course_id = course_id
        # CONNECTOR
        self.url_course        = '<path>/courses/<course_id>'

    def get(self, params = None):
        url = self.url_course
        url = url.replace('<course_id>', self.course_id)
        return super().get(url,params)

    def get_summary(self, params = None):
        data =  self.get(params)
        return  {NAME : data[NAME]}
