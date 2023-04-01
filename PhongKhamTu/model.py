from sqlalchemy import Column, Integer, String, Date, Float, Boolean, ForeignKey
from sqlalchemy.orm import relationship, backref
from PhongKhamTu import db, app

class NguoiDung(db.Model):
    id =Column(Integer, primary_key=True, autoincrement=True)
    HoTen =Column(String(50))
    Usename =Column(String(50))
    Password = Column(String(20))
    Email =Column(String(20))
    NgayThamGia = Column(Date)
    CapBac = Column(String(20))
    dsdatlich = relationship('DSDatLich', backref='nguoidung', lazy=True)
    hoadon = relationship('HoaDon', backref='nguoidung', lazy=True)
    phieukham = relationship('PhieuKham', backref='nguoidung', lazy=True)
class DSLichKham(db.Model):
    NgayKham = Column(Date, primary_key=True)
    dsdatlich = relationship('DSDatLich', backref='dslichkham', lazy=True)

class DSDatLich(db.Model):
    id = Column(Integer, primary_key=True, autoincrement=True)
    benhnhan = relationship('BenhNhan', backref='dsdatlich', lazy=True)
    dslichkham_ngaykham = Column(Date, ForeignKey(DSLichKham.NgayKham), nullable=False)
    nguoidung_id = Column(Integer, ForeignKey(NguoiDung.id), nullable=False)

class BenhNhan(db.Model):
    id =Column(Integer, primary_key=True, autoincrement=True)
    HoTen =Column(String(50))
    NamSinh =Column(Integer)
    DiaChi =Column(String(100))
    SDT =Column(Integer)
    dsdatlich_id =Column(Integer,ForeignKey(DSDatLich.id),nullable=False)
    hoadon = relationship('HoaDon', backref='benhnhan', lazy=True)

class PhieuKham(db.Model):
    __tablename__= 'phieukham'

    id =Column(Integer, primary_key=True, autoincrement=True)
    NgayKham =Column(Date)
    TrieuChung = Column(String(100))
    ChuanDoan = Column(String(100))
    hoadon = relationship('HoaDon', backref='phieukham', lazy=True)
    chitietdonthuoc = relationship('ChiTietDonThuoc', backref='phieukham', lazy=True)
    thuoc = relationship("ChiTietDonThuoc", backref="phieukham")
    nguoidung_id = Column(Integer, ForeignKey(NguoiDung.id), nullable=False)
class HoaDon(db.Model):
    id =Column(Integer, primary_key=True, autoincrement=True)
    TienThuoc =Column(Float)
    TienKham = Column(Float)
    TongTien = Column(Float)
    TrangThai =Column(Boolean)
    nguoidung_id = Column(Integer, ForeignKey(NguoiDung.id), nullable=False)
    benhnhan_id = Column(Integer, ForeignKey(BenhNhan.id), nullable=False)
    phieukham_id = Column(Integer, ForeignKey(PhieuKham.id), nullable=False)

LoaiThuoc_Thuoc =db.Table('LoaiThuoc_Thuoc',
                          Column('loaithuoc_id',Integer,ForeignKey('loaithuoc.id'),primary_key=True),
                          Column('thuoc_id',Integer,ForeignKey('thuoc.id'),primary_key=True))
class Thuoc(db.Model):
    __tablename__= 'thuoc'
    id =Column(Integer, primary_key=True, autoincrement=True)
    TenThuoc =Column(String(50))
    Gia = Column(Integer)
    CachSuDung = Column(String(100))
    donvithuoc = relationship('DonViThuoc', backref='thuoc', lazy=True)
    chitietdonthuoc = relationship('ChiTietDonThuoc', backref='thuoc', lazy=True)
    phieukham = relationship("ChiTietDonThuoc", backref="thuoc")
    loaithuoc= relationship('LoaiThuoc',secondary='LoaiThuoc_Thuoc',lazy='subquery', backref=backref('thuoc', lazy=True))

class ChiTietDonThuoc(db.Model):
    phieukham_id = Column(ForeignKey('phieukham.id'), primary_key=True)
    thuoc_id = Column(ForeignKey('thuoc.id'), primary_key=True)
    SoLuong = Column(Integer)
class DonViThuoc(db.Model):
    id = Column(Integer, primary_key=True, autoincrement=True)
    DonVi =Column(String(20), unique=True)
    thuoc_id = Column(Integer, ForeignKey(Thuoc.id), nullable=False)
class LoaiThuoc(db.Model):
    __tablename__= 'loaithuoc'
    id = Column(Integer, primary_key=True, autoincrement=True)
    TenLoaiThuoc = Column(String(50))

if __name__ == '__main__':
    with app.app_context():
        # c1 = BenhNhan(HoTen='Trần Anh Tú', NamSinh='1997', DiaChi='Cà Mau', SDT='0372319888')
        # c2 = BenhNhan(HoTen='Nguyễn Hoài Nam',NamSinh='1990', DiaChi='TPHCM', SDT='0386548732')
        # db.session.add_all([c1,c2])
        # db.session.commit()
        db.create_all()