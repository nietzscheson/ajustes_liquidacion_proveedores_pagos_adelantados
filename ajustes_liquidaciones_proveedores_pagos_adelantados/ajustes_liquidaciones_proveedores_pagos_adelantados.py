from ajustes_liquidaciones_proveedores_pagos_adelantados.ajustes_liquidaciones_proveedores_pagos_adelantados_input import AjustesLiquidacionesProveedoresPagosAdelantadosInput
from ajustes_liquidaciones_proveedores_pagos_adelantados.ajustes_liquidaciones_proveedores_pagos_adelantados_output import AjustesLiquidacionesProveedoresPagosAdelantadosOutput


class AjustesLiquidacionesProveedoresPagosAdelantados:
    def __init__(self, input: AjustesLiquidacionesProveedoresPagosAdelantadosInput) -> None:
        self.input = input

    def __call__(self,) -> AjustesLiquidacionesProveedoresPagosAdelantadosOutput:
        return "Ajustes"