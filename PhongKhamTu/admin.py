from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from PhongKhamTu import app, db
from PhongKhamTu.model import User,DanhSachLichKham,DanhSachDatLich, HoaDon,Thuoc,DonViThuoc,ChiTietDonThuoc, PhieuKhamBenh,LoaiThuoc

class ListDetailView(ModelView):
    can_create = True
    edit_modal = True
    column_labels = {
        'tenBN': 'Tên bệnh nhân',
        'gioiTinh': 'Giới tính',
        'namSinh': 'Năm sinh',
        'diaChi': 'Địa chỉ',
        'user': 'Tên người đăng kí'
    }
    column_exclude_list = ['user']
    form_excluded_columns = ['user']

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
class UserView(ModelView):
    can_view_details = True
    can_export = True
    can_edit = False
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
admin.add_view(UserView(User, db.session, name='Người dùng'))

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


