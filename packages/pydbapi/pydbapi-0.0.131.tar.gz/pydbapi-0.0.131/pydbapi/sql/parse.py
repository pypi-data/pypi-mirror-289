# -*- coding: utf-8 -*-
# @Author: longfengpili
# @Date:   2023-06-02 15:27:41
# @Last Modified by:   longfengpili
# @Last Modified time: 2024-07-16 12:02:02
# @github: https://github.com/longfengpili


import re
import os

from datetime import datetime, date, timedelta

import logging
sqllogger = logging.getLogger(__name__)


REG_BEHIND = r'(?=[,();:\s.])'


class SqlParse(object):

    def __init__(self, orisql):
        self.orisql = orisql

    @property
    def purpose(self):
        purpose = re.match('-- *(【.*?】)\n', self.orisql.strip())
        purpose = f"{purpose.group(1)}" if purpose else 'No Description'
        return purpose

    @property
    def sql(self):
        sql = re.sub('^--.*?\n', '\n', self.orisql.strip() + '\n')
        # sql = re.sub('^--.*?\n', '\n', self.orisql.strip() + '\n', flags=re.M)
        sql = sql.strip()
        # sql = sql if sql and sql.endswith(';') else sql + ';' if sql else ''
        sql = sql[:-1] if sql and sql.endswith(';') else sql if sql else ''
        return sql

    @staticmethod
    def split_sqls(sql):
        sql = sql.strip()
        sql = sql if sql.endswith(';') else sql + ';'
        sql_r1 = re.sub('; *\n', ';\n', sql)  # 处理多余的；
        sql_r2 = re.sub(';$', ';\n', sql_r1)  # 末尾增加'\n'
        sqls = re.split(';\n', sql_r2)[:-1]
        return sqls

    @property
    def comment(self):
        orisql = self.orisql.strip()
        orisql = orisql if orisql.endswith(';') else orisql + ';'
        comment = re.search('^-- *(.*?)\n', orisql)
        comment = comment.group(1) if comment else ''
        return comment.strip()

    @property
    def action(self):
        if not self.sql:
            return 'NoSql'

        sql = self.sql.replace('\n', '')
        splits = sql.split(' ')
        action = splits[0]
        if splits[1].lower() == 'index':
            action += splits[1]
        return action.upper()

    @property
    def tablename(self):
        sql = self.sql
        createt = re.search(rf'create (?:temp |temporary )?table (?:if not exists |if exists )?(.*?){REG_BEHIND}', sql)
        updatet = re.search(rf'update (.*?){REG_BEHIND}', sql)
        deletet = re.search(rf'delete (?:from )?(.*?){REG_BEHIND}', sql)
        insertt = re.search(rf'insert into (.*?){REG_BEHIND}', sql)
        ont = re.search(rf'(?<=on )(.*?){REG_BEHIND}', sql)
        fromt = re.search(rf'select .*? (?<=from )(.*?){REG_BEHIND}', sql, re.S)
        # print(createt, updatet, insertt, ont, fromt)
        tablename = createt or updatet or deletet or insertt or fromt or ont
        tablename = tablename.group(1) if tablename else sql
        return tablename

    @property
    def split_withsqls(self):
        sql = self.sql
        if not sql.lower().startswith('with'):
            raise Exception(f"Sql should startswith [with], but startswith [{sql[:4]}] !!!")

        sqls = re.split(r'(?<=\)), *\n+.*?\n*(?=.*?as *\n)', sql)
        if sqls[-1].startswith('select'):
            sql_last = sqls[-2] + sqls[-1]
            sqls = sqls[:-2] + [sql_last]
        return sqls

    @property
    def combination_sqls(self):
        combination_sqls = []
        sqls = self.split_withsqls
        for idx, sql in enumerate(sqls):
            tablename = re.search(r'(?:with )?(.*?)(?: as)', sql)
            tablename = tablename.group(1) if tablename else ''

            content = f"-- {tablename}_{idx + 1:03d}"
            sql_select = f'select * from {tablename} limit 10' if idx + 1 < len(sqls) else 'limit 10'

            sqls_front = sqls[:idx+1]
            sqls_front = ',\n'.join(sqls_front)
            sqls_front = f'{content}\n{sqls_front}\n{sql_select}'
            combination_sqls.append(sqls_front)
        return combination_sqls


