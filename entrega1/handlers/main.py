#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import webapp2
import math

class MainHandler(webapp2.RequestHandler):
    def post(self):
        kilometros = self.request.get("edKilometros", "-1")
        tiempo = self.request.get("edTiempo", "-1")
        consumo = self.request.get("edConsumoMedio", "-1")
        velocidadmedia = float(kilometros)/int(tiempo)
        consumoresultado = (float(kilometros)*float(consumo))/100

        if math.isnan(float(kilometros)) or math.isnan(int(tiempo)) or math.isnan(float(consumo)):
            self.response.write("Error en el formato, los parametros introducidos no son digitos")


        elif len(kilometros.strip())==0  or len(tiempo.strip())==0 or \
                len(consumo.strip())==0 or  float(tiempo)<=0 \
                or float(consumo) < 0 or float(kilometros)< 0:
            self.response.write("Error en la obtencion de variables, estan vacios o son negativos")

        else:

            self.response.write("La velocidad media alcanzada es de:  " +
                            str(velocidadmedia) + " km/h en  "+ str(tiempo) + " horas " +
                            " produciendo un consumo de: " + str(consumoresultado))

app = webapp2.WSGIApplication([
    ('/entrega1', MainHandler)
], debug=True)
