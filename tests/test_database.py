import unittest
import database as db
import copy

class TestDatabase(unittest.TestCase):

    def setUp(self):
        db.Clientes.lista = [
            db.Cliente('43900419', 'Hugo', 'López'),
            db.Cliente('32904468', 'Roman', 'Martinez'),
            db.Cliente('42030999', 'Benjamín', 'Ibarra')
        ]

    def test_buscar_cliente(self):
        cliente_existente = db.Clientes.buscar('43900419')
        cliente_inexistente = db.Clientes.buscar('20900419')
        self.assertIsNotNone(cliente_existente)
        self.assertIsNone(cliente_inexistente)

    def test_crear_cliente(self):
        nuevo_cliente = db.Clientes.crear('43840326', 'Nahuel', 'Oblitas')
        self.assertEqual(len(db.Clientes.lista), 4)
        self.assertEqual(nuevo_cliente.dni, '43840326')
        self.assertEqual(nuevo_cliente.nombre, 'Nahuel')
        self.assertEqual(nuevo_cliente.apellido, 'Oblitas')

    def test_editar_cliente(self):
        cliente_a_editar = copy.copy(db.Clientes.buscar('42030999'))
        cliente_editado = db.Clientes.editar('42030999', 'Benjamín', 'Vicuña')
        self.assertEqual(cliente_a_editar.apellido, 'Ibarra')
        self.assertEqual(cliente_editado.apellido, 'Vicuña')

    def test_borrar_cliente(self):
        cliente_borrado = db.Clientes.borrar('32904468')
        cliente_rebuscado = db.Clientes.buscar('32904468')
        self.assertEqual(cliente_borrado.dni, '32904468')
        self.assertIsNone(cliente_rebuscado)