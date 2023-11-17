import pytest
from datetime import datetime


@pytest.fixture
def historico_pagos_adelantados():
    datetime_format = "%Y-%m-%d: %I:%M %p"
    
    return [
        {"id": 1, "monto_deuda_recuperado_dia_T_pago_ad": 200, "monto_deuda_pendiente_nueva_pago_ad": -500, "id_pago_adelantado": 1, "fecha_modificacion": datetime.strptime("2023-10-07: 10:00 am", datetime_format)},
        {"id": 2, "monto_deuda_recuperado_dia_T_pago_ad": 300, "monto_deuda_pendiente_nueva_pago_ad": -400, "id_pago_adelantado": 1, "fecha_modificacion": datetime.strptime("2023-10-07: 10:30 am", datetime_format)},
        {"id": 3, "monto_deuda_recuperado_dia_T_pago_ad": 0, "monto_deuda_pendiente_nueva_pago_ad": -600, "id_pago_adelantado": 2, "fecha_modificacion": datetime.strptime("2023-10-07: 11:00 am", datetime_format)}
    ]