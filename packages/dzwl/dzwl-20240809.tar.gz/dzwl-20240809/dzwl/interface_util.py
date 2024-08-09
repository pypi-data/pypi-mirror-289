import copy
import requests
from dzwl.fun_util import fun_util,DateEncoder
import os
import yaml
from string import Template
import json
from Config.config import CommonConfig
import pytest

class requsts_util:
    session = requests.session()
    @classmethod
    def send_request(cls,method,url,data,headers,**kwargs):
        method = str(method).lower()
        try:
            if method == 'get':
                rep = requsts_util.session.request(method=method, url=url, params=data,headers = headers,**kwargs)
            elif method == 'delete':
                rep = requsts_util.session.delete(url=url, params=data,headers = headers,**kwargs)
            else:
                if 'form' in str(headers):
                    rep = requsts_util.session.request(method=method, url=url, data=data,headers= headers, **kwargs)
                else:
                    rep = requsts_util.session.request(method=method, url=url, json=data,headers= headers, **kwargs)
        except Exception as e:
            print('无法连接:'+str(e))
        else:
            if rep.status_code==200:
                resp = json.loads(rep.text)
                return resp
            else:
                print('请求状态异常：'+str(rep.status_code))

    @classmethod
    def excute_interface(cls,caseinfo,domain):
        #循环读取yml中配置的接口参数
            #caseinfo是个dic，通过caseinfo.keys()获取key，使用list()转为list类型，取下标0即可，yml测试数据的动态管理
            #caseinfo_key = list(caseinfo.keys())[0]
            #从config文件中读取domain与接口地址拼接,login接口可能用别的域名，判断一下
            url = domain + caseinfo['path']
            #读取请求类型
            method = caseinfo['method']
            #读取请求数据
            data = caseinfo['data']
            #读取请求头
            headers = caseinfo['headers']
            #读取描述
            description = caseinfo['description']
            #发送请求
            resp = cls.send_request(method=method,url=url,data=data,headers=headers)
            print('\n')
            fun_util.logView('描述：'+description)
            fun_util.logView('请求url：'+url)
            fun_util.logView('请求header：'+json.dumps(headers,indent = 4,ensure_ascii=False))
            fun_util.logView('请求body：'+json.dumps(data,indent = 4,ensure_ascii=False,cls=DateEncoder))
            fun_util.logView('返回：'+json.dumps(resp,indent = 4,ensure_ascii=False))
            if 'assert_type' in caseinfo and 'is_assert' in caseinfo:
                # 读取断言类型
                assert_type = caseinfo['assert_type']
                # 读取断言信息
                is_assert = caseinfo['is_assert']
                requsts_util.check_assert(is_assert,resp,assert_type)
            return resp

    @classmethod
    def check_assert(cls,expected, result, type):
        fun_util.logView('-------------------------------------------------------------------------------------')
        fun_util.logView('断言期望内容：' + json.dumps(expected, indent=4, ensure_ascii=False) + '；断言模式：' + type)
        if result != None:
            if expected == None:
                fun_util.logView('断言结果：无须断言')
                pytest.assume(True)
                return True
            else:
                if type == 'and':
                    for expected_key, expected_value in expected.items():
                        # 取出的键值拼装新的单个字典
                        dic = dict.fromkeys([expected_key], expected_value)
                        # 字典转为字符串，并截取dic的花括号
                        dic = str(dic)
                        # 截取去除花括号
                        dic = dic[1:len(dic) - 1]
                        result = str(result)
                        if dic in result:
                            continue
                        if dic not in result:
                            fun_util.logView('断言结果：断言失败')
                            pytest.fail('\n'+'接口实际返回：' +'\n\n'+ result + '\n\n' + '中不包含期望的断言：' + '\n\n' + dic)
                            return False
                    fun_util.logView('断言结果：断言成功')
                    pytest.assume(True)
                    return True
                if type == 'or':
                    for expected_key, expected_value in expected.items():
                        # 取出的键值拼装新的单个字典
                        dic = dict.fromkeys([expected_key], expected_value)
                        # 字典转为字符串，并截取dic的花括号
                        dic = str(dic)
                        # 截取去除花括号
                        dic = dic[1:len(dic) - 1]
                        result = str(result)
                        if dic in result:
                            fun_util.logView('断言结果：断言成功')
                            pytest.assume(True)
                            return True
                        if dic not in result:
                            continue
                    fun_util.logView('断言结果：断言失败')
                    pytest.fail('\n'+'接口实际返回：' +'\n\n'+ result + '\n\n' + '中不包含期望的断言：' + '\n\n' + dic)
                    return False
                if type == 'not_and':
                    for expected_key, expected_value in expected.items():
                        # 取出的键值拼装新的单个字典
                        dic = dict.fromkeys([expected_key], expected_value)
                        # 字典转为字符串，并截取dic的花括号
                        dic = str(dic)
                        # 截取去除花括号
                        dic = dic[1:len(dic) - 1]
                        result = str(result)
                        # print(str(dic),str(result))
                        if dic not in result:
                            continue
                        if dic in result:
                            fun_util.logView('断言结果：断言失败')
                            pytest.fail('\n'+'接口实际返回：' +'\n\n'+ result + '\n\n' + '中不包含期望的断言：' + '\n\n' + dic)
                            return False
                    fun_util.logView('断言结果：断言成功')
                    pytest.assume(True)
                    return True
                if type == 'not_or':
                    for expected_key, expected_value in expected.items():
                        # 取出的键值拼装新的单个字典
                        dic = dict.fromkeys([expected_key], expected_value)
                        # 字典转为字符串，并截取dic的花括号
                        dic = str(dic)
                        # 截取去除花括号
                        dic = dic[1:len(dic) - 1]
                        result = str(result)
                        if dic not in result:
                            fun_util.logView('断言结果：断言成功')
                            pytest.assume(True)
                            return True
                        if dic in result:
                            continue
                    fun_util.logView('断言结果：断言失败')
                    pytest.fail('\n'+'接口实际返回：' +'\n\n'+ result + '\n\n' + '中不包含期望的断言：' + '\n\n' + dic)
                    return False
        else:
            pytest.fail(result+'中不包含期望的'+dic)
            return False
            print('接口返回为空')

