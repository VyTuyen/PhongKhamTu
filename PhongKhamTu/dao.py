# from PhongKhamTu.model import  user
# from PhongKhamTu import db, app
# import hashlib
#
# def get_user_by_id(Nguoidung_id):
#     return NguoiDung.query.get(Nguoidung_id)
#
#
# def auth_user(User,Password):
#     Password = str(hashlib.md5(Password.encode('utf-8')).hexdigest())
#
#     return NguoiDung.query.filter(NguoiDung.usename.__eq__(User),
#                              NguoiDung.password.__eq__(Password)).first()
#
