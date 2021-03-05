#coding=utf-8
import sys
sys.path.append('c:/project')
from util.excel_uti import ExcelUti
from keywordselenium.actionMethod import ActionMethod
class KeyWordCase:
    def run_main(self):
        self.action_method=ActionMethod()
        handle_excel=ExcelUti("C:/project/config/keyword.xls")
        case_lines=handle_excel.get_lines()
        if case_lines!=None:
            for i in range(1,case_lines):
                is_run=handle_excel.get_col_value(i,3)
                if is_run=='Yes':
                    method=handle_excel.get_col_value(i,4)
                    send_value=handle_excel.get_col_value(i,5)
                    handle_value=handle_excel.get_col_value(i,6)
                    except_result_method=handle_excel.get_col_value(i,7)
                    except_result=handle_excel.get_col_value(i,8)
                    self.run_method(method,send_value,handle_value)
                    if except_result!='':
                        except_value=self.get_except_result_value(except_result)
                        if except_value[0]=='text':
                            result=self.run_method(except_result_method)
                            if except_value[1] in result:
                                handle_excel.write_value(i,'Pass')
                            else:
                                handle_excel.write_value(i,'Fail')
                        elif except_value[0]=='element':
                            result=self.run_method(except_result_method,except_value[1])
                            # print(except_value[1]+'---->')
                            # print(result)
                            if result:
                                handle_excel.write_value(i,'Pass')
                            else:
                                handle_excel.write_value(i,'Fail')

    def get_except_result_value(self,data):
        return data.split('=')


    def run_method(self,method,send_value='',handle_value=''):
        
        method_value=getattr(self.action_method,method)
        if send_value != '' and handle_value!='': 
            result=method_value(send_value,handle_value)
        elif send_value == '' and handle_value!='': 
            result=method_value(handle_value)
        elif send_value != '' and handle_value=='': 
            result=method_value(send_value)
        else:
            result=method_value()
        return result

if __name__ == "__main__":
    case=KeyWordCase()
    case.run_main()

