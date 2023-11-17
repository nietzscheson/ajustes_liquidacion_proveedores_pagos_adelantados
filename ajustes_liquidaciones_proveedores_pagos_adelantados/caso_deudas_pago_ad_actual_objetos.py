from pydantic import BaseModel, Field
from datetime import datetime
from typing import List, Optional



class CasoDeudasPagoAdActualObjetosHistoricos(BaseModel):
    id: int
    monto_deuda_recuperado_dia_T_pago_ad_actual: float = Field(alias="monto_deuda_recuperado_dia_T_pago_ad")
    monto_deuda_pendiente_pago_adelantado_actual: float = Field(alias="monto_deuda_pendiente_nueva_pago_ad")
    id_pago_adelantado_actual: int = Field(alias="id_pago_adelantado")
    fecha_modificacion: datetime

class CasoDeudasPagoAdActualObjetos(BaseModel):
    historicos: Optional[List[CasoDeudasPagoAdActualObjetosHistoricos]] = None