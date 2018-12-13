class User < ApplicationRecord
  validates :name, presence: true
  validates :phone_number, presence: true, numericality: { only_integer: true },
    length: { minimum: 12 }, uniqueness: true
  has_secure_password
end