class SqlFileParse(object):

    def __init__(self, filepath):
        self.filepath = filepath

    def get_content(self):
        if not os.path.isfile(self.filepath):
            raise Exception(f'File 【{self.filepath}】 not exists !')

        with open(self.filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        return content

    def parse_argument(self, argument, arguments):
        key, value = argument.split('=', 1)
        key, value = key.strip(), value.strip()
        try:
            globals_value = {'timedelta': timedelta}
            value = eval(value, globals_value, arguments)
        except NameError as e:
            raise NameError(f"{e}, please set it before '{key}' !!!")
        return key, value

    @property
    def parameters(self):
        content = self.get_content()
        content = re.sub('--.*?\n', '\n', content)  # 去掉注释
        parameters = re.findall(rf"\$(\w+){REG_BEHIND}", content)
        return set(parameters)

    @property
    def arguments(self):
        '''[summary]

        [description]
            获取文件中配置的arguments
        Returns:
            [dict] -- [返回文件中的参数设置]
        '''
        arguments = {
            'today': date.today(),
            'now': datetime.now(),
        }
        content = self.get_content()
        content = re.sub('--.*?\n', '\n', content)  # 去掉注释
        arguments_infile = re.findall(r'(?<!--)\s*#【arguments】#\s*\n(.*?)#【arguments】#', content, re.S)
        arguments_infile = ';'.join(arguments_infile).replace('\n', ';')
        arguments_infile = [argument.strip() for argument in arguments_infile.split(';') if argument]
        for argument in arguments_infile:
            key, value = self.parse_argument(argument, arguments)
            arguments[key] = value

        arguments = {k: f"'{datetime.strftime(v, '%Y-%m-%d %H:%M:%S')}'" if isinstance(v, datetime)
                        else f"'{datetime.strftime(v, '%Y-%m-%d')}'" if isinstance(v, date)
                        else v for k, v in arguments.items()}  # 处理时间
        # print(arguments)
        return arguments

    def replace_params(self, **kwargs):
        '''[summary]

        [description]
            替换具体的参数值，传入的参数值会覆盖文件中设置的参数值
        Arguments:
            **kwargs {[参数]} -- [传入的参数值]

        Returns:
            [str] -- [替换过后的内容]

        Raises:
            Exception -- [需要设置参数]
        '''
        filename = os.path.basename(self.filepath)
        kwargs = {k: v for k, v in kwargs.items() if v}
        arguments = self.arguments

        arguments_same = set(arguments) & set(kwargs)
        argsamelog = None
        if arguments_same:
            arguments_same = sorted(arguments_same)
            file_arg = {arg: arguments.get(arg) for arg in arguments_same}
            argsamelog = f"Replace FileSetting {file_arg}"

        arguments.update(kwargs)
        arguments_lack = self.parameters - set(arguments)
        if arguments_lack:
            raise Exception(f"Need params 【{'】, 【'.join(arguments_lack)}】 !")

        content = self.get_content()
        for key, value in arguments.items():
            content = re.sub(rf"\${key}{REG_BEHIND}", f"{value}", content)
        arguments = {k: arguments.get(k) for k in self.parameters}

        arglog = f"【Final Arguments】【{filename}】 Use arguments {arguments}" \
                 if arguments else f"【Final Arguments】【{filename}】 no arguments !!!"
        arglog = arglog + f", {argsamelog}" if argsamelog else arglog
        sqllogger.warning(arglog)

        return arguments, content

    def get_filesqls(self, with_test: bool = False, with_snum: int = 0, **kwargs):
        sqls = {}
        arguments, content = self.replace_params(**kwargs)
        sqls_tmp = re.findall(r'(?<!--)\s*###\s*\n(.*?)###', content, re.S)
        for idx, sql in enumerate(sqls_tmp):
            sqlparser = SqlParse(sql)
            purpose = f"【{idx + 1:0>3d}】{sqlparser.purpose}"
            sql = re.sub('--【.*?\n', '', sql.strip())

            if with_test:
                combination_sqls = sqlparser.combination_sqls
                sqls[f"{purpose}_{with_snum:03d}"] = combination_sqls[with_snum-1]
            else:
                sqls[purpose] = sql
        return arguments, sqls
