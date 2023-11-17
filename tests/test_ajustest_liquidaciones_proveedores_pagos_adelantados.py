from ajustes_liquidaciones_proveedores_pagos_adelantados.ajustes_liquidaciones_proveedores_pagos_adelantados import AjustesLiquidacionesProveedoresPagosAdelantados
from ajustes_liquidaciones_proveedores_pagos_adelantados.ajustes_liquidaciones_proveedores_pagos_adelantados_input import AjustesLiquidacionesProveedoresPagosAdelantadosInput



def test_ajustest_liquidaciones_proveedores_pagos_adelantados_caso_deudas_compensacion_menor_cero(historico_pagos_adelantados):
    
    ajustes_liquidaciones_proveedores_pagos_adelantados_input = AjustesLiquidacionesProveedoresPagosAdelantadosInput(
        suma_conceptos_ajuste_transaccion_abono=-200,
        compensacion_actual=100,
        suma_conceptos_ajuste_transaccion_cargo=100,
        total_liquidar_actual=300,
        sumatoria_conceptos_ajustes_transaccion=-150,
        total_pago_adelantando=450,
        historico_pagos_adelantados=historico_pagos_adelantados
    )
     
    ajustes_liquidaciones_proveedores_pagos_adelantados = AjustesLiquidacionesProveedoresPagosAdelantados(input=ajustes_liquidaciones_proveedores_pagos_adelantados_input)
         
    assert ajustes_liquidaciones_proveedores_pagos_adelantados() == "Ajustes"
    