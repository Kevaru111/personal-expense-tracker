from dataclasses import dataclass
from typing import Optional


@dataclass
class Transaction:
    user_id: int
    category_id: int
    payment_method_id: Optional[int]
    amount: float
    transaction_type: str
    description: Optional[str]
    transaction_date: str
    id: Optional[int] = None
    created_at: Optional[str] = None


@dataclass
class User:
    username: str
    email: Optional[str] = None
    id: Optional[int] = None
    created_at: Optional[str] = None


@dataclass
class Category:
    name: str
    category_type: str
    id: Optional[int] = None


@dataclass
class PaymentMethod:
    name: str
    id: Optional[int] = None