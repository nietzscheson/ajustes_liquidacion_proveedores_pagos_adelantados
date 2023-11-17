from pydantic import BaseModel
from datetime import datetime


class CasoDeudasPagoAdActualObjetos(BaseModel):
    monto_deuda_recuperado_dia_T_pago_ad_actual: float
    monto_deuda_pendiente_pago_adelantado_actual: float
    id_pago_adelantado_actual: int
    fecha_modificacion: datetime