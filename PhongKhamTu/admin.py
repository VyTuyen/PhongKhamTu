from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from PhongKhamTu import app, db
from PhongKhamTu.model import DSDatLich, BenhNhan, NguoiDung, HoaDon,Thuoc,DonViThuoc,ChiTietDonThuoc, PhieuKham,LoaiThuoc

admin= Admin(app,name='QUẢN TRỊ PHÒNG KHÁM', template_mode='bootstrap4')
admin.add_view(ModelView(BenhNhan,db.session,name="Bệnh nhân", category='Lists'))
admin.add_view(ModelView(DSDatLich,db.session,name="Medicines", category='Lists'))
admin.add_view(ModelView(NguoiDung,db.session))
admin.add_view(ModelView(HoaDon,db.session))
admin.add_view(ModelView(Thuoc,db.session))
admin.add_view(ModelView(DonViThuoc,db.session))
admin.add_view(ModelView(ChiTietDonThuoc,db.session))
admin.add_view(ModelView(PhieuKham,db.session))
admin.add_view(ModelView(LoaiThuoc,db.session))
