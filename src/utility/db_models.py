import datetime
from flask_sqlalchemy import SQLAlchemy
from dialogSystem.run import app

db = SQLAlchemy(app)


class movie_dcit(db.Model):
    __tablename__ = 'movie_dict'

    id = db.Column(db.Integer, primary_key=True)
    city = db.Column(db.String(128), nullable=False)
    moviename = db.Column(db.String(128), nullable=False)
    date = db.Column(db.String(30), nullable=False)
    starttime = db.Column(db.String(30), nullable=True)
    theater = db.Column(db.String(128), nullable=False)
    theater_chain = db.Column(db.String(30), nullable=True)
    distanceconstraints = db.Column(db.String(128), nullable=True)
    actor = db.Column(db.String(30), nullable=True)
    actress = db.Column(db.String(30), nullable=True)
    genre = db.Column(db.String(30), nullable=True)
    numberofpeople = db.Column(db.String(30), nullable=True)
    numberofkids = db.Column(db.String(30), nullable=True)
    state = db.Column(db.String(30), nullable=True)
    zip = db.Column(db.String(30), nullable=True)
    video_format = db.Column(db.String(30), nullable=True)
    other = db.Column(db.String(128), nullable=True)
    create_time = db.Column(db.TIMESTAMP, nullable=False)

    def __init__(self):
        self.create_time = datetime.utcnow()

    def __repr__(self):
        return '<Duomai_detail %s>' % self.__tablename__


class dialog_History(db.Model):
    __tablename__ = 'dialog_history'

    id = db.Column(db.Integer, primary_key=True)
    # 业务类型
    business_type = db.Column(db.String(20), nullable=True)
    # 推广渠道
    promotion_channels = db.Column(db.String(50), nullable=False)
    # 佣金类型
    type = db.Column(db.String(30), nullable=True)
    # 金额
    amount = db.Column(db.DECIMAL)
    # 记录创建时间
    create_time = db.Column(db.TIMESTAMP, nullable=False)

    def __init__(self):
        self.create_time = datetime.utcnow()
        self.modify_time = datetime.utcnow()

    def __repr__(self):
        return '<JD_detail %s>' % self.__tablename__


class Taobao_detail(db.Model):
    __tablename__ = 'taobao_product_effect'

    id = db.Column(db.Integer, primary_key=True)
    # 时间
    promotion_date = db.Column(db.TIMESTAMP, nullable=False)
    # 推广位
    promotion_bit = db.Column(db.String(50), nullable=False)
    # 点击数
    clicks = db.Column(db.Integer, nullable=False)
    # 付款笔数
    payments = db.Column(db.Integer, nullable=False)
    # 预估效果
    effects = db.Column(db.String(50), nullable=True)
    # 预估收入
    revenue = db.Column(db.DECIMAL, nullable=True)
    # 记录创建时间
    create_time = db.Column(db.TIMESTAMP, nullable=False)
    # 记录最后一次修改时间
    modify_time = db.Column(db.TIMESTAMP, nullable=False)

    def __init__(self):
        self.create_time = datetime.utcnow()
        self.modify_time = datetime.utcnow()

    def __repr__(self):
        return '<Taobao_detail %s>' % self.__tablename__
