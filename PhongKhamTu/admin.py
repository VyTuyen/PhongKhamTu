from flask import redirect
<<<<<<< HEAD
from flask_admin import Admin, expose,BaseView
=======
from flask_admin import Admin, BaseView, expose
>>>>>>> c742fa719d8ffa1e1e5c999c866f59d3bb8270b7
from flask_admin.contrib.sqla import ModelView
from flask_login import logout_user, current_user

from PhongKhamTu import app, db
from PhongKhamTu.model import User,DanhSachDatLich,Thuoc,DonViThuoc,LoaiThuoc
from flask_login import current_user,logout_user

class ListDetailView(ModelView):
    can_create = False
    edit_modal = True
    column_labels = {
        'tenBN': 'Tên bệnh nhân',
        'gioiTinh': 'Giới tính',
        'namSinh': 'Năm sinh',
        'SDT':'Số điện thoại',
        'diaChi': 'Địa chỉ',
        'user': 'Tên người đăng kí'
    }
    column_exclude_list = ['user'] #ẩn cột
    form_excluded_columns = ['user'] #ẩn cột ở form
class UnitView(ModelView):
    column_display_pk = True #hiển thị khoá chính
    can_view_details = True
    can_export = True
    create_modal = True
    edit_modal = True
    details_modal = True
    column_searchable_list = ['id', 'name']
    column_labels = {
        'id': 'Mã đơn vị',
        'name': 'Tên đơn vị'
    }
    # form_excluded_columns = ['medicines']
class CateView(ModelView):
    column_display_pk = True
    can_view_details = True
    can_export = True
    create_modal = True
    edit_modal = True
    details_modal = True
    column_searchable_list = ['id', 'name']
    column_labels = {
        'id': 'Mã loại thuốc',
        'name': 'Tên loại thuốc'
    }
    # form_excluded_columns = ['medicine']


<<<<<<< HEAD
class MedicineView(ModelView):
    column_display_pk = True
    can_view_details = True
    can_export = True
    create_modal = True
    edit_modal = True
    details_modal = True
    column_searchable_list = ['id', 'name']
    column_filters = 'id', 'name'
    # column_display_all_relations = True
    column_exclude_list = ['phieuKhamBenh']
    column_labels = {
        'id': 'Mã thuốc',
        'name': 'Tên thuốc',
        'donViThuoc_id': 'Đơn vị tính',
        'giaThuoc': 'Giá tiền',
        'CachSD': 'Cách dùng',
        'loaiThuoc_id':'Loại thuốc',
        'DonViThuoc': 'Đơn vị thuốc',
        'danh_muc_thuoc': 'Loại thuốc'
    }
    form_columns = ['name','donViThuoc_id','giaThuoc','CachSD','loaiThuoc_id']
    form_excluded_columns = ['phieuKhamBenh']
=======

>>>>>>> c742fa719d8ffa1e1e5c999c866f59d3bb8270b7
class LogoutView(BaseView):
    @expose('/')
    def index(self):
        logout_user()
        return redirect('/admin')

    def is_accessible(self):
        return current_user.is_authenticated
