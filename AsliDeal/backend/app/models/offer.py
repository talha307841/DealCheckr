from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Offer(Base):
    __tablename__ = 'offers'

    id = Column(Integer, primary_key=True, index=True)
    product_name = Column(String, index=True)
    original_price = Column(Float)
    discounted_price = Column(Float)
    discount_percentage = Column(Float)
    url = Column(String, index=True)
    created_at = Column(String)  # You may want to use DateTime for actual timestamps
    updated_at = Column(String)  # Same as above

    def __repr__(self):
        return f"<Offer(id={self.id}, product_name={self.product_name}, original_price={self.original_price}, discounted_price={self.discounted_price})>"