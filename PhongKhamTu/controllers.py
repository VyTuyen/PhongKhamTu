# from flask import render_template, request, redirect, session
# from PhongKhamTu import utils, app, model
# from PhongKhamTu.model import DSDatLich
# from PhongKhamTu.model import ChiTietDonThuoc, PhieuKham
# from twilio.rest import Client
# from PhongKhamTu.admin import *
# from flask_login import current_user
#
# def index():
#     success_msg = ''
#     if request.method.__eq__('POST'):
#         hoten= request.form.get('hoten')
#         sdt = request.form.get('sdt')
#         namsinh = request.form.get('namsinh')
#         diachi= request.form.get('diachi')
#
#         try:
#             utils.add_patient(hoten=hoten,
#                               sdt=sdt,
#                               namsinh=namsinh,
#                               diachi=diachi)
#             success_msg = 'Đăng ký thành công'
#         except:
#             success_msg = 'Đăng ký thất bại'
#     return render_template('index.html', success_msg=success_msg)
#
#
# def create_list():
#     b = model.BenhNhan.query.all()
#     return render_template('createList.html', benh=b)
#
#
# def add_date():
#     success_msg = ''
#     BenhNhan = 0
#     dem = 0
#     if request.method.__eq__('POST'):
#         day = request.form.get('day')
#         b = model.BenhNhan.query.all()
#         d = model.DSDatLich.query.all()
#         data = model.QuyDinh.query.all()
#         for s in data:
#             if s.id == 2:
#                 BenhNhan = s.content
#         for c in d:
#             if c.ngay_kham == day:
#                 for benh in b:
#                     if benh.danh_sach_id == c.id:
#                         dem = dem + 1
#                 if dem >= BenhNhan:
#                     success_msg = 'Ngày khám đã đủ bệnh nhân'
#                     return render_template('createList.html', benh=b, success_msg=success_msg)
#                 else:
#                     for e in b:
#                         if not e.danh_sach_id:
#                             id = DSDatLich.query.filter_by(ngay_kham=day).first().id
#                             utils.update_date(e.id, id)
#                             dem = dem + 1
#                         if (dem >= BenhNhan):
#                             break
#                     success_msg = 'Lập danh sách thành công'
#                     SID = 'AC3358f25bf3496999d130b7e25462d34d'
#                     Auth_Token = "063acb205a778783c9f8b17eb8e4b785"
#                     cl = Client(SID, Auth_Token)
#                     cl.messages.create(body='Bạn có lịch khám tại phòng mạch tư vào ngày ' + day,
#                                        from_='+15673843325', to='+84971539058')
#                 return render_template('createList.html', benh=b, success_msg=success_msg)
#         utils.add_date(day)
#         count = 0
#         for e in b:
#             if not e.danh_sach_id:
#                 id = DSDatLich.query.filter_by(ngay_kham=day).first().id
#                  utils.update_date(e.id, id)
#                 count = count + 1