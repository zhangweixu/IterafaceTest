
class global_var:
    # case_id
    Id = '0'
    request_name = '1'
    url = '2'
    run = '3'
    request_way = '4'
    header = '5'
    case_depend = '6'
    data_depend = '7'
    field_depend = '8'
    data = '9'
    expect = '10'
    sql='11'
    result = '12'


def get_id():
    """获取case_ID"""
    return global_var.Id


def get_request_name():
    """获取模块名称"""
    return global_var.request_name


def get_url():
    """获取url"""
    return global_var.url


def get_run():
    """是否运行"""
    return global_var.run


def get_run_way():
    """请求方式"""
    return global_var.request_way


def get_header():
    """是否携带header"""
    return global_var.header


def get_case_depend():
    """case依赖"""
    return global_var.case_depend


def get_data_depend():
    """依赖的返回数据"""
    return global_var.data_depend


def get_field_depend():
    """数据依赖字段"""
    return global_var.field_depend


def get_data():
    """请求数据"""
    return global_var.data


def get_expect():
    """获取预期结果"""
    return global_var.expect


def get_result():
    """获取实际结果"""
    return global_var.result

def get_header_value():
    """获取header的值"""
    return global_var.header

def get_sql():
    """获取SQL"""
    return global_var.sql
