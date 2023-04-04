from sqlalchemy import Column, Integer, String, Date, Float, Boolean, ForeignKey, Enum
from sqlalchemy.orm import relationship, backref
from PhongKhamTu import db, app
from enum import Enum as UserEnum

class UseRole(UserEnum):
    admin=1
    doctor = 2
    nurse=3

class NguoiDung(db.Model):
    id =Column(Integer, primary_key=True, autoincrement=True)
    hoten =Column(String(50),nullable=False)
    usename =Column(String(50),nullable=False,unique=True)
    password = Column(String(20), nullable=False)
    avatar =Column(String(100))
    email =Column(String(20))
    active =Column(Boolean,default=True)
    ngayThamGia = Column(Date)
    capBac = Column(Enum(UseRole))
    dsdatlich = relationship('DSDatLich', backref='nguoidung', lazy=True)
    hoadon = relationship('HoaDon', backref='nguoidung', lazy=True)
    phieukham = relationship('PhieuKham', backref='nguoidung', lazy=True)
class DSDatLich(db.Model):
    id = Column(Integer, primary_key=True, autoincrement=True)
    ngayKham = Column(Date, primary_key=True,nullable=False)
    benhnhan = relationship('BenhNhan', backref='dsdatlich', lazy=True)
    nguoidung_id = Column(Integer, ForeignKey(NguoiDung.id), nullable=False)

class BenhNhan(db.Model):
    id =Column(Integer, primary_key=True, autoincrement=True)
    hoten =Column(String(50),nullable=False)
    namsinh =Column(Integer)
    diachi =Column(String(100))
    sdt =Column(Integer,unique=True)
    dsdatlich_id =Column(Integer,ForeignKey(DSDatLich.id))
    hoadon = relationship('HoaDon', backref='benhnhan', lazy=True)

class PhieuKham(db.Model):
    __tablename__= 'phieukham'

    id =Column(Integer, primary_key=True, autoincrement=True)
    ngaykham =Column(Date)
    trieuchung = Column(String(100))
    chuandoan = Column(String(100))
    hoadon = relationship('HoaDon', backref='phieukham', lazy=True)
    thuoc = relationship("ChiTietDonThuoc", backref="phieukham")
    nguoidung_id = Column(Integer, ForeignKey(NguoiDung.id), nullable=False)
class HoaDon(db.Model):
    id =Column(Integer, primary_key=True, autoincrement=True)
    tienThuoc =Column(Float)
    tienKham = Column(Float)
    tongtien = Column(Float)
    trangthai =Column(Boolean, default=False)
    nguoidung_id = Column(Integer, ForeignKey(NguoiDung.id), nullable=False)
    benhnhan_id = Column(Integer, ForeignKey(BenhNhan.id), nullable=False)
    phieukham_id = Column(Integer, ForeignKey(PhieuKham.id), nullable=False)

LoaiThuoc_Thuoc =db.Table('LoaiThuoc_Thuoc',
                          Column('loaithuoc_id',Integer,ForeignKey('loaithuoc.id'),primary_key=True),
                          Column('thuoc_id',Integer,ForeignKey('thuoc.id'),primary_key=True))
class Thuoc(db.Model):
    __tablename__= 'thuoc'
    id =Column(Integer, primary_key=True, autoincrement=True)
    tenthuoc =Column(String(50))
    gia = Column(Integer)
    cachsudung = Column(String(100))
    donvithuoc = relationship('DonViThuoc', backref='thuoc', lazy=True)
    phieukham = relationship("ChiTietDonThuoc", backref="thuoc")
    loaithuoc= relationship('LoaiThuoc',secondary='LoaiThuoc_Thuoc',lazy='subquery', backref=backref('thuoc', lazy=True))

class ChiTietDonThuoc(db.Model):
    phieukham_id = Column(ForeignKey('phieukham.id'), primary_key=True)
    thuoc_id = Column(ForeignKey('thuoc.id'), primary_key=True)
    soluong = Column(Integer)
class DonViThuoc(db.Model):
    id = Column(Integer, primary_key=True, autoincrement=True)
    donvi =Column(String(20), unique=True)
    thuoc_id = Column(Integer, ForeignKey(Thuoc.id), nullable=False)
class LoaiThuoc(db.Model):
    __tablename__= 'loaithuoc'
    id = Column(Integer, primary_key=True, autoincrement=True)
    tenloaithuoc = Column(String(50))

if __name__ == '__main__':
    with app.app_context():
        # c1 = BenhNhan(HoTen='Trần Anh Tú', NamSinh='1997', DiaChi='Cà Mau', SDT='0372319888')
        # c2 = BenhNhan(HoTen='Nguyễn Hoài Nam',NamSinh='1990', DiaChi='TPHCM', SDT='0386548732')
        # db.session.add_all([c1,c2])
        # db.session.commit()
        db.create_all()