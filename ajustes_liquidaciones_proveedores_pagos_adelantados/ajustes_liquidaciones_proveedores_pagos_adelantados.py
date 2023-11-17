from ajustes_liquidaciones_proveedores_pagos_adelantados.ajustes_liquidaciones_proveedores_pagos_adelantados_input_scheme import (
    AjustesLiquidacionesProveedoresPagosAdelantadosInputScheme,
)
from ajustes_liquidaciones_proveedores_pagos_adelantados.ajustes_liquidaciones_proveedores_pagos_adelantados_output_scheme import (
    AjustesLiquidacionesProveedoresPagosAdelantadosOutputScheme,
)
from ajustes_liquidaciones_proveedores_pagos_adelantados.caso_deudas_pago_ad_actual_objetos import (
    CasoDeudasPagoAdActualObjetos, CasoDeudasPagoAdActualObjetosHistoricos
)

from typing import List


class AjustesLiquidacionesProveedoresPagosAdelantados:
    def __init__(
        self, input: AjustesLiquidacionesProveedoresPagosAdelantadosInputScheme
    ) -> None:
        self.input = input

    def __call__(
        self,
    ) -> AjustesLiquidacionesProveedoresPagosAdelantadosOutputScheme:

        ### Positiva o 0
        compensacion = self.input.suma_conceptos_ajuste_transaccion_abono

        if compensacion > 0:
            sumatoria_compensacion = compensacion + self.input.compensacion_actual

            lista_tupla_ajuste_transaccion_abono = (
                self.input.lista_tupla_ajuste_transaccion_abono
            )
            
            """
            Extraemos el Historico de Pagos Adelantados
            """
            historico_pagos_adelantados = self.input.historico_pagos_adelantados

            historicos_pagos_adelantados_id_pago_adelantado_duplicados = self.__historico_pagos_adelantados_duplicados(historico_pagos_adelantados)

            pagos_adelantados_recientes = self.__pagos_adelantados_recientes(historico_pagos_adelantados, historicos_pagos_adelantados_id_pago_adelantado_duplicados)
            
            historicos = self.__historicos(pagos_adelantados_recientes)

            caso_deudas_pago_ad_actual_objetos = self.__caso_deudas_pago_ad_actual_objetos(historicos)

            self._total_2_pago_ad_actual_resolver(
                lista_tupla_ajuste_transaccion_abono=lista_tupla_ajuste_transaccion_abono,
                caso_deudas_pago_ad_actual_objetos=caso_deudas_pago_ad_actual_objetos.historicos
            )

            output = AjustesLiquidacionesProveedoresPagosAdelantadosOutputScheme(
                sumatoria_compensacion=sumatoria_compensacion
            )

            return output

        sumatoria_compensacion = self.input.compensacion_actual

        total_final = (
            self.input.total_liquidar_actual
            + self.input.sumatoria_conceptos_ajustes_transaccion
        )
        deuda_nueva_ajuste_transaccion = (
            self.input.sumatoria_conceptos_ajustes_transaccion
        )
        monto_deuda_recuperado_transaccion_dia_T = 0
        monto_deuda_pendiente_nueva_transaccion = (
            self.input.sumatoria_conceptos_ajustes_transaccion
        )

        total_liquidar_final = total_final
        id_estatus_liquidacion_proveedor = 6

        if self.input.total_pago_adelantando > 0:
            total_liquidar_final = self.input.total_pago_adelantando
            id_estatus_liquidacion_proveedor = 1

        output = AjustesLiquidacionesProveedoresPagosAdelantadosOutputScheme(
            sumatoria_compensacion=sumatoria_compensacion,
            total_final=total_final,
            deuda_nueva_ajuste_transaccion=deuda_nueva_ajuste_transaccion,
            monto_deuda_recuperado_transaccion_dia_T=monto_deuda_recuperado_transaccion_dia_T,
            monto_deuda_pendiente_nueva_transaccion=monto_deuda_pendiente_nueva_transaccion,
            total_liquidar_final=total_liquidar_final,
            id_estatus_liquidacion_proveedor=id_estatus_liquidacion_proveedor,
        )

        return output

    @classmethod
    def _total_2_pago_ad_actual_resolver(
        cls,
        index: int = 0,
        lista_tupla_ajuste_transaccion_abono=List[tuple],
        caso_deudas_pago_ad_actual_objetos = List[CasoDeudasPagoAdActualObjetos],
        total_2_pago_ad_actual: float = 0,
        movimientos: List = [],
    ):
        if not lista_tupla_ajuste_transaccion_abono and not caso_deudas_pago_ad_actual_objetos:
            return total_2_pago_ad_actual

        abono = None
        abono_id = None
        abono_monto = None
        
        if lista_tupla_ajuste_transaccion_abono:
            
            abono = lista_tupla_ajuste_transaccion_abono[0]
            abono_id = abono[0]
            abono_monto = abono[1]
            
            lista_tupla_ajuste_transaccion_abono.pop(0)
        
        historico = None
        
        if index == 0:
        
            if caso_deudas_pago_ad_actual_objetos:
                historico = caso_deudas_pago_ad_actual_objetos[0]
            
                caso_deudas_pago_ad_actual_objetos.pop(0)
            
            total_2_pago_ad_actual = (
                abono_monto + historico.monto_deuda_pendiente_pago_adelantado_actual
            )
        else:
            
            if total_2_pago_ad_actual > 0:
                historico = caso_deudas_pago_ad_actual_objetos[0]
            
                caso_deudas_pago_ad_actual_objetos.pop(0)
            
                total_2_pago_ad_actual = (
                    total_2_pago_ad_actual + historico.monto_deuda_pendiente_pago_adelantado_actual
                )
            else:
                total_2_pago_ad_actual = abono_monto + total_2_pago_ad_actual

        index = index + 1
        
        if total_2_pago_ad_actual < 0:
            movimiento = {
                "id_ajuste_transaccion": abono_id,
                "monto_disponible": 0,
                "monto_pagado": abono_monto,
                "id_historico_pagado_actual": historico.id_pago_adelantado_actual, 
            }
            
            movimientos.append(movimiento)

            return AjustesLiquidacionesProveedoresPagosAdelantados._total_2_pago_ad_actual_resolver(
                index=index,
                lista_tupla_ajuste_transaccion_abono=lista_tupla_ajuste_transaccion_abono,
                caso_deudas_pago_ad_actual_objetos=caso_deudas_pago_ad_actual_objetos,
                total_2_pago_ad_actual=total_2_pago_ad_actual,
                movimientos=movimientos
            )

        id_pago_adelantado = historico.id_pago_adelantado_actual if historico else movimientos[-1]["id_historico_pagado_actual"]

        movimiento = {
            "id_ajuste_transaccion": abono_id,
            "monto_disponible": total_2_pago_ad_actual,
            "monto_pagado": abono[1] - total_2_pago_ad_actual,
            "id_historico_pagado_actual": id_pago_adelantado, 
        }
        
        movimientos.append(movimiento)

        return AjustesLiquidacionesProveedoresPagosAdelantados._total_2_pago_ad_actual_resolver(
            index=index,
            lista_tupla_ajuste_transaccion_abono=lista_tupla_ajuste_transaccion_abono,
            caso_deudas_pago_ad_actual_objetos=caso_deudas_pago_ad_actual_objetos,
            total_2_pago_ad_actual=total_2_pago_ad_actual,
            movimientos=movimientos
        )

    def __historico_pagos_adelantados_duplicados(self, historico_pagos_adelantados):
        """
            Recorremos el Historico de Pagos Adelantados 
            para identificar los pagos adelantados duplicados
            con el id_pago_adelantado
        """
        return [
            id_pago
            for id_pago in {
                item.id_pago_adelantado for item in historico_pagos_adelantados
            }
            if [item.id_pago_adelantado for item in historico_pagos_adelantados].count(
                id_pago
            )
            > 1
        ]
        
    def __pagos_adelantados_recientes(self, historico_pagos_adelantados, historicos_pagos_adelantados_id_pago_adelantado_duplicados):
        """
            Extraemos los pagos adelantados mas recientes de cada pago adelantado duplicado
        """
        return [
            max(
                (
                    item
                    for item in historico_pagos_adelantados
                    if item.id_pago_adelantado == id_pago
                ),
                key=lambda x: x.fecha_modificacion,
            )
            for id_pago in historicos_pagos_adelantados_id_pago_adelantado_duplicados
        ]
        
    def __historicos(self, pagos_adelantados_recientes):
    
        """
            Se crean los objetos historicos de los pagos adelantados recientes
        """
        return [
            CasoDeudasPagoAdActualObjetosHistoricos(**vars(historico)) for historico in pagos_adelantados_recientes
        ]
        
    def __caso_deudas_pago_ad_actual_objetos(self, historicos):
    
        """
            Se crea el objeto Caso Deudas Pago Ad Actual Objetos
        """
        return CasoDeudasPagoAdActualObjetos(
            historicos=historicos,
        )
    