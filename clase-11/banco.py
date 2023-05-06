class Banco:
    cuentas = []
    movimientos = []

    def __init__(self):
        pass

    def agregar_cuenta(self, _cuenta, _rut):
        self.cuentas.append({
            'numero_cuenta': _cuenta,
            'rut': _rut,
            'correlativo_movimiento': 1,
            'saldo': 0

        })

    def agregar_movimiento(self, _cuenta, _fecha, _tipo, _monto):
        for elemento in self.cuentas:
            if elemento['numero_cuenta'] == _cuenta:
                if _tipo == 'Retiro':
                    if (elemento['saldo'] - _monto < 0):
                        print("Saldo insuficiente")
                    else:
                        self.movimientos.append({
                            'cuenta': _cuenta,
                            'fecha': _fecha,
                            'tipo': _tipo,
                            'monto': _monto,
                            'saldo': elemento['saldo'] - _monto
                        })
                        elemento['saldo'] = elemento['saldo'] - _monto
                        elemento['correlativo_movimiento'] = elemento['correlativo_movimiento'] + 1
                else:
                    self.movimientos.append({
                        'cuenta': _cuenta,
                        'fecha': _fecha,
                        'tipo': _tipo,
                        'monto': _monto,
                        'saldo': elemento['saldo'] + _monto
                    })
                    elemento['saldo'] = elemento['saldo'] + _monto
                    elemento['correlativo_movimiento'] = elemento['correlativo_movimiento'] + 1
                break

        
