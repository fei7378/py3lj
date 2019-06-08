from TestSQLAlchemyOEM import OrmTest
import re
if __name__ == '__main__':
    alldic = {}
    text = ['项目地址：', '成洛大道5333号', '售楼处地址：', '成洛大道5333号（接待时间9:00-18:00）', '开发商：', '成都银诚投资管理有限公司', '物业公司：', '成都千禾物业服务有限公司', '最新开盘：', '2019.05.04', '物业类型：', '商业类', '交房时间：', '2022年06月30日', '容积率：', '6.40', '产权年限：', '40年', '绿化率：', '10%', '规划户数：', '暂无', '物业费用：', '2.6元/m²/月', '车位情况：', '地下车位数2918', '供暖方式：', '自采暖', '供水方式：', '民水', '供电方式：', '商电', '建筑类型：', '塔楼', '嫌恶设施：', '暂无', '占地面积：', '89,333㎡', '建筑面积：', '750,000㎡', '查看更多']
    for i in range(1,40,2):
        alldic[text[i-1][:-1]] = text[i]
    print(len(alldic.keys()))

if __name__ == '__main__':
    patternpro = re.compile(r'\&project_name=[a-zA-Z]+\&')
    dataOther="15&project_name=bcyxaapvl&recommend_log_info=&strategy_info"
    print(dataOther[0:50])
    project_name_all = re.findall(patternpro, dataOther)
    print(project_name_all)

