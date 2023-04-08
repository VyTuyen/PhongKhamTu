from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from PhongKhamTu import app, db
from PhongKhamTu.model import User,DanhSachDatLich,Thuoc,DonViThuoc,LoaiThuoc

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

admin.add_view(MedicineView(Thuoc, db.session, name='Thuốc', category='Quản lý thuốc'))
admin.add_view(UnitView(DonViThuoc, db.session, name='Đơn vị tính', category='Quản lý thuốc'))
admin.add_view(CateView(LoaiThuoc, db.session, name='Loại thuốc', category='Quản lý thuốc'))

admin.add_view(UserView(User, db.session, name='Người dùng'))


