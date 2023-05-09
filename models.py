from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, DateTime, TEXT
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


class CompanyInfo(Base):
    __tablename__ = "CompanyInfo"
    Tax_code = Column(String(20), primary_key=True)
    Link = Column(String(256))
    Company_name = Column(String(256))
    Trading_name = Column(String(256))
    Issued_date = Column(String(100))
    Status = Column(TEXT, default='')
    Registered_office = Column(String(256))
    Address = Column(String(256))
    Commune = Column(String(256))
    District = Column(String(256))
    Provincial = Column(String(256))
    Head_office_address = Column(String(256))
    Owner = Column(String(256))
    Director = Column(String(256))
    Business_lines = Column(String(256))
    Note = Column(TEXT, default='')

    def to_string(self):
        return [self.Tax_code, self.Link, self.Company_name, self.Trading_name, self.Issued_date, self.Status, self.Registered_office, self.Address, self.Commune, self.District, self.Provincial,
                self.Head_office_address, self.Owner, self.Director, self.Business_lines, self.Note]


# class CompanyInfo:
#     def __init__(self, Tax_code, Company_name, Trading_name, Issued_date, Status, Registered_office,
#                  Head_office_address, Owner, Director, Business_lines, Note):
#         self.Tax_code = Tax_code
#         self.Company_name = Company_name
#         self.Trading_name = Trading_name
#         self.Issued_date = Issued_date
#         self.Status = Status
#         self.Registered_office = Registered_office
#         self.Head_office_address = Head_office_address
#         self.Owner = Owner
#         self.Director = Director
#         self.Business_lines = Business_lines
#         self.Note = Note

#     def to_string(self):
#         return f'Tax code: {self.Tax_code}\n' \
#                f'Company name: {self.Company_name}\n' \
#                f'Trading name: {self.Trading_name}\n' \
#                f'Issued date: {self.Issued_date}\n' \
#                f'Status: {self.Status}\n' \
#                f'Registered office: {self.Registered_office}\n' \
#                f'Head office address: {self.Head_office_address}\n' \
#                f'Owner: {self.Owner}\n' \
#                f'Director: {self.Director}\n' \
#                f'Business lines: {self.Business_lines}\n' \
#                f'Note: {self.Note}'

if __name__ == '__main__':
    from confict import engine
    Base.metadata.create_all(engine)
else:
    from confict import engine
