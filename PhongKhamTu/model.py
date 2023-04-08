from sqlalchemy import Column, Integer, String, DateTime, Float, Boolean, ForeignKey, Enum
from sqlalchemy.orm import relationship, backref
from PhongKhamTu import db, app
from enum import Enum as UserEnum
from flask_login import UserMixin
from datetime import datetime

class UserRole(UserEnum):
    ADMIN = 1
    KHACHHANG = 2
    NHANVIENTHANHTOAN = 3
    BACSI = 4
    YTA = 5
class BaseModel(db.Model):
    __abstract__= True
    id = Column(Integer, primary_key=True, autoincrement=True)
class User(BaseModel, UserMixin):
    hoten = Column(String(50), nullable=False)
    username = Column(String(50), nullable=False, unique=True)
    password = Column(String(50), nullable=False)
    email = Column(String(100), nullable=False)
    ngayThamGia = Column(DateTime, default=datetime.now())
    active = Column(Boolean, default=True)
    user_role = Column(Enum(UserRole))
    DSDatLich = relationship('DanhSachDatLich', backref='user', lazy=True)
    hoadon = relationship('HoaDon', backref='user', lazy=True)
    def __str__(self):
        return self.hoten
class DanhSachLichKham(BaseModel):
    ngayTao = Column(DateTime, default=datetime.now(), nullable=False)
    DSDatLich = relationship('DanhSachDatLich', backref='DanhSachLichKham', lazy=True)

    def __str__(self):
        return self.ngayTao.__str__()
class DanhSachDatLich(BaseModel):
    tenBN = Column(String(255), nullable=False)
    gioiTinh = Column(String(50), nullable=False)
    namSinh = Column(String(100))
    SDT = Column(String(100))
    diaChi = Column(String(100))
    user_id = Column(Integer, ForeignKey(User.id), nullable=False)
    DSLichKham_id = Column(Integer, ForeignKey(DanhSachLichKham.id), nullable=False)
class DonViThuoc(BaseModel):
    name = Column(String(20), nullable=False)
    thuoc = relationship('Thuoc', backref='DonViThuoc', lazy=True)
    def __str__(self):
        return self.name
class LoaiThuoc(BaseModel):
    name = Column(String(50), nullable=False)
    thuoc = relationship('Thuoc', backref='LoaiThuoc', lazy=True)
    def __str__(self):
        return self.name
class Thuoc(BaseModel):
    name = Column(String(50), nullable=False)
    giaThuoc = Column(Float, default=0)
    CachSD = Column(String(500))
    donViThuoc_id = Column(Integer, ForeignKey(DonViThuoc.id), nullable=False)
    loaiThuoc_id = Column(Integer, ForeignKey(LoaiThuoc.id), nullable=False)
    phieuKhamBenh = relationship('ChiTietDonThuoc', backref='Thuoc', lazy=True)
    def __str__(self):
        return self.name

class PhieuKhamBenh(BaseModel):
    fullname = Column(String(300),nullable=False)
    chanDoan = Column(String(300), nullable=False)
    trieuChung = Column(String(300), nullable=False)
    ngaylap = Column(DateTime, default=datetime.now())
    user_id = Column(Integer, ForeignKey(User.id), nullable=False)
    thuoc = relationship('ChiTietDonThuoc', backref='PhieuKhamBenh', lazy=True)

    def __str__(self):
        return self.id.__str__()


class HoaDon(BaseModel):
    tenHD = Column(String(100), nullable=False)
    ngayLapHD = Column(DateTime, default=datetime.now())
    tienKham = Column(Float, default=100000)
    tienThuoc = Column(Float, default=0)
    trangThai = Column(Boolean, default=False, nullable=False)  # trang thai thanh toan
    user_id = Column(Integer, ForeignKey(User.id), nullable=False)
    phieuKhamBenh_id = Column(Integer, ForeignKey(PhieuKhamBenh.id), nullable=False)
class ChiTietDonThuoc(db.Model):
    soLuong = Column(Integer, nullable=False, default=1)  # số lượng thuốc
    Thuoc_id = Column(Integer, ForeignKey(Thuoc.id), nullable=False, primary_key=True)  # id thuốc
    phieuKhamBenh_id = Column(Integer, ForeignKey(PhieuKhamBenh.id), nullable=False, primary_key=True)
    def __str__(self):
        return self.phieuKhamBenh_id.__str__()




if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        # c1 = BenhNhan(HoTen='Trần Anh Tú', NamSinh='1997', DiaChi='Cà Mau', SDT='0372319888')
        # c2 = BenhNhan(HoTen='Nguyễn Hoài Nam',NamSinh='1990', DiaChi='TPHCM', SDT='0386548732')
        # db.session.add_all([c1,c2])
        # db.session.commit()
