import xmltodict
def corregir_nombre(factura):
    if type(factura.afip_xml_response) is not bool:
        response_dict = xmltodict.parse(factura.afip_xml_response)
        nro_afip = response_dict['soap:Envelope']['soap:Body']['FECAESolicitarResponse']['FECAESolicitarResult']['FeDetResp']['FECAEDetResponse']['CbteHasta'] #Se obtiene el valor correcto de la AFIP
        pto_venta = response_dict['soap:Envelope']['soap:Body']['FECAESolicitarResponse']['FECAESolicitarResult']['FeCabResp']['PtoVta']
        if int(factura.name[12:]) != int(nro_afip):
            nro_factura = '0'*(8 - len(str(nro_afip)))+str(nro_afip) #En STRING
            nombre = "FA-A 0000"+str(pto_venta)+"-"+nro_factura
            print(nombre)
            #factura.write({'name':nombre}) #Descomentar para ejecutar los cambios.
            #self.env.cr.commit()  #Descomentar para ejecutar los cambios.

facturas = self.env['account.move']
#for item in facturas.search([('name','ilike','FA-A')]):
#opciones para ordenar ascendente y descendente las FC, descomentar segun la necesidad
for item in facturas.search([('name', 'ilike', 'FA-A')], order='name asc'):
#for item in facturas.search([('name', 'ilike', 'FA-A')], order='name desc'):
    corregir_nombre(item)