from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from PhongKhamTu import app, db
from PhongKhamTu.model import DSDatLich, BenhNhan, NguoiDung, HoaDon,Thuoc,DonViThuoc,ChiTietDonThuoc, PhieuKham,LoaiThuoc

class BenhNhanView(ModelView):
    can_view_details = True
    can_export = True
    column_searchable_list = ['hoten']
    column_labels = {
        'hoten':'Họ tên' ,
        'namsinh' :'Năm sinh',
        'diachi': 'Địa chỉ',
         'sdt': 'Số điện thoại'
    }

class DonViThuocView(ModelView):
    can_view_details = True
    form_columns = ['donvi', 'thuoc_id']
    column_labels = {
        'donvi':'đơn vị'
    }
class DSDatLichView(ModelView):
    form_columns = ['ngayKham','benhnhan_id','nguoidung_id']

admin= Admin(app,name='QUẢN TRỊ PHÒNG KHÁM', template_mode='bootstrap4')
admin.add_view(ModelView(DSDatLich,db.session,name="Đăng kí khám bệnh"))
admin.add_view(ModelView(HoaDon,db.session, name="Hoá đơn", category='Quản lý khám bệnh'))
admin.add_view(ModelView(Thuoc,db.session,name="Thuốc", category='Quản lý thuốc'))
admin.add_view(BenhNhanView(BenhNhan,db.session,name="Bệnh nhân"))
admin.add_view(ModelView(NguoiDung,db.session,name ="User"))
admin.add_view(ModelView(PhieuKham,db.session, name="Phiếu khám bệnh", category='Quản lý khám bệnh'))
admin.add_view(ModelView(ChiTietDonThuoc,db.session, name="Chi tiết đơn thuốc", category='Quản lý khám bệnh'))
admin.add_view(ModelView(LoaiThuoc,db.session,name="Loại thuốc", category='Quản lý thuốc'))
admin.add_view(DonViThuocView(DonViThuoc,db.session,name="Đơn vị", category='Quản lý thuốc'))