<<<<<<< HEAD
=======
# class PhieuKhamView(ModelView):
#     can_view_details = True
#     can_export = True
#     # column_searchable_list = ['thuoc']
#     form_columns = ['ngaykham','trieuchung','chuandoan','benhnhan_id','nguoidung_id']
#     column_labels = {
#         'benhnhan_id': 'Bệnh nhân',
#         'ngaykham': 'Ngày khám',
#         'trieuchung': 'Triệu chứng',
#         'chuandoan': 'Chuẩn đoán',
#         'nguoidung_id': 'Người lập'
#     }
# class HoaDonView(ModelView):
#     column_display_pk = True
#     can_view_details = True
#     can_export = True
#     column_searchable_list = ['id']
#     form_columns = [ 'tienthuoc','tienkham','tongtien','trangthai','benhnhan_id']
#     column_labels = {
#         'tienthuoc':'Tiền thuốc',
#         'tienkham':'Tiền khám',
#         'tongtien':'Tổng tiền',
#         'trangthai':'Trạng thái',
#         'benhnhan_id':'Bệnh nhân'
#     }
# class ChiTietDonThuocView(ModelView):
#     can_view_details = True
#     # column_searchable_list = 'thuoc_id'
#     form_columns = ['thuoc_id','phieukham_id','soluong']
#     column_labels = {
#         'thuoc_id':'thuốc'
#     }
# class ThuocView(ModelView):
#     can_view_details = True
#     column_searchable_list = ['tenthuoc']
#     form_columns = ['tenthuoc','gia','cachsudung','ten_donvi','ten_loaithuoc']
#     column_labels = {
#         'tenthuoc':'Tên thuốc',
#         'gia':'Giá',
#         'cachsudung':'Cách sử dụng',
#         'ten_donvi':'Đơn vị thuốc',
#         'ten_loaithuoc':'Tên loại thuốc'
#     }
# class LoaiThuocView(ModelView):
#     column_display_pk = True
#     can_view_details = True
#     form_columns = ['tenloaithuoc']
#     column_exclude_list = ['thuoc_id']
#     column_labels = {
#         'tenloaithuoc': 'Tên loại thuốc'
#     }
# class DonViThuocView(ModelView):
#     column_display_pk = True
#     can_view_details = True
#     form_columns = ['donvi']
#     column_labels = {
#         'donvi':'Đơn vị'
#     }
# class BenhNhanView(ModelView):
#     can_view_details = True
#     can_export = True
#     column_searchable_list = ['hoten']
#     form_columns = ['hoten', 'namsinh', 'diachi', 'sdt', 'hoadon', 'phieukham']
#     column_labels = {
#         'hoten':'Họ tên',
#         'namsinh':'Năm sinh',
#         'diachi': 'Địa chỉ',
#          'sdt': 'Số điện thoại',
#         'dsdatlich_id': 'Danh sáchdđặt lịch'
#     }
>>>>>>> c742fa719d8ffa1e1e5c999c866f59d3bb8270b7
class UserView(ModelView):
    can_view_details = True
    can_export = True
    create_modal = True
    details_modal = True
    column_filters = ['username']
    column_searchable_list = ['username']
    column_exclude_list = ['active', 'ngayThamGia', 'password']
    column_labels = {
        'name': 'Họ và tên',
        'username': 'Tên đăng nhập',
        'user_role': 'Quyền',
        'joined_date': 'Ngày tạo'
    }

admin= Admin(app,name='QUẢN LÝ PHÒNG KHÁM', template_mode='bootstrap4')

admin.add_view(ListDetailView(DanhSachDatLich, db.session, name='Danh sách đặt lịch', category='Quản lý danh sách khám'))
<<<<<<< HEAD

admin.add_view(MedicineView(Thuoc, db.session, name='Thuốc', category='Quản lý thuốc'))
admin.add_view(UnitView(DonViThuoc, db.session, name='Đơn vị tính', category='Quản lý thuốc'))
admin.add_view(CateView(LoaiThuoc, db.session, name='Loại thuốc', category='Quản lý thuốc'))

admin.add_view(UserView(User, db.session, name='Người dùng'))
admin.add_view(LogoutView(name='Đăng xuất'))
=======
admin.add_view(UserView(User, db.session, name='Người dùng'))
admin.add_view(LogoutView(name='Đăng xuất'))
# admin.add_view(LichKhamView(DanhSachLichKham,db.session,name="Lịch khám bệnh",category='Khám bệnh'))
#
# admin.add_view(PhieuKhamView(PhieuKhamBenh,db.session, name="Phiếu khám bệnh", category='Quản lý khám bệnh'))
#
# admin.add_view(ChiTietDonThuocView(ChiTietDonThuoc,db.session, name="Chi tiết đơn thuốc", category='Quản lý khám bệnh'))
#
# admin.add_view(ThuocView(Thuoc,db.session,name="Thuốc", category='Quản lý thuốc'))
#
# admin.add_view(LoaiThuocView(LoaiThuoc,db.session,name="Loại thuốc", category='Quản lý thuốc'))
#
# admin.add_view(DonViThuocView(DonViThuoc,db.session,name="Đơn vị", category='Quản lý thuốc'))
#
# admin.add_view(HoaDonView(HoaDon,db.session, name="Quản lý hoá đơn"))
#
# # admin.add_view(BenhNhanView(B,db.session,name="Bệnh nhân"))
>>>>>>> c742fa719d8ffa1e1e5c999c866f59d3bb8270b7


