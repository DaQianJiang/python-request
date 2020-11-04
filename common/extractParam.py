class Extrct():
    params_dict = {}
    def uniform_extractData(self,extrat_data,response):
        #respondata = response.json()
        for data in extrat_data:
            respondata = response
            for k,v in data.items():
                if '.' in v:
                    vs  = v.split('.')
                    for s in vs[1:]:
                        respondata = respondata[s]
                        self.params_dict[k]=respondata
                else:
                    respondata = respondata[v]
                    self.params_dict[k] = respondata

        return self.params_dict

    def findall_variables(self):
        
        return

    def new_response(self,responsed,extrad):

        return

if __name__ == '__main__':
    e = Extrct()
    extra = [{'ordernum': 'content.data.id'}, {'dtat': 'content.data.name'}]
    response ={'code': 200, 'message': 'success', 'data': {'id': '21', 'name': '会理软籽石榴-臻选', 'type': 1, 'code': 'G00000000015', 'subTitle': None, 'coverImage': ['https://prod-boutique.oss-accelerate.aliyuncs.com/G00000000015.png'], 'thumbnail': ['https://prod-boutique.oss-accelerate.aliyuncs.com/G00000000015.png'], 'details': '<p><img src="https://prod-boutique.oss-accelerate.aliyuncs.com/G00000000015-detail.png"></p>', 'specVoList': [{'id': '21', 'name': '3.5KG/件(大果)', 'stock': 4941, 'goodsQuantity': 1, 'price': '12800', 'score': '0', 'specExpandVo': None}], 'activityVo': None, 'activityResult': None, 'minPriceAndScore': {'price': 12800, 'score': 0}}}
    res = e.uniform_extractData(extra,response)
    print(res)
