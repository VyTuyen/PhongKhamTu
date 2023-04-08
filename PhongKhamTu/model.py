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
    name = Column(String(50), nullable=False)
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
        # db.create_all()
        u1 = DonViThuoc(name='Chai')
        u2 = DonViThuoc(name='Vỹ')
        u3 = DonViThuoc(name='Viên')
        db.session.add(u1)
        db.session.add(u2)
        db.session.add(u3)

        c1 = LoaiThuoc(name='Say xe')
        c2 = LoaiThuoc(name='Đau bụng')
        c3 = LoaiThuoc(name='Nhức đầu')
        c4 = LoaiThuoc(name='Canxi')
        db.session.add(c1)
        db.session.add(c2)
        db.session.add(c3)
        db.session.add(c4)


        t1 = Thuoc(name='diphenhydramine', donViThuoc_id=3,loaiThuoc_id=1, giaThuoc=5000,
                   CachSD='Uống trước khi khởi hàng 30 phút', )
        t2 = Thuoc(name='dimenhydrinate', donViThuoc_id=3,loaiThuoc_id=2, giaThuoc=6000,
                   CachSD='Uống trước khi khởi hàng 30 phút', )
        t3 = Thuoc(name='cinnarizine', donViThuoc_id=3,loaiThuoc_id=3, giaThuoc=7000,
                   CachSD='Uống trước khi khởi hàng 30 phút', )
        t4 = Thuoc(name='meclizine', donViThuoc_id=3,loaiThuoc_id=1, giaThuoc=8000,
                   CachSD='Uống trước khi khởi hàng 30 phút', )
        t5 = Thuoc(name='Ostelin Vitamin D3 & Calcium.', donViThuoc_id=3,loaiThuoc_id=3, giaThuoc=10000,
                   CachSD='Uống vào buổi sáng', )
        t6 = Thuoc(name="Calcium Magnesium Zinc của Nature's Bounty", donViThuoc_id=3,loaiThuoc_id=2, giaThuoc=12000,
                   CachSD='Uống vào buổi sáng', )
        t7 = Thuoc(name='Total Calcium Magnesium + D3.', donViThuoc_id=3,loaiThuoc_id=2,giaThuoc=15000,
                   CachSD='Uống vào buổi sáng', )
        t8 = Thuoc(name='Kirkland Calcium 600mg + D3', donViThuoc_id=1,loaiThuoc_id=1, giaThuoc=18000,
                   CachSD='Uống vào buổi sáng', )
        t9 = Thuoc(name='nizatidine (Axid)', donViThuoc_id=2, loaiThuoc_id=1,giaThuoc=50000,
                   CachSD='Uống sau khi ăn', )
        t10 = Thuoc(name='famotidine (Pepcid, Pepcid AC)', donViThuoc_id=3,loaiThuoc_id=3, giaThuoc=180000,
                    CachSD='Uống sau khi ăn', )
        t11 = Thuoc(name='cimetidine (Tagamet, Tagamet HB)', donViThuoc_id=1,loaiThuoc_id=2,
                    giaThuoc=18000, CachSD='Uống sau khi ăn')
        db.session.add(t1)
        db.session.add(t2)
        db.session.add(t3)
        db.session.add(t4)
        db.session.add(t5)
        db.session.add(t6)
        db.session.add(t7)
        db.session.add(t8)
        db.session.add(t9)
        db.session.add(t10)
        db.session.add(t11)

        # user1 = User(name='admin', username='admin', password='123456',
        #              email='thuy11@gmail.com',
        #              user_role='1')
        #
        # user2 = User(name='tuyen', username='tuyen', password='123',
        #              email='tuyennlv@gmail.com',
        #              user_role='2')
        #
        # user3 = User(name='staff', username='staff', password='123',
        #              email='ngan@gmail.com',
        #              user_role='3')
        #
        # user4 = User(name='doctor', username='doctor', password='123',
        #              email='tuyennlv@gmail.com',
        #              user_role='4')
        #
        # user5 = User(name='nurse', username='nurse', password='123',
        #              email='kimngan@gmail.com',
        #              user_role='5')
        # db.session.add(user1)
        # db.session.add(user2)
        # db.session.add(user3)
        # db.session.add(user4)
        # db.session.add(user5)
        #
        db.session.commit()
