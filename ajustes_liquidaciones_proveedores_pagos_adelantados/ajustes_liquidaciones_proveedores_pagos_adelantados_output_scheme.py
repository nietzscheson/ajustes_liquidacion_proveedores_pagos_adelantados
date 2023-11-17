from pydantic import BaseModel
from typing import Optional


class AjustesLiquidacionesProveedoresPagosAdelantadosOutputScheme(BaseModel):
    sumatoria_compensacion: Optional[float] = None
    total_final: Optional[float] = None
    deuda_nueva_ajuste_transaccion: Optional[float] = None
    monto_deuda_recuperado_transaccion_dia_T: Optional[float] = None
    monto_deuda_pendiente_nueva_transaccion: Optional[float] = None
    total_liquidar_final: Optional[float] = None
    id_estatus_liquidacion_proveedor: Optional[int] = None
