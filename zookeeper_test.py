import unittest
from zookeeper import Ztree

class TestZookeeper(unittest.TestCase):

    def test_crear_znode(self):
        tree = Ztree()
        tree.create('/node1', 'algo', True, True, 10, '/')
        self.assertEqual(tree.getData('/node1'), 'algo')

    def test_no_se_puede_crear(self):
        with self.assertRaises(Exception):
            tree = Ztree()
            tree.create('/node1/node2/node3', 'algo', True, True, 10, None)

    def test_eliminar_znode(self):
    	print("\n--------------Prueba: Eliminar znode--------------")
    	tree = Ztree()
    	tree.create('/node1', 'algo', True, True, 10, '/')
    	tree.delete('/node1', 0)
    	self.assertFalse(tree.exist('/node1'))
    	tree.showTree()    	

    def test_no_se_puede_eliminar_znode_version(self):
    	print("\n--------------Prueba: No se puede eliminar znode por versión incorrecta--------------")
    	tree = Ztree()
    	tree.create('/node1', 'algo', True, True, 10, '/')
    	tree.delete('/node1', 10)
    	self.assertTrue(tree.exist('/node1'))
    	tree.showTree()

    def test_no_se_puede_eliminar_znode_no_existe(self):
    	print("\n--------------Prueba: No se puede eliminar znode porque no existe--------------")
    	tree = Ztree()
    	tree.create('/node1', 'algo', True, True, 10, '/')
    	tree.delete('/node1/node2', 0)
    	self.assertTrue(tree.exist('/node1'))
    	tree.showTree()

    def test_modificando_contenido_znode(self):
    	print("\n--------------Prueba: Modificando contenido de znode--------------")
    	tree = Ztree()
    	tree.create('/node1', 'algo', True, True, 10, '/')
    	tree.showNode('/node1')
    	tree.setData('/node1', 'otro_contenido')
    	tree.showNode('/node1')
    	self.assertEqual(tree.getData('/node1'), 'otro_contenido')

    def test_mostrar_hijos(self):
    	print("\n--------------Prueba: Mostrando hijos--------------")
    	tree = Ztree()
    	tree.create('/node1', 'algo', True, True, 10, '/')
    	tree.create('/node2', 'algo', True, True, 10, '/node1')
    	tree.create('/node3', 'algo', True, True, 10, '/node1')
    	tree.getChildren('/node1')


if __name__ == '__main__':
    unittest.main()

