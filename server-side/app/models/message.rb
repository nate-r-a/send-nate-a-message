class Message < ApplicationRecord
  scope :unprinted, -> { where(printed: false) }
  scope :not_private, -> { where(private: false) }
end
