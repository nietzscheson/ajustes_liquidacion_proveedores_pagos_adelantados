from ajustes_liquidaciones_proveedores_pagos_adelantados.ajustes_liquidaciones_proveedores_pagos_adelantados import AjustesLiquidacionesProveedoresPagosAdelantados
from ajustes_liquidaciones_proveedores_pagos_adelantados.ajustes_liquidaciones_proveedores_pagos_adelantados_input_scheme import AjustesLiquidacionesProveedoresPagosAdelantadosInputScheme



def test_ajustes_liquidaciones_proveedores_pagos_adelantados_caso_deudas_compensacion_menor_a_cero(historico_pagos_adelantados):
    
    ajustes_liquidaciones_proveedores_pagos_adelantados_input = AjustesLiquidacionesProveedoresPagosAdelantadosInputScheme(
        suma_conceptos_ajuste_transaccion_abono=-200,
        compensacion_actual=100,
        suma_conceptos_ajuste_transaccion_cargo=100,
        total_liquidar_actual=300,
        sumatoria_conceptos_ajustes_transaccion=-150,
        total_pago_adelantando=450,
        historico_pagos_adelantados=historico_pagos_adelantados
    )
    
    ajustes_liquidaciones_proveedores_pagos_adelantados = AjustesLiquidacionesProveedoresPagosAdelantados(input=ajustes_liquidaciones_proveedores_pagos_adelantados_input)
    
    output = ajustes_liquidaciones_proveedores_pagos_adelantados()

    assert output.sumatoria_compensacion == 100.0
    assert output.total_final == 150.0
    assert output.deuda_nueva_ajuste_transaccion == -150.0
    assert output.monto_deuda_recuperado_transaccion_dia_T == -0.0
    assert output.monto_deuda_pendiente_nueva_transaccion == -150.0
    assert output.total_liquidar_final == 450.0
    assert output.id_estatus_liquidacion_proveedor == 1
    
    