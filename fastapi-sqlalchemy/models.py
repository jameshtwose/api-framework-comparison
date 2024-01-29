from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DateTime, Boolean

Base = declarative_base()


class ComplaintsTable(Base):
    __tablename__ = "complaints_table"
    date_received = Column(DateTime)
    product = Column(String)
    sub_product = Column(String)
    issue = Column(String)
    sub_issue = Column(String)
    consumer_complaint_narrative = Column(String)
    company_public_response = Column(String)
    company = Column(String)
    state = Column(String)
    zip_code = Column(String)
    tags = Column(String)
    consumer_consent_provided = Column(String)
    submitted_via = Column(String)
    date_sent_to_company = Column(DateTime)
    company_response_to_consumer = Column(String)
    timely_response = Column(Boolean)
    consumer_disputed = Column(Boolean)
    complaint_id = Column(Integer, primary_key=True)

    def __repr__(self):
        return (
            f"<ComplaintsTable(product={self.product}, issue={self.issue})>"
        )