class yaml_util:
    rootPath = CommonConfig.rootPath
    # 读取common_var.yml文件
    @classmethod
    def read_extract_yaml(cls, key, file_path=rootPath + "/Common/common_var.yml"):
        with open(file_path, mode='r', encoding='utf-8') as f:
            value = yaml.load(stream=f, Loader=yaml.FullLoader)
            if value == None:
                return None
            else:
                for kk in value:
                    if key == kk:
                        if value == None:
                            return None
                        else:
                            return value[key];
                    else:
                        continue
                    return None

    # 写入common_var.yml文件
    @classmethod
    def write_extract_yaml(cls,data,file_path = rootPath + "/Common/common_var.yml"):
        #   写入公共变量模式
        if "/Common/common_var.yml" in file_path:
            # 读取文件中的所有数据
            with open(file_path, mode='r', encoding='utf-8') as f:
                all_data = yaml.safe_load(f) or {}
            # 将传入的数据转换为字典格式，并更新到all_data中
            for d in data:
                for key_data in d.keys():
                    if key_data in all_data:
                        all_data[key_data]=d[key_data]
                    else:
                        all_data.update(d)
            # 将所有数据写入文件中
            with open(file_path, mode='w', encoding='utf-8') as f:
                yaml.dump(data=all_data, stream=f, allow_unicode=True)
        #写入文件模式
        else:
            # 获取文件所在的目录路径
            dir_path = os.path.dirname(file_path)
            # 检查目录是否存在，如果不存在则创建目录
            if not os.path.exists(dir_path):
                os.makedirs(dir_path)


            # 将所有数据写入文件中
            with open(file_path, mode='w', encoding='utf-8') as f:
                yaml.dump(data=data, stream=f, allow_unicode=True)
    #旧
    # @classmethod
    # def write_extract_yaml(self,data):
    #     file_path = os.path.join(self.rootPath, "Common", "common_var.yml")
    #
    #     # 读取文件中的所有数据
    #     with open(file_path, mode='r', encoding='utf-8') as f:
    #         all_data = yaml.safe_load(f) or {}
    #     # 将传入的数据转换为字典格式，并更新到all_data中
    #     for d in data:
    #         for key_data in d.keys():
    #             if key_data in all_data:
    #                 all_data[key_data]=d[key_data]
    #             else:
    #                 all_data.update(d)
    #     # 将所有数据写入文件中
    #     with open(file_path, mode='w', encoding='utf-8') as f:
    #         yaml.dump(data=all_data, stream=f, allow_unicode=True)


    # 清除common_var.yml文件
    @classmethod
    def clean_extract_yaml(cls) :
        with open(cls.rootPath+"/Common/common_var.yml",mode='w',encoding='utf-8') as f:
            f.truncate()

    #读取测试用例的yml文件
    @classmethod
    def read_testcase_yaml(cls,yaml_name):
        with open(cls.rootPath+yaml_name,mode='r',encoding='utf-8') as f:
            value = yaml.load(stream=f,Loader=yaml.FullLoader)
            return value;

    #写入测试用例的yml文件
    @classmethod
    def write_testcase_yaml(cls,caseinfo,content) :
        def toDict(caseinfo_tmp,new_key,new_value):
            #值为list时
            if isinstance(caseinfo_tmp, list):
                for caseinfo_tmp_value in caseinfo_tmp:
                    toDict(caseinfo_tmp_value, new_key, new_value)
            #值为dict时
            if isinstance(caseinfo_tmp, dict):
                for caseinfo_tmp_key, caseinfo_tmp_value in caseinfo_tmp.items():
                    #判断是否有请求内容，没有跳过
                    if caseinfo_tmp_value!=None:
                        #判断模板中字段值是否有下一级，没有进行替换值
                        if isinstance(caseinfo_tmp_value, str):
                            #判断匹配
                            if '${' + new_key + '}' in caseinfo_tmp_value:
                                #全部替换
                                if '${' + new_key + '}' == caseinfo_tmp_value:
                                    caseinfo_tmp[caseinfo_tmp_key] = new_value
                                #模糊替换
                                else:
                                    caseinfo_tmp[caseinfo_tmp_key] = caseinfo_tmp[caseinfo_tmp_key].replace('${' + new_key + '}',new_value)
                        #子字段值为嵌套dict
                        if isinstance(caseinfo_tmp_value, dict):
                            toDict(caseinfo_tmp_value,new_key,new_value)
                        #子字段值为list
                        if isinstance(caseinfo_tmp_value, list):
                            toDict(caseinfo_tmp_value, new_key, new_value)

                    else:
                        continue
        #拿到模板dict
        caseinfo_tmp = copy.deepcopy(caseinfo)
        # 从参数list获取每个要替换的字段dict
        for cont in content:
            #获取每个字段与对应值
            for new_key,new_value in cont.items():
                    toDict(caseinfo_tmp,new_key,new_value)
        return  caseinfo_tmp

    @classmethod
    #添加测试用例中的键值对
    #使用示例：caseinfo中添加多个键值对，并返回新的caseinfo
    #caseinfo = yaml_util.test_add_testcase_yaml(caseinfo,['data', 'param'],{'new1':1,'new2':'value2'})
    def add_testcase_yaml(cls,d, path_index, key_values):
        """
        递归地在嵌套字典和列表中添加键值对，并返回新字典。

        :param d: 原始数据结构的浅拷贝（字典或列表）。
        :param path_index: 用于导航到数据结构中正确位置的索引列表。
        :param key: 要添加的新键。
        :param value: 与新键关联的值。
        :return: 修改后的新数据结构。
        """

        def recursive_add(d, index):
            if index:
                current = index[0]
                remaining = index[1:]

                if isinstance(d, list):
                    if current.isdigit() and 0 <= int(current) < len(d):
                        d[int(current)] = recursive_add(d[int(current)], remaining)
                elif isinstance(d, dict):
                    if current in d:
                        d[current] = recursive_add(d[current], remaining)

            if not index:
                if isinstance(d, dict):
                    d.update(key_values)  # 使用 update 方法添加所有键值对
                else:
                    raise TypeError("The target is not a dictionary. Cannot add key-value pairs.")

            return d
        # 首先进行深拷贝以避免修改原始字典
        new_d = copy.deepcopy(d)
        return recursive_add(new_d, path_index)


    @classmethod
    #移除测试用例中的键值对
    #使用示例：删除caseinfo下对应的键值对
    #info = yaml_util.test_remove_testcase_yaml(caseinfo, ['data'], 'innerTag')
    def remove_testcase_yaml(cls,data_structure, path, key_to_delete):
        """在嵌套的数据结构中删除指定的键值对，并返回新数据结构。"""
        # 深拷贝数据结构
        new_structure = copy.deepcopy(data_structure)

        def recursive_delete(current_data, path_parts):
            if not path_parts:  # 路径为空，执行删除操作
                if key_to_delete in current_data:
                    del current_data[key_to_delete]
                else:
                    pytest.fail(key_to_delete+'不存在，检查字典的删除路径是否存在于\n'+json.dumps(current_data))
                return current_data

            # 获取当前路径部分
            next_part = path_parts[0]

            if isinstance(current_data, list) and next_part.isdigit():
                index = int(next_part)
                if 0 <= index < len(current_data):  # 索引在列表范围内
                    current_data[index] = recursive_delete(current_data[index], path_parts[1:])
            elif isinstance(current_data, dict) and next_part in current_data:
                current_data[next_part] = recursive_delete(current_data[next_part], path_parts[1:])

            return current_data

        # 执行递归删除操作
        return recursive_delete(new_structure, path)


