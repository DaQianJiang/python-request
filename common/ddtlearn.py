from common.excel_reader import dataReader
import ddt
import  unittest
import paramunittest

#login_excel = dataReader().get_excel("user.xlsx",'login')
login_excel = dataReader().get_excel("user.xlsx",'testlearn')

@ddt.ddt
class ddtlearn(unittest.TestCase):

    def setUp(self):
        print('start')

    @ddt.data(*login_excel)

    def test_1getexceldata(self,data):
        id,name,description = data
        #self.url = data['url']
        #print(data)
        #print(data[2])
        print(id)


    def tearDown(self):
        print('end')

# @paramunittest.parametrized(*login_excel)
# class paramlearn(unittest.TestCase):
#     def setUp(self):
#         print('start')
#     def tearDown(self):
#         print('end')
#     def setParameters(self,id,name,description):
#         self.id = id
#         self.name = name
#         self.description = description
#     def test_getdata(self):
#         print(self.id,self.name,self.description)

if __name__ == '__main__':
    unittest.main()
