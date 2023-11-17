from ajustes_liquidaciones_proveedores_pagos_adelantados.ajustes_liquidaciones_proveedores_pagos_adelantados_input_scheme import AjustesLiquidacionesProveedoresPagosAdelantadosInputScheme
from ajustes_liquidaciones_proveedores_pagos_adelantados.ajustes_liquidaciones_proveedores_pagos_adelantados_output_scheme import AjustesLiquidacionesProveedoresPagosAdelantadosOutputScheme
from ajustes_liquidaciones_proveedores_pagos_adelantados.caso_deudas_pago_ad_actual_objetos import CasoDeudasPagoAdActualObjetos
from datetime import datetime

class AjustesLiquidacionesProveedoresPagosAdelantados:
    def __init__(self, input: AjustesLiquidacionesProveedoresPagosAdelantadosInputScheme) -> None:
        self.input = input

    def __call__(self,) -> AjustesLiquidacionesProveedoresPagosAdelantadosOutputScheme:
       
        """
            Extraemos el Historico de Pagos Adelantados
        """ 
        historico_pagos_adelantados = self.input.historico_pagos_adelantados
        
        """
            Recorremos el Historico de Pagos Adelantados para identificar los pagos adelantados duplicados
        """
        historico_pagos_adelantados_id_pago_adelantado_duplicado = [
            id_pago for id_pago in {item.id_pago_adelantado for item in historico_pagos_adelantados} 
            if [item.id_pago_adelantado for item in historico_pagos_adelantados].count(id_pago) > 1
        ]
        
        """
            Extraemos los pagos adelantados mas recientes de cada pago adelantado duplicado
        """

        pago_adelantado_reciente = [max((item for item in historico_pagos_adelantados if item.id_pago_adelantado == id_pago), key=lambda x: x.fecha_modificacion)for id_pago in historico_pagos_adelantados_id_pago_adelantado_duplicado][0]

        """
            Se crea el objeto Caso Deudas Pago Ad Actual Objetos
        """
        caso_deudas_pago_ad_actual_objetos = CasoDeudasPagoAdActualObjetos(
            monto_deuda_recuperado_dia_T_pago_ad_actual=pago_adelantado_reciente.id,
            monto_deuda_pendiente_pago_adelantado_actual=pago_adelantado_reciente.monto_deuda_pendiente_nueva_pago_ad,
            id_pago_adelantado_actual=pago_adelantado_reciente.id_pago_adelantado,
            fecha_modificacion=pago_adelantado_reciente.fecha_modificacion,
        )
        
        compensacion = self.input.suma_conceptos_ajuste_transaccion_abono
         
        if compensacion > 0:
            
            sumatoria_compensacion = compensacion + self.input.compensacion_actual
            
            output = AjustesLiquidacionesProveedoresPagosAdelantadosOutputScheme(
                sumatoria_compensacion=sumatoria_compensacion
            )
            
            return output
        
        sumatoria_compensacion = self.input.compensacion_actual
        total_final = self.input.total_liquidar_actual + self.input.sumatoria_conceptos_ajustes_transaccion
        deuda_nueva_ajuste_transaccion = self.input.sumatoria_conceptos_ajustes_transaccion
        monto_deuda_recuperado_transaccion_dia_T = 0
        monto_deuda_pendiente_nueva_transaccion = self.input.sumatoria_conceptos_ajustes_transaccion

        total_liquidar_final = self.input.total_pago_adelantando
        id_estatus_liquidacion_proveedor = 1
        
        output = AjustesLiquidacionesProveedoresPagosAdelantadosOutputScheme(
            sumatoria_compensacion=sumatoria_compensacion,
            total_final=total_final,
            deuda_nueva_ajuste_transaccion=deuda_nueva_ajuste_transaccion,
            monto_deuda_recuperado_transaccion_dia_T=monto_deuda_recuperado_transaccion_dia_T,
            monto_deuda_pendiente_nueva_transaccion=monto_deuda_pendiente_nueva_transaccion,
            total_liquidar_final=total_liquidar_final,
            id_estatus_liquidacion_proveedor=id_estatus_liquidacion_proveedor
        )
        
        return output
        
        #print(caso_deudas_pago_ad_actual_objetos)
        #return "Ajustes"