from typing import List, Optional
from pydantic import BaseModel, field_validator
from datetime import datetime



class HistoricosPagosAdelantadosScheme(BaseModel):
    id: int
    monto_deuda_recuperado_dia_T_pago_ad: float
    monto_deuda_pendiente_nueva_pago_ad: float
    id_pago_adelantado: int
    fecha_modificacion: datetime


class AjustesLiquidacionesProveedoresPagosAdelantadosInputScheme(BaseModel):
    suma_conceptos_ajuste_transaccion_abono: float
    compensacion_actual: float
    suma_conceptos_ajuste_transaccion_cargo: float
    total_liquidar_actual: float
    sumatoria_conceptos_ajustes_transaccion: float
    total_pago_adelantando: float
    historico_pagos_adelantados: Optional[List[HistoricosPagosAdelantadosScheme]]
    
    @field_validator('sumatoria_conceptos_ajustes_transaccion')
    def convert_to_negative(cls, v):
        if v > 0:
            return -v
        return v
    
    @field_validator('total_pago_adelantando')
    def convert_to_non_negative(cls, v):
        return abs(v)