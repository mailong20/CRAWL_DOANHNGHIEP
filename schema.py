from confict import Session
from sqlalchemy.exc import PendingRollbackError, IntegrityError
from models import CompanyInfo
session = Session()


async def add_full_page(link, company_info_list):
    companyInfo_new = CompanyInfo()
    companyInfo_new.Link = link
    for _name, _info in company_info_list:
        if _name == 'Tên doanh ngiệp:':
            companyInfo_new.Company_name = _info
        elif _name == 'Tên giao dịch:':
            companyInfo_new.Trading_name = _info
        elif _name == 'Mã số thuế:':
            companyInfo_new.Tax_code = _info
        elif _name == 'Ngày cấp:':
            companyInfo_new.Issued_date = _info
        elif _name == 'Tình trạng hoạt động:':
            companyInfo_new.Status = _info
        elif _name == 'Nơi đăng ký quản lý:':
            companyInfo_new.Registered_office = _info
        elif _name == 'Địa chỉ trụ sở:':

            _info_list = _info.split(',')
            try:
                companyInfo_new.Address = ','.join(_info_list[:-3])
            except:
                pass
            try:
                companyInfo_new.Commune = _info_list[-3]
            except:
                pass
            try:
                companyInfo_new.District = _info_list[-2]
            except:
                pass
            try:
                companyInfo_new.Provincial = _info_list[-1]
            except:
                pass
            try:
                companyInfo_new.Head_office_address = _info
            except:
                pass

            # print(companyInfo_new.Address, companyInfo_new.Commune,
            #       companyInfo_new.District, companyInfo_new.Provincial)
        elif _name == 'Chủ sở hữu:':
            companyInfo_new.Owner = _info
        elif _name == 'Giám đốc:':
            companyInfo_new.Director = _info
        elif _name == 'Ngành nghề kinh doanh:':
            companyInfo_new.Business_lines = _info
        elif _name == 'Ghi chú:':
            companyInfo_new.Note = _info
    try:
        session.add(companyInfo_new)
        await session.commit()
        return True
    except Exception as e:
        # print(e)
        await session.rollback()
        return False


def get_all_company():
    try:
        companys = session.query(CompanyInfo).filter(
            CompanyInfo.Tax_code != '').all()
        return companys
    except Exception as ex:
        # print(ex)
        return []
