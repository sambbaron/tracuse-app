"""SQLAlchemy Models for General Mixins and Base extension"""

from sqlalchemy import Column, Index
from sqlalchemy import ForeignKey, Integer, String, DateTime, Boolean
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.hybrid import hybrid_property


