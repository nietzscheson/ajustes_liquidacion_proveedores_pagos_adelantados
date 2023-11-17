from pydantic import BaseModel
from typing import List, Optional

class AjustesLiquidacionesProveedoresPagosAdelantadosOutputScheme(BaseModel):
    sumatoria_compensacion: Optional[float]
    total_final: Optional[float]
    deuda_nueva_ajuste_transaccion: Optional[float]
    monto_deuda_recuperado_transaccion_dia_T: Optional[float]
    monto_deuda_pendiente_nueva_transaccion: Optional[float]
    total_liquidar_final: Optional[float]
    id_estatus_liquidacion_proveedor: Optional[int]